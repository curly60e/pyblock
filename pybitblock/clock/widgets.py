"""Clock widget components: countdown, epoch bar, fees, UTC time, and visuals."""

import math
from datetime import datetime, timezone

from cfonts import render

SPARK_BLOCKS = " \u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588"


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


def render_miner_pool(pool_name, term_width):
    """Render the mining pool that found the last block."""
    if not pool_name:
        return ""
    text = f"  \033[1;33;40m\u26cf\033[0;37;40m  Mined by: \033[1;36;40m{pool_name}\033[0;37;40m"
    pad = max(0, (term_width - len(pool_name) - 18) // 2)
    return ' ' * pad + text


def render_block_weight(weight, max_weight, term_width):
    """Render block weight as a fullness meter."""
    if weight <= 0:
        return ""
    pct = min(100.0, (weight / max_weight) * 100)
    bar_width = min(20, term_width - 40)
    filled = int(bar_width * pct / 100)
    empty = bar_width - filled

    if pct > 90:
        color = "\033[1;31;40m"  # red = nearly full
    elif pct > 70:
        color = "\033[1;33;40m"  # yellow
    else:
        color = "\033[1;32;40m"  # green

    bar = f"{color}\u2588" * filled + f"\033[0;37;40m\u2591" * empty
    text = f"  \033[0;37;40mBlock weight [{bar}\033[0;37;40m] {pct:.0f}%"
    pad = max(0, (term_width - bar_width - 22) // 2)
    return ' ' * pad + text


def render_peer_count(peers, term_width):
    """Render connected peer count."""
    if peers <= 0:
        return ""
    if peers >= 8:
        color = "\033[1;32;40m"  # green = healthy
    elif peers >= 4:
        color = "\033[1;33;40m"  # yellow
    else:
        color = "\033[1;31;40m"  # red = low

    text = f"  \033[0;37;40m\u2637 Peers: {color}{peers}\033[0;37;40m"
    pad = max(0, (term_width - 16) // 2)
    return ' ' * pad + text


def render_block_time_histogram(intervals, term_width):
    """Render mini histogram of recent block times.

    Each bar represents one block interval. Height = time taken.
    """
    if not intervals:
        return ""

    mn = min(intervals)
    mx = max(intervals)
    rng = mx - mn if mx != mn else 1

    bars = ""
    for iv in intervals:
        idx = int((iv - mn) / rng * (len(SPARK_BLOCKS) - 1))
        # Color: green for fast (<600s), yellow for normal, red for slow (>900s)
        if iv < 300:
            color = "\033[1;36;40m"  # cyan = very fast
        elif iv < 600:
            color = "\033[1;32;40m"  # green
        elif iv < 900:
            color = "\033[1;33;40m"  # yellow
        else:
            color = "\033[1;31;40m"  # red = slow
        bars += f"{color}{SPARK_BLOCKS[idx]}"

    avg_secs = sum(intervals) / len(intervals)
    avg_min = avg_secs / 60

    text = f"  \033[0;37;40mBlock times {bars}\033[0;37;40m avg {avg_min:.1f}m"
    pad = max(0, (term_width - len(intervals) - 26) // 2)
    return ' ' * pad + text


def render_streak(streak_type, streak_count, term_width):
    """Render consecutive fast/slow block streak."""
    if not streak_type or streak_count < 2:
        return ""

    if streak_type == "fast":
        color = "\033[1;32;40m"
        icon = "\u26a1"
        label = "Fast streak"
    else:
        color = "\033[1;31;40m"
        icon = "\u231b"
        label = "Slow streak"

    text = f"  {color}{icon} {label}: {streak_count} blocks\033[0;37;40m"
    pad = max(0, (term_width - 28) // 2)
    return ' ' * pad + text


def render_moon_phase(term_width):
    """Render current lunar phase as ASCII art."""
    # Calculate moon phase (0=new, 0.5=full)
    now = datetime.now(timezone.utc)
    # Known new moon: Jan 6, 2000 18:14 UTC
    ref = datetime(2000, 1, 6, 18, 14, tzinfo=timezone.utc)
    days = (now - ref).total_seconds() / 86400
    lunation = 29.53058770576
    phase = (days % lunation) / lunation  # 0.0 to 1.0

    # Moon ASCII art (8 phases)
    moons = [
        # New moon
        [" _.--. ", "|      |", "|      |", " `--'\u00b4 "],
        # Waxing crescent
        [" _.--. ", "|   )|", "|   )|", " `--'\u00b4 "],
        # First quarter
        [" _.--. ", "|  )|", "|  )|", " `--'\u00b4 "],
        # Waxing gibbous
        [" _.--. ", "|(  )|", "|(  )|", " `--'\u00b4 "],
        # Full moon
        [" _.--. ", "|(())|", "|(())|", " `--'\u00b4 "],
        # Waning gibbous
        [" _.--. ", "|(  )|", "|(  )|", " `--'\u00b4 "],
        # Last quarter
        [" _.--. ", "|(  |", "|(  |", " `--'\u00b4 "],
        # Waning crescent
        [" _.--. ", "|(   |", "|(   |", " `--'\u00b4 "],
    ]

    # Simple emoji-based moon (more reliable across terminals)
    moon_chars = [
        "\U0001f311",  # new
        "\U0001f312",  # waxing crescent
        "\U0001f313",  # first quarter
        "\U0001f314",  # waxing gibbous
        "\U0001f315",  # full
        "\U0001f316",  # waning gibbous
        "\U0001f317",  # last quarter
        "\U0001f318",  # waning crescent
    ]

    phase_names = [
        "New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
        "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent",
    ]

    idx = int(phase * 8) % 8
    moon = moon_chars[idx]
    name = phase_names[idx]

    text = f"  \033[0;37;40m{moon}  \033[1;37;40m{name}\033[0;37;40m"
    pad = max(0, (term_width - len(name) - 8) // 2)
    return ' ' * pad + text
