#!/bin/bash
set -e

CONFIG_DIR="/app/pyblock/pybitblock/config"
mkdir -p "$CONFIG_DIR"

# Auto-generate Bitcoin config from env vars if set
if [ -n "$BITCOIN_RPC_HOST" ] && [ -n "$BITCOIN_RPC_USER" ]; then
    BITCOIN_RPC_PORT="${BITCOIN_RPC_PORT:-8332}"
    cat > "$CONFIG_DIR/bclock.conf" <<BTCEOF
{
  "ip_port": "http://${BITCOIN_RPC_HOST}:${BITCOIN_RPC_PORT}",
  "rpcuser": "${BITCOIN_RPC_USER}",
  "rpcpass": "${BITCOIN_RPC_PASS}",
  "bitcoincli": "${BITCOIN_CLI_PATH:-}"
}
BTCEOF
    echo "[PyBLOCK] Bitcoin RPC configured: ${BITCOIN_RPC_HOST}:${BITCOIN_RPC_PORT}"
fi

# Auto-generate LND config from env vars if set
if [ -n "$LND_HOST" ] || [ -n "$LND_TLS_CERT_PATH" ]; then
    LND_GRPC_PORT="${LND_GRPC_PORT:-10009}"
    # Only build ip_port if LND_HOST is set (matches Python _env_lnd_config)
    if [ -n "$LND_HOST" ]; then
        LND_IP_PORT="${LND_HOST}:${LND_GRPC_PORT}"
    else
        LND_IP_PORT=""
    fi
    cat > "$CONFIG_DIR/blndconnect.conf" <<LNDEOF
{
  "ip_port": "${LND_IP_PORT}",
  "tls": "${LND_TLS_CERT_PATH:-}",
  "macaroon": "${LND_MACAROON_PATH:-}",
  "ln": "${LND_CLI_PATH:-}"
}
LNDEOF
    echo "[PyBLOCK] LND configured: ${LND_IP_PORT:-local paths only}"
fi

# Auto-set mode if specified (PYBLOCK_MODE always overwrites)
PYBLOCK_MODE="${PYBLOCK_MODE:-}"
if [ -n "$PYBLOCK_MODE" ]; then
    echo "\"${PYBLOCK_MODE}\"" > "$CONFIG_DIR/intro.conf"
    echo "[PyBLOCK] Mode set to: ${PYBLOCK_MODE}"
elif [ -n "$BITCOIN_RPC_HOST" ] && [ ! -f "$CONFIG_DIR/intro.conf" ]; then
    # Auto-detect mode from available env vars
    if [ -n "$LND_HOST" ] || [ -n "$LND_TLS_CERT_PATH" ]; then
        echo '"A"' > "$CONFIG_DIR/intro.conf"
        echo "[PyBLOCK] Auto-detected mode: A (Bitcoin + Lightning)"
    else
        echo '"B"' > "$CONFIG_DIR/intro.conf"
        echo "[PyBLOCK] Auto-detected mode: B (Bitcoin Only)"
    fi
fi

# Generate default settings if missing
if [ ! -f "$CONFIG_DIR/pyblocksettings.conf" ]; then
    cat > "$CONFIG_DIR/pyblocksettings.conf" <<SEOF
{
  "gradient": "",
  "design": "block",
  "colorA": "green",
  "colorB": "yellow"
}
SEOF
fi

if [ ! -f "$CONFIG_DIR/pyblocksettingsClock.conf" ]; then
    cat > "$CONFIG_DIR/pyblocksettingsClock.conf" <<SCEOF
{
  "gradient": "",
  "colorA": "green",
  "colorB": "yellow"
}
SCEOF
fi

echo "[PyBLOCK] Starting..."

# Launch PyBLOCK via ttyd
exec ttyd -W -p "${PYBLOCK_PORT:-6969}" \
    ${PYBLOCK_TTYD_AUTH:+-c "$PYBLOCK_TTYD_AUTH"} \
    python3 /app/pyblock/pybitblock/PyBlock.py "$@"
