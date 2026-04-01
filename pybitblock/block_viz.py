"""
PyBLOCK Interactive Block Visualizer.

A colorful, interactive treemap of Bitcoin block transactions.
Works with both local bitcoin-cli and mempool.space API.

Launch: python3 block_viz.py [block_height]
"""

import json
import math
import os
import subprocess
import sys
import time

import requests
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.layout import Layout
from rich.style import Style
from rich.color import Color

console = Console()

# ─── Fee color scale (purple → blue → green → yellow → orange → red) ───
FEE_COLORS = [
    (68, 1, 84),      # very low - dark purple
    (59, 82, 139),     # low - blue
    (33, 145, 140),    # below avg - teal
    (94, 201, 98),     # avg - green
    (253, 231, 37),    # above avg - yellow
    (253, 174, 37),    # high - orange
    (237, 105, 37),    # very high - dark orange
    (215, 48, 31),     # extreme - red
]


def fee_to_color(fee_rate, min_rate=1, max_rate=100):
    """Map a fee rate to an RGB color using the scale."""
    if max_rate <= min_rate:
        t = 0.5
    else:
        t = min(1.0, max(0.0, (fee_rate - min_rate) / (max_rate - min_rate)))

    idx = t * (len(FEE_COLORS) - 1)
    lo = int(idx)
    hi = min(lo + 1, len(FEE_COLORS) - 1)
    frac = idx - lo

    r = int(FEE_COLORS[lo][0] * (1 - frac) + FEE_COLORS[hi][0] * frac)
    g = int(FEE_COLORS[lo][1] * (1 - frac) + FEE_COLORS[hi][1] * frac)
    b = int(FEE_COLORS[lo][2] * (1 - frac) + FEE_COLORS[hi][2] * frac)
    return r, g, b


def fee_to_style(fee_rate, min_rate=1, max_rate=100):
    """Get a Rich Style for a fee rate."""
    r, g, b = fee_to_color(fee_rate, min_rate, max_rate)
    return Style(bgcolor=f"rgb({r},{g},{b})", color="white" if (r + g + b) < 380 else "black")


# ─── Data Fetching ───

def fetch_block_api(height=None):
    """Fetch block data from mempool.space API."""
    try:
        if height is None:
            tip = requests.get("https://mempool.space/api/blocks/tip/height", timeout=5).json()
            height = tip

        block_hash = requests.get(f"https://mempool.space/api/block-height/{height}", timeout=5).text
        block = requests.get(f"https://mempool.space/api/block/{block_hash}", timeout=5).json()
        txs = requests.get(f"https://mempool.space/api/block/{block_hash}/txs/0", timeout=5).json()

        # Get more txs if needed (API returns 25 at a time)
        all_txs = txs
        if block.get("tx_count", 0) > 25:
            for i in range(25, min(block["tx_count"], 200), 25):
                more = requests.get(f"https://mempool.space/api/block/{block_hash}/txs/{i}", timeout=5).json()
                all_txs.extend(more)

        transactions = []
        for tx in all_txs:
            fee = tx.get("fee", 0)
            vsize = tx.get("weight", tx.get("size", 1) * 4) / 4
            fee_rate = fee / max(vsize, 1)
            transactions.append({
                "txid": tx.get("txid", "")[:16],
                "fee": fee,
                "vsize": int(vsize),
                "fee_rate": round(fee_rate, 1),
                "inputs": len(tx.get("vin", [])),
                "outputs": len(tx.get("vout", [])),
            })

        transactions.sort(key=lambda x: x["fee_rate"], reverse=True)

        pool = block.get("extras", {}).get("pool", {}).get("name", "Unknown")
        return {
            "height": block.get("height", height),
            "hash": block_hash[:16] + "...",
            "timestamp": block.get("timestamp", 0),
            "tx_count": block.get("tx_count", len(all_txs)),
            "size_mb": round(block.get("size", 0) / 1_000_000, 2),
            "weight_mu": round(block.get("weight", 0) / 1_000_000, 2),
            "pool": pool,
            "transactions": transactions,
            "total_fee": sum(t["fee"] for t in transactions),
        }
    except Exception as e:
        return {"error": str(e)}


