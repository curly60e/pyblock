"""Address balance and mempool exposure via the local node."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Any

from oraclevision.addresses import parse_address_query, script_type_from_validation
from oraclevision.bitcoin_cli import BitcoinCLI, BitcoinCLIError
from oraclevision.config import InspectorConfig


class AddressQueryError(ValueError):
    """Invalid or unresolvable address query."""


@dataclass
class AddressInspection:
    address: str
    valid: bool = False
    script_type: str = ""
    balance_btc: float = 0.0
    utxo_count: int = 0
    mempool_tx_count: int = 0
    mempool_pending_btc: float = 0.0
    scan_seconds: float | None = None
    error: str | None = None


def format_address_inspection(ins: AddressInspection) -> str:
    lines: list[str] = [
        f"[bold rgb(255,215,0)]Address[/]  {ins.address}",
        "",
    ]
    if ins.error:
        lines.append(f"[red]{ins.error}[/]")
        return "\n".join(lines)

    valid_style = "green" if ins.valid else "red"
    lines.extend([
        f"[bold]Valid[/]       [{valid_style}]{'yes' if ins.valid else 'no'}[/]",
        f"[bold]Type[/]        {ins.script_type or '—'}",
        f"[bold]UTXO balance[/] {ins.balance_btc:.8f} BTC  ({ins.utxo_count} UTXOs)",
    ])
    if ins.scan_seconds is not None:
        lines.append(f"[bold]Scan time[/]   {ins.scan_seconds:.1f}s  (scantxoutset)")
    lines.extend([
        "",
        f"[bold]Mempool[/]     {ins.mempool_tx_count} pending tx(s)  "
        f"·  {ins.mempool_pending_btc:.8f} BTC to this address",
        "",
        "[dim]Balance is confirmed UTXO set only — not full transaction history.[/]",
        "[dim]Enter a txid from mempool exposure to inspect in Transaction mode.[/]",
    ])
    return "\n".join(lines)


class AddressService:
    """Inspect addresses via validateaddress and scantxoutset."""

    def __init__(
        self,
        cli: BitcoinCLI,
        config: InspectorConfig | None = None,
    ) -> None:
        self.cli = cli
        self.config = config or InspectorConfig()

    def inspect(self, raw_query: str) -> AddressInspection:
        address = parse_address_query(raw_query)
        return self.inspect_address(address)

    def inspect_address(self, address: str) -> AddressInspection:
        result = AddressInspection(address=address)

        try:
            validation = self.cli.validate_address(address)
        except BitcoinCLIError as exc:
            result.error = str(exc)
            return result

        result.valid = bool(validation.get("isvalid"))
        result.script_type = script_type_from_validation(validation)

        if result.valid and not result.script_type:
            try:
                info = self.cli.get_address_info(address)
                spk = info.get("scriptPubKey") or {}
                if isinstance(spk, dict) and spk.get("type"):
                    result.script_type = str(spk["type"])
            except BitcoinCLIError:
                pass

        if not result.valid:
            result.error = "Address failed node validation"
            return result

        started = time.monotonic()
        try:
            scan = self.cli.scantxoutset_address(
                address,
                timeout=self.config.scantxoutset_timeout,
            )
            result.scan_seconds = time.monotonic() - started
            if isinstance(scan, dict):
                total = scan.get("total_amount")
                if total is not None:
                    result.balance_btc = float(total)
                unspents = scan.get("unspents")
                if isinstance(unspents, list):
                    result.utxo_count = len(unspents)
        except BitcoinCLIError as exc:
            result.error = f"UTXO scan failed: {exc}"
            return result

        mempool_tx, mempool_btc = self._scan_mempool_for_address(address)
        result.mempool_tx_count = mempool_tx
        result.mempool_pending_btc = mempool_btc
        return result

    def _scan_mempool_for_address(self, address: str) -> tuple[int, float]:
        """Best-effort mempool exposure scan (capped RPC calls)."""
        limit = self.config.mempool_scan_limit
        try:
            mempool = self.cli.get_raw_mempool(verbose=False)
        except BitcoinCLIError:
            return 0, 0.0

        if not isinstance(mempool, list):
            return 0, 0.0

        count = 0
        pending_btc = 0.0
        for txid in mempool[:limit]:
            try:
                tx = self.cli.get_raw_transaction(str(txid), True)
            except BitcoinCLIError:
                continue
            if not isinstance(tx, dict):
                continue
            matched = False
            for vout in tx.get("vout", []):
                if not isinstance(vout, dict):
                    continue
                spk = vout.get("scriptPubKey") or {}
                addr = spk.get("address")
                addrs = spk.get("addresses") or []
                if addr == address or address in addrs:
                    pending_btc += float(vout.get("value", 0) or 0)
                    matched = True
            if matched:
                count += 1
        return count, pending_btc