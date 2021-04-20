FROM python:3.9-slim

ENV DEBIAN_FRONTEND=noninteractive

ENV DEBCONF_NONINTERACTIVE_SEEN=true

WORKDIR /app

COPY templates templates

RUN debconf-set-selections ./templates/tzseeds.txt

# hadolint ignore=DL3008,DL3009
RUN apt-get update -y && \
    apt-get install -y \
    postgresql \
    libpq-dev \
    zsh --no-install-recommends

# hadolint ignore=DL3013
RUN pip install --no-cache-dir pip --upgrade && \
    pip install --no-cache-dir --requirement ./templates/requirements.txt

RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/*
