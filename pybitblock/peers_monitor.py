import curses
import json
import subprocess
import time
import logging
from blessings import Terminal
from execute_load_config import load_config

# Configura el archivo de registro
logging.basicConfig(filename='debug_peer_monitor.log', level=logging.DEBUG, format='%(asctime)s %(message)s')

# Load configuration
path, settings, settingsClock = load_config()

def setup_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    logging.debug("Colors set up")

def fetch_peers(path):
    logging.debug("Fetching peers")
    raw_peers = subprocess.run([path["bitcoincli"], "getpeerinfo"], capture_output=True, text=True)
    peers_data = json.loads(raw_peers.stdout)
    logging.debug(f"Peers fetched: {peers_data}")
    return peers_data

def disconnect_peer(path, peer_ip):
    logging.debug(f"Disconnecting peer: {peer_ip}")
    subprocess.run([path["bitcoincli"], "disconnectnode", peer_ip], capture_output=True, text=True)

def ban_peer(path, peer_ip, ban_time=86400):
    logging.debug(f"Banning peer: {peer_ip} for {ban_time} seconds")
    subprocess.run([path["bitcoincli"], "setban", peer_ip, "add", str(ban_time)], capture_output=True, text=True)

def unban_peer(path, peer_ip):
    logging.debug(f"Unbanning peer: {peer_ip}")
    subprocess.run([path["bitcoincli"], "setban", peer_ip, "remove"], capture_output=True, text=True)

def draw_peers(win, peers, selected_peer_idx):
    logging.debug("Drawing peers")
    win.clear()
    height, width = win.getmaxyx()

    win.border()
    win.addstr(0, 2, " Peer List ", curses.A_BOLD | curses.color_pair(1))

    for idx, peer in enumerate(peers):
        y = idx + 1
        if y >= height - 1:
            break
        if idx == selected_peer_idx:
            win.addstr(y, 1, f"Peer {idx + 1}: {peer['addr']}", curses.A_REVERSE | curses.color_pair(2))
        else:
            win.addstr(y, 1, f"Peer {idx + 1}: {peer['addr']}", curses.color_pair(2))

    win.refresh()
    logging.debug("Peers drawn and window refreshed")

def draw_peer_details(win, peer):
    logging.debug("Drawing peer details")
    win.clear()
    height, width = win.getmaxyx()

    win.border()
    win.addstr(0, 2, " Peer Details ", curses.A_BOLD | curses.color_pair(1))

    details = [
        f"Address: {peer['addr']}",
        f"Services: {peer['services']}",
        f"Last Send: {peer['lastsend']}",
        f"Last Receive: {peer['lastrecv']}",
        f"Bytes Sent: {peer['bytessent']}",
        f"Bytes Received: {peer['bytesrecv']}",
        f"Connection Time: {peer['conntime']}",
        f"Ping Time: {peer['pingtime']}",
        f"Version: {peer['version']}",
        f"Subversion: {peer['subver']}",
        f"Inbound: {peer['inbound']}",
        f"Starting Height: {peer['startingheight']}",
    ]

    for idx, detail in enumerate(details):
        if idx >= height - 2:
            break
        win.addstr(idx + 1, 1, detail)

    win.refresh()
    logging.debug("Peer details drawn and window refreshed")

def draw_help(win):
    logging.debug("Drawing help menu")
    win.clear()
    win.border()
    win.addstr(0, 2, " Help Menu ", curses.A_BOLD | curses.color_pair(1))
    help_text = [
        "Up/Down Arrow: Navigate peers",
        "d: Show details of selected peer",
        "x: Disconnect selected peer",
        "b: Ban selected peer",
        "u: Unban peer",
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
    win.addstr(0, 0, "Bitcoin Node Peers", curses.A_BOLD | curses.color_pair(1))
    win.refresh()
    logging.debug("Title drawn and window refreshed")

def draw_footer(win):
    logging.debug("Drawing footer")
    win.clear()
    win.addstr(0, 0, "Press 'h' for help, 'q' to quit", curses.A_BOLD | curses.color_pair(1))
    win.refresh()
    logging.debug("Footer drawn and window refreshed")

def refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx):
    logging.debug("Refreshing screen")
    draw_title(title_win)
    draw_peers(peer_list_win, peers, selected_peer_idx)
    draw_peer_details(details_win, peers[selected_peer_idx])
    draw_footer(footer_win)
    logging.debug("Screen refreshed")

