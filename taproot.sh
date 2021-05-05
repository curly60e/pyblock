#!/bin/bash
BLOCKCHAININFO=$(bitcoin-cli getblockchaininfo)
TAPROOT=$(echo "$BLOCKCHAININFO" | jq .softforks.taproot.bip9)
SINCE=$(echo "$TAPROOT" | jq .since)
ELAPSED=$(echo "$TAPROOT" | jq .statistics.elapsed)
 for BLOCK in $(seq "$SINCE" $((SINCE + ELAPSED - 1))); do
  HASH=$(bitcoin-cli getblockhash "$BLOCK")
  HEADER=$(bitcoin-cli getblockheader "$HASH")
  VERSION=$(echo "$HEADER" | jq .version)
  SIGNAL=$(((VERSION & 3758096388) == 536870916))
  case $SIGNAL in
    (1) echo -n "🌱";;
    (0) echo -n "🆘";;
  esac
done
echo
