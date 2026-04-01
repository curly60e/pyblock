"""
Logging configuration for PyBLOCK.

Usage:
    from log import get_logger
    logger = get_logger(__name__)
    logger.debug("detailed info")
    logger.error("user-facing error: %s", e)
"""

import logging
import os
from logging.handlers import RotatingFileHandler

_configured = False


def _setup():
    global _configured
    if _configured:
        return
    _configured = True

    log_dir = os.path.join(os.path.dirname(__file__), "config")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "pyblock.log")

    root = logging.getLogger("pyblock")
    root.setLevel(logging.DEBUG)

    if not root.handlers:
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1_048_576, backupCount=3, encoding="utf-8"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        ))
        root.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(logging.Formatter(
            "\033[1;31;40m[%(levelname)s]\033[0;37;40m %(message)s"
        ))
        root.addHandler(console_handler)


def get_logger(name):
    _setup()
    return logging.getLogger(f"pyblock.{name}")
