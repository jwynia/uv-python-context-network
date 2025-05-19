# UV Python Project Structure

## Purpose
This document provides detailed information about the structure of UV Python projects, including file organization, configuration, and best practices.

## Classification
- **Domain:** Python Development
- **Stability:** Semi-stable
- **Abstraction:** Structural
- **Confidence:** Established

## Content

### Standard Project Structure

A standard UV Python project follows this structure:

```
project-root/
├── .devcontainer/              # Development container configuration
│   ├── Dockerfile              # Custom container with UV-only setup
│   └── devcontainer.json       # VS Code devcontainer configuration
├── .venv/                      # Virtual environment (created by UV)
├── src/                        # Source code (using src-layout)
│   └── package_name/           # Main package directory
│       ├── __init__.py         # Package initialization
│       ├── py.typed            # Marker file for type checking (optional)
│       └── ...                 # Package modules
├── tests/                      # Test directory
│   ├── __init__.py             # Makes tests importable
│   ├── conftest.py             # pytest configuration (optional)
│   └── ...                     # Test modules
├── pyproject.toml              # Project configuration (PEP 621)
├── requirements.lock           # Generated lockfile for reproducible builds
├── .gitignore                  # Git ignore file (should include .venv/)
├── README.md                   # Project documentation
└── context-network/            # Project planning and architecture documentation
```

#### Required vs. Recommended Files

| File/Directory | Status | Purpose |
|----------------|--------|---------|
| `.devcontainer/` | Required | Enforces UV-only approach |
| `pyproject.toml` | Required | Central project configuration |
| `src/` | Required | Package code using src-layout |
| `tests/` | Recommended | Test code |
| `requirements.lock` | Recommended | Ensures reproducible builds |
| `.gitignore` | Recommended | Prevents committing virtual environments |
| `README.md` | Recommended | Project documentation |

### Key Files and Directories

#### pyproject.toml

The central configuration file for UV Python projects follows PEP 621 standards:

```toml
[project]
name = "project-name"
version = "0.1.0"
description = "Project description"
requires-python = ">=3.12"
authors = [
    {name = "Author Name", email = "author@example.com"}
]
readme = "README.md"
license = {text = "MIT"}
dependencies = [
    # Project dependencies listed here
    "requests>=2.28.0",
    "pydantic>=2.0.0",
]

[project.optional-dependencies]
dev = [
    # Development dependencies
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.0.0",
]
test = [
    # Testing dependencies
    "pytest>=7.0.0",
    "pytest-cov>=4.0.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
python = "3.12"

# Additional tool configurations
[tool.ruff]
target-version = "py312"

[tool.mypy]
python_version = "3.12"
strict = true

[tool.pytest.ini_options]
testpaths = ["tests"]
```

The pyproject.toml file serves multiple purposes:

1. **Project Metadata**: Name, version, description, authors, etc.
2. **Dependency Management**: Core and optional dependencies
3. **Build Configuration**: Specifies build system requirements
4. **Tool Configuration**: UV settings and configurations for other tools
5. **Entry Points**: Can define console scripts and other entry points

#### .devcontainer Directory

The `.devcontainer` directory contains files that configure the development container:

1. **Dockerfile**: Creates a container with UV installed and traditional Python tools blocked
   ```dockerfile
   # Simplified example
   FROM debian:bookworm-slim
   
   # Install minimal dependencies
   RUN apt-get update && apt-get install -y --no-install-recommends \
       ca-certificates \
       curl \
       git \
       && rm -rf /var/lib/apt/lists/*
   
   # Install UV only
   ADD https://astral.sh/uv/install.sh /uv-installer.sh
   RUN chmod +x /uv-installer.sh && /uv-installer.sh && rm /uv-installer.sh
   
   # Create wrapper scripts that intercept traditional commands
   RUN echo '#!/bin/sh\necho "Error: pip is disabled in this environment. Please use uv commands instead."\nexit 1' > /usr/local/bin/pip && \
       chmod +x /usr/local/bin/pip
   
   # Pre-install Python with UV
   RUN uv python install 3.12
   ```

2. **devcontainer.json**: Configures VS Code's development container extension
   ```json
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
           "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python"
         }
       }
     },
     "postCreateCommand": "uv venv && uv sync"
   }
   ```

#### src Directory

Following the src-layout pattern, all package code is contained within the `src` directory:

1. **Package Directory**: Contains the actual Python package
   ```
   src/
   └── package_name/
       ├── __init__.py          # Package initialization
       ├── py.typed             # Marker file for type checking (optional)
       ├── core/                # Core functionality subpackage
       │   ├── __init__.py
       │   └── ...
       ├── utils/               # Utilities subpackage
       │   ├── __init__.py
       │   └── ...
       └── cli.py               # Command-line interface
   ```

2. **__init__.py**: Defines the package and its exports
   ```python
   """Package docstring."""
   
   __version__ = "0.1.0"
   
   from .core import CoreClass  # Re-export important classes
   ```

3. **Additional Files**:
   - **py.typed**: Empty marker file that indicates the package provides type hints
   - **__main__.py**: Optional file that allows running the package as a module
   - **README.md**: Optional package-specific documentation

### Structure Rationale

#### Why src-layout?

The src-layout pattern (placing package code in a src directory) offers several advantages:

