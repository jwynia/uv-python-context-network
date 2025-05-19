# UV Python Project Principles

## Purpose
This document outlines the core principles and standards that guide decision-making and development across the UV Python project template.

## Classification
- **Domain:** Core Concept
- **Stability:** Static
- **Abstraction:** Conceptual
- **Confidence:** Established

## Content

### Core Values

1. **Consistency**
   The project prioritizes consistent tooling and workflows to eliminate confusion and reduce cognitive load. By enforcing UV-only approaches, we ensure that all package management and Python environment operations follow a single, coherent pattern.

2. **Performance**
   UV's Rust-based implementation offers significant performance improvements over traditional Python tools. The project embraces these performance benefits by making UV the exclusive tool for Python operations.

3. **Modern Best Practices**
   The project embraces modern Python development best practices, including PEP 621 packaging standards, src-layout project structure, and containerized development environments.

4. **Clarity**
   Clear separation between implementation code and planning/architecture documentation ensures that the project remains understandable and maintainable.

### Design Principles

1. **UV Exclusivity**
   All Python package management and environment operations must be performed exclusively through UV, with no fallback to traditional Python tools.
   
   *Example:* The DevContainer configuration deliberately blocks access to pip and traditional Python commands, forcing the use of UV alternatives.

2. **Explicit Configuration**
   Project configuration should be explicit and centralized in the pyproject.toml file, following modern Python packaging standards.
   
   *Example:* All dependencies and project metadata are defined in the pyproject.toml file rather than in separate requirements files.

3. **Separation of Concerns**
   Clear separation between implementation code, configuration, and documentation ensures maintainability and clarity.
   
   *Example:* Implementation code lives in the src directory, while planning and architectural documentation lives in the context network.

4. **Containerized Development**
   Development environments should be containerized to ensure consistency across different machines and prevent "works on my machine" issues.
   
   *Example:* The project includes DevContainer configuration that creates a consistent, isolated environment with UV pre-installed.

### Standards and Guidelines

#### Quality Standards

- All Python code should follow PEP 8 style guidelines
- Project configuration should follow PEP 621 standards
- Dependencies should be explicitly versioned
- UV's lockfile approach should be used to ensure reproducible builds

#### Structural Standards

- Use src-layout for Python package organization
- Keep implementation code separate from project configuration
- Store all planning and architectural documentation in the context network
- Maintain a clear separation between development environment configuration and project code

#### Safety and Security Standards

- Use UV's deterministic dependency resolution to prevent supply chain attacks
- Regularly update dependencies to incorporate security fixes
- Use containerized development to isolate the development environment
- Follow the principle of least privilege in development container configuration

#### Performance and Efficiency Standards

- Leverage UV's performance advantages for package operations
- Use UV's caching capabilities to speed up repeated operations
- Minimize unnecessary dependencies to keep the project lean
- Optimize development workflows to reduce friction and waiting time

### Process Principles

1. **Reproducible Environments**
   Development environments should be reproducible across different machines and setups, ensuring consistent behavior regardless of where the code is run.

2. **Documentation-Driven Development**
   Key decisions and architectural considerations should be documented in the context network before implementation, ensuring clarity of purpose and approach.

3. **Incremental Adoption**
   While the template enforces UV-only usage, it should be designed to allow users to incrementally adopt UV practices in their existing projects.

4. **Continuous Improvement**
   The template should evolve as UV and Python packaging practices evolve, incorporating new best practices and capabilities.

### Decision-Making Framework

#### Decision Criteria

- Consistency with UV's approach and philosophy
- Alignment with modern Python packaging standards
- Impact on developer experience and productivity
- Compatibility with existing Python ecosystem
- Performance implications

#### Trade-off Considerations

- Strictness vs. flexibility in enforcing UV-only usage
- Simplicity vs. comprehensiveness in template features
- Familiarity vs. innovation in development approaches
- Performance vs. compatibility in tool selection

### Principle Application

#### When Principles Conflict

When principles conflict, prioritize in this order:
1. Consistency (UV-only approach)
2. Modern best practices
3. Performance
4. Flexibility

For example, if a particular workflow is more familiar but would require traditional Python tools, prefer the UV-based approach even if it requires learning new commands.

#### Exceptions to Principles

Exceptions to the UV-only principle may be considered in these limited circumstances:
- When a critical package or tool is fundamentally incompatible with UV
- When debugging specific UV-related issues requires comparison with traditional tools
- During migration phases for existing projects adopting the template

In such cases, exceptions should be clearly documented and treated as temporary measures.

## Relationships
- **Parent Nodes:** [foundation/project_definition.md]
- **Child Nodes:** None
- **Related Nodes:** 
  - [foundation/structure.md] - implements - Project structure implements these principles
  - [processes/creation.md] - guided-by - Creation processes follow these principles
  - [decisions/uv_exclusive_approach.md] - evaluated-against - Decisions are evaluated against these principles
  - [elements/uv-python/workflow.md] - applies - Workflow applies these principles in practice

## Navigation Guidance
- **Access Context:** Use this document when making significant decisions about UV Python project setup or evaluating options
- **Common Next Steps:** After reviewing principles, typically explore structure.md or UV Python element documentation
- **Related Tasks:** Python project setup, dependency management decisions, development workflow design
- **Update Patterns:** This document should be updated when fundamental UV capabilities or Python packaging standards change

## Metadata
- **Created:** 2025-05-19
- **Last Updated:** 2025-05-19
- **Updated By:** Claude

## Change History
- 2025-05-19: Updated principles document to reflect UV Python template specifics
