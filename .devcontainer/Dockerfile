FROM mcr.microsoft.com/devcontainers/base:debian
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install UV only (don't install Python directly)
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN chmod +x /uv-installer.sh && /uv-installer.sh && rm /uv-installer.sh

# Create shell wrapper scripts that intercept traditional commands
RUN echo '#!/bin/sh\necho "Error: pip is disabled in this environment. Please use uv commands instead."\nexit 1' > /usr/local/bin/pip && \
    chmod +x /usr/local/bin/pip && \
    ln -s /usr/local/bin/pip /usr/local/bin/pip3 && \
    echo '#!/bin/sh\necho "Error: Python is managed through uv in this environment. Use uv run instead."\nexit 1' > /usr/local/bin/python && \
    chmod +x /usr/local/bin/python && \
    ln -s /usr/local/bin/python /usr/local/bin/python3

# Make sure UV is on the path
ENV PATH="/root/.local/bin:$PATH"

# Set environment variables to make UV the default
ENV UV_SYSTEM_PYTHON=0
ENV UV_PYTHON_PATH="/root/.local/share/uv/python"
ENV UV_CACHE_DIR="/root/.cache/uv"

# Pre-install a Python version with UV (optional)
RUN uv python install 3.12