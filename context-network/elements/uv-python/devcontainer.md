# UV Python DevContainer Configuration

## Purpose
This document details the development container configuration that enforces UV-only Python package and environment management, preventing fallback to traditional Python tools.

## Classification
- **Domain:** Development Environment
- **Stability:** Semi-stable
- **Abstraction:** Detailed
- **Confidence:** Established

## Content

### Overview

The DevContainer configuration creates an isolated development environment that exclusively uses UV for Python package and environment management. This configuration deliberately blocks access to traditional Python tools to ensure consistency and prevent confusion, particularly when working with AI agents.

### Key Components

#### Dockerfile

The custom Dockerfile creates a container with these key characteristics:

1. **UV Installation**: Installs UV directly from the official source
2. **Command Interception**: Creates wrapper scripts that intercept attempts to use traditional Python tools
3. **Environment Configuration**: Sets environment variables to ensure UV is used for all Python operations
4. **Python Installation**: Pre-installs Python using UV rather than system packages

```dockerfile
# .devcontainer/Dockerfile
FROM debian:bookworm-slim

# Install minimal dependencies
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

# Create workspace directory
WORKDIR /workspaces/project

# Set environment variables to make UV the default
ENV UV_SYSTEM_PYTHON=0
ENV UV_PYTHON_PATH="/root/.local/share/uv/python"
ENV UV_CACHE_DIR="/root/.cache/uv"

# Pre-install a Python version with UV
RUN uv python install 3.12
```

#### devcontainer.json

The devcontainer.json file configures VS Code's development container extension:

```json
// .devcontainer/devcontainer.json
{
  "name": "UV-Only Python Environment",
  "build": {
    "dockerfile": "Dockerfile",
    "context": ".."
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ],
      "settings": {
        "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
        "python.terminal.activateEnvironment": false,
        "python.terminal.activateEnvInCurrentTerminal": false,
        "terminal.integrated.defaultProfile.linux": "bash",
        "terminal.integrated.profiles.linux": {
          "bash": {
            "path": "/bin/bash",
            "args": []
          }
        }
      }
    }
  },
  "postCreateCommand": "uv venv && uv sync",
  "remoteUser": "root"
}
```

### Command Interception Mechanism

A key aspect of the UV-only enforcement is the command interception mechanism:

```bash
# Create a wrapper script for pip
echo '#!/bin/sh
echo "Error: pip is disabled in this environment. Please use uv commands instead."
exit 1' > /usr/local/bin/pip

# Make it executable
chmod +x /usr/local/bin/pip

# Link it to pip3 as well
ln -s /usr/local/bin/pip /usr/local/bin/pip3

# Similar approach for python/python3
echo '#!/bin/sh
echo "Error: Python is managed through uv in this environment. Use uv run instead."
exit 1' > /usr/local/bin/python
chmod +x /usr/local/bin/python
ln -s /usr/local/bin/python /usr/local/bin/python3
```

This creates shell scripts that intercept attempts to use `pip`, `pip3`, `python`, or `python3` directly, providing clear error messages that direct users to the appropriate UV commands instead.

### Environment Variables

The Dockerfile sets several environment variables to control UV's behavior:

| Variable | Value | Purpose |
|----------|-------|---------|
| `UV_SYSTEM_PYTHON` | `0` | Prevents UV from using system Python |
| `UV_PYTHON_PATH` | `/root/.local/share/uv/python` | Specifies where UV installs Python versions |
| `UV_CACHE_DIR` | `/root/.cache/uv` | Controls UV's cache location |

### VS Code Integration

The devcontainer.json file includes configuration for VS Code:

1. **Extensions**: Installs Python and Pylance extensions
2. **Interpreter Path**: Points to the UV-created virtual environment
3. **Terminal Settings**: Configures the integrated terminal
4. **Post-Create Command**: Automatically creates a virtual environment and syncs dependencies

### Usage for Developers

When a developer opens the project in VS Code with the Dev Containers extension installed:

1. VS Code builds the container using the Dockerfile
2. The container includes UV but blocks traditional Python tools
3. A virtual environment is automatically created
4. Dependencies are installed from pyproject.toml
5. The Python extension is configured to use the virtual environment

### Advantages for AI Agents

This configuration is particularly beneficial when working with AI agents:

1. **Clear Constraints**: The agent can only use UV commands, preventing confusion
2. **Consistent Approach**: All package operations follow the same pattern
3. **Error Messages**: If the agent attempts to use traditional tools, it receives clear guidance
4. **Modern Standards**: The configuration encourages the use of modern Python practices

### Customization Options

The DevContainer configuration can be customized in several ways:

1. **Base Image**: Change the base image for different OS requirements
2. **Python Version**: Modify the pre-installed Python version
3. **Extensions**: Add additional VS Code extensions
4. **Post-Create Commands**: Add additional setup steps
5. **Environment Variables**: Adjust UV's behavior through environment variables

## Relationships
- **Parent Nodes:** [elements/uv-python/overview.md]
- **Child Nodes:** None
- **Related Nodes:** 
  - [elements/uv-python/structure.md] - complements - Project structure that works with this DevContainer
  - [elements/uv-python/workflow.md] - enables - Workflows that operate in this environment
  - [decisions/uv_exclusive_approach.md] - implements - Decision to use UV exclusively

## Navigation Guidance
- **Access Context:** Use this document when setting up or customizing the development environment
- **Common Next Steps:** After reviewing this configuration, explore workflow.md for development processes
- **Related Tasks:** Development environment setup, container customization, VS Code configuration
- **Update Patterns:** This document should be updated when UV capabilities or DevContainer best practices evolve

## Metadata
- **Created:** 2025-05-19
- **Last Updated:** 2025-05-19
- **Updated By:** Claude

## Change History
- 2025-05-19: Initial creation of UV Python DevContainer documentation
