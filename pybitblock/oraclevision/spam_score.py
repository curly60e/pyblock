"""
Spam score and BIP-110 status classification.

Weights are heuristic — tune in oraclevision.conf or extend compute_spam_score()
for community-driven improvements.
"""

from __future__ import annotations


def compute_spam_score(
    *,
    block_weight: int,
    total_txs: int,
    violation_weight: int,
    inscription_count: int,
    brc20_count: int,
    runes_count: int,
    op_return_count: int,
    large_witness_bytes: int,
    violation_count: int,
) -> int:
    """Compute 0-100 spam score for a block."""
    if block_weight <= 0:
        block_weight = 1
    if total_txs <= 0:
        total_txs = 1

    violation_ratio = violation_weight / block_weight
    inscription_ratio = inscription_count / total_txs
    token_ratio = (brc20_count + runes_count) / total_txs
    witness_ratio = large_witness_bytes / block_weight
    op_return_ratio = op_return_count / total_txs

    score = (
        40 * violation_ratio
        + 25 * inscription_ratio
        + 15 * witness_ratio
        + 10 * op_return_ratio
        + 10 * token_ratio * 5
    )

    if violation_count > 10:
        score += min(20, violation_count)

    return min(100, int(round(score)))


def classify_status(
    spam_score: int,
    violation_count: int,
    violation_weight: int,
    block_weight: int,
    *,
    spam_threshold: int = 45,
    violation_pct_threshold: float = 5.0,
) -> str:
    """Return CLEAN, SUSPICIOUS, or VIOLATION."""
    violation_pct = (violation_weight / max(block_weight, 1)) * 100

    if spam_score > spam_threshold or violation_pct > violation_pct_threshold:
        return "VIOLATION"
    if spam_score >= 15 or violation_count > 0:
        return "SUSPICIOUS"
    return "CLEAN"


def status_style(status: str) -> str:
    """Rich style name for terminal display."""
    return {
        "CLEAN": "bold green",
        "SUSPICIOUS": "bold yellow",
        "VIOLATION": "bold red",
    }.get(status, "white")