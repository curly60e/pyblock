# OracleVision v2.2: Transaction Inspector & Pluggable Detectors

## Summary

This PR upgrades PyBLOCK's OracleVision integration from the initial v1 port to **v2.2 analysis parity**, adding deep transaction inspection, address lookup, pluggable BIP-110 detectors, and cross-menu drill-down from block analysis.

All features run locally via `bitcoin-cli` — **Don't Trust, Verify**.

## Motivation

The initial OracleVision integration (PR #738) gave PyBLOCK operators block scanning, Mempool Glass, and block detail views. The standalone [OracleVision](https://github.com/MarcanoFilms/oraculovision) project has since shipped **v2.2** with:

- **Transaction Inspector** — input/output flow, fees, BIP-110 flags, spam signals
- **Address Inspector** — UTXO balance via `scantxoutset`, mempool exposure
- **Pluggable detectors** — community-extensible BIP-110 rule checks
- **Pruned-node support** — partial inspection from block scan cache (`flagged_raw`)

This PR ports those analysis capabilities into PyBLOCK's Rich terminal UI so operators get v2.2 tooling without leaving the PyBLOCK menu.

## What's New

### Menu changes

| Option | Before | After |
|--------|--------|-------|
| A | BIP-110 Block Scanner | *(unchanged)* |
| B | Mempool Glass | *(unchanged, improved docs)* |
| C | Block Detail View | **+ drill-down to Transaction Inspector** |
| D | Launch Full TUI | **Transaction & Address Inspector** |
| E | — | Launch Full OracleVision TUI *(was D)* |

### New module: Transaction & Address Inspector (D)

Dual-mode inspector accepting a **64-char txid** or **Bitcoin address**:

**Transaction mode** shows:
- Mempool / confirmation status, block height, fees (BTC + sat/vB)
- Input/output flow with addresses, values, script types
- Mempool category (economic / spam / coinjoin / consolidation)
- BIP-110 compliance label and flag list
- Spam signals (inscription, BRC-20, runes, ordinals, OP_RETURN)

**Address mode** shows:
- Node validation, script type
- UTXO balance and count (`scantxoutset`, configurable timeout)
- Mempool exposure (capped scan of pending outputs)

**Pruned-node handling:**
- Block Detail caches flagged raw transactions during scan
- Inspector uses cached data when `getrawtransaction` is unavailable
- Partial view clearly labeled with yellow border

### Pluggable detectors (`pybitblock/oraclevision/detectors/`)

Refactored `bip110.py` to delegate per-transaction analysis to a detector registry:

| File | Purpose |
|------|---------|
| `detectors/__init__.py` | Registry API: `register()`, `run_detectors()`, `configure_detectors()` |
| `detectors/builtin.py` | Default Knots BIP-110 + spam heuristics (extracted from monolithic bip110) |

Community PRs can add new detectors without touching UI code. Enable via `detectors_enabled` in config.

### New supporting modules

| File | Purpose |
|------|---------|
| `tx_flow.py` | Pure I/O parsing: inputs, outputs, fees, senders/recipients |
| `tx_service.py` | Fetch, enrich, and format transaction inspections |
| `address_service.py` | Address validation, UTXO scan, mempool exposure |
| `addresses.py` | Query classification (txid vs address) |
| `markup.py` | Safe Rich markup escaping for node-sourced text |

### Extended `bitcoin_cli.py`

New RPC wrappers for the inspector:
- `getrawmempool(verbose)`
- `getrawtransaction(txid, verbose, block_hash=…)` — pruned-node compatible
- `getblockchaininfo()`
- `validateaddress(address)`
- `scantxoutset_address(address, timeout=…)`

### Block analysis improvements

- `BlockAnalysis.flagged_raw` — caches raw tx dicts for flagged transactions
- Block Detail prompts for tx drill-down after showing problematic transactions
- Mempool Glass notes link to Transaction Inspector

## Configuration

New keys in `oraclevision.conf`:

| Setting | Default | Description |
|---------|---------|-------------|
| `max_vin_lookups` | 4 | Parent tx RPC lookups to resolve missing prevouts |
| `scantxoutset_timeout` | 90 | Seconds for UTXO scan (address mode) |
| `mempool_scan_limit` | 30 | Max mempool txs scanned for address exposure |
| `detectors_enabled` | `["builtin"]` | Active detector plugins |

## Design Principles

- **Zero extra dependencies** — Rich UI + bitcoin-cli only (same as PyBLOCK)
- **Modular analysis** — detectors, tx_flow, services separated from terminal UI
- **Upstream alignment** — ported from OracleVision v2.2 analysis layer
- **Full TUI still external** — option E launches standalone Textual dashboard

## Relationship to Standalone OracleVision

| Feature | PyBLOCK built-in | Full OracleVision TUI |
|---------|------------------|----------------------|
| Block scanner | Yes | Yes (+ live charts) |
| Mempool Glass | Yes | Yes (+ dedicated screen) |
| Tx Inspector | Yes (Rich terminal) | Yes (Textual, keyboard nav) |
| Address Inspector | Yes (UTXO + mempool) | Yes (+ history export) |
| DATUM mining panel | No | Yes |
| Ocean account stats | No | Yes |
| Multi-screen navigation | No | Yes |

Operators who want the full dashboard install OracleVision separately and use **E. Launch Full OracleVision TUI**.

## Testing

```bash
cd pybitblock

# Import check
python3 -c "from oraclevision.tx_service import TxService; print('ok')"

# Unit tests
python3 -m pytest tests/oraclevision/ -v

# Manual test path
python3 PyBlock.py
# → B. Bitcoin → OV. OracleVision
#   → D. Transaction & Address Inspector (paste a txid)
#   → C. Block Detail View → inspect flagged tx
```

### Node requirements

- Synced Knots/Core with RPC enabled
- `getblock` verbosity 2 (block scanner, block detail)
- `getblocktemplate` with mining RPC (Mempool Glass)
- `getrawtransaction` with optional `blockhash` (tx inspector)
- `scantxoutset` (address mode — can take up to 90s on large UTXO sets)

## Files Changed

### New
- `pybitblock/oraclevision/detectors/__init__.py`
- `pybitblock/oraclevision/detectors/builtin.py`
- `pybitblock/oraclevision/tx_flow.py`
- `pybitblock/oraclevision/tx_service.py`
- `pybitblock/oraclevision/address_service.py`
- `pybitblock/oraclevision/addresses.py`
- `pybitblock/oraclevision/markup.py`
- `pybitblock/tests/oraclevision/test_tx_flow.py`
- `pybitblock/tests/oraclevision/test_detectors.py`
- `pybitblock/tests/oraclevision/test_addresses.py`
- `PR_ORACLEVISION_V2.2.md`

### Modified
- `pybitblock/oraclevision/bip110.py` — detector architecture + `flagged_raw`
- `pybitblock/oraclevision/bitcoin_cli.py` — tx/address RPC methods
- `pybitblock/oraclevision/config.py` — inspector settings + detector config
- `pybitblock/oraclevision/ui.py` — menu D/E, tx inspector, block drill-down
- `pybitblock/oraclevision/__init__.py` — new exports
- `pybitblock/oraclevision/mempool_compose.py` — legacy aliases
- `pybitblock/config/oraclevision.conf.example`
- `README.md`

## Upstream

Analysis logic ported from [MarcanoFilms/oraculovision](https://github.com/MarcanoFilms/oraculovision) v2.2.0a1.