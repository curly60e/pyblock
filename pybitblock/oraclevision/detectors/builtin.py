"""Built-in BIP-110 and spam signal detectors."""

from __future__ import annotations

from typing import Any

from oraclevision.detectors import DetectorResult, TxDetector
from oraclevision.script_parser import (
    MAX_CONTROL_BLOCK_SIZE,
    MAX_OPRETURN_SIZE,
    MAX_PUSHDATA_SIZE,
    MAX_SCRIPTPUBKEY_SIZE,
    detect_inscription_in_witness,
    detect_token_patterns,
    has_annex,
    infer_taproot_script_path,
    is_op_return,
    is_valid_taproot_control_block,
    scan_tapscript_violations,
    script_has_large_push,
    vout_script_size,
    witness_total_bytes,
)


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


class BuiltinDetector:
    """Default Knots BIP-110 and spam signal detection."""

    name = "builtin"

    def detect(self, tx: dict[str, Any]) -> DetectorResult:
        bip110: set[str] = set()
        signals: set[str] = set()
        witness_bytes = 0
        all_hex = str(tx.get("txid", tx.get("hash", "")))

        for vout in tx.get("vout", []):
            size = vout_script_size(vout)
            if is_op_return(vout):
                signals.add("op_return")
                if size > MAX_OPRETURN_SIZE:
                    bip110.add("large_scriptpubkey")
            elif size > MAX_SCRIPTPUBKEY_SIZE:
                bip110.add("large_scriptpubkey")

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

        signals |= detect_token_patterns(all_hex)

        return DetectorResult(
            bip110_flags=bip110,
            signals=signals,
            witness_bytes=witness_bytes,
        )