"""
BIP-110 block/transaction analysis engine.

Checks reduced_data policy rules locally against decoded block data.
Extend _check_witness_rules() and analyze_transaction() for new rules.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from oraclevision.script_parser import (
    MAX_CONTROL_BLOCK_SIZE,
    MAX_OPRETURN_SIZE,
    MAX_PUSHDATA_SIZE,
    MAX_SCRIPTPUBKEY_SIZE,
    decode_coinbase_tag,
    detect_inscription_in_witness,
    detect_token_patterns,
    has_annex,
    infer_taproot_script_path,
    is_op_return,
    is_signaling_bip110,
    is_valid_taproot_control_block,
    scan_tapscript_violations,
    script_has_large_push,
    vout_script_size,
    witness_total_bytes,
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


def _prevout_type(vin: dict) -> str | None:
    if isinstance(vin.get("prevout"), dict):
        spk = vin["prevout"].get("scriptPubKey", {})
        return spk.get("type")
    return None


def _check_witness_rules(vin: dict) -> set[str]:
    flags: set[str] = set()
    witness: list[str] = vin.get("txinwitness") or vin.get("witness") or []
    if not witness:
        return flags

    annex = has_annex(witness)
    prevout_type = _prevout_type(vin)
    is_taproot_prevout = prevout_type == "witness_v1_taproot" or prevout_type == "v1_p2tr"
    is_script_path = (
        (is_taproot_prevout and len(witness) > (2 if annex else 1))
        or infer_taproot_script_path(witness)
    )

    if annex and (is_taproot_prevout or is_script_path):
        flags.add("taproot_annex")

    exempt: set[int] = set()
    executing_scripts: list[int] = []

    if annex:
        exempt.add(len(witness) - 1)

    if is_script_path:
        cb_idx = len(witness) - (2 if annex else 1)
        tap_idx = cb_idx - 1
        exempt.add(cb_idx)
        if tap_idx >= 0:
            exempt.add(tap_idx)
            executing_scripts.append(tap_idx)
    elif is_taproot_prevout:
        sig_idx = len(witness) - 1 - (1 if annex else 0)
        if sig_idx >= 0:
            exempt.add(sig_idx)
    elif prevout_type in ("witness_v0_scripthash", "v0_p2wsh", "scripthash", "p2sh") or prevout_type is None:
        ws_idx = len(witness) - 1 - (1 if annex else 0)
        if ws_idx >= 0:
            exempt.add(ws_idx)
            executing_scripts.append(ws_idx)

    for i, item in enumerate(witness):
        if i in exempt:
            continue
        if len(item) // 2 > MAX_PUSHDATA_SIZE:
            flags.add("large_pushdata")
            break

    if is_script_path:
        cb_idx = len(witness) - (2 if annex else 1)
        cb = witness[cb_idx]
        if len(cb) // 2 > MAX_CONTROL_BLOCK_SIZE:
            flags.add("large_control_block")
        if is_valid_taproot_control_block(cb):
            leaf_version = int(cb[:2], 16) & 0xFE
            if leaf_version != 0xC0:
                flags.add("undefined_witness")
        tap_idx = cb_idx - 1
        if tap_idx >= 0:
            tapscript = witness[tap_idx]
            op_success, op_if = scan_tapscript_violations(tapscript)
            if op_success:
                flags.add("op_success")
            if op_if:
                flags.add("op_if_notif")

    if "large_pushdata" not in flags:
        for idx in executing_scripts:
            if script_has_large_push(witness[idx]):
                flags.add("large_pushdata")
                break

    return flags


def _check_scriptsig_rules(vin: dict) -> set[str]:
    flags: set[str] = set()
    scriptsig = vin.get("scriptSig", {})
    hex_sig = scriptsig.get("hex", "") if isinstance(scriptsig, dict) else ""
    if not hex_sig:
        return flags

    asm = scriptsig.get("asm", "") if isinstance(scriptsig, dict) else ""
    if asm:
        parts = asm.split()
        prevout_type = _prevout_type(vin)
        redeem_idx = len(parts) - 1 if prevout_type in ("scripthash", "p2sh") else -1
        for i, part in enumerate(parts):
            if part.startswith("OP_"):
                continue
            if i == redeem_idx:
                if script_has_large_push(part):
                    flags.add("large_pushdata")
                continue
            if len(part) // 2 > MAX_PUSHDATA_SIZE:
                flags.add("large_pushdata")
                break
    elif script_has_large_push(hex_sig):
        flags.add("large_pushdata")
    return flags


def analyze_transaction(tx: dict[str, Any]) -> TxAnalysis:
    txid = tx.get("txid", tx.get("hash", ""))
    weight = int(tx.get("weight") or (tx.get("vsize", 0) * 4))
    vsize = int(tx.get("vsize") or weight // 4)

    analysis = TxAnalysis(txid=txid, weight=weight, vsize=vsize)
    bip110: set[str] = set()
    signals: set[str] = set()

    for vout in tx.get("vout", []):
        size = vout_script_size(vout)
        if is_op_return(vout):
            signals.add("op_return")
            if size > MAX_OPRETURN_SIZE:
                bip110.add("large_scriptpubkey")
        elif size > MAX_SCRIPTPUBKEY_SIZE:
            bip110.add("large_scriptpubkey")

    witness_bytes = 0
    all_hex = txid

    for vin in tx.get("vin", []):
        if vin.get("coinbase"):
            continue
        witness: list[str] = vin.get("txinwitness") or vin.get("witness") or []
        witness_bytes += witness_total_bytes(witness)
        all_hex += "".join(witness)

        bip110 |= _check_witness_rules(vin)
        bip110 |= _check_scriptsig_rules(vin)

        if detect_inscription_in_witness(witness):
            signals.add("inscription")

        scriptsig = vin.get("scriptSig", {})
        if isinstance(scriptsig, dict):
            all_hex += scriptsig.get("hex", "")

    for vout in tx.get("vout", []):
        spk = vout.get("scriptPubKey", {})
        all_hex += spk.get("hex", "")

    token_hits = detect_token_patterns(all_hex)
    signals |= token_hits

    analysis.bip110_flags = bip110
    analysis.signals = signals
    analysis.witness_bytes = witness_bytes
    return analysis


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
    )