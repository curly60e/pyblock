"""
Block template composition analysis for Mempool Glass.

Classifies transactions from getblocktemplate into economic, consolidation,
coinjoin, and spam buckets. Extend categorize_transaction() to add categories.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

from oraclevision.bip110 import analyze_transaction
from oraclevision.script_parser import MAX_PUSHDATA_SIZE, witness_total_bytes


@dataclass
class MempoolComposition:
    """Composition stats derived from the node's block template."""

    total_tx: int = 0
    total_weight: int = 0
    analyzed_tx: int = 0
    analyzed_weight: int = 0
    economic_weight: int = 0
    consolidation_weight: int = 0
    coinjoin_weight: int = 0
    spam_weight: int = 0
    economic_count: int = 0
    consolidation_count: int = 0
    coinjoin_count: int = 0
    spam_count: int = 0
    template_height: int = 0
    weight_limit: int = 4_000_000
    fill_pct: float = 0.0
    mempool_size: int = 0
    source: str = "block_template"
    error: str | None = None

    def pct(self, weight: int) -> float:
        base = self.analyzed_weight or 1
        return (weight / base) * 100


def _witness_has_oversized_item(tx: dict[str, Any]) -> bool:
    for vin in tx.get("vin", []):
        witness = vin.get("txinwitness") or vin.get("witness") or []
        for item in witness:
            if len(item) // 2 > MAX_PUSHDATA_SIZE:
                return True
    return False


def _excess_witness_ratio(tx: dict[str, Any]) -> bool:
    weight = int(tx.get("weight") or 1)
    wbytes = 0
    for vin in tx.get("vin", []):
        witness = vin.get("txinwitness") or vin.get("witness") or []
        wbytes += witness_total_bytes(witness)
    return wbytes > 2000 and (wbytes / weight) > 0.45


def _is_consolidation(tx: dict[str, Any]) -> bool:
    vin = len(tx.get("vin", []))
    vout = len(tx.get("vout", []))
    return vout <= 2 and vin >= 5


def _is_coinjoin(tx: dict[str, Any]) -> bool:
    vin = tx.get("vin", [])
    vout = tx.get("vout", [])
    if len(vin) < 5 or len(vout) < 5:
        return False
    in_vals: dict[float, int] = {}
    out_vals: dict[float, int] = {}
    for i in vin:
        v = (i.get("prevout") or {}).get("value")
        if v is not None:
            in_vals[v] = in_vals.get(v, 0) + 1
    for o in vout:
        v = o.get("value")
        if v is not None:
            out_vals[v] = out_vals.get(v, 0) + 1
    if not in_vals and not out_vals:
        return len(vin) >= 8 and len(vout) >= 8 and abs(len(vin) - len(vout)) <= 2
    unique = len(set(in_vals) | set(out_vals))
    total = len(vin) + len(vout)
    return unique <= total // 2


def _is_spam_tx(tx: dict[str, Any]) -> bool:
    analysis = analyze_transaction(tx)
    if analysis.has_bip110_violation or analysis.is_spam_signal:
        return True
    if _witness_has_oversized_item(tx):
        return True
    if _excess_witness_ratio(tx):
        return True
    return False


def categorize_transaction(tx: dict[str, Any]) -> str:
    """Return category: spam, coinjoin, consolidation, economic."""
    if _is_spam_tx(tx):
        return "spam"
    if _is_coinjoin(tx):
        return "coinjoin"
    if _is_consolidation(tx):
        return "consolidation"
    return "economic"


def analyze_block_template(
    template: dict[str, Any],
    decode_tx: Callable[[str], dict[str, Any]],
) -> MempoolComposition:
    """Classify all transactions in the node's current block template."""
    result = MempoolComposition()
    txs = template.get("transactions", [])
    result.template_height = int(template.get("height", 0))
    result.weight_limit = int(template.get("weightlimit", 4_000_000))
    result.total_tx = len(txs)

    if not txs:
        result.error = "Block template is empty"
        return result

    for entry in txs:
        weight = int(entry.get("weight", 0))
        result.total_weight += weight
        hex_data = entry.get("data", "")
        if not hex_data:
            continue
        try:
            tx = decode_tx(hex_data)
            if entry.get("txid"):
                tx["txid"] = entry["txid"]
            if weight and not tx.get("weight"):
                tx["weight"] = weight
        except Exception:
            continue

        result.analyzed_tx += 1
        w = int(tx.get("weight") or weight or 0)
        result.analyzed_weight += w

        cat = categorize_transaction(tx)
        if cat == "spam":
            result.spam_weight += w
            result.spam_count += 1
        elif cat == "coinjoin":
            result.coinjoin_weight += w
            result.coinjoin_count += 1
        elif cat == "consolidation":
            result.consolidation_weight += w
            result.consolidation_count += 1
        else:
            result.economic_weight += w
            result.economic_count += 1

    if result.analyzed_tx == 0:
        result.error = "Could not decode transactions from the template"
    else:
        result.fill_pct = (result.analyzed_weight / result.weight_limit * 100) if result.weight_limit else 0

    return result