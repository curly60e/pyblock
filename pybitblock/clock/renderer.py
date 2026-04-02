"""Screen layout and rendering engine for the enhanced block clock.

Uses ANSI cursor positioning for flicker-free partial screen updates.
Composes cfonts output with widget overlays.
"""

import shutil
import sys
import time

from cfonts import render

from .widgets import (
    render_countdown,
    render_epoch_bar,
    render_fees,
    render_utc_time,
)
from .sparkline import render_sparkline
from .generative import hash_art
from .sound import play_sound


# ANSI helpers
def _move(row, col=1):
    return f"\033[{row};{col}H"


def _clear_line():
    return "\033[2K"


def _hide_cursor():
    return "\x1b[?25l"


def _show_cursor():
    return "\x1b[?25h"


def _bold(text):
    return f"\033[1m{text}\033[0m"


def _dim(text):
    return f"\033[2m{text}\033[0m"


def _clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()


def _render_block_height(height, settings):
    """Render block height using cfonts."""
    colors = [settings.get('colorA', 'green'), settings.get('colorB', 'yellow')]
    gradient = settings.get('gradient', '')
    font = settings.get('design', 'block')

    kwargs = {'align': 'center', 'font': font}
    if gradient == 'grd':
        kwargs['gradient'] = colors
    else:
        kwargs['colors'] = colors

    return render(str(height), **kwargs)


class Layout:
    """Manages screen regions and partial updates."""

    def __init__(self, settings):
        self.settings = settings
        self.term_width, self.term_height = shutil.get_terminal_size((80, 24))
        self._height_lines = 0
        self._heartbeat_step = 0
        self._last_rendered_height = None

    def _is_zen(self):
        return self.settings.get('zen_mode', False)

    def _write(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()

    def _render_cfonts_at(self, output, start_row):
        """Render cfonts output at a specific row, line by line."""
        lines = output.rstrip('\n').split('\n')
        self._height_lines = len(lines)
        buf = []
        for i, line in enumerate(lines):
            buf.append(_move(start_row + i) + _clear_line() + line)
        self._write(''.join(buf))
        return start_row + len(lines)

    def render_full(self, data):
        """Clear screen and render all regions."""
        _clear_screen()
        self._write(_hide_cursor())
        self.term_width, self.term_height = shutil.get_terminal_size((80, 24))

        output = _render_block_height(data.block_height, self.settings)
        self._last_rendered_height = data.block_height

        if self._is_zen():
            # Center vertically
            lines = output.rstrip('\n').split('\n')
            start = max(1, (self.term_height - len(lines)) // 2)
            self._render_cfonts_at(output, start)
            return

        # Region 1: Block height (row 2)
        next_row = self._render_cfonts_at(output, 2)

        # Region 2: Block info
        next_row = self._render_info(data, next_row + 1)

        # Region 3+: Widgets
        self._render_widgets(data, next_row + 1)

    def _render_info(self, data, row):
        """Render block size and tx count line."""
        if data.block_size > 0:
            size_mb = data.block_size / 1_000_000
            info = f"  \033[0;37;40m{size_mb:.2f} MB  ·  {data.block_tx_count} txs"
            center_pad = max(0, (self.term_width - len(info) + 20) // 2)
            self._write(_move(row) + _clear_line() + ' ' * center_pad + info)
            return row + 1
        return row

    def _render_widgets(self, data, start_row):
        """Render all enabled widget overlays."""
        row = start_row
        s = self.settings
        w = self.term_width

        if s.get('show_countdown', True):
            text = render_countdown(data.seconds_since_block, w)
            self._write(_move(row) + _clear_line() + text)
            row += 2

        if s.get('show_epoch_bar', True):
            text = render_epoch_bar(
                data.block_height, data.epoch_block,
                data.blocks_to_halving, data.next_halving_block, w
            )
            self._write(_move(row) + _clear_line() + text)
            row += 2

        if s.get('show_fee_rates', True):
            text = render_fees(
                data.fee_fastest, data.fee_half_hour, data.fee_hour, w
            )
            self._write(_move(row) + _clear_line() + text)
            row += 2

        if s.get('show_sparkline', False) and data.hashrate_history:
            text = render_sparkline(
                data.hashrate_history, data.hashrate_current, w
            )
            self._write(_move(row) + _clear_line() + text)
            row += 2

        if s.get('show_utc_time', False):
            text = render_utc_time(
                [s.get('colorA', 'green'), s.get('colorB', 'yellow')]
            )
            lines = text.rstrip('\n').split('\n')
            for i, line in enumerate(lines):
                self._write(_move(row + i) + _clear_line() + line)
            row += len(lines) + 1

        if s.get('generative_art', False) and data.block_hash:
            art = hash_art(data.block_hash, min(60, w - 4), 6)
            lines = art.split('\n')
            for i, line in enumerate(lines):
                self._write(_move(row + i) + _clear_line() + line)
            row += len(lines) + 1

        return row

    def update_countdown(self, data):
        """Update only the countdown timer (called every poll cycle)."""
        if self._is_zen() or not self.settings.get('show_countdown', True):
            return
        # Countdown is rendered right after block height + info line
        row = 2 + self._height_lines + 2
        text = render_countdown(data.seconds_since_block, self.term_width)
        self._write(_move(row) + _clear_line() + text)

    def heartbeat(self, data):
        """Toggle bold/dim on block height for breathing effect."""
        if self._is_zen() or not self.settings.get('heartbeat', True):
            return
        if self._last_rendered_height is None:
            return

        self._heartbeat_step += 1
        output = _render_block_height(data.block_height, self.settings)
        lines = output.rstrip('\n').split('\n')

        start_row = 2
        if self._is_zen():
            start_row = max(1, (self.term_height - len(lines)) // 2)

        # Apply dim on odd steps
        wrapper = _dim if self._heartbeat_step % 2 == 1 else lambda x: x
        buf = []
        for i, line in enumerate(lines):
            buf.append(_move(start_row + i) + _clear_line() + wrapper(line))
        self._write(''.join(buf))

    def on_new_block(self, data, animations_mod):
        """Handle new block arrival: sound, animation, then full re-render."""
        play_sound(self.settings.get('sound', 'bell'))

        anim = self.settings.get('animation', 'matrix')

        # Check for milestone fireworks first
        if self.settings.get('fireworks', True):
            milestone = animations_mod.is_milestone_block(data.block_height)
            if milestone:
                animations_mod.fireworks_animation(
                    self.term_width, self.term_height, duration=5.0
                )

        if anim == 'matrix':
            animations_mod.mining_animation(duration=3.0)
        elif anim == 'odometer' and self._last_rendered_height is not None:
            animations_mod.odometer_transition(
                str(self._last_rendered_height),
                str(data.block_height),
                self.settings, 2
            )

        self.render_full(data)

    def cleanup(self):
        """Restore terminal state."""
        self._write(_show_cursor() + "\033[0m")
