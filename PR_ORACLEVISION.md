# Add OracleVision integration: BIP-110 spam detection and block template analysis

## Motivation

Sovereign Bitcoin node operators — especially those running **Bitcoin Knots** with **BIP-110** (`reduced_data`) policy — need local visibility into L1 spam and consensus-rule violations. Third-party block explorers and dashboards require trust. PyBLOCK already talks to `bitcoin-cli`; this PR adds **Don't Trust, Verify** tooling so operators can audit blocks and mempool composition from their own node.

## What was added

### New module: `pybitblock/oraclevision/`

A self-contained, zero-extra-dependency analysis engine ported from [OracleVision](https://github.com/MarcanoFilms/oraculovision):

| File | Purpose |
|------|---------|
| `script_parser.py` | BIP-110 size limits, witness/script parsing, inscription & token heuristics |
| `bip110.py` | Per-transaction and per-block BIP-110 rule checks |
| `spam_score.py` | 0–100 spam score and CLEAN/SUSPICIOUS/VIOLATION classification |
| `mempool_compose.py` | `getblocktemplate` transaction categorization (economic / consolidation / coinjoin / spam) |
| `bitcoin_cli.py` | Thin `bitcoin-cli` wrapper using PyBLOCK's existing config |
| `config.py` | Settings loader (`config/oraclevision.conf`) |
| `ui.py` | Terminal menus matching PyBLOCK's Rich/cyberpunk aesthetic |

### Menu integration

- **Bitcoin → OV. OracleVision** in the MONITORING section
- Submenu:
  - **A.** BIP-110 Block Scanner (recent blocks table)
  - **B.** Mempool Glass (`getblocktemplate` categorization)
  - **C.** Block Detail View (height or hash)
  - **D.** Launch Full OracleVision TUI (if installed)

### Configuration

- `pybitblock/config/oraclevision.conf.example` — scan count, spam threshold, datadir, TUI command
- Environment overrides for Docker/Umbrel deployments

### Documentation

- README section explaining built-in vs. full OracleVision, configuration, and how to extend detection logic

## Relationship to OracleVision

This PR does **not** port the full Textual dashboard into PyBLOCK. Instead:

1. **Built-in tools** give immediate value inside PyBLOCK's existing menu-driven workflow
2. **Launch option** promotes the standalone [OracleVision](https://github.com/MarcanoFilms/oraculovision) project for operators who want DATUM mining panels, Ocean account stats, live charts, and the full rich TUI

The detection logic is shared in spirit with OracleVision and designed to be maintained in one place (`pybitblock/oraclevision/`) so the community can improve heuristics via PRs without touching UI code.

## Design principles

- **Low dependencies** — uses only `bitcoin-cli` (same as PyBLOCK) and existing Rich UI
- **Modular** — detection rules separated from terminal presentation
- **Community-extensible** — documented module boundaries for new BIP-110 checks and spam heuristics
- **Knots + BIP-110 aligned** — version bit 4 signaling, reduced_data rule checks, local verification framing

## Testing notes

1. Requires a synced Knots/Core node with RPC enabled
2. `getblocktemplate` needs mining RPC capability (standard on most node setups)
3. Block scanner needs `getblock` verbosity 2 (decoded transactions)
4. Full TUI launch requires separate OracleVision installation

```bash
# Quick import check
cd pybitblock && python3 -c "from oraclevision.bip110 import analyze_block; print('ok')"

# Manual test path
python3 PyBlock.py
# → B. Bitcoin → OV. OracleVision → A/B/C
```

## Files changed

- `pybitblock/oraclevision/` (new package, 7 files)
- `pybitblock/config/oraclevision.conf.example` (new)
- `pybitblock/PyBlock.py` (menu entry + handler)
- `README.md` (OracleVision section)