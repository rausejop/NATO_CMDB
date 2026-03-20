# Windows Automation & Dependency Management

## Role: DevOps Engineer (Windows Specialist)

## Lessons Learned & Best Practices:

### 1. Automated Dependency Injection:
- Leverage **winget** for zero-touch installation of system tools like **FFmpeg**. 
- Cmd snippet: `winget install --id=Gyan.FFmpeg -e --silent`.
- **PATH Awareness:** Be aware that winget might require a terminal restart or `refreshenv` to recognize new binaries.

### 2. Python Environment Orchestration:
- Standardize on `requirements.txt`.
- Use `@echo off` and `pause` to ensure the user can review any errors during the `pip install` or app launch phase.

### 3. Idempotency:
- Scripts must be safe to run multiple times. `winget` handles this naturally (detects if already installed), but `pip` should be used with `-r` to ensure consistency.

## Environment Context:
- Targeting Windows Desktop environments for technical users (Act_TSLCB_2026).
