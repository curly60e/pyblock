"""Pluggable transaction detector registry."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol

_DEFAULT_ENABLED = ("builtin",)


@dataclass
class DetectorResult:
    bip110_flags: set[str] = field(default_factory=set)
    signals: set[str] = field(default_factory=set)
    witness_bytes: int = 0


class TxDetector(Protocol):
    name: str

    def detect(self, tx: dict[str, Any]) -> DetectorResult: ...


_REGISTRY: dict[str, TxDetector] = {}
_ACTIVE: tuple[str, ...] = _DEFAULT_ENABLED


def register(detector: TxDetector) -> None:
    _REGISTRY[detector.name] = detector


def set_enabled(names: list[str] | tuple[str, ...] | None) -> None:
    global _ACTIVE
    if not names:
        _ACTIVE = _DEFAULT_ENABLED
        return
    _ACTIVE = tuple(names)


def enabled_detectors() -> tuple[str, ...]:
    return _ACTIVE


def run_detectors(tx: dict[str, Any], *, enabled: tuple[str, ...] | None = None) -> DetectorResult:
    """Run enabled detectors and merge their results.

    ``witness_bytes`` uses max() because each detector must report the full
    transaction witness size, not a per-input partial measurement.
    """
    names = enabled or _ACTIVE
    combined = DetectorResult()
    for name in names:
        detector = _REGISTRY.get(name)
        if detector is None:
            continue
        result = detector.detect(tx)
        combined.bip110_flags |= result.bip110_flags
        combined.signals |= result.signals
        combined.witness_bytes = max(combined.witness_bytes, result.witness_bytes)
    return combined


def _ensure_builtin_registered() -> None:
    if "builtin" not in _REGISTRY:
        from oraclevision.detectors.builtin import BuiltinDetector

        register(BuiltinDetector())


def configure_detectors(enabled: list[str] | None = None) -> None:
    """Load built-in detectors and apply config-enabled list."""
    _ensure_builtin_registered()
    if enabled:
        for name in enabled:
            if name == "example_dust":
                try:
                    from oraclevision.detectors.example_dust import DustDetector

                    register(DustDetector())
                except ImportError:
                    pass
    set_enabled(enabled)
