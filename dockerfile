FROM ubuntu:latest
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
    && apt-get install -y build-essential cmake git libjson-c-dev libwebsockets-dev \
    && apt-get clean \
    && apt-get install python3 -y \
    && apt install curl \
    && apt install jq -y \
    && apt install wget -y \
    && apt-get install python3-pip -y
RUN git clone https://github.com/tsl0922/ttyd.git \
    && cd ttyd \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make \
    && make install \
    && cd .. && rm -rf ttyd
RUN pip3 install --upgrade pip --break-package-system
RUN pip3 install embit --break-package-system
RUN pip3 install requests --break-package-system
RUN git clone https://github.com/curly60e/pyblock.git \
    && cd pyblock \
    && pip3 install -r requirements.txt --break-package-system \
    && cd pybitblock
CMD ttyd -W -p 6969 -c Running:PyBLOCK python3 PyBlock.py
