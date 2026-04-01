"""
Shared color and formatting utilities for PyBLOCK.

Used by both PyBlock.py and SPV/spvblock.py for ANSI color rendering.
"""


def get_ansi_color_code(r, g, b):
    if r == g == b:
        if r < 8:
            return 16
        return 231 if r > 248 else round(((r - 8) / 247) * 24) + 232
    return 16 + (36 * round(r / 255 * 5)) + (6 * round(g / 255 * 5)) + round(b / 255 * 5)


def get_color(r, g, b):
    return f"\x1b[48;5;{int(get_ansi_color_code(r, g, b))}m \x1b[0m"
