"""
Terminal UI for OracleVision features inside PyBLOCK.

Don't Trust, Verify — all analysis runs locally against your Knots node.
"""

from __future__ import annotations

import subprocess
import time as t

from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from oraclevision.address_service import AddressService, format_address_inspection
from oraclevision.addresses import AddressQueryError, classify_query
from oraclevision.bip110 import BlockAnalysis, TxAnalysis, analyze_block
from oraclevision.bitcoin_cli import BitcoinCLI, BitcoinCLIError
from oraclevision.config import load_settings
from oraclevision.mempool_compose import analyze_block_template
from oraclevision.security import resolve_executable
from oraclevision.spam_score import status_style
from oraclevision.tx_service import (
    TxInspectContext,
    TxQueryError,
    TxService,
    format_inspection,
)
from shared.display import clear
from shared.rich_ui import console, rich_error, rich_prompt
from shared.ui import show_error


def _header() -> None:
    console.print()
    console.print(
        Panel(
            Text.from_markup(
                "[bold rgb(255,102,0)]OracleVision[/]  ·  "
                "[dim]Don't Trust, Verify[/]\n"
                "[dim]Local BIP-110 & mempool analysis via bitcoin-cli[/]"
            ),
            border_style="rgb(255,102,0)",
        )
    )
    console.print()


def _menu_items() -> None:
    console.print("    [bold cyan]A.[/] BIP-110 Block Scanner")
    console.print("    [bold cyan]B.[/] Mempool Glass (getblocktemplate)")
    console.print("    [bold cyan]C.[/] Block Detail View")
    console.print("    [bold cyan]D.[/] Transaction & Address Inspector")
    console.print("    [bold cyan]E.[/] Launch Full OracleVision TUI")
    console.print("    [bold yellow]R.[/] Return")
    console.print()


def _cli_for(path: dict) -> BitcoinCLI:
    settings = load_settings()
    return BitcoinCLI.from_path_config(
        path,
        datadir=settings.bitcoin_datadir,
        timeout=float(settings.cli_timeout_seconds),
    )


def _inspection_border_style(
    *,
    partial: bool = False,
    has_violation: bool = False,
    is_spam: bool = False,
    address_mode: bool = False,
) -> str:
    if partial:
        return "yellow"
    if has_violation:
        return "red"
    if is_spam:
        return "rgb(255,215,0)"
    if address_mode:
        return "cyan"
    return "green"


def _format_block_row(analysis: BlockAnalysis) -> tuple:
    sig = "Y" if analysis.bip110_signaling else "n"
    flags = []
    if analysis.violation_count:
        flags.append(f"bip110:{analysis.violation_count}")
    if analysis.inscription_count:
        flags.append(f"insc:{analysis.inscription_count}")
    if analysis.brc20_count:
        flags.append(f"brc20:{analysis.brc20_count}")
    if analysis.runes_count:
        flags.append(f"runes:{analysis.runes_count}")
    flag_text = ", ".join(flags) if flags else "—"
    return (
        str(analysis.height),
        analysis.miner_tag[:24],
        str(analysis.spam_score),
        f"[{status_style(analysis.status)}]{analysis.status}[/]",
        sig,
        flag_text,
    )


def scan_recent_blocks(path: dict, count: int | None = None) -> None:
    """Scan recent blocks for BIP-110 violations and spam signals."""
    settings = load_settings()
    count = count or settings.block_scan_count
    cli = _cli_for(path)

    clear()
    _header()
    console.print(f"[dim]Scanning last {count} blocks from your node…[/]\n")

    try:
        tip = cli.get_block_count()
        table = Table(title="BIP-110 Block Scanner", show_lines=True)
        table.add_column("Height", style="cyan", justify="right")
        table.add_column("Miner", style="white")
        table.add_column("Score", justify="right")
        table.add_column("Status")
        table.add_column("BIP110", justify="center")
        table.add_column("Flags", style="dim")

        for height in range(tip, max(tip - count, -1), -1):
            block_hash = cli.get_block_hash(height)
            block = cli.get_block(block_hash, 2)
            analysis = analyze_block(block, spam_threshold=settings.spam_score_threshold)
            table.add_row(*_format_block_row(analysis))

        console.print(table)
        console.print(
            "\n[dim]Score 0-100 · CLEAN / SUSPICIOUS / VIOLATION · "
            "BIP110 = version bit 4 signaling[/]"
        )
    except BitcoinCLIError as exc:
        rich_error(str(exc))
        if exc.hint:
            console.print(f"    [dim]→ {exc.hint}[/]")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        show_error(str(exc))

    input("\n\aContinue...")


