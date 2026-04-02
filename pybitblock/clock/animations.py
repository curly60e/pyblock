"""Visual animations for the block clock.

Mining rain, odometer digit transition, fireworks on milestones.
"""

import shutil
import subprocess
import sys
import time
from random import choice, randrange

from cfonts import render

# Halving blocks for milestone detection
HALVING_BLOCKS = {210_000 * i for i in range(1, 65)}


def is_milestone_block(height):
    """Check if block is a milestone. Returns description or None."""
    if height in HALVING_BLOCKS:
        return f"HALVING #{height // 210_000}"
    if height % 100_000 == 0:
        return f"BLOCK {height:,}"
    if height % 10_000 == 0:
        return f"BLOCK {height:,}"
    return None


def mining_animation(duration=3.0):
    """Matrix-style mining rain animation for new block discovery.

    Uses inline implementation to avoid import issues with terminal_matrix.
    """
    cols, lines = shutil.get_terminal_size((80, 24))
    chars = [chr(i) for i in range(0x30, 0x80)]
    green = "\033[32m"
    bright_green = "\033[1;32m"
    reset = "\033[0m"

    # Initialize cascades
    cascades = {}
    sys.stdout.write("\033[2J\033[H\x1b[?25l")

    end_time = time.time() + duration
    while time.time() < end_time:
        # Spawn new cascades
        if len(cascades) < cols // 2:
            col = randrange(1, cols + 1)
            if col not in cascades:
                speed = randrange(1, 4)
                length = randrange(4, lines // 2)
                cascades[col] = {'row': 1, 'speed': speed, 'length': length}

        buf = []
        to_remove = []
        for col, c in cascades.items():
            row = c['row']
            if row <= lines:
                char = choice(chars)
                buf.append(f"\033[{row};{col}H{bright_green}{char}")
                # Dim the trail
                trail_row = row - c['length']
                if 1 <= trail_row <= lines:
                    buf.append(f"\033[{trail_row};{col}H{reset} ")
            c['row'] += c['speed']
            if c['row'] - c['length'] > lines:
                to_remove.append(col)

        for col in to_remove:
            del cascades[col]

        if buf:
            sys.stdout.write(''.join(buf))
            sys.stdout.flush()

        time.sleep(0.03)

    sys.stdout.write(f"\033[2J\033[H{reset}\x1b[?25l")
    sys.stdout.flush()


def odometer_transition(old_height_str, new_height_str, settings, start_row):
    """Animate changing digits like a mechanical odometer.

    Renders intermediate digit values at the positions that changed.
    """
    colors = [settings.get('colorA', 'green'), settings.get('colorB', 'yellow')]
    font = settings.get('design', 'block')

    # Pad to same length
    max_len = max(len(old_height_str), len(new_height_str))
    old = old_height_str.zfill(max_len)
    new = new_height_str.zfill(max_len)

    # Find which digits changed
    changed = [i for i in range(max_len) if old[i] != new[i]]

    if not changed:
        return

    # Animate: show 3 intermediate frames
    frames = 3
    for frame in range(frames):
        intermediate = list(old)
        for i in changed:
            old_d = int(old[i])
            new_d = int(new[i])
            # Roll through digits
            step = (old_d + (frame + 1) * (new_d - old_d + 10) // (frames + 1)) % 10
            if frame == frames - 1:
                step = new_d
            intermediate[i] = str(step)

        text = ''.join(intermediate)
        output = render(text, colors=colors, align='center', font=font)
        lines = output.rstrip('\n').split('\n')

        buf = []
        for j, line in enumerate(lines):
            buf.append(f"\033[{start_row + j};1H\033[2K{line}")
        sys.stdout.write(''.join(buf))
        sys.stdout.flush()
        time.sleep(0.12)


def fireworks_animation(term_width, term_height, duration=5.0):
    """ASCII fireworks celebration for milestone blocks."""
    colors = [
        "\033[1;31m",  # red
        "\033[1;33m",  # yellow
        "\033[1;32m",  # green
        "\033[1;36m",  # cyan
        "\033[1;35m",  # magenta
        "\033[1;37m",  # white
    ]
    sparks = ['*', '.', '+', 'o', '\u2022', '\u2726', '\u2727', '\u2728']
    reset = "\033[0m"

    sys.stdout.write("\033[2J\033[H\x1b[?25l")

    end_time = time.time() + duration
    explosions = []

    while time.time() < end_time:
        # Spawn new explosion
        if randrange(5) == 0 or not explosions:
            cx = randrange(5, term_width - 5)
            cy = randrange(3, term_height - 3)
            color = choice(colors)
            explosions.append({
                'cx': cx, 'cy': cy, 'color': color,
                'radius': 0, 'max_radius': randrange(3, 8),
                'age': 0
            })

        buf = []
        alive = []
        for exp in explosions:
            exp['age'] += 1
            exp['radius'] = min(exp['radius'] + 1, exp['max_radius'])

            if exp['age'] > exp['max_radius'] * 3:
                # Fade: clear spark positions
                for _ in range(8):
                    dx = randrange(-exp['max_radius'], exp['max_radius'] + 1)
                    dy = randrange(-exp['max_radius'] // 2, exp['max_radius'] // 2 + 1)
                    x = exp['cx'] + dx
                    y = exp['cy'] + dy
                    if 1 <= x <= term_width and 1 <= y <= term_height:
                        buf.append(f"\033[{y};{x}H ")
                continue

            alive.append(exp)
            r = exp['radius']
            for _ in range(r * 4):
                dx = randrange(-r, r + 1)
                dy = randrange(-r // 2, r // 2 + 1)
                x = exp['cx'] + dx
                y = exp['cy'] + dy
                if 1 <= x <= term_width and 1 <= y <= term_height:
                    spark = choice(sparks)
                    buf.append(f"\033[{y};{x}H{exp['color']}{spark}")

        explosions = alive

        if buf:
            sys.stdout.write(''.join(buf) + reset)
            sys.stdout.flush()

        time.sleep(0.08)

    sys.stdout.write(f"\033[2J\033[H{reset}\x1b[?25l")
    sys.stdout.flush()
