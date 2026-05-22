"""Gather Bitcoin/Lightning node data for AI context injection."""

import codecs
import json
import logging
import shlex
import subprocess

import requests

logger = logging.getLogger(__name__)


def gather_node_context(path, lndconnectload=None):
    """Collect node data to send with AI queries.

    path: dict with bitcoincli, ip_port, rpcuser, rpcpass
    lndconnectload: dict with LND connection info (optional)
    """
    ctx = {}

    # Bitcoin Core data
    if path.get("bitcoincli"):
        ctx.update(_bitcoin_cli_context(path))
    elif path.get("ip_port") and path.get("rpcuser"):
        ctx.update(_bitcoin_rpc_context(path))
    else:
        ctx.update(_bitcoin_api_context())

    # Lightning data
    if lndconnectload and lndconnectload.get("ip_port"):
        ctx.update(_lightning_context(lndconnectload))

    return ctx


def _run_cli(cli_args, command):
    """Run a bitcoin-cli command safely. Returns stdout or empty string."""
    # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit
    return subprocess.run(
        cli_args + [command],
        capture_output=True, text=True, timeout=10
    ).stdout


def _bitcoin_cli_context(path):
    """Gather context via bitcoin-cli."""
    ctx = {}
    cli = shlex.split(path["bitcoincli"])
    try:
        raw = _run_cli(cli, "getblockchaininfo")
        info = json.loads(raw)
        ctx["block_height"] = info.get("blocks", 0)
        ctx["chain"] = info.get("chain", "")
        ctx["verification_progress"] = round(
            info.get("verificationprogress", 0), 4
        )
        ctx["size_on_disk_gb"] = round(
            info.get("size_on_disk", 0) / 1e9, 2
        )
    except (subprocess.SubprocessError, OSError, json.JSONDecodeError, KeyError, ValueError) as e:
        logger.debug("getblockchaininfo failed: %s", e)

    try:
        raw = _run_cli(cli, "getmempoolinfo")
        mempool = json.loads(raw)
        ctx["mempool_size"] = mempool.get("size", 0)
        ctx["mempool_bytes"] = mempool.get("bytes", 0)
    except (subprocess.SubprocessError, OSError, json.JSONDecodeError, KeyError, ValueError) as e:
        logger.debug("getmempoolinfo failed: %s", e)

    try:
        raw = _run_cli(cli, "getnetworkinfo")
        net = json.loads(raw)
        ctx["peer_count"] = net.get("connections", 0)
    except (subprocess.SubprocessError, OSError, json.JSONDecodeError, KeyError, ValueError) as e:
        logger.debug("getnetworkinfo failed: %s", e)

    # Fee rates from mempool.space (fast/medium/slow)
    ctx.update(_fee_rates())

    return ctx


def _bitcoin_rpc_context(path):
    """Gather context via JSON-RPC."""
    ctx = {}
    try:
        def rpc(method, params=None):
            payload = json.dumps({
                "jsonrpc": "2.0", "id": "ai",
                "method": method, "params": params or []
            })
            r = requests.post(
                path["ip_port"],
                auth=(path["rpcuser"], path["rpcpass"]),
                data=payload, timeout=10
            )
            return r.json()["result"]

        info = rpc("getblockchaininfo")
        ctx["block_height"] = info.get("blocks", 0)
        ctx["chain"] = info.get("chain", "")

        mempool = rpc("getmempoolinfo")
        ctx["mempool_size"] = mempool.get("size", 0)

        net = rpc("getnetworkinfo")
        ctx["peer_count"] = net.get("connections", 0)
    except (requests.RequestException, json.JSONDecodeError, KeyError, ValueError) as e:
        logger.debug("Bitcoin RPC context failed: %s", e)

    ctx.update(_fee_rates())
    return ctx


def _bitcoin_api_context():
    """Gather context from mempool.space API (lite mode)."""
    ctx = {}
    try:
        r = requests.get(
            "https://mempool.space/api/blocks/tip/height", timeout=10
        )
        ctx["block_height"] = int(r.text.strip())
    except (requests.RequestException, ValueError) as e:
        logger.debug("API block height fetch failed: %s", e)

    try:
        r = requests.get(
            "https://mempool.space/api/mempool", timeout=10
        )
        data = r.json()
        ctx["mempool_size"] = data.get("count", 0)
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("API mempool fetch failed: %s", e)

    ctx.update(_fee_rates())
    return ctx


def _fee_rates():
    """Fetch recommended fee rates from mempool.space."""
    try:
        r = requests.get(
            "https://mempool.space/api/v1/fees/recommended", timeout=10
        )
        fees = r.json()
        return {
            "fee_rates": {
                "fast": fees.get("fastestFee", 0),
                "medium": fees.get("halfHourFee", 0),
                "slow": fees.get("hourFee", 0),
            }
        }
    except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
        logger.debug("Fee rate fetch failed: %s", e)
        return {}


def _lightning_context(lndconnectload):
    """Gather Lightning node context from LND."""
    ctx = {}
    try:
        cert_path = lndconnectload.get("tls", "")
        macaroon_path = lndconnectload.get("macaroon", "")
        if not cert_path or not macaroon_path:
            return ctx

        with open(macaroon_path, "rb") as f:
            macaroon = codecs.encode(f.read(), "hex")
        headers = {"Grpc-Metadata-macaroon": macaroon}
        url = f'https://{lndconnectload["ip_port"]}/v1/getinfo'
        r = requests.get(url, headers=headers, verify=cert_path, timeout=10)
        info = r.json()
        ctx["ln_alias"] = info.get("alias", "")
        ctx["ln_channels"] = info.get("num_active_channels", 0)
        ctx["ln_peers"] = info.get("num_peers", 0)

        # Channel balances
        url_bal = f'https://{lndconnectload["ip_port"]}/v1/balance/channels'
        r2 = requests.get(url_bal, headers=headers, verify=cert_path, timeout=10)
        bal = r2.json()
        ctx["local_balance_sats"] = int(bal.get("local_balance", {}).get("sat", 0))
        ctx["remote_balance_sats"] = int(bal.get("remote_balance", {}).get("sat", 0))
    except (requests.RequestException, json.JSONDecodeError, KeyError, ValueError, OSError) as e:
        logger.debug("Lightning context failed: %s", e)

    return ctx
