import asyncio
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
import subprocess
import json
import time
import psutil

def fetch_network_info():
    raw_info = subprocess.run(["bitcoin-cli", "getnetworkinfo"], capture_output=True, text=True)
    network_info = json.loads(raw_info.stdout)
    return network_info

def fetch_blockchain_info():
    raw_info = subprocess.run(["bitcoin-cli", "getblockchaininfo"], capture_output=True, text=True)
    blockchain_info = json.loads(raw_info.stdout)
    return blockchain_info

def fetch_net_totals():
    raw_info = subprocess.run(["bitcoin-cli", "getnettotals"], capture_output=True, text=True)
    net_totals = json.loads(raw_info.stdout)
    return net_totals

def fetch_peer_info():
    raw_info = subprocess.run(["bitcoin-cli", "getpeerinfo"], capture_output=True, text=True)
    peer_info = json.loads(raw_info.stdout)
    return peer_info

def fetch_mempool_info():
    raw_info = subprocess.run(["bitcoin-cli", "getmempoolinfo"], capture_output=True, text=True)
    mempool_info = json.loads(raw_info.stdout)
    return mempool_info

def fetch_orphan_info():
    raw_info = subprocess.run(["bitcoin-cli", "getchaintips"], capture_output=True, text=True)
    chaintips_info = json.loads(raw_info.stdout)
    orphan_blocks = [tip for tip in chaintips_info if tip['status'] in ['orphan', 'invalid', 'valid-fork']]
    return orphan_blocks

def fetch_uptime():
    raw_info = subprocess.run(["bitcoin-cli", "uptime"], capture_output=True, text=True)
    return int(raw_info.stdout.strip())

def create_node_info_table(network_info, blockchain_info, uptime):
    table = Table(title="Node Information")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Version", network_info["subversion"])
    table.add_row("Connections", str(network_info["connections"]))
    table.add_row("Protocol Version", str(network_info["protocolversion"]))
    table.add_row("Relay Fee", f"{network_info['relayfee']:.8f} BTC")
    table.add_row("Network Active", str(network_info["networkactive"]))
    table.add_row("Uptime", str(uptime) + " seconds")

    table.add_row("Blocks", str(blockchain_info["blocks"]))
    table.add_row("Headers", str(blockchain_info["headers"]))
    table.add_row("Best Blockhash", blockchain_info["bestblockhash"])
    table.add_row("Difficulty", f"{blockchain_info['difficulty']:.2f}")
    table.add_row("Median Time", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(blockchain_info['mediantime'])))
    table.add_row("Verification Progress", f"{blockchain_info['verificationprogress']:.2%}")

    return table

def create_net_totals_table(net_totals):
    table = Table(title="Network Traffic")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Total Bytes Sent", f"{net_totals['totalbytessent']} bytes")
    table.add_row("Total Bytes Received", f"{net_totals['totalbytesrecv']} bytes")

    return table

def create_peer_info_table(peer_info):
    table = Table(title="Peer Info")
    table.add_column("Peer", style="cyan")
    table.add_column("Address", style="magenta")

    for peer in peer_info[:10]:
        table.add_row(str(peer['id']), peer['addr'])

    return table

def create_orphan_info_table(orphan_blocks):
    table = Table(title="Orphan Blocks Info")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Orphan Blocks", str(len(orphan_blocks)))
    for block in orphan_blocks:
        table.add_row(str(block["height"]), block["hash"], block["status"])

    return table

def create_mempool_info_table(mempool_info):
    table = Table(title="Mempool Info")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Size", f"{mempool_info['size']} transactions")
    table.add_row("Bytes", f"{mempool_info['bytes']} bytes")
    table.add_row("Usage", f"{mempool_info['usage']} bytes")

    return table

async def display_node_info():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=1),
    )
    layout["main"].split_row(
        Layout(name="left", ratio=1),
        Layout(name="right", ratio=1),
    )
    layout["left"].split(
        Layout(name="node_info"),
        Layout(name="orphan_info"),
    )
    layout["right"].split(Layout(name="net_totals"), Layout(name="peer_info"))
    layout["footer"].update(Text("Loading..."))

    layout["node_info"].update(Panel(Text("Loading..."), title="Node Information"))
    layout["net_totals"].update(Panel(Text("Loading..."), title="Network Traffic"))
    layout["peer_info"].update(Panel(Text("Loading..."), title="Peer Info"))
    layout["orphan_info"].update(Panel(Text("Loading..."), title="Orphan Blocks Info"))
    layout["header"].update(Text("Node Monitor", style="bold magenta"))

    with Live(layout, refresh_per_second=1, screen=True):
        while True:
            network_info = fetch_network_info()
            blockchain_info = fetch_blockchain_info()
            net_totals = fetch_net_totals()
            peer_info = fetch_peer_info()
            orphan_info = fetch_orphan_info()
            uptime = fetch_uptime()

            node_info_table = create_node_info_table(network_info, blockchain_info, uptime)
            net_totals_table = create_net_totals_table(net_totals)
            peer_info_table = create_peer_info_table(peer_info)
            orphan_info_table = create_orphan_info_table(orphan_info)

            layout["node_info"].update(Panel(node_info_table, title="Node Information"))
            layout["net_totals"].update(Panel(net_totals_table, title="Network Traffic"))
            layout["peer_info"].update(Panel(peer_info_table, title="Peer Info"))
            layout["orphan_info"].update(Panel(orphan_info_table, title="Orphan Blocks Info"))

            layout["footer"].update(Text(""))

def run_display_node_info():
    asyncio.run(display_node_info())

if __name__ == "__main__":
    run_display_node_info()