def show_mempool_glass(path: dict) -> None:
    """Show Mempool Glass composition from getblocktemplate."""
    cli = _cli_for(path)

    clear()
    _header()
    console.print("[dim]Fetching block template from your node…[/]\n")

    try:
        template = cli.get_block_template()
        composition = analyze_block_template(template, cli.decode_raw_transaction)
        mempool = cli.get_mempool_info()

        if composition.error:
            rich_error(composition.error)
            input("\n\aContinue...")
            return

        summary = Table(title="Mempool Glass — Block Template", show_header=False)
        summary.add_column("Metric", style="cyan")
        summary.add_column("Value", style="white")
        summary.add_row("Template height", str(composition.template_height))
        summary.add_row("Mempool txs", str(mempool.get("size", "?")))
        summary.add_row("Template txs", str(composition.total_tx))
        summary.add_row("Analyzed txs", str(composition.analyzed_tx))
        summary.add_row("Template weight", f"{composition.analyzed_weight:,} / {composition.weight_limit:,}")
        summary.add_row("Fill", f"{composition.fill_pct:.1f}%")
        summary.add_row("Source", composition.source)

        cats = Table(title="Transaction Categories", show_lines=True)
        cats.add_column("Category", style="bold")
        cats.add_column("Count", justify="right")
        cats.add_column("Weight", justify="right")
        cats.add_column("% of template", justify="right")

        rows = [
            ("economic", composition.economic_count, composition.economic_weight, "green"),
            ("consolidation", composition.consolidation_count, composition.consolidation_weight, "cyan"),
            ("coinjoin", composition.coinjoin_count, composition.coinjoin_weight, "blue"),
            ("spam", composition.spam_count, composition.spam_weight, "red"),
        ]
        for name, cnt, wt, color in rows:
            cats.add_row(
                f"[{color}]{name}[/]",
                str(cnt),
                f"{wt:,}",
                f"{composition.pct(wt):.1f}%",
            )

        console.print(summary)
        console.print()
        console.print(cats)
        console.print(
            "\n[dim]Based on your node's current block template (Knots + BIP-110 policy). "
            "Spam = BIP-110 violations, inscriptions, tokens, oversized witness.[/]"
        )
        console.print(
            "[dim]Use [bold]D. Transaction Inspector[/] to drill into a specific txid.[/]"
        )
    except BitcoinCLIError as exc:
        rich_error(str(exc))
        if exc.hint:
            console.print(f"    [dim]→ {exc.hint}[/]")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        show_error(str(exc))

    input("\n\aContinue...")


def _get_flagged_transactions(analysis: BlockAnalysis) -> list[TxAnalysis]:
    """Return problematic transactions sorted by weight (heaviest first)."""
    bad_txs = [
        tx for tx in analysis.transactions
        if tx.has_bip110_violation or tx.is_spam_signal
    ]
    bad_txs.sort(key=lambda tx: tx.weight, reverse=True)
    return bad_txs


