"""Tests for pluggable transaction detectors."""

from __future__ import annotations

from oraclevision.bip110 import analyze_transaction
from oraclevision.detectors import configure_detectors, run_detectors


def test_builtin_detector_flags_large_op_return() -> None:
    configure_detectors(["builtin"])
    tx = {
        "txid": "cc" * 32,
        "weight": 400,
        "vsize": 100,
        "vin": [{"txid": "aa" * 32, "vout": 0, "scriptSig": {"hex": ""}}],
        "vout": [
            {
                "value": 0,
                "scriptPubKey": {
                    "type": "nulldata",
                    "hex": "6a" + "00" * 100,
                    "asm": "OP_RETURN " + "00" * 100,
                },
            }
        ],
    }
    result = run_detectors(tx)
    assert "op_return" in result.signals

    analysis = analyze_transaction(tx)
    assert analysis.txid == "cc" * 32