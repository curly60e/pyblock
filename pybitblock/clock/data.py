"""Bitcoin data layer for the enhanced block clock.

Fetches block height, block details, fees, hashrate, and epoch info
from either a local bitcoin-cli or JSON-RPC, plus mempool.space API
for fee rates and hashrate.
"""

import json
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

        # Internal
        self._lock = threading.Lock()
        self._bg_thread = None
        self._last_api_fetch = 0

    # --- RPC / CLI abstraction ---

    def _cli(self, command):
        """Run bitcoin-cli command, return stdout string."""
        cmd = f'{self.path["bitcoincli"]} {command}'
        result = subprocess.run(cmd.split(), capture_output=True, text=True)
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
            r = requests.get(MEMPOOL_HEIGHT_URL, timeout=10)
            tip_hash = requests.get(
                "https://mempool.space/api/blocks/tip/hash", timeout=10
            ).text.strip()
            r2 = requests.get(f"{MEMPOOL_BLOCK_URL}{tip_hash}", timeout=10)
            block = r2.json()
            self.block_hash = tip_hash
            self.block_time = block.get('timestamp', int(time.time()))
            self.block_size = block.get('size', 0)
            self.block_tx_count = block.get('tx_count', 0)
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
        """Fetch fee rates and hashrate from mempool.space (non-blocking)."""
        try:
            r = requests.get(MEMPOOL_FEES_URL, timeout=10)
            fees = r.json()
            with self._lock:
                self.fee_fastest = fees.get('fastestFee', 0)
                self.fee_half_hour = fees.get('halfHourFee', 0)
                self.fee_hour = fees.get('hourFee', 0)
        except Exception:
            pass

        try:
            r = requests.get(MEMPOOL_HASHRATE_URL, timeout=10)
            data = r.json()
            with self._lock:
                self.hashrate_current = data.get('currentHashrate', 0)
                self.difficulty = data.get('currentDifficulty', 0)
                hashrates = data.get('hashrates', [])
                self.hashrate_history = [
                    h.get('avgHashrate', 0) for h in hashrates[-20:]
                ]
        except Exception:
            pass

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
        return int(time.time()) - self.block_time