def _render_block_detail(analysis: BlockAnalysis) -> BlockAnalysis:
    sig = "YES" if analysis.bip110_signaling else "no"
    title = (
        f"Block #{analysis.height}  ·  Spam {analysis.spam_score}/100  ·  "
        f"{analysis.status}  ·  BIP110 bit4: {sig}"
    )

    info = Table(show_header=False, title=title)
    info.add_column("Field", style="cyan")
    info.add_column("Value")
    info.add_row("Hash", analysis.hash)
    info.add_row("Miner", analysis.miner_tag)
    info.add_row("Weight", f"{analysis.weight:,} ({analysis.tx_count} txs)")
    info.add_row("Witness", f"{analysis.witness_pct:.1f}% of block weight")
    info.add_row("Inscriptions", str(analysis.inscription_count))
    info.add_row("BRC-20", str(analysis.brc20_count))
    info.add_row("Runes", str(analysis.runes_count))
    info.add_row("OP_RETURN", str(analysis.op_return_count))
    info.add_row(
        "BIP-110 violations",
        f"{analysis.violation_count} txs ({analysis.violation_weight:,} wt)",
    )

    console.print(info)
    console.print()

    bad = _get_flagged_transactions(analysis)

    if not bad:
        console.print("[green]No problematic transactions detected.[/]")
        return analysis

    tx_table = Table(title="Problematic Transactions (top 25)", show_lines=True)
    tx_table.add_column("#", justify="right", style="dim")
    tx_table.add_column("TXID", style="red")
    tx_table.add_column("Weight", justify="right")
    tx_table.add_column("BIP-110 flags")
    tx_table.add_column("Signals")

    for idx, tx in enumerate(bad[:25], start=1):
        flags = ", ".join(sorted(tx.bip110_flags)) or "—"
        signals = ", ".join(sorted(tx.signals)) or "—"
        tx_table.add_row(str(idx), tx.txid[:20] + "…", f"{tx.weight:,}", flags, signals)

    console.print(tx_table)
    if len(bad) > 25:
        console.print(f"[dim]… and {len(bad) - 25} more[/]")
    return analysis


def _prompt_tx_inspection_from_block(
    path: dict,
    analysis: BlockAnalysis,
    bad_txs: list[TxAnalysis],
) -> None:
    if not bad_txs:
        return

    console.print()
    choice = input(
        "\033[1;32;40mInspect tx (# or full txid, Enter to skip): \033[0;37;40m"
    ).strip()
    if not choice:
        return

    tx_analysis: TxAnalysis | None = None
    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= min(len(bad_txs), 25):
            tx_analysis = bad_txs[idx - 1]
    else:
        for tx in bad_txs:
            if tx.txid.startswith(choice.lower()) or tx.txid == choice.lower():
                tx_analysis = tx
                break

    if tx_analysis is None:
        show_error("Transaction not found in this block's flagged list")
        input("\n\aContinue...")
        return

    raw_tx = analysis.flagged_raw.get(tx_analysis.txid)
    context = TxInspectContext(
        block_hash=analysis.hash,
        block_height=analysis.height,
        raw_tx=raw_tx,
        cached_analysis=tx_analysis,
    )
    show_tx_inspector(path, context=context, initial_query=tx_analysis.txid)


def show_block_detail(path: dict, target: str | None = None) -> None:
    """Analyze a single block by height or hash."""
    cli = _cli_for(path)
    settings = load_settings()

    clear()
    _header()

    if not target:
        target = input("\033[1;32;40mBlock height or hash: \033[0;37;40m").strip()
    if not target:
        return

    try:
        if target.isdigit():
            block_hash = cli.get_block_hash(int(target))
        else:
            block_hash = target

        console.print(f"[dim]Loading block {block_hash[:16]}…[/]\n")
        block = cli.get_block(block_hash, 2)
        analysis = analyze_block(block, spam_threshold=settings.spam_score_threshold)
        _render_block_detail(analysis)
        _prompt_tx_inspection_from_block(path, analysis, _get_flagged_transactions(analysis))
    except BitcoinCLIError as exc:
        rich_error(str(exc))
        if exc.hint:
            console.print(f"    [dim]→ {exc.hint}[/]")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        show_error(str(exc))

    input("\n\aContinue...")


def _render_tx_inspection(ins) -> None:
    border = _inspection_border_style(
        partial=ins.partial,
        has_violation=ins.analysis.has_bip110_violation,
        is_spam=ins.analysis.is_spam_signal,
    )
    console.print(
        Panel(
            Text.from_markup(format_inspection(ins)),
            title="Transaction Inspector",
            border_style=border,
        )
    )