1. **Prevents Accidental Imports**: Code can't be imported from the project root
2. **Forces Installation**: Ensures testing against the installed package
3. **Separates Code from Project Files**: Keeps package code separate from project configuration
4. **Industry Standard**: Follows modern Python packaging best practices

#### Why pyproject.toml?

The pyproject.toml file (PEP 621) offers several advantages over traditional setup.py:

1. **Declarative Configuration**: Simple, declarative format
2. **Standard Format**: Consistent across different build systems
3. **Tool Configuration**: Single file for configuring multiple tools
4. **Modern Standard**: Aligned with current Python packaging standards

#### Why .devcontainer?

The .devcontainer configuration:

1. **Ensures Consistency**: Provides the same environment for all developers
2. **Enforces UV Usage**: Blocks access to traditional Python tools
3. **Simplifies Setup**: New developers can start immediately with the correct environment
4. **Integrates with VS Code**: Provides seamless development experience

### UV-Specific Structure Elements

#### Virtual Environment Location

UV creates virtual environments in the `.venv` directory by default, which is recognized by most Python tools and IDEs.

```
.venv/
├── bin/                # Scripts and executables
│   ├── python          # Python interpreter
│   ├── pip             # Pip (redirects to UV)
│   └── ...             # Other entry points
├── lib/                # Python libraries
│   └── python3.12/     # Python version-specific
│       └── site-packages/  # Installed packages
└── pyvenv.cfg          # Environment configuration
```

#### UV Configuration in pyproject.toml

UV-specific configuration is placed in the `[tool.uv]` section of pyproject.toml:

```toml
[tool.uv]
python = "3.12"  # Specify Python version
```

Additional UV configuration options include:
- `exclude`: Patterns to exclude from installation
- `index-url`: Custom package index URL
- `no-binary`: Packages to build from source

#### UV Environment Variables

In containerized environments, these environment variables may be set:

- `UV_SYSTEM_PYTHON`: Controls whether UV uses system Python
- `UV_PYTHON_PATH`: Specifies where UV installs Python versions
- `UV_CACHE_DIR`: Controls UV's cache location
- `UV_VIRTUALENV_PYTHON`: Specifies Python version for new environments
- `UV_INDEX_URL`: Sets default package index URL

#### Generated Files

UV generates several files during normal operation:

1. **requirements.lock**: Generated from pyproject.toml using `uv pip compile`
   ```
   # Generated by uv
   requests==2.31.0
     certifi==2024.2.2
     charset-normalizer==3.3.2
     idna==3.6
     urllib3==2.2.0
   ```

2. **.python-version**: Optional file that specifies the Python version for tools like pyenv

### UV's Interaction with File Structure

UV interacts with the project structure in several key ways:

#### 1. Project Discovery

UV uses the presence of `pyproject.toml` in the current or parent directories to identify the project root. This is critical for commands like:
- `uv pip install -e .` (install in development mode)
- `uv pip compile` (generate lockfiles)
- `uv sync` (synchronize environment with dependencies)

#### 2. Virtual Environment Management

UV creates and manages virtual environments:
- Default location: `.venv` in the project root
- Can be customized with `--venv` flag or environment variables
- Integrates with VS Code and other IDEs through standard paths

#### 3. Package Building and Installation

UV handles package building and installation:
- Uses `src` directory for package source
- Reads metadata from `pyproject.toml`
- Generates distribution files in `dist/` directory
- Creates and uses lockfiles for reproducible builds

#### 4. Tool Integration

UV provides integration with development tools:
- Runs tools through `uv run -m [tool]`
- Tools read configuration from `pyproject.toml`
- Ensures tools run in the correct environment

### Best Practices

1. **Keep pyproject.toml Minimal**: Include only necessary dependencies
2. **Use src-layout**: Place all package code in the src directory
3. **Separate Dev Dependencies**: Use optional-dependencies for development tools
4. **Version Pin Dependencies**: Specify version constraints for reproducibility
5. **Include .venv in .gitignore**: Don't commit the virtual environment
6. **Document UV Usage**: Include instructions for UV commands in README.md
7. **Use Lockfiles**: Generate and commit lockfiles for reproducible builds
8. **Follow Type Checking Standards**: Include py.typed and type annotations
9. **Organize Subpackages Logically**: Group related functionality in subpackages
10. **Provide Clear Entry Points**: Define console scripts in pyproject.toml

## Relationships
- **Parent Nodes:** [elements/uv-python/overview.md]
- **Child Nodes:** None
- **Related Nodes:** 
  - [foundation/structure.md] - generalizes - General project structure principles
  - [elements/uv-python/devcontainer.md] - details - DevContainer configuration specifics
  - [elements/uv-python/workflow.md] - uses - Workflows that operate on this structure
  - [elements/uv-python/constraints.md] - defines - Technical constraints that shape this structure

## Navigation Guidance
- **Access Context:** Use this document when setting up a new UV Python project or understanding the structure of an existing one
- **Common Next Steps:** After reviewing this structure, explore devcontainer.md for environment setup or workflow.md for development processes
- **Related Tasks:** Project initialization, package configuration, development environment setup
- **Update Patterns:** This document should be updated when best practices for Python project structure evolve

## Metadata
- **Created:** 2025-05-19
- **Last Updated:** 2025-05-19
- **Updated By:** Claude

## Change History
- 2025-05-19: Initial creation of UV Python structure documentation
- 2025-05-19: Enhanced with additional details about file structure and UV interactions
