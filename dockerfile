FROM ubuntu:24.04@sha256:b59d21599a2b151e7f6a8d7b6f0e864fbb4ce8b0c9cf09be2e67f4d6e3b942a4

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

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

RUN pip install --no-cache-dir --upgrade pip \
    && git clone --depth 1 https://github.com/curly60e/pyblock.git \
    && cd pyblock \
    && pip install --no-cache-dir -r requirements.txt

RUN useradd -m -s /bin/bash pyblock \
    && chown -R pyblock:pyblock /app

USER pyblock

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:6969/ || exit 1

CMD ["ttyd", "-W", "-p", "6969", "-c", "Running:PyBLOCK", "python3", "pyblock/pybitblock/PyBlock.py"]
