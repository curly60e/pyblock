"""Hashrate sparkline using Unicode block characters."""

SPARK_CHARS = " \u2581\u2582\u2583\u2584\u2585\u2586\u2587\u2588"


def render_sparkline(values, current_hashrate, term_width):
    """Render a mini sparkline graph for hashrate history.

    values: list of hashrate floats (last N data points)
    current_hashrate: current hashrate in H/s
    term_width: terminal width for centering
    """
    if not values:
        return ""

    mn = min(values)
    mx = max(values)
    rng = mx - mn if mx != mn else 1

    spark = ""
    for v in values:
        idx = int((v - mn) / rng * (len(SPARK_CHARS) - 1))
        spark += SPARK_CHARS[idx]

    # Format hashrate in human-readable units
    hr_str = _format_hashrate(current_hashrate)

    text = f"  \033[1;33;40mHashrate\033[0;37;40m {spark} {hr_str}"
    pad = max(0, (term_width - len(spark) - len(hr_str) - 12) // 2)
    return ' ' * pad + text


def _format_hashrate(h):
    """Format hashrate in appropriate unit."""
    if h <= 0:
        return "-- H/s"
    units = [
        (1e18, "EH/s"),
        (1e15, "PH/s"),
        (1e12, "TH/s"),
        (1e9, "GH/s"),
        (1e6, "MH/s"),
        (1e3, "KH/s"),
    ]
    for threshold, unit in units:
        if h >= threshold:
            return f"{h / threshold:.1f} {unit}"
    return f"{h:.0f} H/s"
