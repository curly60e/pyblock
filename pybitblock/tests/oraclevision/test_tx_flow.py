"""Tests for transaction flow parsing."""

from __future__ import annotations

from oraclevision.tx_flow import build_flow_summary, parse_outputs


def test_parse_outputs_with_addresses() -> None:
    tx = {
        "vin": [],
        "vout": [
            {
                "n": 0,
                "value": 0.5,
                "scriptPubKey": {
                    "type": "witness_v0_keyhash",
                    "address": "bc1qrecipientxxxxxxxxxxxxxxxxxxxxxx",
                },
            },
            {
                "n": 1,
                "value": 0.0499,
                "scriptPubKey": {
                    "type": "witness_v0_keyhash",
                    "address": "bc1qchangexxxxxxxxxxxxxxxxxxxxxxxx",
                },
            },
        ],
    }
    flow = build_flow_summary(tx)
    assert len(flow.outputs) == 2
    assert flow.total_output_btc == 0.5499
    assert len(flow.recipients) == 2
    assert flow.recipients[0].startswith("bc1q")


def test_build_flow_with_prevouts_and_fee() -> None:
    tx = {
        "vin": [
            {
                "txid": "aa" * 32,
                "vout": 0,
                "prevout": {
                    "value": 1.0,
                    "scriptPubKey": {
                        "type": "witness_v0_keyhash",
                        "address": "bc1qsenderxxxxxxxxxxxxxxxxxxxxxxxx",
                    },
                },
            }
        ],
        "vout": [
            {
                "n": 0,
                "value": 0.9999,
                "scriptPubKey": {
                    "address": "bc1qoutxxxxxxxxxxxxxxxxxxxxxxxxxxx",
                },
            }
        ],
    }
    flow = build_flow_summary(tx)
    assert flow.inputs_resolved
    assert flow.total_input_btc == 1.0
    assert abs(flow.fee_btc - 0.0001) < 1e-8
    assert flow.senders == ["bc1qsenderxxxxxxxxxxxxxxxxxxxxxxxx"]


def test_partial_inputs_when_prevout_missing() -> None:
    tx = {
        "vin": [{"txid": "bb" * 32, "vout": 1}],
        "vout": [
            {
                "n": 0,
                "value": 0.1,
                "scriptPubKey": {"address": "bc1qoutxxxxxxxxxxxxxxxxxxxxxxxxxxx"},
            }
        ],
    }
    flow = build_flow_summary(tx)
    assert not flow.inputs_resolved
    assert flow.inputs[0].label == "prevout unavailable"
    assert flow.total_output_btc == 0.1