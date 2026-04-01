"""
Centralized configuration singleton for PyBLOCK.

Loads all .conf files once at startup and caches them in memory.
Call cfg.load() once, then access cfg.path, cfg.lndconnectload, etc.
Call cfg.reload() after the setup wizard writes new config files.
"""

import json
import os

_DEFAULT_PATH = {"ip_port": "", "rpcuser": "", "rpcpass": "", "bitcoincli": ""}
_DEFAULT_LND = {"ip_port": "", "tls": "", "macaroon": "", "ln": ""}
_DEFAULT_SETTINGS = {"gradient": "", "design": "block", "colorA": "green", "colorB": "yellow"}
_DEFAULT_SETTINGS_CLOCK = {"gradient": "", "colorA": "green", "colorB": "yellow"}


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

    def load(self):
        self.path = self._load_json("bclock.conf", _DEFAULT_PATH)
        self.lndconnectload = self._load_json("blndconnect.conf", _DEFAULT_LND)
        self.settings = self._load_json("pyblocksettings.conf", _DEFAULT_SETTINGS)
        self.settings_clock = self._load_json("pyblocksettingsClock.conf", _DEFAULT_SETTINGS_CLOCK)
        self.intro_mode = self._load_json("intro.conf")
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
