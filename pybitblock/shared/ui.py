"""
Shared UI utilities for PyBLOCK.

Provides status bar, error display, loading spinner, and input validation
for both PyBlock.py and SPV/spvblock.py.
"""

import sys
import threading
import time


# ANSI color constants
RED = "\033[1;31;40m"
GREEN = "\033[1;32;40m"
YELLOW = "\033[1;33;40m"
CYAN = "\033[1;36;40m"
WHITE = "\033[0;37;40m"
DIM = "\033[2;37;40m"
BOLD = "\033[1;37;40m"
RESET = "\033[0;37;40m"


def status_bar(mode="", block_height="", btc_price="", extra=""):
    """Print a persistent status bar showing current state."""
    mode_colors = {
        "local": GREEN,
        "remote": CYAN,
        "onchain_only": YELLOW,
        "lite": YELLOW,
    }
    mode_labels = {
        "local": "Bitcoin + Lightning",
        "remote": "Remote Node",
        "onchain_only": "Bitcoin Only",
        "lite": "Lite Mode",
    }
    color = mode_colors.get(mode, WHITE)
    label = mode_labels.get(mode, mode)

    parts = []
    if label:
        parts.append(f"{color}{label}{RESET}")
    if block_height:
        parts.append(f"{DIM}Block:{RESET} {BOLD}{block_height}{RESET}")
    if btc_price:
        parts.append(f"{DIM}BTC:{RESET} {GREEN}${btc_price}{RESET}")
    if extra:
        parts.append(extra)

    bar = f"  {DIM}|{RESET} ".join(parts)
    print(f"    {DIM}[{RESET} {bar} {DIM}]{RESET}")
    print(f"    {DIM}{'─' * 50}{RESET}")


def show_error(message):
    """Display a visible error message to the user."""
    print(f"\n    {RED}! Error: {RESET}{message}")
    print()


def show_warning(message):
    """Display a visible warning message to the user."""
    print(f"\n    {YELLOW}! Warning: {RESET}{message}")
    print()


def show_success(message):
    """Display a success message to the user."""
    print(f"\n    {GREEN}+ {RESET}{message}")
    print()


class Spinner:
    """Simple terminal spinner for loading operations."""

    FRAMES = [".", "..", "...", "....", "....."]

    def __init__(self, label="Loading"):
        self.label = label
        self._stop = threading.Event()
        self._thread = None

    def _animate(self):
        idx = 0
        while not self._stop.is_set():
            frame = self.FRAMES[idx % len(self.FRAMES)]
            sys.stdout.write(f"\r    {DIM}{self.label}{frame}{RESET}     ")
            sys.stdout.flush()
            idx += 1
            self._stop.wait(0.4)
        sys.stdout.write(f"\r{'':60}\r")
        sys.stdout.flush()

    def __enter__(self):
        self._thread = threading.Thread(target=self._animate, daemon=True)
        self._thread.start()
        return self

    def __exit__(self, *args):
        self._stop.set()
        if self._thread:
            self._thread.join(timeout=1)


def prompt_menu(prompt_text, valid_keys, back_fn=None):
    """Prompt for menu selection with validation and back support.

    Args:
        prompt_text: The prompt to display
        valid_keys: List/set of valid key strings (case-insensitive)
        back_fn: Function to call when user presses 'B' for back.
                 If None, 'B' is not offered.

    Returns:
        The validated key in uppercase, or None if back was selected.
    """
    valid_upper = {k.upper() for k in valid_keys}
    if back_fn is not None:
        valid_upper.add("B")

    while True:
        choice = input(prompt_text).strip()
        if not choice:
            continue

        upper = choice.upper()

        if upper == "B" and back_fn is not None:
            back_fn()
            return None

        if upper in valid_upper:
            return upper

        print(f"    {YELLOW}Invalid option '{choice}'. Try again.{RESET}")


def loading(label="Connecting"):
    """Convenience function to create a Spinner context manager."""
    return Spinner(label)
