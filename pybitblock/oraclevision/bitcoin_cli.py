"""
bitcoin-cli wrapper for OracleVision analysis inside PyBLOCK.

Uses the same bitcoin-cli path configured in bclock.conf. No extra deps.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from typing import Any


class BitcoinCLIError(Exception):
    """Raised when bitcoin-cli fails or is unavailable."""

    def __init__(self, message: str, *, hint: str | None = None) -> None:
        self.hint = hint
        super().__init__(message)


class BitcoinCLI:
    """Thin wrapper around bitcoin-cli JSON-RPC for analysis commands."""

    def __init__(
        self,
        cli_path: str,
        datadir: str | None = None,
        timeout: float = 60.0,
    ) -> None:
        self.cli_path = cli_path or os.environ.get("BITCOIN_CLI", "bitcoin-cli")
        self.datadir = datadir or os.environ.get("BITCOIN_DATADIR") or ""
        self.timeout = timeout

    def _base_cmd(self) -> list[str]:
        cmd = [self.cli_path]
        if self.datadir:
            cmd.extend(["-datadir", self.datadir])
        return cmd

    def call(self, method: str, *params: Any) -> Any:
        if not shutil.which(self.cli_path) and not os.path.isabs(self.cli_path):
            raise BitcoinCLIError(
                f"bitcoin-cli not found: {self.cli_path}",
                hint="Install Bitcoin Knots or set bitcoincli in config/bclock.conf",
            )

        cmd = self._base_cmd() + [method]
        for param in params:
            if isinstance(param, (dict, list)):
                cmd.append(json.dumps(param))
            elif isinstance(param, bool):
                cmd.append("true" if param else "false")
            else:
                cmd.append(str(param))

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
                check=False,
            )
        except subprocess.TimeoutExpired as exc:
            raise BitcoinCLIError(
                f"Timeout calling {method} ({self.timeout}s)",
                hint="The node may be busy or unresponsive.",
            ) from exc
        except FileNotFoundError as exc:
            raise BitcoinCLIError(
                f"bitcoin-cli not found: {self.cli_path}",
                hint="Check your Knots/Core installation.",
            ) from exc

        if result.returncode != 0:
            stderr = (result.stderr or result.stdout or "").strip()
            hint = None
            lower = stderr.lower()
            if "could not connect" in lower or "connection refused" in lower:
                hint = "Start bitcoind/knots and check RPC (bitcoin.conf)."
            elif "verifying blocks" in lower or "initial block download" in lower:
                hint = "Node still syncing. Wait for IBD to finish."
            elif "not available" in lower and method == "getblocktemplate":
                hint = "Enable mining RPC or use a node that supports getblocktemplate."
            raise BitcoinCLIError(stderr or f"Error in {method}", hint=hint)

        stdout = result.stdout.strip()
        if not stdout:
            return None
        try:
            return json.loads(stdout)
        except json.JSONDecodeError:
            return stdout

    def get_block_count(self) -> int:
        return int(self.call("getblockcount"))

    def get_block_hash(self, height: int) -> str:
        return str(self.call("getblockhash", height))

    def get_block(self, block_hash: str, verbosity: int = 2) -> dict[str, Any]:
        return self.call("getblock", block_hash, verbosity)

    def get_mempool_info(self) -> dict[str, Any]:
        return self.call("getmempoolinfo")

    def get_block_template(self) -> dict[str, Any]:
        return self.call("getblocktemplate", {"rules": ["segwit"]})

    def decode_raw_transaction(self, hex_data: str) -> dict[str, Any]:
        return self.call("decoderawtransaction", hex_data)

    @classmethod
    def from_path_config(cls, path: dict[str, str], datadir: str = "", timeout: float = 60.0) -> "BitcoinCLI":
        return cls(path.get("bitcoincli", "bitcoin-cli"), datadir=datadir, timeout=timeout)