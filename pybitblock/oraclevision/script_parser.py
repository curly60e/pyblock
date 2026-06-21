"""
Low-level Bitcoin script/witness parsing helpers.

Ported from OracleVision (https://github.com/MarcanoFilms/oraculovision).
These functions implement BIP-110 size checks and spam heuristics. Extend
this module when adding new detection rules — keep UI code separate.
"""

from __future__ import annotations

import re
from typing import Iterable

# BIP-110 size limits (reduced_data policy)
MAX_SCRIPTPUBKEY_SIZE = 34
MAX_OPRETURN_SIZE = 83
MAX_PUSHDATA_SIZE = 256
MAX_CONTROL_BLOCK_SIZE = 257

OP_IF = 0x63
OP_NOTIF = 0x64
OP_FALSE = 0x00

_SPAM_HEX_PATTERNS = (
    b"6272632d3230",      # brc-20
    b"2270223a22627263",  # "p":"brc
    b"7469636b",          # tick
    b"6f7264",            # ord
    b"52554e45",          # RUNE
    b"746578742f706c61696e",  # text/plain
)


def hex_to_bytes(hex_str: str) -> bytes:
    if not hex_str:
        return b""
    try:
        return bytes.fromhex(hex_str)
    except ValueError:
        return b""


def witness_total_bytes(witness: Iterable[str] | None) -> int:
    if not witness:
        return 0
    return sum(len(w) // 2 for w in witness)


def has_annex(witness: list[str] | None) -> bool:
    if not witness or len(witness) < 2:
        return False
    return witness[-1].startswith("50")


def is_valid_taproot_control_block(cb_hex: str) -> bool:
    cb = hex_to_bytes(cb_hex)
    if len(cb) < 33 or (len(cb) - 33) % 32 != 0:
        return False
    return (cb[0] & 0xFE) >= 0xC0


def infer_taproot_script_path(witness: list[str]) -> bool:
    """Infer taproot script-path spend from witness structure without prevout."""
    if not witness or len(witness) < 3:
        return False
    annex = has_annex(witness)
    cb_idx = len(witness) - (2 if annex else 1)
    if cb_idx < 1:
        return False
    return is_valid_taproot_control_block(witness[cb_idx])


def script_has_large_push(script_hex: str) -> bool:
    """BIP-110 Rule 2: OP_PUSHDATA payloads > 256 bytes inside executing scripts."""
    buf = hex_to_bytes(script_hex)
    i = 0
    while i < len(buf):
        op = buf[i]
        if 0x01 <= op <= 0x4B:
            header_len, data_len = 1, op
        elif op == 0x4C:
            if i + 2 > len(buf):
                break
            header_len, data_len = 2, buf[i + 1]
        elif op == 0x4D:
            if i + 3 > len(buf):
                break
            header_len, data_len = 3, int.from_bytes(buf[i + 1 : i + 3], "little")
        elif op == 0x4E:
            if i + 5 > len(buf):
                break
            header_len, data_len = 5, int.from_bytes(buf[i + 1 : i + 5], "little")
        else:
            i += 1
            continue
        if i + header_len + data_len > len(buf):
            break
        if data_len > MAX_PUSHDATA_SIZE:
            return True
        i += header_len + data_len
    return False


def scan_tapscript_violations(script_hex: str) -> tuple[bool, bool]:
    """Return (op_success, op_if_notif) for BIP-110 rules 6 & 7."""
    buf = hex_to_bytes(script_hex)
    op_success = False
    op_if_notif = False
    i = 0
    while i < len(buf):
        op = buf[i]
        if 0x01 <= op <= 0x4B:
            i += 1 + op
            continue
        if op == 0x4C:
            if i + 1 >= len(buf):
                break
            i += 2 + buf[i + 1]
            continue
        if op == 0x4D:
            if i + 2 >= len(buf):
                break
            i += 3 + int.from_bytes(buf[i + 1 : i + 3], "little")
            continue
        if op == 0x4E:
            if i + 4 >= len(buf):
                break
            i += 5 + int.from_bytes(buf[i + 1 : i + 5], "little")
            continue

        if (
            op in (80, 98)
            or (126 <= op <= 129)
            or (131 <= op <= 134)
            or (137 <= op <= 138)
            or (141 <= op <= 142)
            or (149 <= op <= 153)
            or (187 <= op <= 254)
        ):
            op_success = True
        elif op in (OP_IF, OP_NOTIF):
            op_if_notif = True

        i += 1
        if op_success and op_if_notif:
            break
    return op_success, op_if_notif


def has_op_false_op_if_envelope(script_hex: str) -> bool:
    """Detect Ordinals inscription envelope: OP_FALSE ... OP_IF."""
    buf = hex_to_bytes(script_hex)
    if len(buf) < 3:
        return False
    for i in range(len(buf) - 1):
        if buf[i] == OP_FALSE and buf[i + 1] == OP_IF:
            return True
    return False


def detect_inscription_in_witness(witness: list[str] | None) -> bool:
    if not witness:
        return False
    annex = has_annex(witness)
    if len(witness) > (2 if annex else 1):
        script_idx = len(witness) - (3 if annex else 2)
        if script_idx >= 0:
            tapscript = witness[script_idx]
            if has_op_false_op_if_envelope(tapscript):
                return True
    for item in witness:
        if has_op_false_op_if_envelope(item):
            return True
    return False


def detect_token_patterns(hex_blob: str) -> set[str]:
    """Heuristic detection of BRC-20, Runes, Ordinals content in hex."""
    found: set[str] = set()
    lower = hex_blob.lower()
    raw = hex_to_bytes(hex_blob)

    if b"6272632d3230" in raw or b'"p":"brc-20"' in raw or b'"p": "brc-20"' in raw:
        found.add("brc20")
    if b"7469636b" in raw and (b"627263" in raw or b"6f7264" in raw):
        found.add("brc20")
    if b"52554e45" in raw:
        found.add("runes")
    if b"6f7264" in raw or b"746578742f706c61696e" in raw:
        found.add("ordinals")
    if "ord" in lower or "inscription" in lower:
        found.add("ordinals")

    for pat in _SPAM_HEX_PATTERNS:
        if pat in raw:
            if pat == b"52554e45":
                found.add("runes")
            elif pat in (b"6272632d3230", b"2270223a22627263", b"7469636b"):
                found.add("brc20")
            else:
                found.add("ordinals")
    return found


def decode_coinbase_tag(coinbase_hex: str) -> str:
    """Extract readable miner/pool tag from coinbase hex."""
    raw = hex_to_bytes(coinbase_hex)
    if len(raw) < 4:
        return "unknown"

    text = raw.decode("ascii", errors="ignore")
    runs = re.findall(r"[\x20-\x7e]{4,}", text)
    if not runs:
        return "unknown"

    pool_runs = [r.strip() for r in runs if "/" in r and len(r.strip()) >= 5]
    if pool_runs:
        return max(pool_runs, key=len)[:40]

    candidates = [r.strip() for r in runs if len(r.strip()) >= 6]
    if candidates:
        return max(candidates, key=len)[:40]
    return runs[-1].strip()[:40] or "unknown"


def is_signaling_bip110(version: int) -> bool:
    """BIP-110 reduced_data uses version bit 4."""
    return bool(version & (1 << 4))


def vout_script_size(vout: dict) -> int:
    spk = vout.get("scriptPubKey", {})
    hex_data = spk.get("hex", "")
    return len(hex_data) // 2


def is_op_return(vout: dict) -> bool:
    spk = vout.get("scriptPubKey", {})
    return spk.get("type") == "nulldata" or spk.get("asm", "").startswith("OP_RETURN")