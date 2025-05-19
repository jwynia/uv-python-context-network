# UV Python Technical Constraints

## Purpose
This document outlines the technical constraints and requirements imposed by the UV-exclusive approach, including folder structure constraints, integration limitations, and common pitfalls.

## Classification
- **Domain:** Python Development
- **Stability:** Semi-stable
- **Abstraction:** Detailed
- **Confidence:** Established

## Content

### Folder Structure Constraints

#### Required Project Structure

The UV Python project template enforces certain structural constraints to ensure proper functionality:

```
project-root/
├── .devcontainer/              # Required for UV-only enforcement
│   ├── Dockerfile              # Required for UV-only setup
│   └── devcontainer.json       # Required for VS Code integration
├── pyproject.toml              # Required for UV configuration
├── src/                        # Required for package code (src-layout)
│   └── package_name/           # Package directory
│       └── __init__.py         # Package initialization
└── tests/                      # Recommended for test code
```

#### Critical Requirements

1. **pyproject.toml Location**: Must be in the project root directory
   - UV relies on finding this file to determine project configuration
   - Cannot be renamed or moved to subdirectories

2. **.devcontainer Configuration**: Required for enforcing UV-only approach
   - Custom Dockerfile must include command interception mechanisms
   - devcontainer.json must configure VS Code to use UV virtual environments

3. **src-layout Structure**: Required for proper package isolation
   - All package code must be within the src directory
   - Cannot mix package code with project files in the root directory

### File Naming Constraints

1. **Python Package Names**: Must follow standard Python naming conventions
   - Lowercase with underscores
   - Must be valid Python identifiers
   - Should match the name in pyproject.toml

2. **Virtual Environment Location**: UV creates virtual environments in `.venv` by default
   - This location is recognized by most Python tools and IDEs
   - Changing this location may cause integration issues with some tools

3. **UV Configuration**: Must be in the `[tool.uv]` section of pyproject.toml
   - Cannot use separate configuration files for UV settings

### Integration Limitations

#### IDE Integration

1. **VS Code**:
   - Requires specific configuration in devcontainer.json
   - Python extension must be configured to use the UV-created virtual environment
   - Some Python extension features may expect traditional Python tools

2. **PyCharm**:
   - Limited native support for UV
   - Must configure to use the UV-created virtual environment
   - May attempt to use built-in pip functionality

3. **Jupyter Notebooks**:
   - Must be run through `uv run -m jupyter notebook`
   - Cannot use direct `jupyter` commands
   - May require additional configuration for kernel discovery

#### CI/CD Integration

1. **GitHub Actions**:
   - Requires custom setup steps to install and use UV
   - Cannot use standard Python setup actions without modification
   - Example workflow:
     ```yaml
     - name: Install UV
       run: curl -LsSf https://astral.sh/uv/install.sh | sh
     - name: Setup Python with UV
       run: uv python install 3.12
     - name: Install dependencies
       run: uv pip sync requirements.lock
     ```

2. **Jenkins/GitLab CI**:
   - Similar limitations requiring custom setup steps
   - Cannot use standard Python plugins without modification

#### Tool Integration

1. **Linters/Formatters**:
   - Must be run through `uv run -m [tool]`
   - Cannot use direct commands like `black`, `flake8`, etc.
   - May require additional configuration for tool discovery

2. **Build Tools**:
   - Must use UV for building packages
   - Cannot use direct `python setup.py` commands
   - Build process must be configured in pyproject.toml

### Common Pitfalls and Workarounds

#### 1. Attempting to Use Traditional Python Tools

**Problem**: Developers or AI agents attempt to use `pip`, `python`, etc. directly.

**Solution**: 
- The DevContainer is configured to intercept these commands with helpful error messages
- Always prefix Python commands with `uv run`
- Use `uv pip` instead of `pip`

#### 2. Missing Dependencies in Development

**Problem**: Development dependencies are not available in the environment.

**Solution**:
- Add development dependencies to `[project.optional-dependencies]` in pyproject.toml
- Install with `uv pip install -e ".[dev]"`
- Use lockfiles for reproducible environments

#### 3. Virtual Environment Not Recognized

**Problem**: IDE or tools cannot find the Python interpreter in the virtual environment.

**Solution**:
- Ensure the virtual environment is created in the default location (`.venv`)
- Configure IDE to look for Python in `${workspaceFolder}/.venv/bin/python`
- Run tools through UV: `uv run -m [tool]`

#### 4. Package Installation Failures

**Problem**: Packages fail to install with UV.

**Solution**:
- Check for package compatibility with your Python version
- Try with verbose output: `uv pip install package_name -v`
- For problematic packages, specify version constraints

#### 5. Script Execution Issues

**Problem**: Scripts fail to run or find dependencies.

**Solution**:
- Always run scripts through UV: `uv run script.py`
- Ensure the script is using relative imports correctly
- For entry points, configure them in pyproject.toml

### Migration Considerations

When migrating existing Python projects to the UV-exclusive approach:

1. **Convert requirements.txt to pyproject.toml**:
   ```bash
   uv pip compile requirements.txt -o requirements.lock
   ```
   Then manually add dependencies to pyproject.toml.

2. **Replace setup.py with pyproject.toml**:
   Follow PEP 621 standards for project metadata.

3. **Reorganize to src-layout** if not already using it:
   - Move package code to `src/package_name/`
   - Update imports accordingly
   - Update tests to import from the installed package

4. **Update CI/CD pipelines**:
   - Replace pip commands with UV equivalents
   - Add UV installation steps

## Relationships
- **Parent Nodes:** [elements/uv-python/overview.md]
- **Child Nodes:** None
- **Related Nodes:** 
  - [elements/uv-python/structure.md] - details - Project structure that works within these constraints
  - [elements/uv-python/devcontainer.md] - implements - DevContainer that enforces these constraints
  - [elements/uv-python/workflow.md] - adapts-to - Workflows designed around these constraints
  - [decisions/uv_exclusive_approach.md] - justifies - Decision that establishes these constraints

## Navigation Guidance
- **Access Context:** Use this document when encountering issues with the UV-exclusive approach or when planning project structure
- **Common Next Steps:** After reviewing constraints, explore structure.md for implementation details or workflow.md for working within these constraints
- **Related Tasks:** Project setup, migration from traditional Python tools, troubleshooting integration issues
- **Update Patterns:** This document should be updated when new constraints are discovered or when UV capabilities evolve

## Metadata
- **Created:** 2025-05-19
- **Last Updated:** 2025-05-19
- **Updated By:** Claude

## Change History
- 2025-05-19: Initial creation of UV Python constraints documentation