def main(stdscr):
    logging.debug("Starting main function")
    curses.curs_set(0)
    setup_colors()
    height, width = stdscr.getmaxyx()

    # Create windows for different sections
    title_win = curses.newwin(1, width, 0, 0)
    peer_list_win = curses.newwin(height - 3, width // 2, 1, 0)
    details_win = curses.newwin(height - 3, width // 2, 1, width // 2)
    footer_win = curses.newwin(1, width, height - 1, 0)

    # Draw initial screen structure
    logging.debug("Drawing initial screen structure")
    draw_title(title_win)
    peer_list_win.border()
    peer_list_win.addstr(0, 2, " Peer List ", curses.A_BOLD | curses.color_pair(1))
    peer_list_win.refresh()
    details_win.border()
    details_win.addstr(0, 2, " Peer Details ", curses.A_BOLD | curses.color_pair(1))
    details_win.refresh()
    draw_footer(footer_win)

    # Delay to allow initial loading
    logging.debug("Delaying to allow initial loading")
    time.sleep(1)

    # Get peers from Bitcoin node
    logging.debug("Fetching initial peers")
    peers = fetch_peers(path)
    selected_peer_idx = 0

    # Initial screen refresh with data
    logging.debug("Refreshing screen with initial data")
    draw_title(title_win)
    draw_peers(peer_list_win, peers, selected_peer_idx)
    draw_peer_details(details_win, peers[selected_peer_idx])
    draw_footer(footer_win)
    title_win.refresh()
    peer_list_win.refresh()
    details_win.refresh()
    footer_win.refresh()
    logging.debug("Screen refreshed with initial data")

    # Main loop
    logging.debug("Entering main loop")
    refresh_interval = 1
    last_refresh_time = time.time()

    while True:
        current_time = time.time()
        if current_time - last_refresh_time >= refresh_interval:
            logging.debug("Refreshing peers")
            peers = fetch_peers(path)
            last_refresh_time = current_time
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)

        key = stdscr.getch()
        logging.debug(f"Key pressed: {key}")

        if key == ord('q'):
            logging.debug("Quit key pressed")
            break
        elif key == curses.KEY_UP and selected_peer_idx > 0:
            logging.debug("Up key pressed")
            selected_peer_idx -= 1
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
        elif key == curses.KEY_DOWN and selected_peer_idx < len(peers) - 1:
            logging.debug("Down key pressed")
            selected_peer_idx += 1
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
        elif key == ord('d'):  # Press 'd' to show details
            logging.debug("Details key pressed")
            draw_peer_details(details_win, peers[selected_peer_idx])
            stdscr.getch()  # Wait for another key press to go back
            # Redraw main screen after returning from details
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
        elif key == ord('x'):  # Press 'x' to disconnect the selected peer
            logging.debug("Disconnect key pressed")
            peer_ip = peers[selected_peer_idx]['addr']
            disconnect_peer(path, peer_ip)
            peers = fetch_peers(path)  # Refresh the peers list after disconnection
            last_refresh_time = time.time()  # Reset the refresh timer
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
        elif key == ord('b'):  # Press 'b' to ban the selected peer
            logging.debug("Ban key pressed")
            peer_ip = peers[selected_peer_idx]['addr']
            ban_peer(path, peer_ip)
            peers = fetch_peers(path)  # Refresh the peers list after banning
            last_refresh_time = time.time()  # Reset the refresh timer
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
        elif key == ord('u'):  # Press 'u' to unban the selected peer
            logging.debug("Unban key pressed")
            peer_ip = peers[selected_peer_idx]['addr']
            unban_peer(path, peer_ip)
            peers = fetch_peers(path)  # Refresh the peers list after unbanning
            last_refresh_time = time.time()  # Reset the refresh timer
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
        elif key == ord('h'):  # Press 'h' to show help
            logging.debug("Help key pressed")
            draw_help(stdscr)
            stdscr.getch()  # Wait for another key press to go back
            # Redraw main screen after returning from help
            refresh_screen(title_win, peer_list_win, details_win, footer_win, peers, selected_peer_idx)
            title_win.refresh()
            peer_list_win.refresh()
            details_win.refresh()
            footer_win.refresh()

def run_peers_monitor():
    logging.debug("Starting peers monitor")
    curses.wrapper(main)

if __name__ == "__main__":
    run_peers_monitor()