def _render_address_inspection(ins) -> None:
    console.print(
        Panel(
            Text.from_markup(format_address_inspection(ins)),
            title="Address Inspector",
            border_style=_inspection_border_style(address_mode=True),
        )
    )


def show_tx_inspector(
    path: dict,
    *,
    context: TxInspectContext | None = None,
    initial_query: str | None = None,
) -> None:
    """Interactive transaction and address inspector."""
    settings = load_settings()
    cli = _cli_for(path)
    tx_service = TxService(cli, config=settings.inspector)
    addr_service = AddressService(cli, config=settings.inspector)

    while True:
        clear()
        _header()
        console.print(
            Panel(
                Text.from_markup(
                    "[bold]Transaction & Address Inspector[/]\n"
                    "[dim]Enter a 64-char txid or Bitcoin address (bc1…, 1…, 3…)[/]\n"
                    "[dim]All data verified locally — no third-party explorer[/]"
                ),
                border_style="cyan",
            )
        )
        console.print()

        query = initial_query
        initial_query = None
        if not query:
            query = input(
                "\033[1;32;40mQuery (txid or address, R to return): \033[0;37;40m"
            ).strip()
        if not query or query.upper() == "R":
            return

        try:
            kind, value = classify_query(query)
        except (ValueError, AddressQueryError) as exc:
            rich_error(str(exc))
            input("\n\aContinue...")
            continue

        try:
            if kind == "txid":
                ins = tx_service.inspect_txid(value, context=context)
                _render_tx_inspection(ins)
            else:
                ins = addr_service.inspect_address(value)
                _render_address_inspection(ins)
        except TxQueryError as exc:
            rich_error(str(exc))
        except BitcoinCLIError as exc:
            rich_error(str(exc))
            if exc.hint:
                console.print(f"    [dim]→ {exc.hint}[/]")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            show_error(str(exc))

        console.print()
        follow = input(
            "\033[1;32;40m[N] new query  [R] return to menu: \033[0;37;40m"
        ).strip().upper()
        if follow == "R":
            return
        context = None


def launch_full_oraculovision(path: dict) -> None:
    """Launch the standalone OracleVision Textual TUI if installed."""
    settings = load_settings()
    command = settings.oraculovision_command

    clear()
    _header()

    try:
        launch_cmd = resolve_executable(command)
    except ValueError as exc:
        rich_error(str(exc))
        console.print(
            "    [dim]→ Install OracleVision: pip install -e . from "
            "https://github.com/MarcanoFilms/oraculovision[/]"
        )
        input("\n\aContinue...")
        return

    console.print(f"[dim]Launching {launch_cmd[0]}…[/]\n")
    console.print("[yellow]Press Ctrl+C in OracleVision to return to PyBLOCK.[/]\n")
    t.sleep(1)

    env = dict(**{k: v for k, v in __import__("os").environ.items()})
    if settings.bitcoin_datadir:
        env["BITCOIN_DATADIR"] = settings.bitcoin_datadir
    if path.get("bitcoincli"):
        env["BITCOIN_CLI"] = path["bitcoincli"]

    try:
        # nosemgrep: python.lang.security.audit.dangerous-subprocess-use-audit
        subprocess.run(launch_cmd, env=env, check=False)
    except FileNotFoundError:
        rich_error(f"Could not execute: {launch_cmd[0]}")
    except KeyboardInterrupt:
        pass

    input("\n\aContinue...")


def run_oraclevision_menu(path: dict) -> None:
    """Main OracleVision submenu loop."""
    settings = load_settings()
    if settings.load_error:
        rich_error(f"Config warning: {settings.load_error}")

    while True:
        clear()
        _header()
        _menu_items()
        choice = rich_prompt("Select option").strip().upper()

        if choice in ("A",):
            scan_recent_blocks(path)
        elif choice in ("B",):
            show_mempool_glass(path)
        elif choice in ("C",):
            show_block_detail(path)
        elif choice in ("D",):
            show_tx_inspector(path)
        elif choice in ("E",):
            launch_full_oraculovision(path)
        elif choice in ("R", ""):
            break
        else:
            show_error(f"Invalid option '{choice}'")
            t.sleep(1)