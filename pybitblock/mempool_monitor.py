import asyncio
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
import subprocess
import json
import time
import plotext as plt

def fetch_mempool_data():
    raw_mempool = subprocess.run(["bitcoin-cli", "getmempoolinfo"], capture_output=True, text=True)
    mempool_data = json.loads(raw_mempool.stdout)
    return mempool_data

def fetch_mempool_transactions():
    raw_mempool = subprocess.run(["bitcoin-cli", "getrawmempool", "true"], capture_output=True, text=True)
    mempool_transactions = json.loads(raw_mempool.stdout)
    return mempool_transactions

def fetch_blockchain_info():
    raw_info = subprocess.run(["bitcoin-cli", "getblockchaininfo"], capture_output=True, text=True)
    blockchain_info = json.loads(raw_info.stdout)
    return blockchain_info

def calculate_average_median_fee(mempool_transactions):
    fees_per_byte = []
    for tx in mempool_transactions.values():
        fee = tx['fees']['base'] * 1e8  # Convert BTC to satoshis
        size = tx['vsize']
        fee_per_byte = fee / size
        fees_per_byte.append(fee_per_byte)

    average_fee = sum(fees_per_byte) / len(fees_per_byte) if fees_per_byte else 0
    median_fee = sorted(fees_per_byte)[len(fees_per_byte) // 2] if fees_per_byte else 0

    return average_fee, median_fee

def create_mempool_info_table(mempool_data, mempool_transactions):
    table = Table(title="Mempool Information")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="magenta")

    table.add_row("Mempool Size", f"{mempool_data['size']} transactions")
    table.add_row("Mempool Bytes", f"{mempool_data['bytes']} bytes")
    table.add_row("Usage", f"{mempool_data['usage']} bytes")
    table.add_row("Max Mempool", f"{mempool_data['maxmempool']} bytes")
    table.add_row("Mempool Min Fee", f"{mempool_data['mempoolminfee']:.8f} BTC")
    table.add_row("Min Relay Tx Fee", f"{mempool_data['minrelaytxfee']:.8f} BTC")

    average_fee, median_fee = calculate_average_median_fee(mempool_transactions)
    table.add_row("Average Fee", f"{average_fee:.2f} sat/byte")
    table.add_row("Median Fee", f"{median_fee:.2f} sat/byte")

    segwit_txs = sum(1 for tx in mempool_transactions.values() if tx.get('wtxid'))
    non_segwit_txs = len(mempool_transactions) - segwit_txs
    table.add_row("SegWit Transactions", str(segwit_txs))
    table.add_row("Non-SegWit Transactions", str(non_segwit_txs))

    return table

def create_recent_blocks_table():
    table = Table(title="Recent Blocks")
    table.add_column("Height", style="cyan")
    table.add_column("Transactions", style="magenta")
    table.add_column("Size", style="green")
    table.add_column("Time", style="yellow")

    recent_blocks = fetch_blockchain_info()
    latest_height = recent_blocks['blocks']

    for i in range(17):
        block_height = latest_height - i
        block_hash = subprocess.run(["bitcoin-cli", "getblockhash", str(block_height)], capture_output=True, text=True).stdout.strip()
        block_info = subprocess.run(["bitcoin-cli", "getblock", block_hash], capture_output=True, text=True)
        block_data = json.loads(block_info.stdout)

        table.add_row(
            str(block_height),
            str(block_data['nTx']),
            f"{block_data['size']} bytes",
            time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(block_data['time']))
        )

    return table

def create_mempool_transactions_table(mempool_transactions):
    table = Table(title="Mempool Transactions")
    table.add_column("Transaction ID", style="cyan")
    table.add_column("Size", style="magenta")
    table.add_column("Fee", style="green")

    sorted_transactions = sorted(mempool_transactions.items(), key=lambda item: item[1]['time'], reverse=True)

    for txid, details in sorted_transactions[:17]:
        fee = details.get('fees', {}).get('base', 0)
        size = details.get('vsize', 'N/A')
        table.add_row(txid, str(size), f"{fee:.8f} BTC")

    return table

def create_mempool_flow_chart():
    plt.clear_color()
    plt.title("Mempool Flow")
    plt.xlabel("Time")
    plt.ylabel("Transactions")
    plt.plot_size(80, 20)

    # Add dummy data
    x = list(range(10))
    y = [i ** 2 for i in x]
    plt.plot(x, y)
    chart = plt.build()

    return chart

async def display_mempool_info():
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
    layout["left"].split(Layout(name="mempool_info"), Layout(name="recent_blocks"))
    layout["right"].split(Layout(name="mempool_chart"), Layout(name="mempool_transactions"))
    layout["footer"].update(Text("Loading..."))

    layout["mempool_info"].update(Panel(Text("Loading..."), title="General Information"))
    layout["mempool_chart"].update(Panel(Text("Loading..."), title="Mempool Flow"))
    layout["recent_blocks"].update(Panel(Text("Loading..."), title="Last Blocks"))
    layout["header"].update(Text("Mempool Monitor", style="bold magenta"))

    mempool_data_points = []

    with Live(layout, refresh_per_second=1, screen=True):
        while True:
            mempool_data = fetch_mempool_data()
            mempool_transactions = fetch_mempool_transactions()
            mempool_info_table = create_mempool_info_table(mempool_data, mempool_transactions)
            recent_blocks_table = create_recent_blocks_table()
            mempool_transactions_table = create_mempool_transactions_table(mempool_transactions)

            current_time = time.time()
            mempool_data_points.append({'time': current_time, 'size': mempool_data['size']})

            if len(mempool_data_points) > 10:  # Keep only the last 10 data points
                mempool_data_points.pop(0)

            mempool_flow_chart = create_mempool_flow_chart()

            layout["mempool_info"].update(Panel(mempool_info_table, title="General Information"))
            layout["recent_blocks"].update(Panel(recent_blocks_table, title="Recent Blocks"))
            layout["mempool_transactions"].update(Panel(mempool_transactions_table, title="Recent Transactions"))
            layout["mempool_chart"].update(Panel(mempool_flow_chart, title="Mempool Flow"))

            layout["footer"].update(Text(""))

if __name__ == "__main__":
    asyncio.run(display_mempool_info())
