"""Async data workers for fetching Bitcoin data."""

import requests


def fetch_block_height():
    """Fetch current block height from mempool.space."""
    try:
        r = requests.get("https://mempool.space/api/blocks/tip/height", timeout=5)
        return str(r.json())
    except Exception:
        return "---"


def fetch_btc_price():
    """Fetch current BTC/USD price from mempool.space."""
    try:
        r = requests.get("https://mempool.space/api/v1/prices", timeout=5)
        price = r.json().get("USD", 0)
        return f"{price:,}"
    except Exception:
        return "---"


def fetch_fees():
    """Fetch recommended fees from mempool.space."""
    try:
        r = requests.get("https://mempool.space/api/v1/fees/recommended", timeout=5)
        return r.json()
    except Exception:
        return {"fastestFee": "?", "halfHourFee": "?", "hourFee": "?"}


def fetch_mempool_info():
    """Fetch mempool summary."""
    try:
        r = requests.get("https://mempool.space/api/mempool", timeout=5)
        data = r.json()
        return {
            "count": data.get("count", 0),
            "vsize": data.get("vsize", 0),
            "total_fee": data.get("total_fee", 0),
        }
    except Exception:
        return {"count": "?", "vsize": "?", "total_fee": "?"}


def fetch_latest_blocks():
    """Fetch latest 5 blocks from mempool.space."""
    try:
        r = requests.get("https://mempool.space/api/v1/blocks", timeout=5)
        blocks = r.json()[:5]
        return [
            {
                "height": b.get("height", "?"),
                "tx_count": b.get("tx_count", "?"),
                "size": round(b.get("size", 0) / 1_000_000, 2),
                "pool": b.get("extras", {}).get("pool", {}).get("name", "Unknown"),
            }
            for b in blocks
        ]
    except Exception:
        return []


def fetch_hashrate():
    """Fetch network hashrate info."""
    try:
        r = requests.get("https://mempool.space/api/v1/mining/hashrate/3d", timeout=5)
        data = r.json()
        current = data.get("currentHashrate", 0)
        difficulty = data.get("currentDifficulty", 0)
        eh = current / 1e18
        return {"hashrate_eh": f"{eh:.1f}", "difficulty": f"{difficulty:.2e}"}
    except Exception:
        return {"hashrate_eh": "?", "difficulty": "?"}
