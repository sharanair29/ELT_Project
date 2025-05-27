##
# Dockerfile for DBT CLI usage (no RPC server)
##

FROM python:3.9.14-slim-bullseye

# System setup
RUN apt-get update \
  && apt-get dist-upgrade -y \
  && apt-get install -y --no-install-recommends \
    git \
    ssh-client \
    software-properties-common \
    make \
    build-essential \
    ca-certificates \
    libpq-dev \
  && apt-get clean \
  && rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/*

# Env vars
ENV PYTHONIOENCODING=utf-8
ENV LANG=C.UTF-8

# Upgrade pip and setuptools
RUN python -m pip install --upgrade pip setuptools wheel --no-cache-dir

# Set workdir
WORKDIR /usr/app/dbt/
VOLUME /usr/app

# Install Python dependencies
COPY ["./requirements.txt", "/usr/app/dbt/"]
RUN pip install -r requirements.txt

# Copy DBT project files
COPY ["./p1_jc", "."]

# Copy DBT profiles
COPY ["profile.yml", "/root/.dbt/profiles.yml"]

# Default command allows override in container
ENTRYPOINT ["dbt"]
CMD ["--help"]