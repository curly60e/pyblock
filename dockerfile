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

RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copy project files
COPY requirements.txt /app/pyblock/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /app/pyblock/requirements.txt

COPY . /app/pyblock/

# Entrypoint for auto-configuration
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Create config volume mount point
RUN mkdir -p /app/pyblock/pybitblock/config

RUN useradd -m -s /bin/bash pyblock \
    && chown -R pyblock:pyblock /app

USER pyblock

EXPOSE 6969

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:${PYBLOCK_PORT:-6969}/ || exit 1

ENTRYPOINT ["/app/entrypoint.sh"]
