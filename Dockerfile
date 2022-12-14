# pull the official base image
FROM 3.10-slim-bullseye

# set working directory
WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install ttyd dependencies
RUN apt-get update \
    && apt-get install -y build-essential cmake git libjson-c-dev libwebsockets-dev \
    && && apt-get clean

RUN git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd .. && rm -rf ttyd

# install python dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip
RUN pip install poetry \
  && poetry export -f requirements.txt > requirements.txt --dev --without-hashes \
  && pip install -r requirements.txt

# add app
COPY . .

ENTRYPOINT ["ttyd", "-p", "8080", "pyblock"]
