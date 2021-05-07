FROM python:3.9.5-slim-buster
RUN export DEBIAN_FRONTEND=noninteractive && \
apt-get update && \
apt-get -y upgrade && \
apt-get install -y --no-install-recommends tini && \
apt-get -y clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade --no-cache-dir pip && pip install --no-cache-dir -r requirements.txt
RUN useradd --create-home action
USER action
COPY swid_lint /app/swid_lint
ENV PYTHONFAULTHANDLER=1
ENTRYPOINT ["tini", "--", "python", "-m", "swid_lint"]
ARG BUILD_TS
ARG REVISION
ARG VERSION
LABEL org.opencontainers.image.created=$BUILD_TS \
    org.opencontainers.image.authors="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.url="https://hub.docker.com/repository/docker/shagen/swid-lint/" \
    org.opencontainers.image.documentation="https://sthagen.github.io/silver-pancake/" \
    org.opencontainers.image.source="https://github.com/sthagen/silver-pancake/" \
    org.opencontainers.image.version=$VERSION \
    org.opencontainers.image.revision=$REVISION \
    org.opencontainers.image.vendor="Stefan Hagen <mailto:stefan@hagen.link>" \
    org.opencontainers.image.licenses="MIT License" \
    org.opencontainers.image.ref.name="shagen/swid-lint" \
    org.opencontainers.image.title="swid-lint." \
    org.opencontainers.image.description="Experimental SWID envelope and body profile validator."
