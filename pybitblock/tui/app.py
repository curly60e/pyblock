"""
PyBLOCK Textual TUI Application.

Launch with: python3 -m pybitblock.tui.app
Or from PyBlock.py with: --tui flag
"""

from textual.app import App, ComposeResult
from textual.widgets import Footer, Static
from textual.containers import Vertical
from textual.timer import Timer
from textual.binding import Binding

from tui.widgets.status_bar import StatusBar
from tui.screens.main_menu import MainMenuScreen
from tui.workers.data_fetcher import fetch_block_height, fetch_btc_price, fetch_fees


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
        Binding("ctrl+q", "quit", "Quit", show=True, priority=True),
        Binding("ctrl+r", "refresh_data", "Refresh", show=True),
    ]

    def __init__(self, mode="lite"):
        super().__init__()
        self.mode = mode
        self._update_timer = None

    def compose(self) -> ComposeResult:
        yield StatusBar(id="status-bar")
        yield Vertical(
            MainMenuScreen(mode=self.mode),
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
        self._update_timer = self.set_interval(30, self._refresh_data)
        self.run_worker(self._initial_load)

    async def _initial_load(self):
        await self._refresh_data()

    async def _refresh_data(self):
        block = await self.run_in_thread(fetch_block_height)
        price = await self.run_in_thread(fetch_btc_price)
        fees = await self.run_in_thread(fetch_fees)

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

    def action_refresh_data(self):
        self.run_worker(self._refresh_data)
        self.notify("Refreshing data...", timeout=1)

    def action_quit(self):
        self.exit()


def run(mode="lite"):
    """Run the PyBLOCK TUI application."""
    app = PyBlockApp(mode=mode)
    app.run()


if __name__ == "__main__":
    run()
