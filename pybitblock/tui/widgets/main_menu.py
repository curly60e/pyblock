"""Main menu widget for PyBLOCK TUI."""

from textual.widgets import Static
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class MainMenu(Static):
    """The primary navigation menu rendered as a widget."""

    def __init__(self, mode="lite", **kwargs):
        super().__init__(**kwargs)
        self.mode = mode

    def on_mount(self):
        self.update(self._build_menu())

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
