"""Configurable sound notifications for new blocks."""

import sys
import time


def play_sound(mode):
    """Play sound notification based on mode setting.

    mode: 'bell' (single beep), 'pattern' (rhythmic), 'silent' (nothing)
    """
    if mode == 'silent':
        return
    elif mode == 'pattern':
        # Three short beeps
        for _ in range(3):
            sys.stdout.write('\a')
            sys.stdout.flush()
            time.sleep(0.15)
    else:
        # Default: single bell
        sys.stdout.write('\a')
        sys.stdout.flush()
