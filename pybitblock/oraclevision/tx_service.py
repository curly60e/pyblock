"""Transaction fetch and deep analysis for PyBLOCK's terminal inspector."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

from oraclevision.bip110 import TxAnalysis, analyze_transaction
from oraclevision.mempool_compose import categorize_transaction
from oraclevision.bitcoin_cli import BitcoinCLI, BitcoinCLIError
from oraclevision.config import InspectorConfig
from oraclevision.markup import safe_markup_text
from oraclevision.tx_flow import TxFlowSummary, TxIO, build_flow_summary, parse_inputs_from_tx

_TXID_RE = re.compile(r"^[0-9a-f]{64}$")


class TxQueryError(ValueError):
    """Invalid or unresolvable transaction query."""


@dataclass
class TxInspectContext:
    """Optional hints when inspecting from Block Detail or Mempool Glass."""

    block_hash: str | None = None
    block_height: int | None = None
    raw_tx: dict[str, Any] | None = None
    cached_analysis: TxAnalysis | None = None


@dataclass
class TxInspection:
    """Full inspection result for a transaction."""

    txid: str
    raw: dict[str, Any]
    analysis: TxAnalysis
    category: str
    in_mempool: bool = False
    confirmed: bool = False
    block_hash: str | None = None
    block_height: int | None = None
    fee_btc: float | None = None
    fee_rate: float | None = None
    mempool_descendant_count: int | None = None
    partial: bool = False
    source_note: str | None = None
    error: str | None = None
    flow: TxFlowSummary | None = None

    @property
    def compliance_label(self) -> str:
        if self.analysis.has_bip110_violation:
            return "BIP-110 VIOLATION"
        if self.analysis.is_spam_signal:
            return "SPAM SIGNAL"
        if self.category != "economic":
            return self.category.upper()
        return "CLEAN"


def parse_tx_query(raw: str) -> str:
    """Validate and normalize a txid query."""
    txid = (raw or "").strip().lower()
    if not txid:
        raise TxQueryError("Enter a 64-character transaction ID (txid)")
    if not _TXID_RE.fullmatch(txid):
        raise TxQueryError("Invalid txid — must be 64 hexadecimal characters")
    return txid


def _category_from_analysis(analysis: TxAnalysis) -> str:
    if analysis.has_bip110_violation or analysis.is_spam_signal:
        return "spam"
    return "economic"


def _truncate_addr(address: str, width: int = 20) -> str:
    if len(address) <= width:
        return address
    return f"{address[:width - 1]}…"


def _format_io_table(title: str, rows: list[TxIO]) -> list[str]:
    lines = [f"[bold rgb(255,215,0)]{title}[/]"]
    if not rows:
        lines.append("  [dim]none[/]")
        return lines
    for io in rows:
        addr = safe_markup_text(_truncate_addr(io.display_address, 44))
        value = f"{io.value_btc:.8f} BTC"
        stype = safe_markup_text(io.script_type)
        lines.append(f"  [{io.index}] {addr}  {value}  ({stype})")
    return lines


class TxService:
    """Fetch and analyze transactions via the local node."""

    def __init__(
        self,
        cli: BitcoinCLI,
        config: InspectorConfig | None = None,
    ) -> None:
        self.cli = cli
        self.config = config or InspectorConfig()

    def inspect(
        self,
        raw_query: str,
        context: TxInspectContext | None = None,
    ) -> TxInspection:
        txid = parse_tx_query(raw_query)
        return self.inspect_txid(txid, context=context)

    def inspect_txid(
        self,
        txid: str,
        *,
        context: TxInspectContext | None = None,
    ) -> TxInspection:
        ctx = context or TxInspectContext()
        in_mempool = False
        mempool_entry: dict[str, Any] | None = None

        try:
            mempool = self.cli.get_raw_mempool(verbose=True)
            if isinstance(mempool, dict) and txid in mempool:
                in_mempool = True
                mempool_entry = mempool[txid]
        except BitcoinCLIError:
            pass

        tx, source_note = self._resolve_raw_tx(txid, ctx)

        if tx is None:
            if ctx.cached_analysis is not None:
                return self._partial_inspection(
                    txid,
                    ctx.cached_analysis,
                    ctx,
                    in_mempool=in_mempool,
                )
            raise TxQueryError(self._not_found_message(txid, ctx))

        if not isinstance(tx, dict):
            raise TxQueryError("Unexpected response from getrawtransaction")

        analysis = analyze_transaction(tx)
        category = categorize_transaction(tx)

        confirmed = bool(tx.get("blockhash") or ctx.block_hash)
        block_hash = tx.get("blockhash") or ctx.block_hash
        block_height = tx.get("blockheight") or ctx.block_height
        if block_height is not None:
            block_height = int(block_height)

        flow = self._enrich_flow(tx)
        fee_btc, fee_rate = _extract_fees(tx, mempool_entry, flow)

        return TxInspection(
            txid=txid,
            raw=tx,
            analysis=analysis,
            category=category,
            in_mempool=in_mempool,
            confirmed=confirmed,
            block_hash=block_hash,
            block_height=block_height,
            fee_btc=fee_btc,
            fee_rate=fee_rate,
            mempool_descendant_count=(
                int(mempool_entry["descendantcount"])
                if mempool_entry and "descendantcount" in mempool_entry
                else None
            ),
            source_note=source_note,
            flow=flow,
        )

    def _enrich_flow(self, tx: dict[str, Any]) -> TxFlowSummary:
        inputs = parse_inputs_from_tx(tx)
        lookups = 0
        max_lookups = max(0, self.config.max_vin_lookups)

        for io in inputs:
            if io.label != "prevout unavailable":
                continue
            if lookups >= max_lookups:
                break
            vin = tx.get("vin", [])
            if io.index >= len(vin):
                continue
            vin_entry = vin[io.index]
            if not isinstance(vin_entry, dict):
                continue
            parent_txid = vin_entry.get("txid")
            parent_vout = vin_entry.get("vout")
            if parent_txid is None or parent_vout is None:
                continue
            try:
                parent = self.cli.get_raw_transaction(str(parent_txid), True)
            except BitcoinCLIError:
                lookups += 1
                continue
            lookups += 1
            if not isinstance(parent, dict):
                continue
            vouts = parent.get("vout", [])
            if not isinstance(parent_vout, int) or parent_vout >= len(vouts):
                continue
            prevout = vouts[parent_vout]
            if not isinstance(prevout, dict):
                continue
            spk = prevout.get("scriptPubKey") or {}
            io.address = spk.get("address") or (
                (spk.get("addresses") or [None])[0]
            )
            io.value_btc = float(prevout.get("value", 0) or 0)
            io.script_type = str(spk.get("type") or "unknown")
            io.label = ""

        return build_flow_summary(tx, resolved_inputs=inputs)

    def _resolve_raw_tx(
        self,
        txid: str,
        ctx: TxInspectContext,
    ) -> tuple[dict[str, Any] | None, str | None]:
        if ctx.raw_tx and isinstance(ctx.raw_tx, dict):
            raw = dict(ctx.raw_tx)
            if not raw.get("txid"):
                raw["txid"] = txid
            return raw, "Loaded from block analysis cache (no extra RPC)"

        attempts: list[tuple[str | None, str]] = [
            (None, "getrawtransaction"),
        ]
        if ctx.block_hash:
            attempts.append((ctx.block_hash, "getrawtransaction + blockhash"))

        last_exc: BitcoinCLIError | None = None
        for block_hash, label in attempts:
            try:
                tx = self.cli.get_raw_transaction(
                    txid,
                    True,
                    block_hash=block_hash,
                )
                if isinstance(tx, dict):
                    note = f"Verified via {label} on your node"
                    if block_hash and label.endswith("blockhash"):
                        note += " (pruned-node compatible)"
                    return tx, note
            except BitcoinCLIError as exc:
                last_exc = exc

        if last_exc:
            _ = last_exc
        return None, None

    def _partial_inspection(
        self,
        txid: str,
        cached: TxAnalysis,
        ctx: TxInspectContext,
        *,
        in_mempool: bool,
    ) -> TxInspection:
        note = (
            "Partial view from block scan — raw tx not on disk "
            "(pruned node or block pruned). Flags and signals are from "
            "getblock analysis at scan time."
        )
        raw = ctx.raw_tx if isinstance(ctx.raw_tx, dict) else {"vin": [], "vout": [], "txid": txid}
        flow = build_flow_summary(raw) if raw.get("vout") else None
        return TxInspection(
            txid=txid,
            raw=raw,
            analysis=cached,
            category=_category_from_analysis(cached),
            in_mempool=in_mempool,
            confirmed=True,
            block_hash=ctx.block_hash,
            block_height=ctx.block_height,
            partial=True,
            source_note=note,
            flow=flow,
        )

    def _not_found_message(self, txid: str, ctx: TxInspectContext) -> str:
        lines = [
            "Transaction not found in mempool or on-disk chain.",
        ]
        try:
            chain = self.cli.get_blockchain_info()
            if chain.get("pruned"):
                prune_h = chain.get("pruneheight", "?")
                lines.append(
                    f"Your node is pruned (prune height #{prune_h:,}). "
                    "Older confirmed txs are not stored unless you pass block context."
                )
                lines.append(
                    "Tip: inspect from Block Detail View after scanning a block, "
                    "or enable txindex=1 on a full archival node."
                )
            else:
                lines.append(
                    "On a full node, enable txindex=1 and reindex for arbitrary history."
                )
        except BitcoinCLIError:
            pass

        if ctx.block_hash:
            lines.append(
                f"Block context #{ctx.block_height or '?'} was provided but "
                "getrawtransaction still failed — block may be pruned away."
            )

        short = f"{txid[:16]}…"
        return f"{lines[0]} ({short})\n" + "\n".join(lines[1:])


def _extract_fees(
    tx: dict[str, Any],
    mempool_entry: dict[str, Any] | None,
    flow: TxFlowSummary | None,
) -> tuple[float | None, float | None]:
    """Return (fee_btc, fee_rate_sat_vb) when available."""
    fee_btc: float | None = None
    fee_rate: float | None = None

    if mempool_entry:
        fees = mempool_entry.get("fees") or {}
        base = fees.get("base")
        if base is not None:
            fee_btc = float(base)
        vsize = int(mempool_entry.get("vsize") or tx.get("vsize") or 0)
        if fee_btc is not None and vsize > 0:
            fee_rate = (fee_btc * 100_000_000) / vsize

    if fee_btc is None and "fee" in tx:
        fee_btc = float(tx["fee"])
        vsize = int(tx.get("vsize") or 0)
        if vsize > 0:
            fee_rate = (abs(fee_btc) * 100_000_000) / vsize

    if fee_btc is None and flow and flow.fee_btc is not None:
        fee_btc = flow.fee_btc
        vsize = int(tx.get("vsize") or 0)
        if vsize > 0:
            fee_rate = (fee_btc * 100_000_000) / vsize

    return fee_btc, fee_rate


def format_inspection(ins: TxInspection) -> str:
    """Render inspection as Rich markup text."""
    a = ins.analysis
    lines: list[str] = []

    if ins.partial:
        lines.extend([
            "[yellow bold]PARTIAL INSPECTION[/]",
            f"[dim]{ins.source_note}[/]",
            "",
        ])
    elif ins.source_note:
        lines.extend([
            f"[dim]{ins.source_note}[/]",
            "",
        ])

    lines.extend([
        f"[bold rgb(255,215,0)]Transaction[/]  {ins.txid}",
        "",
        f"[bold]Status[/]      "
        + ("mempool" if ins.in_mempool else "not in mempool")
        + ("  ·  confirmed" if ins.confirmed else "  ·  unconfirmed"),
    ])

    if ins.block_height is not None:
        lines.append(f"[bold]Block[/]       #{ins.block_height}  {ins.block_hash or ''}")
    if ins.fee_btc is not None:
        fee_line = f"[bold]Fee[/]         {ins.fee_btc:.8f} BTC"
        if ins.fee_rate is not None:
            fee_line += f"  ({ins.fee_rate:.2f} sat/vB)"
        lines.append(fee_line)
    if ins.mempool_descendant_count is not None:
        lines.append(
            f"[bold]Descendants[/] {ins.mempool_descendant_count} in mempool package"
        )

    if ins.flow:
        flow = ins.flow
        lines.extend(["", "[bold rgb(255,215,0)]─── FLOW ───[/]"])
        in_note = f"  ({len(flow.inputs)} inputs)"
        out_note = f"  ({len(flow.outputs)} outputs)"
        if flow.inputs_resolved or flow.total_input_btc > 0:
            lines.append(f"  In:   {flow.total_input_btc:.8f} BTC{in_note}")
        elif flow.inputs_partial:
            lines.append(f"  In:   [dim]partial — some prevouts unavailable (pruned)[/]{in_note}")
        else:
            lines.append(f"  In:   [dim]unknown (prevouts not resolved)[/]{in_note}")
        lines.append(f"  Out:  {flow.total_output_btc:.8f} BTC{out_note}")
        if flow.senders:
            senders = ", ".join(_truncate_addr(a) for a in flow.senders[:4])
            lines.append(f"  From: {safe_markup_text(senders)}")
        if flow.recipients:
            recips = ", ".join(_truncate_addr(a) for a in flow.recipients[:4])
            lines.append(f"  To:   {safe_markup_text(recips)}")
        lines.append("")
        lines.extend(_format_io_table("INPUTS", flow.inputs))
        lines.append("")
        lines.extend(_format_io_table("OUTPUTS", flow.outputs))

    cat_style = {
        "economic": "green",
        "spam": "red bold",
        "coinjoin": "blue",
        "consolidation": "cyan",
    }.get(ins.category, "white")

    comp_style = (
        "red bold" if a.has_bip110_violation
        else "yellow" if a.is_spam_signal
        else "green"
    )

    lines.extend([
        "",
        f"[bold]Size[/]        weight {a.weight:,}  ·  vsize {a.vsize:,}",
        f"[bold]Witness[/]    {a.witness_bytes:,} bytes",
        f"[bold]Category[/]   [{cat_style}]{ins.category}[/]",
        f"[bold]Compliance[/] [{comp_style}]{ins.compliance_label}[/]",
        "",
        "[bold rgb(255,215,0)]BIP-110 flags[/]",
    ])

    if a.bip110_flags:
        lines.append("  " + ", ".join(sorted(a.bip110_flags)))
    else:
        lines.append("  [green]none[/]")

    lines.append("[bold rgb(255,215,0)]Spam signals[/]")
    if a.signals:
        lines.append("  " + ", ".join(sorted(a.signals)))
    else:
        lines.append("  [green]none[/]")

    if ins.partial:
        lines.extend([
            "",
            "[dim]Full input addresses require prevout in block cache or archival node[/]",
        ])
    else:
        lines.extend([
            "",
            "[dim]Verified locally via your node — no third-party explorer[/]",
        ])
    return "\n".join(lines)