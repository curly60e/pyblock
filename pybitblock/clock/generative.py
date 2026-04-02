"""Block hash generative ASCII art.

Uses hash bytes as seeds to create a unique visual pattern per block.
"""

# Characters ordered by visual density
GLYPHS = " \u2591\u2592\u2593\u2588\u2580\u2584\u258c\u2590\u256c\u2550\u2551"

# 256-color ANSI foreground
def _color256(n):
    return f"\033[38;5;{n}m"

RESET = "\033[0m"


def hash_art(block_hash, width=40, height=6):
    """Generate deterministic ASCII art from a block hash string.

    Each pair of hex digits maps to a glyph and color.
    The pattern is mirrored horizontally for symmetry.
    """
    # Convert hex hash to bytes
    raw = block_hash.strip()
    hex_pairs = [raw[i:i+2] for i in range(0, len(raw), 2)]
    values = [int(h, 16) for h in hex_pairs if len(h) == 2]

    if not values:
        return ""

    half_w = width // 2
    lines = []

    for row in range(height):
        left = []
        for col in range(half_w):
            idx = (row * half_w + col) % len(values)
            val = values[idx]

            # Glyph from lower nibble
            glyph = GLYPHS[val % len(GLYPHS)]
            # Color from upper nibble + row offset (for variety)
            color_idx = 16 + ((val + row * 7) % 216)  # 216-color cube
            left.append(f"{_color256(color_idx)}{glyph}")

        # Mirror for symmetry
        right = list(reversed(left))
        line = ''.join(left) + ''.join(right) + RESET
        # Center it
        pad = max(0, (80 - width) // 2)
        lines.append(' ' * pad + line)

    return '\n'.join(lines)
