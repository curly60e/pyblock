"""Tests for pluggable transaction detectors."""

from __future__ import annotations

from oraclevision.bip110 import analyze_transaction
from oraclevision.detectors import (
    DetectorResult,
    configure_detectors,
    enabled_detectors,
    register,
    run_detectors,
)
from oraclevision.detectors.builtin import BuiltinDetector


class _SignalDetector:
    name = "signal_only"

    def detect(self, tx: dict) -> DetectorResult:
        return DetectorResult(signals={"custom"}, witness_bytes=10)


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
    assert analysis.witness_bytes >= 0


def test_configure_detectors_ignores_unknown() -> None:
    configure_detectors(["builtin", "missing_detector"])
    assert enabled_detectors() == ("builtin", "missing_detector")


def test_run_detectors_merges_multiple_detectors() -> None:
    register(BuiltinDetector())
    register(_SignalDetector())
    configure_detectors(["builtin", "signal_only"])

    tx = {
        "txid": "dd" * 32,
        "weight": 200,
        "vsize": 50,
        "vin": [{"txid": "aa" * 32, "vout": 0, "scriptSig": {"hex": ""}}],
        "vout": [{"value": 1.0, "scriptPubKey": {"type": "pubkeyhash", "hex": "76a91400"}}],
    }
    result = run_detectors(tx)
    assert "custom" in result.signals
    assert result.witness_bytes >= 10