def fetch_block_cli(height=None):
    """Fetch block data from local bitcoin-cli."""
    try:
        path = {}
        if os.path.isfile("config/bclock.conf"):
            with open("config/bclock.conf", "r") as f:
                path = json.load(f)

        cli = path.get("bitcoincli", "bitcoin-cli")
        if not cli:
            return fetch_block_api(height)

        if height is None:
            block_hash = subprocess.run([cli, "getbestblockhash"],
                                         capture_output=True, text=True).stdout.strip()
        else:
            block_hash = subprocess.run([cli, "getblockhash", str(height)],
                                         capture_output=True, text=True).stdout.strip()

        block_json = subprocess.run([cli, "getblock", block_hash, "2"],
                                     capture_output=True, text=True).stdout
        block = json.loads(block_json)

        transactions = []
        for tx in block.get("tx", [])[:200]:
            fee = tx.get("fee", 0)
            vsize = tx.get("vsize", tx.get("size", 1))
            fee_rate = (fee * 100_000_000) / max(vsize, 1)  # fee is in BTC
            transactions.append({
                "txid": tx.get("txid", "")[:16],
                "fee": int(fee * 100_000_000),
                "vsize": vsize,
                "fee_rate": round(fee_rate, 1),
                "inputs": len(tx.get("vin", [])),
                "outputs": len(tx.get("vout", [])),
            })

        transactions.sort(key=lambda x: x["fee_rate"], reverse=True)

        return {
            "height": block.get("height", height),
            "hash": block_hash[:16] + "...",
            "timestamp": block.get("time", 0),
            "tx_count": block.get("nTx", len(transactions)),
            "size_mb": round(block.get("size", 0) / 1_000_000, 2),
            "weight_mu": round(block.get("weight", 0) / 1_000_000, 2),
            "pool": "Local Node",
            "transactions": transactions,
            "total_fee": sum(t["fee"] for t in transactions),
        }
    except Exception:
        return fetch_block_api(height)


# ─── Rendering ───

