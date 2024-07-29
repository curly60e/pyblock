import curses
import json
import subprocess
import logging
import numpy as np
from execute_load_config import load_config

# Configura el archivo de registro
logging.basicConfig(filename='debug.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Load configuration
path, settings, settingsClock = load_config()

def setup_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)  # For mined transactions
    curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLACK)  # For unmined transactions
    logging.debug("Colors set up")

def fetch_mempool(path):
    logging.debug("Fetching mempool")
    raw_mempool = subprocess.run([path["bitcoincli"], "getrawmempool"], capture_output=True, text=True)
    mempool_data = json.loads(raw_mempool.stdout)
    logging.debug(f"Mempool fetched: {len(mempool_data)} transactions")
    return mempool_data

def fetch_transaction_details(path, txid):
    logging.debug(f"Fetching transaction details for {txid}")
    raw_tx_details = subprocess.run([path["bitcoincli"], "getrawtransaction", txid, "true"], capture_output=True, text=True)
    tx_details = json.loads(raw_tx_details.stdout)
    logging.debug(f"Transaction details fetched: {tx_details}")
    return tx_details

def fetch_block_info(path, blockhash):
    logging.debug(f"Fetching block info for {blockhash}")
    raw_block_info = subprocess.run([path["bitcoincli"], "getblock", blockhash], capture_output=True, text=True)
    block_info = json.loads(raw_block_info.stdout)
    logging.debug(f"Block info fetched: {block_info}")
    return block_info

def fetch_transaction_in_block(path, txid):
    logging.debug(f"Fetching transaction in blockchain for {txid}")
    try:
        tx_details = fetch_transaction_details(path, txid)
        blockhash = tx_details.get("blockhash")
        if blockhash:
            block_info = fetch_block_info(path, blockhash)
            return tx_details, block_info
        return tx_details, None
    except subprocess.CalledProcessError:
        logging.error(f"Transaction {txid} not found in blockchain")
        return None, None

def draw_search(win, search_query):
    logging.debug("Drawing search panel")
    win.clear()
    height, width = win.getmaxyx()

    win.border()
    win.addstr(0, 2, " Transaction Search ", curses.A_BOLD | curses.color_pair(1))
    win.addstr(2, 2, "Enter Transaction ID or part of it:", curses.color_pair(2))
    win.addstr(3, 2, search_query, curses.color_pair(3))

    win.refresh()
    logging.debug("Search panel drawn and window refreshed")

def draw_transaction_details(win, transaction, mined):
    logging.debug("Drawing transaction details")
    win.clear()
    height, width = win.getmaxyx()

    win.border()
    win.addstr(0, 2, " Transaction Details ", curses.A_BOLD | curses.color_pair(1))

    if transaction:
        details = [
            f"TxID: {transaction['txid']}",
            f"Size: {transaction['size']} bytes",
            f"Version: {transaction['version']}",
            f"Locktime: {transaction['locktime']}",
            "Inputs:",
        ]

        for vin in transaction['vin']:
            details.append(f" - {vin.get('txid', 'Coinbase')}:{vin.get('vout', '')}")
            if 'scriptSig' in vin:
                details.append(f"   ScriptSig: {vin['scriptSig']['hex']}")

        details.append("Outputs:")
        for vout in transaction['vout']:
            details.append(f" - Value: {vout['value']} BTC")
            details.append(f"   ScriptPubKey: {vout['scriptPubKey']['hex']}")

        color_pair = curses.color_pair(6) if mined else curses.color_pair(7)

        for idx, detail in enumerate(details):
            if idx >= height - 2:
                break
            win.addstr(idx + 1, 1, detail, color_pair)
    else:
        win.addstr(2, 2, "No transaction selected", curses.color_pair(3))

    win.refresh()
    logging.debug("Transaction details drawn and window refreshed")

def draw_help(win):
    logging.debug("Drawing help menu")
    win.clear()
    win.border()
    win.addstr(0, 2, " Help Menu ", curses.A_BOLD | curses.color_pair(1))
    help_text = [
        "Up/Down Arrow: Navigate results",
        "Enter: Select transaction",
        "h: Show this help menu",
        "q: Quit",
        "Press any key to return"
    ]

    for idx, line in enumerate(help_text):
        win.addstr(idx + 2, 1, line)

    win.refresh()
    win.getch()  # Wait for another key press to go back
    logging.debug("Help menu drawn and window refreshed")

def draw_title(win):
    logging.debug("Drawing title")
    win.clear()
    win.addstr(0, 0, "Bitcoin Mempool Search", curses.A_BOLD | curses.color_pair(1))
    win.refresh()
    logging.debug("Title drawn and window refreshed")

def draw_footer(win):
    logging.debug("Drawing footer")
    win.clear()
    win.addstr(0, 0, "Press 'h' for help, 'q' to quit", curses.A_BOLD | curses.color_pair(1))
    win.refresh()
    logging.debug("Footer drawn and window refreshed")

def refresh_screen(title_win, search_win, details_win, footer_win, search_query, transaction, mined):
    logging.debug("Refreshing screen")
    draw_title(title_win)
    draw_search(search_win, search_query)
    draw_transaction_details(details_win, transaction, mined)
    draw_footer(footer_win)
    logging.debug("Screen refreshed")

def main(stdscr):
    logging.debug("Starting main function")
    curses.curs_set(0)
    setup_colors()
    height, width = stdscr.getmaxyx()

    # Create windows for different sections
    title_win = curses.newwin(1, width, 0, 0)
    search_win = curses.newwin(height - 3, width // 2, 1, 0)
    details_win = curses.newwin(height - 3, width // 2, 1, width // 2)
    footer_win = curses.newwin(1, width, height - 1, 0)

    # Initialize search query and results
    search_query = ""
    selected_transaction = None
    mined = False

    # Initial screen refresh
    refresh_screen(title_win, search_win, details_win, footer_win, search_query, selected_transaction, mined)

    # Main loop
    logging.debug("Entering main loop")
    while True:
        stdscr.nodelay(False)  # Make getch blocking

        key = stdscr.getch()
        logging.debug(f"Key pressed: {key}")

        if key == ord('q'):
            logging.debug("Quit key pressed")
            break
        elif key == ord('h'):  # Press 'h' to show help
            logging.debug("Help key pressed")
            draw_help(stdscr)
            refresh_screen(title_win, search_win, details_win, footer_win, search_query, selected_transaction, mined)
        elif key in (curses.KEY_BACKSPACE, 127, curses.KEY_DC):
            logging.debug("Backspace/Delete key pressed")
            search_query = search_query[:-1]
            refresh_screen(title_win, search_win, details_win, footer_win, search_query, selected_transaction, mined)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            logging.debug("Enter key pressed")
            mempool = fetch_mempool(path)
            tx_ids = np.array(mempool)  # Convertimos la mempool a un array de numpy
            found_in_mempool = False
            for txid in tx_ids:
                if search_query in txid:
                    selected_transaction = fetch_transaction_details(path, txid)
                    mined = False
                    found_in_mempool = True
                    break
            if not found_in_mempool:
                try:
                    selected_transaction, block_info = fetch_transaction_in_block(path, search_query)
                    mined = block_info is not None
                except subprocess.CalledProcessError:
                    selected_transaction = None
                    mined = False
            refresh_screen(title_win, search_win, details_win, footer_win, search_query, selected_transaction, mined)
        elif key != -1:
            search_query += chr(key)
            refresh_screen(title_win, search_win, details_win, footer_win, search_query, selected_transaction, mined)

def search_tx():
    logging.debug("Starting searching engine")
    curses.wrapper(main)

if __name__ == "__main__":
    search_tx()
