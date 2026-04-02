"""Bitcoin data layer for the enhanced block clock.

Fetches block height, block details, fees, hashrate, and epoch info
from either a local bitcoin-cli or JSON-RPC, plus mempool.space API
for fee rates and hashrate.
"""

import json
import shlex
import subprocess
import threading
import time

import requests

# Halving constants
BLOCKS_PER_HALVING = 210_000
BLOCKS_PER_EPOCH = 2016
HALVING_BLOCKS = [BLOCKS_PER_HALVING * i for i in range(1, 65)]

# API endpoints
MEMPOOL_FEES_URL = "https://mempool.space/api/v1/fees/recommended"
MEMPOOL_HASHRATE_URL = "https://mempool.space/api/v1/mining/hashrate/3d"
MEMPOOL_HEIGHT_URL = "https://mempool.space/api/blocks/tip/height"
MEMPOOL_BLOCK_URL = "https://mempool.space/api/block/"
MEMPOOL_BLOCKS_URL = "https://mempool.space/api/v1/blocks"


class ClockData:
    """Fetches and caches Bitcoin data for the clock display."""

    def __init__(self, mode, path):
        """
        mode: 'local', 'remote', or 'lite'
        path: dict with ip_port, rpcuser, rpcpass, bitcoincli
        """
        self.mode = mode
        self.path = path

        # Block data
        self.block_height = 0
        self.block_hash = ""
        self.block_time = 0
        self.block_size = 0
        self.block_tx_count = 0

        # Epoch / halving
        self.epoch_progress = 0.0
        self.epoch_block = 0
        self.blocks_to_halving = 0
        self.next_halving_block = 0

        # Fee rates (sat/vB)
        self.fee_fastest = 0
        self.fee_half_hour = 0
        self.fee_hour = 0

        # Hashrate
        self.hashrate_current = 0.0
        self.hashrate_history = []
        self.difficulty = 0.0

        # Visual features
        self.miner_pool = ""
        self.block_weight = 0
        self.max_block_weight = 4_000_000
        self.peer_count = 0
        self.block_time_history = []  # last N block intervals in seconds
        self.streak_type = ""   # "fast", "slow", or ""
        self.streak_count = 0

        # Internal
        self._bg_thread = None
        self._last_api_fetch = 0

    # --- RPC / CLI abstraction ---

    def _cli(self, command):
        """Run bitcoin-cli command, return stdout string."""
        cmd = shlex.split(self.path["bitcoincli"]) + shlex.split(command)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout.strip()

    def _rpc(self, method, params=None):
        """JSON-RPC call for remote mode."""
        payload = json.dumps({
            "jsonrpc": "2.0", "id": "clock",
            "method": method, "params": params or []
        })
        resp = requests.post(
            self.path['ip_port'],
            auth=(self.path['rpcuser'], self.path['rpcpass']),
            data=payload, timeout=10
        )
        return resp.json()['result']

    def _get_block_count(self):
        if self.mode == 'lite':
            r = requests.get(MEMPOOL_HEIGHT_URL, timeout=10)
            return int(r.text.strip())
        elif self.mode == 'remote':
            return int(self._rpc('getblockcount'))
        else:
            return int(self._cli('getblockcount'))

    def _get_block_details(self):
        """Fetch full block details for current tip."""
        if self.mode == 'lite':
            tip_hash = requests.get(
                "https://mempool.space/api/blocks/tip/hash", timeout=10
            ).text.strip()
            r2 = requests.get(f"{MEMPOOL_BLOCK_URL}{tip_hash}", timeout=10)
            block = r2.json()
            self.block_hash = tip_hash
            self.block_time = block.get('timestamp', int(time.time()))
            self.block_size = block.get('size', 0)
            self.block_tx_count = block.get('tx_count', 0)
            self.block_weight = block.get('weight', 0)
            pool = block.get('extras', {})
            self.miner_pool = pool.get('pool', {}).get('name', '') if isinstance(pool, dict) else ''
        else:
            if self.mode == 'remote':
                block_hash = self._rpc('getbestblockhash')
                block = self._rpc('getblock', [block_hash])
            else:
                block_hash = self._cli('getbestblockhash')
                raw = self._cli(f'getblock {block_hash}')
                block = json.loads(raw)
            self.block_hash = block_hash
            self.block_time = block.get('time', int(time.time()))
            self.block_size = block.get('size', 0)
            self.block_tx_count = block.get('nTx', 0)
            self.block_weight = block.get('weight', 0)

    def _get_peer_count(self):
        """Fetch connected peer count (local/remote only)."""
        try:
            if self.mode == 'local':
                raw = self._cli('getnetworkinfo')
                info = json.loads(raw)
                self.peer_count = info.get('connections', 0)
            elif self.mode == 'remote':
                info = self._rpc('getnetworkinfo')
                self.peer_count = info.get('connections', 0)
        except Exception:
            pass

    def _get_miner_pool_local(self):
        """Extract miner/pool name from coinbase for local/remote mode."""
        try:
            if self.mode == 'local':
                raw = self._cli(f'getblock {self.block_hash} 2')
                block = json.loads(raw)
            elif self.mode == 'remote':
                block = self._rpc('getblock', [self.block_hash, 2])
            else:
                return
            coinbase_tx = block.get('tx', [{}])[0]
            scriptsig_hex = coinbase_tx.get('vin', [{}])[0].get('coinbase', '')
            # Decode hex to ASCII, extract readable part
            try:
                raw_bytes = bytes.fromhex(scriptsig_hex)
                ascii_part = ''.join(
                    c if 32 <= ord(c) < 127 else '' for c in raw_bytes.decode('ascii', errors='replace')
                )
                # Common pool tags
                pools = {
                    'Foundry': 'Foundry USA',
                    'AntPool': 'AntPool',
                    'F2Pool': 'F2Pool',
                    'ViaBTC': 'ViaBTC',
                    'Binance': 'Binance Pool',
                    'Mara': 'MARA Pool',
                    'MARA': 'MARA Pool',
                    'Luxor': 'Luxor',
                    'Ocean': 'OCEAN',
                    'ocean': 'OCEAN',
                    'OCEAN': 'OCEAN',
                    'SBI': 'SBI Crypto',
                    'Braiins': 'Braiins Pool',
                    'slush': 'Braiins Pool',
                    'SpiderPool': 'SpiderPool',
                    'BTC.com': 'BTC.com',
                    'Poolin': 'Poolin',
                    'Titan': 'Titan',
                }
                self.miner_pool = ""
                for tag, name in pools.items():
                    if tag in ascii_part:
                        self.miner_pool = name
                        break
                if not self.miner_pool and len(ascii_part) > 3:
                    # Use the longest readable substring
                    self.miner_pool = ascii_part.strip()[:20]
            except Exception:
                pass
        except Exception:
            pass

    def _fetch_block_time_history(self):
        """Fetch recent block timestamps and compute intervals + streaks."""
        try:
            if self.mode == 'lite':
                r = requests.get(MEMPOOL_BLOCKS_URL, timeout=10)
                blocks = r.json()[:15]
                timestamps = [b.get('timestamp', 0) for b in blocks]
            elif self.mode == 'local':
                timestamps = []
                h = self.block_height
                for i in range(15):
                    bh = self._cli(f'getblockhash {h - i}')
                    raw = self._cli(f'getblock {bh}')
                    block = json.loads(raw)
                    timestamps.append(block.get('time', 0))
            elif self.mode == 'remote':
                timestamps = []
                h = self.block_height
                for i in range(15):
                    bh = self._rpc('getblockhash', [h - i])
                    block = self._rpc('getblock', [bh])
                    timestamps.append(block.get('time', 0))
            else:
                return

            # Timestamps are newest-first, compute intervals
            intervals = []
            for i in range(len(timestamps) - 1):
                diff = abs(timestamps[i] - timestamps[i + 1])
                intervals.append(diff)

            self.block_time_history = intervals

            # Compute streak
            streak = 0
            stype = ""
            for iv in intervals:
                if iv < 300:  # <5 min = fast
                    if stype == "" or stype == "fast":
                        stype = "fast"
                        streak += 1
                    else:
                        break
                elif iv > 900:  # >15 min = slow
                    if stype == "" or stype == "slow":
                        stype = "slow"
                        streak += 1
                    else:
                        break
                else:
                    break

            self.streak_type = stype if streak >= 2 else ""
            self.streak_count = streak if streak >= 2 else 0

        except Exception:
            pass

    def _calc_epoch(self):
        """Calculate epoch and halving progress from block height."""
        h = self.block_height
        self.epoch_block = h % BLOCKS_PER_EPOCH
        self.epoch_progress = self.epoch_block / BLOCKS_PER_EPOCH

        for hb in HALVING_BLOCKS:
            if h < hb:
                self.next_halving_block = hb
                self.blocks_to_halving = hb - h
                break
        else:
            self.blocks_to_halving = 0
            self.next_halving_block = 0

    # --- API data (background thread) ---

    def _fetch_api_data(self):
        """Fetch fee rates, hashrate, block history from APIs (non-blocking)."""
        try:
            r = requests.get(MEMPOOL_FEES_URL, timeout=10)
            fees = r.json()
            self.fee_fastest = fees.get('fastestFee', 0)
            self.fee_half_hour = fees.get('halfHourFee', 0)
            self.fee_hour = fees.get('hourFee', 0)
        except Exception:
            pass

        try:
            r = requests.get(MEMPOOL_HASHRATE_URL, timeout=10)
            data = r.json()
            self.hashrate_current = data.get('currentHashrate', 0)
            self.difficulty = data.get('currentDifficulty', 0)
            hashrates = data.get('hashrates', [])
            self.hashrate_history = [
                h.get('avgHashrate', 0) for h in hashrates[-20:]
            ]
        except Exception:
            pass

        self._fetch_block_time_history()
        self._get_peer_count()
        if self.mode in ('local', 'remote') and not self.miner_pool:
            self._get_miner_pool_local()

    def _start_bg_fetch(self):
        """Fetch API data in background thread if enough time has passed."""
        now = time.time()
        if now - self._last_api_fetch < 30:
            return
        self._last_api_fetch = now
        t = threading.Thread(target=self._fetch_api_data, daemon=True)
        t.start()

    # --- Public API ---

    def refresh(self):
        """Full data fetch: block height, details, epoch, and trigger API fetch."""
        self.block_height = self._get_block_count()
        self._get_block_details()
        self._calc_epoch()
        self._start_bg_fetch()

    def poll(self):
        """Quick poll: just getblockcount. Returns set of changed field names."""
        changed = set()
        new_height = self._get_block_count()
        if new_height != self.block_height:
            old_height = self.block_height
            self.block_height = new_height
            self._get_block_details()
            self._calc_epoch()
            self._start_bg_fetch()
            changed.add('block_height')
        return changed

    @property
    def seconds_since_block(self):
        """Seconds elapsed since the last block timestamp."""
        if self.block_time == 0:
            return 0
        return max(0, int(time.time()) - self.block_time)
