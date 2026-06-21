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
from oraclevision.security import validate_safe_path_token


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
    load_error: str | None = None


def _safe_int(value: object, default: int, *, field: str, errors: list[str]) -> int:
    try:
        return int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        errors.append(f"Invalid {field}; using default {default}")
        return default


def load_settings() -> OracleVisionSettings:
    """Load OracleVision config, merging defaults, file, and env vars."""
    data = dict(_DEFAULTS)
    errors: list[str] = []
    filepath = os.path.join(cfg.config_dir, "oraclevision.conf")

    if os.path.isfile(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                file_data = json.load(f)
            if isinstance(file_data, dict):
                data.update(file_data)
            else:
                errors.append("oraclevision.conf must be a JSON object; using defaults")
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in oraclevision.conf: {exc}")
        except OSError as exc:
            errors.append(f"Could not read oraclevision.conf: {exc}")

    if env_count := os.environ.get("ORACULOVISION_BLOCK_SCAN_COUNT"):
        data["block_scan_count"] = _safe_int(env_count, data["block_scan_count"], field="block_scan_count", errors=errors)
    if env_threshold := os.environ.get("ORACULOVISION_SPAM_THRESHOLD"):
        data["spam_score_threshold"] = _safe_int(
            env_threshold, data["spam_score_threshold"], field="spam_score_threshold", errors=errors
        )
    if env_cmd := os.environ.get("ORACULOVISION_COMMAND"):
        data["oraculovision_command"] = env_cmd
    if env_datadir := os.environ.get("BITCOIN_DATADIR"):
        data["bitcoin_datadir"] = env_datadir

    bitcoin_datadir = ""
    try:
        bitcoin_datadir = validate_safe_path_token(
            str(data.get("bitcoin_datadir", "")), name="bitcoin_datadir", allow_empty=True
        )
    except ValueError as exc:
        errors.append(str(exc))
        bitcoin_datadir = ""

    oraculovision_command = str(data.get("oraculovision_command", "oraculovision"))
    try:
        validate_safe_path_token(oraculovision_command, name="oraculovision_command", allow_empty=False)
    except ValueError as exc:
        errors.append(str(exc))
        oraculovision_command = _DEFAULTS["oraculovision_command"]

    return OracleVisionSettings(
        block_scan_count=_safe_int(
            data.get("block_scan_count", 10), 10, field="block_scan_count", errors=errors
        ),
        spam_score_threshold=_safe_int(
            data.get("spam_score_threshold", 45), 45, field="spam_score_threshold", errors=errors
        ),
        bitcoin_datadir=bitcoin_datadir,
        oraculovision_command=oraculovision_command,
        cli_timeout_seconds=_safe_int(
            data.get("cli_timeout_seconds", 60), 60, field="cli_timeout_seconds", errors=errors
        ),
        load_error="; ".join(errors) if errors else None,
    )