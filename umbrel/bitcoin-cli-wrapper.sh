#!/bin/sh
# bitcoin-cli wrapper for Umbrel/Docker deployments.
#
# PyBLOCK's modes A/B call bitcoin-cli directly via subprocess. Inside the
# Umbrel container we connect to the host's Bitcoin Core (or Knots) over the
# Docker network using the credentials Umbrel injects through APP_BITCOIN_*
# env vars (re-exported by the entrypoint as BITCOIN_RPC_*). This wrapper
# turns every `bitcoin-cli` call into a properly-authenticated remote RPC
# call against that node.
set -e

: "${BITCOIN_RPC_HOST:?BITCOIN_RPC_HOST must be set}"
: "${BITCOIN_RPC_USER:?BITCOIN_RPC_USER must be set}"
: "${BITCOIN_RPC_PASS:?BITCOIN_RPC_PASS must be set}"

exec /usr/local/bin/bitcoin-cli.bin \
    -rpcconnect="${BITCOIN_RPC_HOST}" \
    -rpcport="${BITCOIN_RPC_PORT:-8332}" \
    -rpcuser="${BITCOIN_RPC_USER}" \
    -rpcpassword="${BITCOIN_RPC_PASS}" \
    "$@"