def render_treemap(transactions, width=70, height=20):
    """Render a treemap of transactions as colored blocks."""
    if not transactions:
        return Text("No transactions", style="dim")

    fee_rates = [t["fee_rate"] for t in transactions]
    min_rate = min(fee_rates) if fee_rates else 1
    max_rate = max(fee_rates) if fee_rates else 100

    total_vsize = sum(t["vsize"] for t in transactions)
    if total_vsize == 0:
        return Text("Empty block", style="dim")

    # Build grid
    grid = [[None for _ in range(width)] for _ in range(height)]
    cursor_x, cursor_y = 0, 0

    for tx in transactions:
        area = max(1, int((tx["vsize"] / total_vsize) * width * height * 0.85))
        rect_w = max(1, min(int(math.sqrt(area * 2)), width - cursor_x))
        rect_h = max(1, min(area // max(rect_w, 1), height - cursor_y))

        if cursor_x + rect_w > width:
            cursor_x = 0
            cursor_y += rect_h
            if cursor_y >= height:
                break

        r, g, b = fee_to_color(tx["fee_rate"], min_rate, max_rate)
        for dy in range(rect_h):
            for dx in range(rect_w):
                gy, gx = cursor_y + dy, cursor_x + dx
                if gy < height and gx < width:
                    grid[gy][gx] = (r, g, b, tx)

        cursor_x += rect_w
        if cursor_x >= width:
            cursor_x = 0
            cursor_y += rect_h

    # Render grid to Text
    text = Text()
    for row in grid:
        for cell in row:
            if cell is None:
                text.append("░", style="rgb(40,40,40)")
            else:
                r, g, b, tx = cell
                luma = r * 0.299 + g * 0.587 + b * 0.114
                fg = "black" if luma > 128 else "white"
                text.append("█", style=f"{fg} on rgb({r},{g},{b})")
        text.append("\n")

    return text


def render_legend(min_rate=1, max_rate=100, width=50):
    """Render a color legend bar for fee rates."""
    text = Text()
    text.append("    Fee Rate (sat/vB): ", style="dim")
    text.append(f"{min_rate:.0f}", style="bold")
    text.append(" ")

    steps = min(width, 40)
    for i in range(steps):
        rate = min_rate + (max_rate - min_rate) * (i / steps)
        r, g, b = fee_to_color(rate, min_rate, max_rate)
        text.append("█", style=f"rgb({r},{g},{b})")

    text.append(" ")
    text.append(f"{max_rate:.0f}", style="bold")
    text.append(" sat/vB", style="dim")
    return text


def render_block_header(block_data):
    """Render block info header."""
    b = block_data
    ts = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(b.get("timestamp", 0)))

    table = Table(show_header=False, box=None, padding=(0, 2), expand=False)
    table.add_column("Key", style="bold yellow", width=14)
    table.add_column("Value", style="bold white")

    table.add_row("Block", f"[bold green]{b.get('height', '?')}[/]")
    table.add_row("Hash", f"[dim]{b.get('hash', '?')}[/]")
    table.add_row("Pool", f"[bold cyan]{b.get('pool', '?')}[/]")
    table.add_row("Transactions", f"{b.get('tx_count', '?'):,}")
    table.add_row("Size", f"{b.get('size_mb', '?')} MB")
    table.add_row("Weight", f"{b.get('weight_mu', '?')} MWU")
    table.add_row("Total Fees", f"[bold yellow]{b.get('total_fee', 0):,}[/] sats")
    table.add_row("Time", f"[dim]{ts}[/]")

    return Panel(table, title="[bold red]Block Info[/]", style="on default",
                 border_style="bright_yellow", expand=False, padding=(0, 1))


def render_top_transactions(transactions, n=8):
    """Render table of top fee transactions."""
    table = Table(expand=False, padding=(0, 1))
    table.add_column("#", style="dim", width=3, justify="right")
    table.add_column("TXID", style="cyan", width=16)
    table.add_column("Fee", style="yellow", width=10, justify="right")
    table.add_column("Rate", width=8, justify="right")
    table.add_column("vSize", style="dim", width=8, justify="right")
    table.add_column("In/Out", style="dim", width=7)

    for i, tx in enumerate(transactions[:n], 1):
        rate = tx["fee_rate"]
        r, g, b = fee_to_color(rate,
                                min(t["fee_rate"] for t in transactions),
                                max(t["fee_rate"] for t in transactions))
        rate_style = f"bold rgb({r},{g},{b})"
        table.add_row(
            str(i),
            tx["txid"],
            f"{tx['fee']:,}",
            Text(f"{rate:.1f}", style=rate_style),
            f"{tx['vsize']:,}",
            f"{tx['inputs']}/{tx['outputs']}",
        )

    return Panel(table, title="[bold yellow]Top Fee Transactions[/]", style="on default",
                 border_style="yellow", expand=False, padding=(0, 1))


def render_fee_distribution(transactions):
    """Render fee rate distribution histogram."""
    if not transactions:
        return Text("No data")

    rates = [t["fee_rate"] for t in transactions]
    min_r, max_r = min(rates), max(rates)

    # Create 8 buckets
    buckets = 8
    if max_r <= min_r:
        counts = [len(rates)] + [0] * (buckets - 1)
        edges = [min_r] * (buckets + 1)
    else:
        step = (max_r - min_r) / buckets
        edges = [min_r + i * step for i in range(buckets + 1)]
        counts = [0] * buckets
        for r in rates:
            idx = min(int((r - min_r) / step), buckets - 1)
            counts[idx] += 1

    max_count = max(counts) if counts else 1
    bar_width = 20

    text = Text()
    for i in range(buckets):
        lo, hi = edges[i], edges[i + 1]
        mid_rate = (lo + hi) / 2
        r, g, b = fee_to_color(mid_rate, min_r, max_r)
        bar_len = int((counts[i] / max_count) * bar_width) if max_count > 0 else 0

        text.append(f"  {lo:6.1f}-{hi:6.1f} ", style="dim")
        text.append("█" * bar_len, style=f"rgb({r},{g},{b})")
        text.append(f" {counts[i]}", style="dim")
        text.append("\n")

    return Panel(text, title="[bold magenta]Fee Distribution[/]", style="on default",
                 border_style="magenta", expand=False, padding=(0, 1))


def render_full_block(block_data, term_width=None):
    """Render the complete block visualization."""
    if "error" in block_data:
        return Panel(f"[bold red]Error:[/] {block_data['error']}", style="on default",
                     border_style="red")

    if term_width is None:
        term_width = console.width

    txs = block_data.get("transactions", [])
    fee_rates = [t["fee_rate"] for t in txs] if txs else [0]
    min_rate = min(fee_rates)
    max_rate = max(fee_rates)

    map_width = min(term_width - 4, 80)
    map_height = min(22, max(10, len(txs) // 20))

    treemap = render_treemap(txs, width=map_width, height=map_height)
    legend = render_legend(min_rate, max_rate, width=map_width)
    header = render_block_header(block_data)
    top_txs = render_top_transactions(txs)
    distribution = render_fee_distribution(txs)

    treemap_panel = Panel(
        Group(treemap, "", legend),
        title=f"[bold red]Block #{block_data.get('height', '?')} Transaction Map[/]",
        subtitle=f"[dim]{block_data.get('tx_count', '?')} transactions[/]",
        style="on default",
        border_style="bright_red",
        padding=(1, 1),
    )

    return Group(
        header,
        "",
        treemap_panel,
        "",
        top_txs,
        "",
        distribution,
    )


# ─── Interactive Mode ───

def interactive_visualizer(start_height=None, use_cli=False):
    """Run the interactive block visualizer."""
    console.clear()

    with console.status("[bold green]Loading block data...") as status:
        if use_cli:
            block_data = fetch_block_cli(start_height)
        else:
            block_data = fetch_block_api(start_height)

    current_height = block_data.get("height", 0)

    while True:
        console.clear()
        console.print(render_full_block(block_data))
        console.print()
        console.print(
            "    [bold green]Navigation:[/] "
            "[yellow]←[/] Prev block  "
            "[yellow]→[/] Next block  "
            "[yellow]L[/] Latest  "
            "[yellow]G[/] Go to height  "
            "[yellow]Q[/] Quit"
        )
        console.print()

        choice = console.input("    [bold green]Command:[/] ").strip().lower()

        if choice in ("q", "quit", ""):
            break
        elif choice in ("l", "latest"):
            with console.status("[bold green]Loading latest block..."):
                block_data = fetch_block_api() if not use_cli else fetch_block_cli()
            current_height = block_data.get("height", 0)
        elif choice in ("n", "right", "→"):
            current_height += 1
            with console.status(f"[bold green]Loading block {current_height}..."):
                block_data = fetch_block_api(current_height) if not use_cli else fetch_block_cli(current_height)
        elif choice in ("p", "left", "←"):
            current_height = max(0, current_height - 1)
            with console.status(f"[bold green]Loading block {current_height}..."):
                block_data = fetch_block_api(current_height) if not use_cli else fetch_block_cli(current_height)
        elif choice in ("g", "goto"):
            try:
                h = int(console.input("    [bold green]Block height:[/] "))
                current_height = h
                with console.status(f"[bold green]Loading block {h}..."):
                    block_data = fetch_block_api(h) if not use_cli else fetch_block_cli(h)
            except ValueError:
                console.print("    [red]Invalid height[/]")
                time.sleep(1)
        else:
            # Try as a number
            try:
                h = int(choice)
                current_height = h
                with console.status(f"[bold green]Loading block {h}..."):
                    block_data = fetch_block_api(h) if not use_cli else fetch_block_cli(h)
            except ValueError:
                pass


def run_visualizer():
    """Entry point compatible with existing PyBlock.py integration."""
    interactive_visualizer(use_cli=True)


if __name__ == "__main__":
    height = int(sys.argv[1]) if len(sys.argv) > 1 else None
    use_cli = "--cli" in sys.argv
    interactive_visualizer(start_height=height, use_cli=use_cli)
