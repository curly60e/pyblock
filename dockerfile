FROM ubuntu:24.04

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

RUN git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd /app && rm -rf ttyd

RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

RUN pip install --upgrade pip \
    && git clone https://github.com/curly60e/pyblock.git \
    && cd pyblock \
    && pip install -r requirements.txt

RUN useradd -m -s /bin/bash pyblock \
    && chown -R pyblock:pyblock /app

USER pyblock

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:6969/ || exit 1

CMD ["ttyd", "-W", "-p", "6969", "-c", "Running:PyBLOCK", "python3", "pyblock/pybitblock/PyBlock.py"]
