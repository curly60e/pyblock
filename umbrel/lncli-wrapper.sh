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

if [ ! -r "${LND_TLS_CERT_PATH}" ]; then
    echo "Error: LND TLS certificate not found or not readable at path '${LND_TLS_CERT_PATH}'" >&2
    exit 1
fi

if [ ! -r "${LND_MACAROON_PATH}" ]; then
    echo "Error: LND macaroon not found or not readable at path '${LND_MACAROON_PATH}'" >&2
    exit 1
fi

exec /usr/local/bin/lncli.bin \
    --rpcserver="${LND_HOST}:${LND_GRPC_PORT:-10009}" \
    --tlscertpath="${LND_TLS_CERT_PATH}" \
    --macaroonpath="${LND_MACAROON_PATH}" \
    "$@"
