# UV Python Context Network

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3120/)
[![Package Manager: UV](https://img.shields.io/badge/Package%20Manager-UV-blueviolet)](https://github.com/astral-sh/uv)

This project is a specialized context-network template for Python development using the modern UV package manager. It provides a structured approach to documenting and managing Python projects that exclusively use UV for package and environment management.

Built on the foundation of context networks (more info at https://jwynia.github.io/context-networks/), this template focuses specifically on the technical aspects and constraints of Python development with UV, a high-performance package manager written in Rust that serves as a drop-in replacement for traditional Python tools like pip, pip-tools, and virtualenv.

## Key Features

- **UV-Exclusive Approach**: This template enforces a UV-only approach to Python development, deliberately blocking access to traditional Python tools to ensure consistency and prevent confusion.
- **DevContainer Configuration**: Includes a custom DevContainer setup that creates an isolated development environment with UV pre-installed.
- **Modern Python Structure**: Follows modern Python project structure best practices, including src-layout and pyproject.toml configuration.
- **Comprehensive Documentation**: The context network contains detailed documentation on UV commands, workflows, and best practices.
- **GitHub Integration**: Includes issue templates, PR templates, and CI workflow configuration.

## Getting Started

1. **Use this template**:
   - Click the "Use this template" button on GitHub to create a new repository based on this template
   - Or clone the repository directly:
   ```bash
   git clone https://github.com/yourusername/uv-python-context-network.git my-project
   cd my-project
   ```

2. **Customize the template**:
   - Update the project name, description, and author in `pyproject.toml`
   - Rename the package directory in `src/package_name` to your actual package name
   - Update imports in test files to match your package name
   - Modify the LICENSE file with your name and year
   - Update this README.md with your project-specific information

3. **Open in VS Code with Dev Containers**:
   - Install the Dev Containers extension if not already installed
   - Open the project folder
   - When prompted, click "Reopen in Container"
   - The container will build and set up the UV environment automatically

4. **Start working with an LLM agent**:
   - Use an LLM agent that has file access to all files in the project folder
   - The context network will guide the agent in understanding the UV-specific constraints and workflows
   - Start with planning conversations to describe your specific Python project goals and constraints

## Project Structure

```
uv-python-context-network/
├── .context-network.md        # Context network discovery file
├── .devcontainer/             # Development container configuration
├── .github/                   # GitHub templates and workflows
├── context-network/           # Documentation and planning materials
├── src/                       # Source code (using src-layout)
│   └── package_name/          # Example package (rename this)
├── tests/                     # Test files
├── .gitignore                 # Git ignore patterns
├── LICENSE                    # MIT License
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## UV Python Development

This template enforces the use of UV for all Python operations:

- **Creating environments**: `uv venv`
- **Installing packages**: `uv pip install`
- **Running Python code**: `uv run script.py`
- **Managing dependencies**: `uv pip compile` and `uv pip sync`

The DevContainer configuration deliberately blocks access to traditional Python tools (`pip`, `python`, etc.) to ensure consistency and prevent confusion, particularly when working with AI agents.

For detailed information about UV commands and workflows, see the documentation in the context network:
- `context-network/elements/uv-python/overview.md`
- `context-network/elements/uv-python/commands.md`
- `context-network/elements/uv-python/workflow.md`

## Example Usage

Run the example code:

```bash
uv run -m package_name.example
```

Run the tests:

```bash
uv run -m pytest
```

## Tools for Working with this Template

For the best experience with this template, we recommend:

- **VS Code** (https://code.visualstudio.com/) with the Dev Containers extension
- **Cursor** (https://www.cursor.com/) - An AI-powered code editor built on VS Code
- **Cline** (https://cline.bot/) - A VS Code extension that provides AI agent capabilities

These tools can interact with the context network to understand the UV-specific constraints and workflows.

## Working with the Context Network

### Prompts
For whatever agent you use, include instructions in the system prompt or custom instructions that tell it about context networks and how to navigate them. The prompt in `/inbox/custom-instructions-prompt.md` provides a good starting point.

### Plan/Act Workflow
When working with AI agents:

1. **Plan Mode**: Start in Plan mode to discuss your Python project requirements and constraints
2. **Review UV Documentation**: Have the agent review the UV documentation in the context network
3. **Develop Specific Plans**: Create detailed plans for implementing your Python project with UV
4. **Act Mode**: Switch to Act mode only when you have a specific, well-defined task
5. **Monitor and Guide**: Pay attention to the agent's actions, especially ensuring it uses UV commands correctly

### UV-Specific Best Practices

1. **Always use pyproject.toml**: Keep all project configuration in pyproject.toml
2. **Use lockfiles**: Generate and commit lockfiles for reproducible builds
3. **Run through UV**: Always run Python code through UV (`uv run`)
4. **Follow src-layout**: Keep all package code in the `src/` directory
5. **Document UV usage**: Include clear instructions for UV commands in your project

### Retrospective
Periodically review and improve the context network:
- "What have we learned about UV that should be documented in the context network?"
- "How can we improve our UV workflows based on our experience?"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
