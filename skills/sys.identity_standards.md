# Identity & DNIwallet Integration (Secuware)

Technical requirements for hardware-backed identity verification and eIDAS 2.0 compliance.

## Authentication Hardening (REQ11.01)
- **Protocol**: OIDC/SIOPv2 utilizing Proof Key for Code Exchange (PKCE).
- **Entropy**: Challenge-Response (Nonce) generated using `secrets.token_urlsafe()` (>= 32 bytes).

## Cryptographic Integration (REQ11.02)
- **NFC**: Asynchronous processing for DNIe 3.0/4.0.
- **Polling**: 60-second TTL for QR-based pairing to prevent session hanging.

## Privacy & GDPR (REQ11.03)
- **Selective Disclosure**: Favor SD-JWT.
- **Minimization**: Do NOT store full DNI/NIE; use SHA-256 Hash + System Salt (Peppered Hash) for indexing.

## Security Controls
- **Callbacks**: Strict IP-Allowlist for webhooks; JWS header validation (JWKS).
- **Biometrics**: Zero-bypass policy for biometric failures.
- **Hardware (TPM 2.0)**: Interface with Windows TPM for secure API Key storage where possible.
- **eIDAS 2.0**: Schema compatibility with European Digital Identity Wallet (EUDI).
