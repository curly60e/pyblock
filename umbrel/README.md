# PyBLOCK Umbrel App

## Files

| File | Description |
|------|-------------|
| `docker-compose.yml` | Container configuration for Umbrel |
| `umbrel-app.yml` | App manifest for Umbrel App Store |
| `icon.svg` | 256x256 SVG app icon (cyberpunk Bitcoin theme) |
| `1.jpg` | Gallery: Main menu screenshot |
| `2.jpg` | Gallery: Block visualizer screenshot |
| `3.jpg` | Gallery: Lightning dashboard screenshot |

## Testing on Umbrel

```bash
# 1. Clone umbrel dev environment
git clone https://github.com/getumbrel/umbrel.git
cd umbrel && npm run dev

# 2. Copy PyBLOCK app files
cp -r /path/to/pyblock/umbrel/ ~/umbrel/app-stores/getumbrel-umbrel-apps/pyblock/

# 3. Install via CLI
npm run dev client -- apps.install.mutate -- --appId pyblock
```

## Submitting to Umbrel App Store

1. Fork `getumbrel/umbrel-apps`
2. Copy the `umbrel/` contents into a `pyblock/` directory in the fork
3. Add gallery screenshots (1440x900px PNG)
4. Open PR with the submission template

## Environment Variables (auto-injected by Umbrel)

| Variable | Description |
|----------|-------------|
| `APP_BITCOIN_NODE_IP` | Bitcoin Core IP |
| `APP_BITCOIN_RPC_PORT` | RPC port (8332) |
| `APP_BITCOIN_RPC_USER` | RPC username |
| `APP_BITCOIN_RPC_PASS` | RPC password |
| `APP_LIGHTNING_NODE_IP` | LND IP |
| `APP_LIGHTNING_NODE_GRPC_PORT` | LND gRPC port |
| `APP_LIGHTNING_NODE_DATA_DIR` | LND data (macaroons, TLS) |

## Docker Build (Multi-Arch)

```bash
# Build for ARM64 + AMD64
docker buildx build --platform linux/amd64,linux/arm64 -t curly60e/pyblock:v4.0.0 --push .
```
