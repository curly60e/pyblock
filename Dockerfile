# pull the official base image
FROM 3.10-slim-bullseye

# set working directory
WORKDIR /app

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
COPY pyproject.toml poetry.lock ./
RUN pip install --upgrade pip
RUN pip install poetry \
  && poetry export -f requirements.txt > requirements.txt --dev --without-hashes \
  && pip install -r requirements.txt

# add app
COPY . .

ENTRYPOINT ["pyblock"]
