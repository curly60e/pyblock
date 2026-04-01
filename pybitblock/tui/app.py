"""
PyBLOCK Textual TUI Application.

Launch with: python3 -m pybitblock.tui.app
Or from PyBlock.py with: --tui flag
"""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Static, RichLog
from textual.containers import Vertical
from textual.binding import Binding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from tui.widgets.status_bar import StatusBar
from tui.widgets.main_menu import MainMenu
from tui.workers.data_fetcher import (
    fetch_block_height, fetch_btc_price, fetch_fees,
    fetch_mempool_info, fetch_latest_blocks, fetch_hashrate,
)


CSS = """
Screen {
    background: rgb(15, 15, 15);
}

#status-bar {
    dock: top;
    height: 1;
    background: rgb(20, 20, 20);
}

#content {
    height: 1fr;
    padding: 1 2;
    overflow-y: auto;
}

#fees-panel {
    dock: right;
    width: 28;
    height: 100%;
    padding: 1;
    background: rgb(25, 25, 25);
    border-left: solid rgb(50, 50, 50);
}

Footer {
    background: rgb(30, 30, 30);
}
"""


class PyBlockApp(App):
    """PyBLOCK Bitcoin Dashboard TUI."""

    TITLE = "PyBLOCK"
    SUB_TITLE = "Bitcoin Dashboard"
    CSS = CSS

    BINDINGS = [
        Binding("m", "show_menu", "Menu", show=True),
        Binding("a", "select('pyblock')", "Dashboard", show=True),
        Binding("b", "select('bitcoin')", "Bitcoin", show=True),
        Binding("l", "select('lightning')", "Lightning", show=True),
        Binding("p", "select('platforms')", "Platforms", show=True),
        Binding("s", "select('settings')", "Settings", show=True),
        Binding("q", "quit", "Quit", show=True),
        Binding("ctrl+r", "refresh_data", "Refresh", show=True),
    ]

    def __init__(self, mode="lite"):
        super().__init__()
        self.mode = mode
        self._block = "---"
        self._price = "---"
        self._fees = {}

    def compose(self) -> ComposeResult:
        yield StatusBar(id="status-bar")
        yield Vertical(
            MainMenu(mode=self.mode, id="main-menu"),
            id="content",
        )
        yield self._build_fees_panel()
        yield Footer()

    def _build_fees_panel(self):
        return Static(
            "[bold yellow]Fees[/bold yellow]\n"
            "[dim]Loading...[/dim]",
            id="fees-panel",
        )

    def on_mount(self):
        self.query_one(StatusBar).mode = self.mode
        self.set_interval(30, self._do_refresh)
        self._do_refresh()

    def _do_refresh(self):
        self.run_worker(self._refresh_data_worker, thread=True)

    def _refresh_data_worker(self):
        block = fetch_block_height()
        price = fetch_btc_price()
        fees = fetch_fees()
        self.call_from_thread(self._update_status, block, price, fees)

    def _update_status(self, block, price, fees):
        self._block = block
        self._price = price
        self._fees = fees

        status = self.query_one(StatusBar)
        status.block_height = block
        status.btc_price = price

        fees_panel = self.query_one("#fees-panel", Static)
        fees_panel.update(
            f"[bold yellow]Fees (sat/vB)[/bold yellow]\n\n"
            f"[green]Fast:[/green]     {fees.get('fastestFee', '?')}\n"
            f"[yellow]Medium:[/yellow]   {fees.get('halfHourFee', '?')}\n"
            f"[dim]Slow:[/dim]     {fees.get('hourFee', '?')}\n"
        )

    def _set_content(self, renderable):
        """Replace the content area with new renderable."""
        content = self.query_one("#content", Vertical)
        content.remove_children()
        widget = Static(renderable, id="section-view")
        content.mount(widget)

    # --- Actions ---

    def action_show_menu(self):
        content = self.query_one("#content", Vertical)
        content.remove_children()
        content.mount(MainMenu(mode=self.mode, id="main-menu"))

    def action_select(self, section):
        if section == "pyblock":
            self._load_dashboard()
        elif section == "bitcoin":
            self._load_bitcoin()
        elif section == "lightning":
            self._load_lightning()
        elif section == "platforms":
            self._load_platforms()
        elif section == "settings":
            self._load_settings()

    def _load_dashboard(self):
        """Show dashboard with block, price, mempool summary."""
        self.notify("Loading dashboard...", timeout=1)
        self.run_worker(self._fetch_dashboard, thread=True)

    def _fetch_dashboard(self):
        mempool = fetch_mempool_info()
        blocks = fetch_latest_blocks()
        hashrate = fetch_hashrate()
        self.call_from_thread(self._render_dashboard, mempool, blocks, hashrate)

    def _render_dashboard(self, mempool, blocks, hashrate):
        # Summary panel
        summary = Table(show_header=False, box=None, padding=(0, 2))
        summary.add_column("Key", style="bold yellow", width=18)
        summary.add_column("Value", style="bold white")
        summary.add_row("Block Height", str(self._block))
        summary.add_row("BTC Price", f"${self._price}")
        summary.add_row("Hashrate", f"{hashrate['hashrate_eh']} EH/s")
        summary.add_row("Difficulty", hashrate["difficulty"])
        summary.add_row("Mempool Txs", f"{mempool.get('count', '?'):,}" if isinstance(mempool.get('count'), int) else str(mempool.get('count', '?')))
        summary.add_row("Mempool Size", f"{mempool.get('vsize', 0) / 1_000_000:.1f} MvB" if isinstance(mempool.get('vsize'), (int, float)) else "?")
        summary_panel = Panel(summary, title="[bold red]PyBLOCK Dashboard[/bold red]", expand=False, padding=(1, 2))

        # Latest blocks table
        blocks_table = Table(title="Latest Blocks", expand=False, padding=(0, 1))
        blocks_table.add_column("Height", style="bold green", width=10)
        blocks_table.add_column("Txs", style="white", width=8, justify="right")
        blocks_table.add_column("Size (MB)", style="cyan", width=10, justify="right")
        blocks_table.add_column("Pool", style="yellow", width=16)
        for b in blocks:
            blocks_table.add_row(
                str(b["height"]),
                str(b["tx_count"]),
                str(b["size"]),
                b["pool"],
            )
        blocks_panel = Panel(blocks_table, expand=False, padding=(0, 1))

        content = self.query_one("#content", Vertical)
        content.remove_children()
        content.mount(Static(summary_panel, id="dashboard-summary"))
        content.mount(Static(blocks_panel, id="dashboard-blocks"))

    def _load_bitcoin(self):
        """Show Bitcoin info panel."""
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Key", width=4, justify="right")
        table.add_column("Label")
        items = [
            ("A", "Blockchain Info", "bold rgb(255,102,0)"),
            ("C", "Mempool Monitor", "bold rgb(255,102,0)"),
            ("D", "Latest Blocks", "bold rgb(255,102,0)"),
            ("E", "Fee Estimates", "bold rgb(255,102,0)"),
            ("H", "Hashrate & Difficulty", "bold rgb(255,102,0)"),
        ]
        for key, label, style in items:
            table.add_row(Text(f"{key}.", style=style), Text(label, style="white"))

        panel = Panel(table, title="[bold rgb(255,102,0)]Bitcoin[/bold rgb(255,102,0)]",
                      subtitle="[dim]Press M for main menu[/dim]", expand=False, padding=(1, 2))
        self._set_content(panel)
        self.notify("Bitcoin section - submenu navigation coming soon", timeout=2)

    def _load_lightning(self):
        """Show Lightning info panel."""
        panel = Panel(
            "[bold yellow]Lightning Network[/bold yellow]\n\n"
            "Connect your Lightning node to access:\n\n"
            "  [yellow]1.[/yellow] Channel Management\n"
            "  [yellow]2.[/yellow] Create/Pay Invoices\n"
            "  [yellow]3.[/yellow] Keysend Payments\n"
            "  [yellow]4.[/yellow] Node Info & Peers\n"
            "  [yellow]5.[/yellow] Rebalance Channels\n\n"
            f"[dim]Mode: {self.mode} | Press M for main menu[/dim]",
            title="[bold yellow]Lightning[/bold yellow]",
            expand=False,
            padding=(1, 2),
        )
        self._set_content(panel)

    def _load_platforms(self):
        """Show Platforms panel."""
        panel = Panel(
            "[bold green]Platforms & APIs[/bold green]\n\n"
            "  [green]1.[/green] LNBits\n"
            "  [green]2.[/green] OpenNode\n"
            "  [green]3.[/green] TallyCoin\n"
            "  [green]4.[/green] CoinGecko Price\n"
            "  [green]5.[/green] Weather (wttr.in)\n"
            "  [green]6.[/green] Rate.sx Charts\n\n"
            "[dim]Press M for main menu[/dim]",
            title="[bold green]Platforms[/bold green]",
            expand=False,
            padding=(1, 2),
        )
        self._set_content(panel)

    def _load_settings(self):
        """Show Settings panel."""
        panel = Panel(
            "[bold blue]Settings[/bold blue]\n\n"
            f"  [blue]Mode:[/blue]    {self.mode}\n"
            f"  [blue]Block:[/blue]   {self._block}\n"
            f"  [blue]Refresh:[/blue] 30s auto\n\n"
            "  [dim]Logo colors, fonts, and node\n"
            "  configuration available in\n"
            "  classic mode (without --tui)[/dim]\n\n"
            "[dim]Press M for main menu[/dim]",
            title="[bold blue]Settings[/bold blue]",
            expand=False,
            padding=(1, 2),
        )
        self._set_content(panel)

    def action_refresh_data(self):
        self._do_refresh()
        self.notify("Refreshing data...", timeout=1)

    def action_quit(self):
        self.exit()


def run(mode="lite"):
    """Run the PyBLOCK TUI application."""
    app = PyBlockApp(mode=mode)
    app.run()


if __name__ == "__main__":
    run()
