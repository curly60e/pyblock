"""
Input validation helpers for OracleVision subprocess and config paths.

Prevents command injection when launching external binaries configured by
the node operator (bitcoin-cli path, oraculovision command, datadir).
"""

from __future__ import annotations

import os
import re
import shlex
import shutil

_SHELL_META = re.compile(r"[;|&$`<>\"'\n\\]")
_RPC_METHOD = re.compile(r"^[a-z][a-z0-9_]*$", re.I)


def validate_safe_path_token(value: str, *, name: str = "path", allow_empty: bool = True) -> str:
    """Reject shell metacharacters in filesystem path tokens."""
    value = (value or "").strip()
    if not value:
        if allow_empty:
            return ""
        raise ValueError(f"{name} must not be empty")
    if _SHELL_META.search(value):
        raise ValueError(f"Invalid characters in {name}")
    return value


def validate_rpc_method(method: str) -> str:
    """Ensure bitcoin-cli RPC method names are safe tokens."""
    method = (method or "").strip()
    if not _RPC_METHOD.fullmatch(method):
        raise ValueError(f"Invalid RPC method: {method!r}")
    return method


def resolve_executable(command: str) -> list[str]:
    """Resolve a single executable name or absolute path for subprocess.run."""
    command = (command or "").strip()
    if not command:
        raise ValueError("Empty command")

    parts = shlex.split(command)
    if len(parts) != 1:
        raise ValueError("Command must be a single executable (no shell arguments)")

    exe = validate_safe_path_token(parts[0], name="command", allow_empty=False)

    if os.path.isabs(exe):
        if not os.path.isfile(exe) or not os.access(exe, os.X_OK):
            raise ValueError(f"Not executable: {exe}")
        return [exe]

    resolved = shutil.which(exe)
    if not resolved:
        raise ValueError(f"Command not found: {exe}")
    return [resolved]


def resolve_bitcoin_cli(cli_path: str) -> str:
    """Resolve and validate bitcoin-cli executable path."""
    cli_path = validate_safe_path_token(cli_path or "bitcoin-cli", name="bitcoincli", allow_empty=False)

    if os.path.isabs(cli_path):
        if not os.path.isfile(cli_path):
            raise ValueError(f"bitcoin-cli not found: {cli_path}")
        return cli_path

    resolved = shutil.which(cli_path)
    if not resolved:
        raise ValueError(f"bitcoin-cli not found: {cli_path}")
    return resolved