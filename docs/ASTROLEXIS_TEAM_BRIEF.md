# PyBLOCK AI Integration — Brief for Astrolexis Team

## What is PyBLOCK?

PyBLOCK is an open-source (GPL) terminal-based Bitcoin dashboard. It connects to Bitcoin Core and LND nodes, displaying block data, mempool stats, Lightning channels, and more. It runs on everything from Raspberry Pi to full servers, and is available on the Umbrel App Store.

GitHub: `github.com/curly60e/pyblock`

## What We Built

A new **AI Assistant** inside PyBLOCK (Menu option "I") that lets users ask natural language questions about their Bitcoin node. Every query goes through the **Astrolexis AI Gateway** at `https://api.astrolexis.space/v1`.

## How It Works (End to End)

```
User opens PyBLOCK → Main Menu → I (AI Assistant)
                                    │
                                    ▼
                           Has Astrolexis token?
                          /                     \
                        NO                      YES
                        │                        │
               Setup screen:                Verify token:
               "Get yours at                POST /v1/auth/verify
               astrolexis.space/pyblock"     → shows balance
               User enters token             │
               Saved to config               ▼
                        │              User types question
                        │                    │
                        └────────────────────┘
                                    │
                                    ▼
                    PyBLOCK gathers node context:
                    - block height, chain, sync status
                    - mempool size, fee rates (fast/medium/slow)
                    - peer count, disk usage
                    - Lightning: channels, local/remote balance, alias
                                    │
                                    ▼
                    POST /v1/chat
                    {
                      model: "claude-sonnet-4-6",
                      messages: [{role: "user", content: "..."}],
                      node_context: { block_height: 943356, ... },
                      stream: true
                    }
                                    │
                                    ▼
                        Astrolexis Gateway:
                        1. Verify token + check balance
                        2. Inject system prompt + node context
                        3. Proxy to Anthropic/OpenAI
                        4. Stream response back (SSE)
                        5. Debit sats from balance
                                    │
                                    ▼
                    PyBLOCK renders response in terminal
                    (streaming, character by character)
                                    │
                                    ▼
                    User can ask follow-up questions
                    (conversation history maintained)
```

## PyBLOCK Client Module

Located at `pybitblock/ai/` — 4 files:

| File | Purpose |
|------|---------|
| `client.py` | Astrolexis API client. Handles auth, top-up, chat (SSE streaming), usage. Base URL: `https://api.astrolexis.space` |
| `context.py` | Gathers Bitcoin/Lightning node data. Supports 3 modes: bitcoin-cli (local), JSON-RPC (remote), mempool.space API (lite). Also collects LND data via REST API if available |
| `ui.py` | Terminal interface. Token setup, chat loop with conversation history, Lightning top-up with QR codes, usage stats |
| `__init__.py` | Entry point: `ai_menu(path, lndconnectload)` |

## Endpoints We Use

| Endpoint | When |
|----------|------|
| `POST /v1/auth/verify` | On entering AI menu — validate token, show balance |
| `POST /v1/chat` | Every user query — streaming SSE |
| `POST /v1/topup` | User selects "T" — create Lightning invoice |
| `GET /v1/topup/check/:hash` | Polling every 3s after topup — confirm payment |
| `GET /v1/usage` | User selects "U" — show 30-day stats |

## Top-Up Flow

1. User presses "T", enters amount (100-100,000 sats)
2. PyBLOCK calls `POST /v1/topup`
3. Displays bolt11 invoice as QR code + text in terminal
4. User pays from any Lightning wallet
5. PyBLOCK polls `GET /v1/topup/check/{hash}` every 3 seconds
6. Payment confirmed → balance updated in UI

## Error Handling

| HTTP Code | Our Response |
|-----------|-------------|
| 401 | "Error connecting to Astrolexis. Check your token in Settings." |
| 402 | "Insufficient balance (X sats). Estimated cost: Y sats. Press T to top up." |
| 502 | "Error: {message}" |
| Network error | "Error connecting to Astrolexis: {details}" |

## Configuration

Single value stored in `config/pyblocksettings.conf`:

```json
{
  "astrolexis_token": "astrolexis_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```

Also supports env var override: `ASTROLEXIS_API` for base URL (defaults to `https://api.astrolexis.space`).

## What PyBLOCK Sends in node_context

```json
{
  "block_height": 943356,
  "chain": "main",
  "verification_progress": 0.9999,
  "size_on_disk_gb": 620.5,
  "mempool_size": 45000,
  "mempool_bytes": 98000000,
  "peer_count": 109,
  "fee_rates": {"fast": 12, "medium": 6, "slow": 2},
  "ln_alias": "MyNode",
  "ln_channels": 15,
  "ln_peers": 12,
  "local_balance_sats": 5000000,
  "remote_balance_sats": 3200000
}
```

Fields are optional — lite mode users without a full node will send less data. The gateway should handle partial context gracefully.

## Branding in PyBLOCK

Every AI screen shows:
```
Powered by Astrolexis KCode
```

Token setup screen links to:
```
https://astrolexis.space/pyblock
```

## License Boundary

PyBLOCK is GPL. Astrolexis is proprietary. There is **no license conflict** because PyBLOCK consumes Astrolexis as an external API service (network boundary). No Astrolexis code is embedded in PyBLOCK — only HTTP calls to the gateway.

## Token Acquisition Flow (LIVE)

Users get their token via Stripe checkout:

1. User goes to `https://astrolexis.space/pyblock`
2. Selects a tier and pays with credit card (Stripe)
3. After payment, redirected to success page showing their token
4. User copies token into PyBLOCK (Menu I → setup prompt)

**Backend flow:**
```
astrolexis.space/pyblock → Select tier
    → POST /v1/checkout → Stripe session created
    → Stripe payment page
    → Stripe webhook → /v1/stripe/webhook
    → Token generated + balance credited
    → Redirect to /pyblock/success?session_id=xxx
    → User sees token
```

## What We Need From Astrolexis

1. **Rate limiting** (Phase 4) — Once implemented, document the limits so we can show appropriate messages
2. **Model availability** — If models change or new ones are added, PyBLOCK defaults to `claude-sonnet-4-6` but users could select from `/v1/models`
3. **Uptime monitoring** — PyBLOCK shows errors when the gateway is down. A status page would help
