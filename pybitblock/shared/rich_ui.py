"""
Rich-based UI components for PyBLOCK.

Provides styled menus, status bars, error panels, and progress indicators
using the Rich library. Falls back to ANSI equivalents from shared.ui if needed.
"""

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.columns import Columns
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn
from rich.style import Style
from rich.theme import Theme

# PyBLOCK theme
PYBLOCK_THEME = Theme({
    "pyblock.title": "bold red",
    "pyblock.mode.local": "bold green",
    "pyblock.mode.remote": "bold cyan",
    "pyblock.mode.lite": "bold yellow",
    "pyblock.mode.onchain": "bold yellow",
    "pyblock.menu.key": "bold green",
    "pyblock.menu.label": "white",
    "pyblock.menu.bitcoin": "bold rgb(255,102,0)",
    "pyblock.menu.lightning": "bold yellow",
    "pyblock.menu.platforms": "bold rgb(0,200,0)",
    "pyblock.menu.settings": "bold blue",
    "pyblock.menu.donate": "bold white",
    "pyblock.menu.exit": "bold rgb(128,0,255)",
    "pyblock.error": "bold red",
    "pyblock.warning": "bold yellow",
    "pyblock.success": "bold green",
    "pyblock.dim": "dim white",
    "pyblock.price": "bold green",
    "pyblock.block": "bold white",
})

console = Console(theme=PYBLOCK_THEME)


def rich_status_bar(mode="", block_height="", btc_price="", extra=""):
    """Render a styled status bar with mode, block height, and BTC price."""
    mode_styles = {
        "local": "pyblock.mode.local",
        "remote": "pyblock.mode.remote",
        "onchain_only": "pyblock.mode.onchain",
        "lite": "pyblock.mode.lite",
    }
    mode_labels = {
        "local": "Bitcoin + Lightning",
        "remote": "Remote Node",
        "onchain_only": "Bitcoin Only",
        "lite": "Lite Mode",
    }

    parts = []
    label = mode_labels.get(mode, mode)
    style = mode_styles.get(mode, "white")
    if label:
        parts.append(Text(label, style=style))
    if block_height:
        t = Text()
        t.append("Block: ", style="pyblock.dim")
        t.append(block_height, style="pyblock.block")
        parts.append(t)
    if btc_price:
        t = Text()
        t.append("BTC: ", style="pyblock.dim")
        t.append(f"${btc_price}", style="pyblock.price")
        parts.append(t)
    if extra:
        parts.append(Text(extra))

    separator = Text(" | ", style="pyblock.dim")
    combined = Text()
    for i, part in enumerate(parts):
        if i > 0:
            combined.append_text(separator)
        combined.append_text(part)

    console.print(Panel(combined, style="pyblock.dim", expand=False, padding=(0, 2)))


def rich_sysinfo(cpu_percent, mem_percent):
    """Render CPU and Memory as a compact Rich panel."""
    cpu_color = "green" if cpu_percent < 70 else ("yellow" if cpu_percent < 90 else "red")
    mem_color = "green" if mem_percent < 70 else ("yellow" if mem_percent < 90 else "red")

    cpu_bar = _make_bar(cpu_percent, cpu_color)
    mem_bar = _make_bar(mem_percent, mem_color)

    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(width=10)
    table.add_column(width=22)
    table.add_column(width=5, justify="right")
    table.add_row(
        Text("CPU", style="italic yellow"),
        Text.from_markup(cpu_bar),
        Text(f"{cpu_percent}%", style=f"bold {cpu_color}"),
    )
    table.add_row(
        Text("Memory", style="italic yellow"),
        Text.from_markup(mem_bar),
        Text(f"{mem_percent}%", style=f"bold {mem_color}"),
    )
    console.print(table)


def _make_bar(percent, color):
    """Create a simple text-based progress bar."""
    filled = int(percent / 5)
    empty = 20 - filled
    return f"[{color}]{'█' * filled}[/{color}][dim]{'░' * empty}[/dim]"


def rich_menu(title, items, footer_text=""):
    """Render a styled menu table.

    Args:
        title: Menu section title
        items: List of (key, label, style) tuples
        footer_text: Optional text below the menu
    """
    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        pad_edge=False,
    )
    table.add_column("Key", width=6, justify="right")
    table.add_column("Label")

    for key, label, style in items:
        table.add_row(
            Text(f"{key}.", style=f"bold {style}"),
            Text(label, style="white"),
        )

    console.print()
    console.print(table)
    if footer_text:
        console.print(f"    [pyblock.dim]{footer_text}[/pyblock.dim]")
    console.print()


def rich_error(message):
    """Display error in a red panel."""
    console.print(Panel(
        Text(f" {message}", style="white"),
        title="Error",
        title_align="left",
        style="pyblock.error",
        expand=False,
        padding=(0, 1),
    ))


def rich_warning(message):
    """Display warning in a yellow panel."""
    console.print(Panel(
        Text(f" {message}", style="white"),
        title="Warning",
        title_align="left",
        style="pyblock.warning",
        expand=False,
        padding=(0, 1),
    ))


def rich_success(message):
    """Display success message."""
    console.print(f"    [pyblock.success]✓[/pyblock.success] {message}")


def rich_header(node_type, block_height, version, alias=None):
    """Render the main menu header with node info."""
    info = Text()
    info.append(f"{node_type}", style="bold white")
    info.append(": ", style="dim")
    info.append("PyBLOCK", style="bold red")
    info.append("\n")
    if alias:
        info.append("Node: ", style="bold white")
        info.append(f"{alias}", style="bold yellow")
        info.append("\n")
    info.append("Block: ", style="bold white")
    info.append(f"{block_height}", style="bold green")
    info.append("  ")
    info.append("Version: ", style="bold white")
    info.append(f"{version}", style="dim")

    console.print(Panel(info, style="pyblock.dim", expand=False, padding=(0, 2)))


def rich_loading(label="Loading"):
    """Create a Rich progress context for loading operations."""
    return Progress(
        SpinnerColumn(),
        TextColumn("[pyblock.dim]{task.description}"),
        transient=True,
        console=console,
    )


def rich_prompt(prompt_text="Select option"):
    """Styled input prompt."""
    console.print(f"    [bold green]{prompt_text}:[/bold green] ", end="")
    return input("")
