"""
OracleVision settings for PyBLOCK.

Stored in config/oraclevision.conf (JSON). Environment overrides:
  ORACULOVISION_BLOCK_SCAN_COUNT
  ORACULOVISION_SPAM_THRESHOLD
  ORACULOVISION_COMMAND
  BITCOIN_DATADIR
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass

from config import cfg


_DEFAULTS = {
    "block_scan_count": 10,
    "spam_score_threshold": 45,
    "bitcoin_datadir": "",
    "oraculovision_command": "oraculovision",
    "cli_timeout_seconds": 60,
}


@dataclass
class OracleVisionSettings:
    block_scan_count: int = 10
    spam_score_threshold: int = 45
    bitcoin_datadir: str = ""
    oraculovision_command: str = "oraculovision"
    cli_timeout_seconds: int = 60


def load_settings() -> OracleVisionSettings:
    """Load OracleVision config, merging defaults, file, and env vars."""
    data = dict(_DEFAULTS)
    filepath = os.path.join(cfg.config_dir, "oraclevision.conf")
    if os.path.isfile(filepath):
        with open(filepath, "r") as f:
            file_data = json.load(f)
        if isinstance(file_data, dict):
            data.update(file_data)

    if env_count := os.environ.get("ORACULOVISION_BLOCK_SCAN_COUNT"):
        data["block_scan_count"] = int(env_count)
    if env_threshold := os.environ.get("ORACULOVISION_SPAM_THRESHOLD"):
        data["spam_score_threshold"] = int(env_threshold)
    if env_cmd := os.environ.get("ORACULOVISION_COMMAND"):
        data["oraculovision_command"] = env_cmd
    if env_datadir := os.environ.get("BITCOIN_DATADIR"):
        data["bitcoin_datadir"] = env_datadir

    return OracleVisionSettings(
        block_scan_count=int(data["block_scan_count"]),
        spam_score_threshold=int(data["spam_score_threshold"]),
        bitcoin_datadir=str(data.get("bitcoin_datadir", "")),
        oraculovision_command=str(data.get("oraculovision_command", "oraculovision")),
        cli_timeout_seconds=int(data.get("cli_timeout_seconds", 60)),
    )