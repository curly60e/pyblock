#!/bin/bash
BLOCKCHAININFO=$(bitcoin-cli getblockchaininfo)
BLOCKS=$(echo "$BLOCKCHAININFO" | jq .blocks)
TAPROOT=$(echo "$BLOCKCHAININFO" | jq .softforks.taproot.bip9)
SINCE=$(echo "$TAPROOT" | jq .since)
PERIOD=$(echo "$TAPROOT" | jq .statistics.period)
BLOCKS=$(echo "$BLOCKCHAININFO" | jq .blocks)
PERIOD_COUNT=$(((BLOCKS - SINCE) / PERIOD))
SINCE=$((SINCE + (PERIOD * PERIOD_COUNT)))
ELAPSED=$(echo "$TAPROOT" | jq .statistics.elapsed)
for BLOCK in $(seq "$SINCE" $((SINCE + ELAPSED - 1))); do
  HASH=$(bitcoin-cli getblockhash "$BLOCK")
  HEADER=$(bitcoin-cli getblockheader "$HASH")
  VERSION=$(echo "$HEADER" | jq .version)
  SIGNAL=$(((VERSION & 3758096388) == 536870916))
  case $SIGNAL in
    (1) echo -n "✅";;
    (0) echo -n "❌";;
  esac
done
echo

PERCENTAGE=`echo $BLOCKCHAININFO | jq '.softforks.taproot.bip9.statistics | .count / .elapsed * 100'`
echo $PERCENTAGE
