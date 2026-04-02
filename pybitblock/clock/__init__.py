"""Enhanced block clock for PyBLOCK.

Entry point: run_clock(mode, path, settings_clock)
"""

import time
import sys

from . import animations
from .data import ClockData
from .renderer import Layout


def run_clock(mode, path, settings_clock):
    """Main clock loop with partial screen updates.

    mode: 'local', 'remote', or 'lite'
    path: dict with bitcoincli, ip_port, rpcuser, rpcpass
    settings_clock: dict from pyblocksettingsClock.conf
    """
    data = ClockData(mode, path)
    layout = Layout(settings_clock)

    try:
        # Initial full fetch and render
        data.refresh()
        layout.render_full(data)

        while True:
            time.sleep(2)

            changed = data.poll()

            if 'block_height' in changed:
                layout.on_new_block(data, animations)
            else:
                # Update dynamic elements
                layout.update_countdown(data)
                layout.heartbeat(data)

    except KeyboardInterrupt:
        pass
    finally:
        layout.cleanup()
