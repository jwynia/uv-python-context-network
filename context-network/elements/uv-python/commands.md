# UV Python Commands Reference

## Purpose
This document provides a comprehensive reference for UV commands used in Python development, including syntax, options, and examples.

## Classification
- **Domain:** Development Tools
- **Stability:** Semi-stable
- **Abstraction:** Detailed
- **Confidence:** Established

## Content

### Command Overview

UV provides several command categories for Python development:

1. **Environment Management**: Commands for creating and managing virtual environments
2. **Package Management**: Commands for installing, updating, and removing packages
3. **Python Management**: Commands for installing and managing Python versions
4. **Execution**: Commands for running Python code within UV environments

### Environment Management

#### Creating Virtual Environments

```bash
# Create a virtual environment in the default location (.venv)
uv venv

# Create a virtual environment in a specific location
uv venv /path/to/venv

# Create a virtual environment with a specific Python version
uv venv --python 3.11
```

#### Activating Virtual Environments

Unlike traditional virtual environments, UV environments don't require explicit activation. Instead, use `uv run` to execute commands within the environment:

```bash
# Run Python in the virtual environment
uv run

# Run a script in the virtual environment
uv run script.py
```

### Package Management

#### Installing Packages

```bash
# Install a package
uv pip install requests

# Install multiple packages
uv pip install requests pandas numpy

# Install with version constraints
uv pip install "requests>=2.28.0" "pandas<2.0.0"

# Install from pyproject.toml
uv pip install -e .

# Install with development dependencies
uv pip install -e ".[dev]"

# Install from requirements file
uv pip install -r requirements.txt
```

#### Managing Dependencies with Lockfiles

```bash
# Generate a lockfile from pyproject.toml
uv pip compile pyproject.toml -o requirements.lock

# Generate a lockfile with development dependencies
uv pip compile pyproject.toml --extra=dev -o dev-requirements.lock

# Install from lockfiles
uv pip sync requirements.lock dev-requirements.lock

# Update lockfile with latest compatible versions
uv pip compile --upgrade pyproject.toml -o requirements.lock
```

#### Listing Installed Packages

```bash
# List installed packages
uv pip list

# List outdated packages
uv pip list --outdated
```

#### Uninstalling Packages

```bash
# Uninstall a package
uv pip uninstall requests

# Uninstall multiple packages
uv pip uninstall requests pandas
```

### Python Management

#### Installing Python Versions

```bash
# Install the latest Python version
uv python install

# Install a specific Python version
uv python install 3.11

# Install a specific patch version
uv python install 3.11.4
```

#### Listing Available Python Versions

```bash
# List installed Python versions
uv python list

# List available Python versions
uv python list --available
```

#### Removing Python Versions

```bash
# Remove a Python version
uv python remove 3.11
```

### Execution Commands

#### Running Python Scripts

```bash
# Run a Python script
uv run script.py

# Run a script with arguments
uv run script.py arg1 arg2

# Run a module
uv run -m module_name

# Run a package
uv run -m package_name
```

#### Running Python Interactively

```bash
# Start an interactive Python session
uv run
```

#### Running Python Tools

```bash
# Run pytest
uv run -m pytest

# Run black formatter
uv run -m black src/

# Run mypy type checker
uv run -m mypy src/

# Run pip within the environment
uv run -m pip list
```

### Advanced Usage

#### Environment Variables

UV's behavior can be controlled through environment variables:

| Variable | Purpose | Example |
|----------|---------|---------|
| `UV_SYSTEM_PYTHON` | Controls whether UV uses system Python | `UV_SYSTEM_PYTHON=0` |
| `UV_PYTHON_PATH` | Specifies where UV installs Python versions | `UV_PYTHON_PATH=/path/to/pythons` |
| `UV_CACHE_DIR` | Controls UV's cache location | `UV_CACHE_DIR=/path/to/cache` |
| `UV_VIRTUALENV_PYTHON` | Specifies Python version for new environments | `UV_VIRTUALENV_PYTHON=3.11` |

#### Configuration in pyproject.toml

UV can be configured in the `[tool.uv]` section of pyproject.toml:

```toml
[tool.uv]
python = "3.12"
```

#### Working with Multiple Environments

```bash
# Create a named environment
uv venv --name test-env

# Run commands in a specific environment
uv run --venv /path/to/venv script.py
```

### Common Command Patterns

#### Initial Project Setup

```bash
# Create a virtual environment
uv venv

# Install dependencies
uv pip install -e ".[dev]"
```

#### Dependency Updates

```bash
# Update lockfile
uv pip compile --upgrade pyproject.toml -o requirements.lock

# Sync environment with updated lockfile
uv pip sync requirements.lock
```

#### Testing Workflow

```bash
# Run tests
uv run -m pytest

# Run tests with coverage
uv run -m pytest --cov=src

# Run specific test file
uv run -m pytest tests/test_specific.py
```

#### Code Quality Workflow

```bash
# Format code
uv run -m black src/ tests/

# Lint code
uv run -m ruff check src/ tests/

# Type check
uv run -m mypy src/
```

### Troubleshooting

#### Common Issues and Solutions

1. **Command Not Found**:
   ```bash
   # Ensure UV is installed and in PATH
   which uv
   ```

2. **Package Installation Failures**:
   ```bash
   # Try with verbose output
   uv pip install package_name -v
   ```

3. **Virtual Environment Issues**:
   ```bash
   # Remove and recreate the environment
   rm -rf .venv
   uv venv
   ```

4. **Python Version Issues**:
   ```bash
   # Check available Python versions
   uv python list --available
   ```

## Relationships
- **Parent Nodes:** [elements/uv-python/overview.md]
- **Child Nodes:** None
- **Related Nodes:** 
  - [elements/uv-python/workflow.md] - uses - Workflows use these commands
  - [elements/uv-python/devcontainer.md] - enables - DevContainer enables these commands
  - [decisions/uv_exclusive_approach.md] - justifies - Decision to use these commands exclusively

## Navigation Guidance
- **Access Context:** Use this document as a reference when working with UV commands
- **Common Next Steps:** After reviewing commands, explore workflow.md for how these commands fit into development processes
- **Related Tasks:** Package installation, dependency management, environment setup, Python execution
- **Update Patterns:** This document should be updated when UV adds new commands or changes existing command syntax

## Metadata
- **Created:** 2025-05-19
- **Last Updated:** 2025-05-19
- **Updated By:** Claude

## Change History
- 2025-05-19: Initial creation of UV Python commands reference
