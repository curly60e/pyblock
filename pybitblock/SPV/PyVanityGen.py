##SN PyVanityGen Vanity Generator PyBLOCK Crew##

import os
import random
import multiprocessing
from bitcoinlib.keys import HDKey
from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from queue import Empty

def address_search(search_for, witness_type, progress_queue, console):
    privkey = random.randrange(2**256)
    address = ''
    count = 0

    bech32 = "qpzry9x8gf2tvdw0s3jn54khce6mua7l"
    base58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    is_bech32 = True
    is_base58 = True
    for letter in search_for:
        if letter not in bech32:
            is_bech32 = False
        if letter not in base58:
            is_base58 = False
    if not (is_bech32 or is_base58):
        raise ValueError(f"This is not a valid base58 or bech32 search string: {search_for}")
    if is_base58 and not is_bech32:
        witness_type = 'p2sh-segwit'

    console.print(f"[yellow]Searching for {search_for}, witness_type is {witness_type} (pid {os.getpid()})[/yellow]")

    while True:
        privkey += 1
        k = HDKey(witness_type=witness_type)
        address = k.address()
        count += 1
        progress_queue.put(f"Searched {count} addresses (pid {os.getpid()})")
        if search_for in address:
            progress_queue.put(f"Found Address: {address}\nPrivate Key HEX: {k.private_hex}")
            break

def main():
    console = Console()
    console.clear()

    # Seleccionar tipo de dirección
    witness_type = console.input("Seleccione el tipo de dirección (segwit/legacy/p2sh-segwit): ").strip()

    # Seleccionar texto deseado en la dirección
    search_for = console.input("Ingrese la palabra que desea que aparezca en la vanity address: ").strip()

    # Iniciar los procesos
    processors = 4
    console.print(f"[green]Starting {processors} processes[/green]")

    layout = Layout()
    layout.split(
        Layout(name="progress", ratio=1),
        Layout(name="results", ratio=1),
    )

    progress_panel = Panel("Starting search...", title="Progress", border_style="yellow")
    result_panel = Panel("Waiting for results...", title="Results", border_style="green")
    layout["progress"].update(progress_panel)
    layout["results"].update(result_panel)

    with Live(layout, console=console, refresh_per_second=4) as live:
        progress_queue = multiprocessing.Queue()
        ps = []
        for i in range(processors):
            console.print(f"[cyan]Starting process {i}[/cyan]")
            p = multiprocessing.Process(target=address_search, args=(search_for, witness_type, progress_queue, console))
            p.start()
            ps.append(p)

        try:
            progress_messages = []
            result_messages = []
            while True:
                try:
                    message = progress_queue.get(timeout=1)
                    if "Found Address" in message:
                        result_messages.append(message)
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
            for p in ps:
                p.terminate()
            for p in ps:
                p.join()

if __name__ == "__main__":
    main()
