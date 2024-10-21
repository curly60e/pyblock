##SN PyVanityGen Vanity Generator PyBLOCK Crew##

import os
import random
import multiprocessing
import logging
from bitcoinlib.keys import HDKey
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from queue import Empty
import base58

# Set up debug logging
logging.basicConfig(filename='debugfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Set up results logging
results_logger = logging.getLogger('results_logger')
results_logger.setLevel(logging.INFO)
results_handler = logging.FileHandler('Results.log')
results_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
results_logger.addHandler(results_handler)

def privkey_to_wif(privkey, compressed=True, testnet=False):
    prefix = b'\xEF' if testnet else b'\x80'
    key_bytes = privkey.to_bytes(32, 'big')
    if compressed:
        key_bytes += b'\x01'
    extended_key = prefix + key_bytes
    checksum = extended_key + extended_key[:4]
    wif = base58.b58encode(extended_key + checksum[:4]).decode('utf-8')
    return wif

def address_search(search_for, witness_type, progress_queue, console):
    privkey = random.randrange(2**256)
    address = ''
    count = 0

    logging.info(f"Searching for {search_for}, witness_type is {witness_type} (pid {os.getpid()})")
    console.print(f"[yellow]Searching for {search_for}, witness_type is {witness_type} (pid {os.getpid()})[/yellow]")

    while True:
        try:
            privkey += 1
            k = HDKey(key=privkey.to_bytes(32, 'big'), witness_type=witness_type)
            address = k.address()
            count += 1
            progress_queue.put(f"Searched {count} addresses (pid {os.getpid()})")
            if search_for in address:
                wif_key = privkey_to_wif(privkey)
                result_message = f"Found Address: {address}\nPrivate Key WIF: {wif_key}"
                progress_queue.put(result_message)
                logging.info(result_message)
                results_logger.info(result_message)
                # Continue searching instead of breaking to find more vanity addresses
        except Exception as e:
            logging.error(f"Error during address search: {e}")
            break

def main():
    console = Console()
    console.clear()

    # Seleccionar tipo de dirección
    witness_type = console.input("Type your address format (legacy/segwit/p2sh-segwit): ").strip()

    # Seleccionar texto deseado en la dirección
    search_for = console.input("Put your Word/Target for your Vanity addresses: ").strip()
    # Iniciar los procesos
    processors = 4
    console.print(f"[green]Starting {processors} processes[/green]")
    logging.info(f"Starting {processors} processes for your Vanity addresses search")

    layout = Layout()
    layout.split(
        Layout(name="progress", ratio=1),
        Layout(name="results", ratio=1),
    )

    progress_panel = Panel("Starting search...", title="Progress", border_style="yellow")
    result_panel = Panel("Waiting for results...", title="Results", border_style="green")
    layout["progress"].update(progress_panel)
    layout["results"].update(result_panel)

    with Live(layout, console=console, refresh_per_second=10) as live:
        progress_queue = multiprocessing.Queue()
        ps = []
        for i in range(processors):
            console.print(f"[cyan]Starting process {i}[/cyan]")
            logging.info(f"Starting process {i}")
            p = multiprocessing.Process(target=address_search, args=(search_for, witness_type, progress_queue, console))
            p.start()
            ps.append(p)

        try:
            progress_messages = []
            result_messages = []
            while True:
                try:
                    message = progress_queue.get(timeout=0.1)
                    if "Found Address" in message:
                        result_messages.append(message)
                        if len(result_messages) > 10:
                            result_messages.pop(0)  # Keep only the last 10 results
                        result_panel = Panel(Text("\n".join(result_messages)), title="Results", border_style="green")
                        layout["results"].update(result_panel)
                    else:
                        progress_messages.append(message)
                        if len(progress_messages) > 10:
                            progress_messages.pop(0)  # Keep only the last 10 messages
                        progress_panel = Panel(Text("\n".join(progress_messages)), title="Progress", border_style="yellow")
                        layout["progress"].update(progress_panel)
                    live.update(layout)
                except Empty:
                    pass
        except KeyboardInterrupt:
            console.print("[red]Stopping processes...[/red]")
            logging.info("Stopping processes due to KeyboardInterrupt")
            for p in ps:
                p.terminate()
            for p in ps:
                p.join()

if __name__ == "__main__":
    main()
