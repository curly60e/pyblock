FROM ubuntu:latest
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y build-essential cmake git libjson-c-dev libwebsockets-dev \
    && apt-get clean \
    && apt-get install python3 -y \
    && apt install curl \
    && apt-get install python3-pip -y
RUN git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd .. && rm -rf ttyd
RUN pip3 install --upgrade pip
RUN pip3 install embit
RUN pip3 install requests
RUN pip3 install pybitblock
CMD ttyd -p 6969 -c Running:PyBLOCK pyblock
