
FROM ubuntu:latest
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y build-essential cmake git libjson-c-dev libwebsockets-dev \
    && apt-get clean \
    && apt-get install python3 -y \
    && apt-get install python3-pip -y
RUN git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd .. && rm -rf ttyd
COPY pyproject.toml poetry.lock ./
COPY pybitblock ./
RUN pip3 install --upgrade pip
RUN pip install poetry \
    && poetry export -f requirements.txt > requirements.txt --with dev --without-hashes \
    && pip install -r requirements.txt
COPY . .
CMD cd pybitblock
CMD python3 PyBlock.py
CMD ttyd -p 6969 -c Running:PyBLOCK python3 PyBlock.py
