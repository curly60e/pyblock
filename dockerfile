FROM ubuntu:24.04

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYBLOCK_PORT=6969

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential cmake git libjson-c-dev libwebsockets-dev \
       python3 python3-pip python3-venv \
       curl jq wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Pin ttyd to a specific release tag for reproducibility
RUN git clone --branch 1.7.7 --depth 1 https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd /app && rm -rf ttyd

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       python3-dev libgmp-dev libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install bitcoin-cli and lncli so PyBLOCK's mode A/B can talk to Umbrel's
# Bitcoin Core and LND containers over RPC/gRPC without a degraded Lite Mode
# fallback. The binaries are wrapped by umbrel/{bitcoin-cli,lncli}-wrapper.sh
# (installed below) which inject the connection details Umbrel injects via
# env vars.
ARG TARGETARCH
ARG BITCOIN_VERSION=28.1
ARG LND_VERSION=v0.20.1-beta
RUN set -eux; \
    case "${TARGETARCH}" in \
        amd64) BTC_ARCH=x86_64-linux-gnu; LND_ARCH=amd64 ;; \
        arm64) BTC_ARCH=aarch64-linux-gnu; LND_ARCH=arm64 ;; \
        *) echo "Unsupported TARGETARCH: ${TARGETARCH}" >&2; exit 1 ;; \
    esac; \
    cd /tmp; \
    wget -q "https://bitcoincore.org/bin/bitcoin-core-${BITCOIN_VERSION}/bitcoin-${BITCOIN_VERSION}-${BTC_ARCH}.tar.gz"; \
    wget -q "https://bitcoincore.org/bin/bitcoin-core-${BITCOIN_VERSION}/SHA256SUMS"; \
    grep "bitcoin-${BITCOIN_VERSION}-${BTC_ARCH}.tar.gz" SHA256SUMS | sha256sum -c -; \
    tar -xzf "bitcoin-${BITCOIN_VERSION}-${BTC_ARCH}.tar.gz" "bitcoin-${BITCOIN_VERSION}/bin/bitcoin-cli"; \
    install -m 0755 "bitcoin-${BITCOIN_VERSION}/bin/bitcoin-cli" /usr/local/bin/bitcoin-cli.bin; \
    rm -rf "bitcoin-${BITCOIN_VERSION}" "bitcoin-${BITCOIN_VERSION}-${BTC_ARCH}.tar.gz" SHA256SUMS; \
    wget -q "https://github.com/lightningnetwork/lnd/releases/download/${LND_VERSION}/lnd-linux-${LND_ARCH}-${LND_VERSION}.tar.gz"; \
    tar -xzf "lnd-linux-${LND_ARCH}-${LND_VERSION}.tar.gz" --strip-components=1 "lnd-linux-${LND_ARCH}-${LND_VERSION}/lncli"; \
    install -m 0755 lncli /usr/local/bin/lncli.bin; \
    rm -f lncli "lnd-linux-${LND_ARCH}-${LND_VERSION}.tar.gz"

RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy project files
COPY requirements.txt /app/pyblock/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/pyblock/requirements.txt

COPY . /app/pyblock/

# Install the bitcoin-cli / lncli wrappers as the default CLI paths so any
# subprocess call to bitcoin-cli / lncli (including PyBLOCK's mode A/B menus)
# is transparently routed through RPC/gRPC against the Umbrel dependency
# containers. The real binaries live at /usr/local/bin/{bitcoin-cli,lncli}.bin.
RUN install -m 0755 /app/pyblock/umbrel/bitcoin-cli-wrapper.sh /usr/local/bin/bitcoin-cli \
    && install -m 0755 /app/pyblock/umbrel/lncli-wrapper.sh /usr/local/bin/lncli

# Entrypoint for auto-configuration
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Create config volume mount point
RUN mkdir -p /app/pyblock/pybitblock/config

# Pin pyblock to UID/GID 1000 so it matches the user Umbrel forces via
# `user: "1000:1000"` in docker-compose. The base ubuntu:24.04 image ships an
# `ubuntu` user already at 1000, so remove it first to free the UID.
RUN userdel -r ubuntu 2>/dev/null || true \
    && groupadd -g 1000 pyblock \
    && useradd -m -s /bin/bash -u 1000 -g 1000 pyblock \
    && chown -R pyblock:pyblock /app

USER pyblock

EXPOSE 6969

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:${PYBLOCK_PORT:-6969}/ || exit 1

ENTRYPOINT ["/app/entrypoint.sh"]
