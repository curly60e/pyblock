import asyncio
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich.align import Align
from rich.console import Group
import subprocess
import json
import time
from threading import Event, Thread
from execute_load_config import load_config

# Load configuration
path, settings, settingsClock = load_config()

def fetch_blockchain_info(path):
    raw_info = subprocess.run([path["bitcoincli"], "getblockchaininfo"], capture_output=True, text=True)
    blockchain_info = json.loads(raw_info.stdout)
    return blockchain_info

def fetch_block_info(path, blockhash):
    raw_block_info = subprocess.run([path["bitcoincli"], "getblock", blockhash], capture_output=True, text=True)
    block_info = json.loads(raw_block_info.stdout)
    return block_info

def create_block_info_table(block_height, block_data):
    table = Table(title=f"Block #{block_height}")
    table.add_column("Metric", style="green")
    table.add_column("Value", style="yellow")

    table.add_row("Transactions", str(block_data['nTx']))
    table.add_row("Size", f"{block_data['size']} bytes")
    table.add_row("Weight", f"{block_data['weight']} weight units")
    table.add_row("Version", str(block_data['version']))
    table.add_row("Merkle Root", block_data['merkleroot'])
    table.add_row("Time", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(block_data['time'])))
    table.add_row("Median Time", time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(block_data['mediantime'])))
    table.add_row("Nonce", str(block_data['nonce']))
    table.add_row("Bits", str(block_data['bits']))
    table.add_row("Difficulty", f"{block_data['difficulty']:.2f}")
    table.add_row("Chainwork", block_data['chainwork'])
    table.add_row("Previous Block", block_data['previousblockhash'])
    if 'nextblockhash' in block_data:
        table.add_row("Next Block", block_data['nextblockhash'])

    return table

def fetch_and_store_block_data(path, start_height, count, block_tables):
    latest_height = start_height

    for i in range(count):  # Limitar a los bloques solicitados
        block_height = latest_height - i
        block_hash = subprocess.run([path["bitcoincli"], "getblockhash", str(block_height)], capture_output=True, text=True).stdout.strip()
        block_data = fetch_block_info(path, block_hash)
        table = create_block_info_table(block_height, block_data)
        block_tables.append(table)

def background_block_fetch(path, block_tables, stop_event):
    latest_height = fetch_blockchain_info(path)['blocks']
    while not stop_event.is_set():
        current_height = fetch_blockchain_info(path)['blocks']
        if current_height > latest_height:
            latest_height = current_height
            block_tables.clear()
            fetch_and_store_block_data(path, current_height, 3, block_tables)
        time.sleep(10)

async def display_blocks_info():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main", ratio=1),
        Layout(name="footer", size=1),
    )
    layout["main"].split_row(
        Layout(name="recent_blocks", ratio=1),
    )
    layout["footer"].update(Text("Cypherpunk style..."))

    layout["recent_blocks"].update(Panel(Text("Loading..."), title="Recent Blocks"))
    layout["header"].update(Text("Block Monitor", style="bold cyan"))

    block_tables = []
    blockchain_info = fetch_blockchain_info(path)
    latest_block_height = blockchain_info['blocks']
    fetch_and_store_block_data(path, latest_block_height, 3, block_tables)

    stop_event = Event()
    fetch_thread = Thread(target=background_block_fetch, args=(path, block_tables, stop_event))
    fetch_thread.start()

    async def input_handler():
        while True:
            key = await asyncio.get_event_loop().run_in_executor(None, input)
            if key == 'q':
                stop_event.set()
                fetch_thread.join()
                break

    with Live(layout, refresh_per_second=1, screen=True):
        input_task = asyncio.create_task(input_handler())
        while not stop_event.is_set():
            recent_blocks_group = Group(*block_tables)
            centered_recent_blocks = Align.center(recent_blocks_group)

            layout["recent_blocks"].update(Panel(centered_recent_blocks, title="Recent Blocks"))
            layout["footer"].update(Text("Running the node."))

            await asyncio.sleep(1)

def call_blocks():
    asyncio.run(display_blocks_info())

if __name__ == "__main__":
    call_blocks()
