"""
Centralized configuration singleton for PyBLOCK.

Loads all .conf files once at startup and caches them in memory.
Call cfg.load() once, then access cfg.path, cfg.lndconnectload, etc.
Call cfg.reload() after the setup wizard writes new config files.

Supports Umbrel/Docker environment variables for auto-configuration:
  BITCOIN_RPC_HOST, BITCOIN_RPC_PORT, BITCOIN_RPC_USER, BITCOIN_RPC_PASS
  BITCOIN_CLI_PATH
  LND_HOST, LND_GRPC_PORT, LND_TLS_CERT_PATH, LND_MACAROON_PATH, LND_CLI_PATH
  PYBLOCK_MODE (A=Bitcoin+Lightning, B=Bitcoin, C=Lite)
"""

import json
import os

_DEFAULT_PATH = {"ip_port": "", "rpcuser": "", "rpcpass": "", "bitcoincli": ""}
_DEFAULT_LND = {"ip_port": "", "tls": "", "macaroon": "", "ln": ""}
_DEFAULT_SETTINGS = {"gradient": "", "design": "block", "colorA": "green", "colorB": "yellow"}
_DEFAULT_SETTINGS_CLOCK = {
    "gradient": "", "colorA": "green", "colorB": "yellow",
    "show_countdown": True, "show_epoch_bar": True,
    "show_fee_rates": True, "show_sparkline": False,
    "show_utc_time": False, "zen_mode": False,
    "animation": "matrix",
    "fireworks": True,
    "generative_art": False,
    "sound": "bell",
    "heartbeat": True,
}


def _env_bitcoin_config():
    """Build Bitcoin config from environment variables (Umbrel/Docker)."""
    host = os.environ.get("BITCOIN_RPC_HOST", "")
    port = os.environ.get("BITCOIN_RPC_PORT", "8332")
    user = os.environ.get("BITCOIN_RPC_USER", "")
    passwd = os.environ.get("BITCOIN_RPC_PASS", "")
    cli = os.environ.get("BITCOIN_CLI_PATH", "")

    if host and user:
        return {
            "ip_port": f"http://{host}:{port}",
            "rpcuser": user,
            "rpcpass": passwd,
            "bitcoincli": cli,
        }
    return None


def _env_lnd_config():
    """Build LND config from environment variables (Umbrel/Docker)."""
    host = os.environ.get("LND_HOST", "")
    port = os.environ.get("LND_GRPC_PORT", "10009")
    tls = os.environ.get("LND_TLS_CERT_PATH", "")
    macaroon = os.environ.get("LND_MACAROON_PATH", "")
    cli = os.environ.get("LND_CLI_PATH", "")

    if host or tls or macaroon:
        return {
            "ip_port": f"{host}:{port}" if host else "",
            "tls": tls,
            "macaroon": macaroon,
            "ln": cli,
        }
    return None


def _env_mode():
    """Get PyBLOCK mode from environment variable."""
    return os.environ.get("PYBLOCK_MODE", "")


class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._loaded = False
        return cls._instance

    def __init__(self):
        if not self._loaded:
            self.config_dir = self._find_config_dir()
            self.path = dict(_DEFAULT_PATH)
            self.lndconnectload = dict(_DEFAULT_LND)
            self.settings = dict(_DEFAULT_SETTINGS)
            self.settings_clock = dict(_DEFAULT_SETTINGS_CLOCK)
            self.intro_mode = None

    def _find_config_dir(self):
        candidates = [
            os.path.join(os.path.dirname(__file__), "config"),
            "config",
            os.path.join(os.path.dirname(__file__), "SPV", "config"),
        ]
        for d in candidates:
            if os.path.isdir(d):
                return d
        return "config"

    def _load_json(self, filename, defaults=None):
        filepath = os.path.join(self.config_dir, filename)
        if os.path.isfile(filepath):
            with open(filepath, "r") as f:
                data = json.load(f)
            if defaults and isinstance(data, dict):
                merged = dict(defaults)
                merged.update(data)
                return merged
            return data
        return dict(defaults) if defaults else None

    def _apply_env_overrides(self):
        """Apply environment variable overrides (Umbrel/Docker mode).

        Env vars take priority over config files. If env vars are set,
        they also auto-generate the config files for consistency.
        """
        btc_env = _env_bitcoin_config()
        if btc_env:
            self.path.update(btc_env)
            self._ensure_config("bclock.conf", self.path)

        lnd_env = _env_lnd_config()
        if lnd_env:
            self.lndconnectload.update(lnd_env)
            self._ensure_config("blndconnect.conf", self.lndconnectload)

        mode_env = _env_mode()
        if mode_env and mode_env in ("A", "B", "C"):
            self.intro_mode = mode_env
            self._ensure_config("intro.conf", mode_env)

    def _ensure_config(self, filename, data):
        """Write config file if it doesn't exist or env vars are set."""
        filepath = os.path.join(self.config_dir, filename)
        os.makedirs(self.config_dir, exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        self.path = self._load_json("bclock.conf", _DEFAULT_PATH)
        self.lndconnectload = self._load_json("blndconnect.conf", _DEFAULT_LND)
        self.settings = self._load_json("pyblocksettings.conf", _DEFAULT_SETTINGS)
        self.settings_clock = self._load_json("pyblocksettingsClock.conf", _DEFAULT_SETTINGS_CLOCK)
        self.intro_mode = self._load_json("intro.conf")
        self._apply_env_overrides()
        self._loaded = True

    def reload(self):
        self._loaded = False
        self.load()

    def save(self, filename, data):
        filepath = os.path.join(self.config_dir, filename)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        self.reload()

    def has_config(self, filename):
        return os.path.isfile(os.path.join(self.config_dir, filename))


cfg = Config()
