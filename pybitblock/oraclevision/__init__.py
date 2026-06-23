"""
OracleVision analysis integration for PyBLOCK.

Lightweight BIP-110 and mempool composition tooling for sovereign node
operators. Core detection logic is ported from OracleVision and kept
modular so the community can extend heuristics without touching the UI.

Upstream: https://github.com/MarcanoFilms/oraculovision
"""

from oraclevision.address_service import AddressInspection, AddressService
from oraclevision.bip110 import BlockAnalysis, TxAnalysis, analyze_block, analyze_transaction
from oraclevision.mempool_compose import MempoolComposition, analyze_block_template, categorize_transaction
from oraclevision.tx_flow import TxFlowSummary, TxIO, build_flow_summary
from oraclevision.tx_service import TxInspectContext, TxInspection, TxService

__all__ = [
    "AddressInspection",
    "AddressService",
    "BlockAnalysis",
    "TxAnalysis",
    "TxFlowSummary",
    "TxIO",
    "TxInspectContext",
    "TxInspection",
    "TxService",
    "MempoolComposition",
    "analyze_block",
    "analyze_transaction",
    "analyze_block_template",
    "build_flow_summary",
    "categorize_transaction",
]