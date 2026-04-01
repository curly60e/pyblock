"""Main menu screen for PyBLOCK TUI."""

from textual.screen import Screen
from textual.widgets import Static, Footer, Header
from textual.containers import Vertical, Horizontal
from textual.binding import Binding
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class MainMenuScreen(Screen):
    """The primary navigation screen."""

    BINDINGS = [
        Binding("a", "select('pyblock')", "PyBLOCK", show=True),
        Binding("b", "select('bitcoin')", "Bitcoin", show=True),
        Binding("l", "select('lightning')", "Lightning", show=True),
        Binding("p", "select('platforms')", "Platforms", show=True),
        Binding("s", "select('settings')", "Settings", show=True),
        Binding("x", "select('donate')", "Donate", show=False),
        Binding("q", "quit", "Quit", show=True),
    ]

    def __init__(self, mode="lite"):
        super().__init__()
        self.mode = mode

    def compose(self):
        yield Static(self._build_menu(), id="main-menu")
        yield Footer()

    def _build_menu(self):
        table = Table(
            show_header=False,
            box=None,
            padding=(0, 2),
            expand=False,
        )
        table.add_column("Key", width=4, justify="right")
        table.add_column("Label", width=30)

        items = [
            ("A", "PyBLOCK Dashboard", "bold red"),
            ("B", "Bitcoin", "bold rgb(255,102,0)"),
        ]
        if self.mode != "onchain_only":
            items.append(("L", "Lightning Network", "bold yellow"))
        items.extend([
            ("P", "Platforms & APIs", "bold rgb(0,200,0)"),
            ("S", "Settings", "bold blue"),
            ("X", "Donate", "bold white"),
            ("Q", "Exit", "bold rgb(128,0,255)"),
        ])

        for key, label, style in items:
            table.add_row(
                Text(f"{key}.", style=style),
                Text(label, style="white"),
            )

        return Panel(
            table,
            title="[bold red]PyBLOCK[/bold red]",
            subtitle="[dim]Navigate with keyboard[/dim]",
            expand=False,
            padding=(1, 2),
        )

    def action_select(self, section):
        self.app.notify(f"Opening {section}...", timeout=2)

    def action_quit(self):
        self.app.exit()
