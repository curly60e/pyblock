#!/bin/sh
# lncli wrapper for Umbrel/Docker deployments.
#
# Mirrors umbrel/bitcoin-cli-wrapper.sh: PyBLOCK shells out to lncli for
# Lightning operations, so we turn every `lncli` call into one against the
# Umbrel LND container using the gRPC endpoint, TLS cert, and macaroon
# Umbrel injects through APP_LIGHTNING_* env vars (re-exported by the
# entrypoint as LND_*).
set -e

: "${LND_HOST:?LND_HOST must be set}"
: "${LND_TLS_CERT_PATH:?LND_TLS_CERT_PATH must be set}"
: "${LND_MACAROON_PATH:?LND_MACAROON_PATH must be set}"

exec /usr/local/bin/lncli.bin \
    --rpcserver="${LND_HOST}:${LND_GRPC_PORT:-10009}" \
    --tlscertpath="${LND_TLS_CERT_PATH}" \
    --macaroonpath="${LND_MACAROON_PATH}" \
    "$@"
