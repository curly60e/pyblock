"""Persistent status bar widget showing mode, block height, and BTC price."""

from textual.widgets import Static
from textual.reactive import reactive
from rich.text import Text


class StatusBar(Static):
    """Top status bar with live-updating Bitcoin data."""

    mode = reactive("lite")
    block_height = reactive("---")
    btc_price = reactive("---")
    node_alias = reactive("")

    MODE_LABELS = {
        "local": ("Bitcoin + Lightning", "green"),
        "remote": ("Remote Node", "cyan"),
        "onchain_only": ("Bitcoin Only", "yellow"),
        "lite": ("Lite Mode", "yellow"),
    }

    def render(self):
        label, color = self.MODE_LABELS.get(self.mode, (self.mode, "white"))

        text = Text()
        text.append(f" {label} ", style=f"bold {color} on rgb(30,30,30)")
        text.append("  ", style="on rgb(20,20,20)")
        text.append(f" Block: ", style="dim on rgb(20,20,20)")
        text.append(f"{self.block_height} ", style="bold white on rgb(20,20,20)")
        text.append("  ", style="on rgb(20,20,20)")
        text.append(f" BTC: ", style="dim on rgb(20,20,20)")
        text.append(f"${self.btc_price} ", style="bold green on rgb(20,20,20)")
        if self.node_alias:
            text.append("  ", style="on rgb(20,20,20)")
            text.append(f" Node: {self.node_alias} ", style="bold yellow on rgb(20,20,20)")

        return text
