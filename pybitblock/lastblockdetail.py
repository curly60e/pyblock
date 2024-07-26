import os
import json
import subprocess
import asyncio
import threading
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import urwid
from execute_load_config import load_config

console = Console()

# Load configuration
path, settings, settingsClock = load_config()

# Función para ejecutar comandos de bitcoin-cli y obtener resultados
def bitcoin_cli(command):
    result = subprocess.run([path["bitcoincli"]] + command.split(), capture_output=True, text=True)
    if result.returncode != 0:
        console.print(f"[red]Error executing command:[/red] {command}")
        console.print(result.stderr)
        return None
    return result.stdout.strip()

# Función para obtener los datos del último bloque y verificar cambios
async def fetch_block_data(rich_widget, urwid_loop):
    last_blockhash = None
    while True:
        blockhash = bitcoin_cli('getbestblockhash')
        if not blockhash:
            await asyncio.sleep(10)
            continue

        if blockhash != last_blockhash:
            block_details = bitcoin_cli(f'getblock {blockhash} 2')
            if not block_details:
                await asyncio.sleep(10)
                continue

            try:
                block_data = json.loads(block_details)
            except json.JSONDecodeError as e:
                console.print(f"[red]Error decoding JSON:[/red] {e}")
                console.print(block_details)
                await asyncio.sleep(10)
                continue

            height = block_data.get("height", "Unknown")

            transactions = block_data['tx']
            tx_details = []
            for tx in transactions:
                txid = tx.get("txid", "N/A")
                version = tx.get("version", "N/A")
                weight = tx.get("weight", "N/A")
                size = tx.get("size", "N/A")
                vsize = tx.get("vsize", "N/A")
                locktime = tx.get("locktime", "N/A")
                fee = tx.get("fee", 0) if "fee" in tx else 0
                vin_count = len(tx.get("vin", []))
                vout_count = len(tx.get("vout", []))
                tx_details.append((txid, version, weight, size, vsize, locktime, fee, vin_count, vout_count))

            new_renderable = create_block_renderable(blockhash, height, tx_details)
            rich_widget.update_text(new_renderable)
            urwid_loop.draw_screen()
            last_blockhash = blockhash

        await asyncio.sleep(10)

# Crear el bloque de transacciones usando rich
def create_block_renderable(blockhash, height, tx_details) -> str:
    table = Table(show_header=True, header_style="none")
    table.add_column("Transaction ID", justify="center", style="none")
    table.add_column("Version", justify="center", style="none")
    table.add_column("Weight", justify="center", style="none")
    table.add_column("Size", justify="center", style="none")
    table.add_column("Virtual Size", justify="center", style="none")
    table.add_column("Locktime", justify="center", style="none")
    table.add_column("Fee", justify="center", style="none")
    table.add_column("Inputs", justify="center", style="none")
    table.add_column("Outputs", justify="center", style="none")

    for txid, version, weight, size, vsize, locktime, fee, vin_count, vout_count in tx_details:
        table.add_row(txid, str(version), str(weight), str(size), str(vsize), str(locktime), f"{fee:.8f}", str(vin_count), str(vout_count))

    panel = Panel(table, title=f"Block {height} ({blockhash})", title_align="left")

    with console.capture() as capture:
        console.print(panel)
    return capture.get()

# Urwid widget para renderizar rich content
class RichWidget(urwid.WidgetWrap):
    def __init__(self):
        self.text_widget = urwid.Text("", wrap='clip')
        self.fill = urwid.Filler(self.text_widget, valign='top')
        super().__init__(self.fill)

    def update_text(self, new_text):
        self.text_widget.set_text(new_text)

# Función para iniciar el bucle de asyncio en un hilo separado
def start_asyncio_loop(rich_widget, urwid_loop):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fetch_block_data(rich_widget, urwid_loop))

# Función principal para ejecutar la interfaz urwid
def run_urwid():
    rich_widget = RichWidget()
    scroll = urwid.LineBox(urwid.ListBox(urwid.SimpleFocusListWalker([rich_widget])))
    urwid_loop = urwid.MainLoop(scroll, unhandled_input=exit_on_q)

    asyncio_thread = threading.Thread(target=start_asyncio_loop, args=(rich_widget, urwid_loop), daemon=True)
    asyncio_thread.start()

    urwid_loop.run()

# Salir con 'q'
def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

if __name__ == "__main__":
    run_urwid()
