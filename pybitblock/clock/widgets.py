"""Clock widget components: countdown, epoch bar, fees, UTC time."""

from datetime import datetime, timezone

from cfonts import render


def render_countdown(seconds_since_block, term_width):
    """Render time since last block with color coding.

    Green: <600s (10min), Yellow: 600-1200s, Red: >1200s.
    """
    mins = seconds_since_block // 60
    secs = seconds_since_block % 60

    if seconds_since_block < 600:
        color = "\033[1;32;40m"  # green
    elif seconds_since_block < 1200:
        color = "\033[1;33;40m"  # yellow
    else:
        color = "\033[1;31;40m"  # red

    text = f"{color}  \u23f1  {mins}m {secs:02d}s since last block\033[0;37;40m"
    pad = max(0, (term_width - 35) // 2)
    return ' ' * pad + text


def render_epoch_bar(block_height, epoch_block, blocks_to_halving,
                     next_halving_block, term_width):
    """Render difficulty epoch progress bar + halving info."""
    # Difficulty adjustment progress
    epoch_pct = (epoch_block / 2016) * 100
    bar_width = min(30, term_width - 40)
    filled = int(bar_width * epoch_block / 2016)
    empty = bar_width - filled
    blocks_left = 2016 - epoch_block

    bar = f"\033[1;36;40m\u2593" * filled + f"\033[0;37;40m\u2591" * empty
    epoch_line = (
        f"  \033[1;36;40mEpoch\033[0;37;40m [{bar}\033[0;37;40m] "
        f"{epoch_block}/2016 ({epoch_pct:.1f}%) "
        f"· {blocks_left} blocks to retarget"
    )

    # Halving progress
    if next_halving_block > 0:
        halving_num = next_halving_block // 210_000
        halving_line = (
            f"  \033[1;35;40mHalving #{halving_num}\033[0;37;40m "
            f"in {blocks_to_halving:,} blocks "
            f"(block {next_halving_block:,})"
        )
        return epoch_line + "\n" + halving_line

    return epoch_line


def render_fees(fastest, half_hour, hour, term_width):
    """Render compact fee rate display."""
    if fastest == 0 and half_hour == 0 and hour == 0:
        return ""

    text = (
        f"  \033[1;31;40m\u26a1 {fastest}\033[0;37;40m | "
        f"\033[1;33;40m\u23f3 {half_hour}\033[0;37;40m | "
        f"\033[1;32;40m\u2623 {hour}\033[0;37;40m sat/vB"
    )
    pad = max(0, (term_width - 40) // 2)
    return ' ' * pad + text


def render_utc_time(colors):
    """Render current UTC time in tiny cfonts font."""
    now = datetime.now(timezone.utc).strftime("%H:%M")
    output = render(now, colors=colors, align='center', font='tiny')
    return output
