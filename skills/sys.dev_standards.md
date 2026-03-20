# CONFIANZA23 Python Development Standards

Core technology stack requirements for Python development.

## Framework & Language (REQ2.01)

- **Licensing**: Apache License 2.0.
- **OS**: Windows 11 [Version 10.0.26200.7840].
- **Language**: Python 3.14.3 (PEP 745).
- **Documentation**: Block-style comments placed **directly above** the code they describe (End-of-line comments are prohibited for business logic).
- **Typing**: Strict PEP 484/526/647/742. Use of `typing.TypeIs` is mandatory.
- **Security**: Fail-Safe wrappers (try-except) are mandatory for all UI-interacting background threads.
- **Environment**: Support multi-layered imports for Streamlit `ScriptRunContext` (see `sys.error_handling`).

## Tooling (REQ4.08-4.12)
- **uv**: Dependency installer.
- **Ruff**: Linter and formatter.
- **Pytest + Playwright**: Testing and E2E.
- **GitHub Actions**: CI/CD automation.
- **Pulumi**: Infrastructure as Code (Python).
