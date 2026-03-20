# Security & Audit Standards (CONFIANZA23)

Guidelines for security compliance, code verification, and automated auditing.

## GRC Framework (REQ3.00)
- **OWASP Compliance**: Web Top 10 2025 and LLM Top 10 2025 (Priority: Prompt Injection, Excessive Agency).
- **ISO 27001**: Technical controls alignment.
- **ISA/IEC 62443**: Industrial security compliance.

## Code Verification (REQ6.00)
Every release must pass native verification:
- **Indentation**: `python -m tabnanny <dir>`.
- **AST Analysis**: Check for dangerous functions (`eval`, `exec`) and hardcoded secrets.
- **Bytecode Inspection**: Ensure critical security checks are not optimized out.
- **Path Safety**: Validate against "Zip Slip" using `pathlib` for all artifact ingestion.

## Automated Cyber Audit (REQ8.00)
- **Continuous Audit**: Triggered by GitLab/GitHub release events.
- **Delta-Only Scan**: Focus on the diff between the current and previous stable releases.
- **PoC Generation**: For 'HIGH' or 'CRITICAL' vulnerabilities, generate a sanitized PoC for verification.
- **Remediation**: Every identified gap must have a suggested fix following SOLID and CONFIANZA23 typing standards.
