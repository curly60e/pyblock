"""Bitcoin address and txid query parsing helpers."""

from __future__ import annotations

import re

_TXID_RE = re.compile(r"^[0-9a-f]{64}$")
_ADDRESS_RE = re.compile(
    r"^(bc1[a-z0-9]{25,87}|bc1p[a-z0-9]{25,87}|[13][a-km-zA-HJ-NP-Z1-9]{25,34})$"
)


class AddressQueryError(ValueError):
    """Invalid address query."""


def is_txid_query(raw: str) -> bool:
    return bool(_TXID_RE.fullmatch((raw or "").strip().lower()))


def parse_address_query(raw: str) -> str:
    address = (raw or "").strip()
    if not address:
        raise AddressQueryError("Enter a Bitcoin address (bc1…, 1…, or 3…)")
    if not _ADDRESS_RE.fullmatch(address):
        raise AddressQueryError(
            "Invalid address — use bc1…, 1…, or 3… format"
        )
    return address


def classify_query(raw: str) -> tuple[str, str]:
    """Return ('txid', value) or ('address', value)."""
    text = (raw or "").strip()
    if not text:
        raise ValueError("Empty query")
    if is_txid_query(text):
        return "txid", text.lower()
    return "address", parse_address_query(text)


def script_type_from_validation(validation: dict) -> str:
    """Derive a display script type from validateaddress output.

    Core returns ``scriptPubKey`` as a hex string, not a decoded object.
    Use witness/script flags when the verbose type is unavailable.
    """
    spk = validation.get("scriptPubKey")
    if isinstance(spk, dict):
        return str(spk.get("type", "") or "")

    if validation.get("iswitness"):
        witness_version = validation.get("witness_version")
        if witness_version == 1:
            return "witness_v1_taproot"
        if witness_version == 0:
            return "witness_v0_keyhash"
        return "witness"

    if validation.get("isscript"):
        return "scripthash"

    if validation.get("isvalid"):
        return "pubkeyhash"

    return ""
