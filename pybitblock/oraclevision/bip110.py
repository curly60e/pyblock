"""
BIP-110 block/transaction analysis engine.

Checks reduced_data policy rules locally against decoded block data.
Detection logic is delegated to pluggable detectors in oraclevision/detectors/.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from oraclevision.detectors import configure_detectors, run_detectors
from oraclevision.script_parser import (
    MAX_PUSHDATA_SIZE,
    decode_coinbase_tag,
    is_signaling_bip110,
)
from oraclevision.spam_score import classify_status, compute_spam_score


@dataclass
class TxAnalysis:
    txid: str
    weight: int
    vsize: int
    bip110_flags: set[str] = field(default_factory=set)
    signals: set[str] = field(default_factory=set)
    witness_bytes: int = 0

    @property
    def has_bip110_violation(self) -> bool:
        return bool(self.bip110_flags)

    @property
    def is_spam_signal(self) -> bool:
        return bool(self.signals - {"op_return"})


@dataclass
class BlockAnalysis:
    height: int
    hash: str
    miner_tag: str
    version: int
    weight: int
    tx_count: int
    bip110_signaling: bool
    spam_score: int = 0
    status: str = "CLEAN"
    violation_count: int = 0
    violation_weight: int = 0
    inscription_count: int = 0
    brc20_count: int = 0
    runes_count: int = 0
    op_return_count: int = 0
    large_witness_bytes: int = 0
    witness_pct: float = 0.0
    transactions: list[TxAnalysis] = field(default_factory=list)
    flagged_raw: dict[str, dict[str, Any]] = field(default_factory=dict)


def analyze_transaction(tx: dict[str, Any]) -> TxAnalysis:
    txid = tx.get("txid", tx.get("hash", ""))
    weight = int(tx.get("weight") or (tx.get("vsize", 0) * 4))
    vsize = int(tx.get("vsize") or weight // 4)

    detected = run_detectors(tx)
    return TxAnalysis(
        txid=txid,
        weight=weight,
        vsize=vsize,
        bip110_flags=detected.bip110_flags,
        signals=detected.signals,
        witness_bytes=detected.witness_bytes,
    )


def analyze_block(
    block: dict[str, Any],
    *,
    spam_threshold: int = 45,
) -> BlockAnalysis:
    height = int(block.get("height", 0))
    block_hash = block.get("hash", "")
    version = int(block.get("version", 0))
    weight = int(block.get("weight") or 0)

    txs = block.get("tx", [])
    if txs and isinstance(txs[0], str):
        return BlockAnalysis(
            height=height,
            hash=block_hash,
            miner_tag="?",
            version=version,
            weight=weight,
            tx_count=len(txs),
            bip110_signaling=is_signaling_bip110(version),
        )

    miner_tag = "unknown"
    tx_analyses: list[TxAnalysis] = []
    flagged_raw: dict[str, dict[str, Any]] = {}
    total_witness = 0

    for tx in txs:
        if not isinstance(tx, dict):
            continue
        vin0 = tx.get("vin", [{}])[0]
        if vin0.get("coinbase"):
            miner_tag = decode_coinbase_tag(vin0["coinbase"])
            continue
        ta = analyze_transaction(tx)
        tx_analyses.append(ta)
        total_witness += ta.witness_bytes
        if ta.has_bip110_violation or ta.is_spam_signal:
            txid = ta.txid or tx.get("txid", "")
            if txid:
                flagged_raw[txid] = tx

    violation_count = sum(1 for t in tx_analyses if t.has_bip110_violation)
    violation_weight = sum(t.weight for t in tx_analyses if t.has_bip110_violation)
    inscription_count = sum(1 for t in tx_analyses if "inscription" in t.signals)
    brc20_count = sum(1 for t in tx_analyses if "brc20" in t.signals)
    runes_count = sum(1 for t in tx_analyses if "runes" in t.signals)
    op_return_count = sum(1 for t in tx_analyses if "op_return" in t.signals)

    large_witness_bytes = sum(
        t.witness_bytes for t in tx_analyses if t.witness_bytes > MAX_PUSHDATA_SIZE
    )

    spam_score = compute_spam_score(
        block_weight=weight or 1,
        total_txs=len(tx_analyses),
        violation_weight=violation_weight,
        inscription_count=inscription_count,
        brc20_count=brc20_count,
        runes_count=runes_count,
        op_return_count=op_return_count,
        large_witness_bytes=large_witness_bytes,
        violation_count=violation_count,
    )
    status = classify_status(
        spam_score,
        violation_count,
        violation_weight,
        weight or 1,
        spam_threshold=spam_threshold,
    )
    witness_pct = (total_witness / max(weight, 1)) * 100 if weight else 0.0

    return BlockAnalysis(
        height=height,
        hash=block_hash,
        miner_tag=miner_tag,
        version=version,
        weight=weight,
        tx_count=len(tx_analyses),
        bip110_signaling=is_signaling_bip110(version),
        spam_score=spam_score,
        status=status,
        violation_count=violation_count,
        violation_weight=violation_weight,
        inscription_count=inscription_count,
        brc20_count=brc20_count,
        runes_count=runes_count,
        op_return_count=op_return_count,
        large_witness_bytes=large_witness_bytes,
        witness_pct=witness_pct,
        transactions=tx_analyses,
        flagged_raw=flagged_raw,
    )


configure_detectors(["builtin"])