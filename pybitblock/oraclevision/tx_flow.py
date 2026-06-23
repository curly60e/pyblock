"""Pure transaction flow parsing — inputs, outputs, amounts."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TxIO:
    index: int
    address: str | None
    value_btc: float
    script_type: str
    role: str
    label: str = ""

    @property
    def display_address(self) -> str:
        if self.label:
            return self.label
        if self.address:
            return self.address
        if self.script_type == "nulldata":
            return "OP_RETURN"
        return "unknown"


@dataclass
class TxFlowSummary:
    inputs: list[TxIO] = field(default_factory=list)
    outputs: list[TxIO] = field(default_factory=list)
    total_input_btc: float = 0.0
    total_output_btc: float = 0.0
    fee_btc: float | None = None
    senders: list[str] = field(default_factory=list)
    recipients: list[str] = field(default_factory=list)
    inputs_resolved: bool = False
    inputs_partial: bool = False

    @property
    def all_addresses(self) -> list[str]:
        seen: set[str] = set()
        ordered: list[str] = []
        for io in (*self.inputs, *self.outputs):
            if io.address and io.address not in seen:
                seen.add(io.address)
                ordered.append(io.address)
        return ordered


def _script_address(spk: dict[str, Any]) -> str | None:
    if not spk:
        return None
    addr = spk.get("address")
    if isinstance(addr, str) and addr:
        return addr
    addresses = spk.get("addresses")
    if isinstance(addresses, list) and addresses:
        first = addresses[0]
        if isinstance(first, str) and first:
            return first
    return None


def _script_type(spk: dict[str, Any]) -> str:
    return str(spk.get("type") or spk.get("asm", "unknown") or "unknown")


def _is_op_return(spk: dict[str, Any]) -> bool:
    return _script_type(spk) in ("nulldata", "op_return") or str(spk.get("asm", "")).startswith("OP_RETURN")


def parse_outputs(tx: dict[str, Any]) -> list[TxIO]:
    outputs: list[TxIO] = []
    for vout in tx.get("vout", []):
        if not isinstance(vout, dict):
            continue
        index = int(vout.get("n", len(outputs)))
        spk = vout.get("scriptPubKey") or {}
        value = float(vout.get("value", 0) or 0)
        script_type = _script_type(spk)
        if _is_op_return(spk):
            outputs.append(
                TxIO(
                    index=index,
                    address=None,
                    value_btc=value,
                    script_type="nulldata",
                    role="output",
                    label="OP_RETURN",
                )
            )
            continue
        outputs.append(
            TxIO(
                index=index,
                address=_script_address(spk),
                value_btc=value,
                script_type=script_type,
                role="output",
            )
        )
    return outputs


def parse_inputs_from_tx(tx: dict[str, Any]) -> list[TxIO]:
    inputs: list[TxIO] = []
    for idx, vin in enumerate(tx.get("vin", [])):
        if not isinstance(vin, dict):
            continue
        if vin.get("coinbase"):
            inputs.append(
                TxIO(
                    index=idx,
                    address=None,
                    value_btc=0.0,
                    script_type="coinbase",
                    role="input",
                    label="coinbase",
                )
            )
            continue

        prevout = vin.get("prevout")
        if isinstance(prevout, dict):
            spk = prevout.get("scriptPubKey") or {}
            value = float(prevout.get("value", 0) or 0)
            inputs.append(
                TxIO(
                    index=idx,
                    address=_script_address(spk),
                    value_btc=value,
                    script_type=_script_type(spk),
                    role="input",
                )
            )
        else:
            inputs.append(
                TxIO(
                    index=idx,
                    address=None,
                    value_btc=0.0,
                    script_type="unknown",
                    role="input",
                    label="prevout unavailable",
                )
            )
    return inputs


def build_flow_summary(
    tx: dict[str, Any],
    *,
    resolved_inputs: list[TxIO] | None = None,
) -> TxFlowSummary:
    """Build economic flow summary from a raw transaction dict."""
    outputs = parse_outputs(tx)
    inputs = resolved_inputs if resolved_inputs is not None else parse_inputs_from_tx(tx)

    spend_inputs = [io for io in inputs if io.label != "coinbase"]
    known_inputs = [io for io in spend_inputs if io.label != "prevout unavailable" and io.address]
    inputs_resolved = bool(spend_inputs) and all(
        io.label != "prevout unavailable" for io in spend_inputs
    )
    inputs_partial = bool(spend_inputs) and not inputs_resolved and bool(known_inputs)

    total_in = sum(io.value_btc for io in known_inputs)
    total_out = sum(io.value_btc for io in outputs if io.script_type != "nulldata")

    fee_btc: float | None = None
    if inputs_resolved and total_in > 0:
        fee_btc = max(0.0, total_in - total_out)

    senders = list(dict.fromkeys(io.address for io in known_inputs if io.address))
    recipients = list(
        dict.fromkeys(
            io.address for io in outputs
            if io.address and io.script_type != "nulldata"
        )
    )

    return TxFlowSummary(
        inputs=inputs,
        outputs=outputs,
        total_input_btc=total_in,
        total_output_btc=total_out,
        fee_btc=fee_btc,
        senders=senders,
        recipients=recipients,
        inputs_resolved=inputs_resolved,
        inputs_partial=inputs_partial,
    )