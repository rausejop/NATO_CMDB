# CONFIANZA23 Logging Style (Backend)

## Context
You are a Python backend developer agent focused strictly on execution tracing and instrumentation.
All Streamlit or backend applications generated for "CONFIANZA23 Inteligencia y Seguridad, S.L." MUST implement a unified, interactive, real-time logging mechanism powered by `loguru`.

## Preconditions
1. Python environment must support `loguru` and standard `sys` libraries.
2. The UI framework is assumed to be Streamlit if running a web application.

## Constraints & Rules
- **NEVER** use the default Python `print()` statement for standard logging or operation tracing.
- **MUST** redirect logs simultaneously to both a Streamlit visual container and the system console `sys.stderr`.
- **MUST** enforce the application of time, level, and message formats with colorizations as strictly dictated.

## Postconditions
- All logs emitted during business logic execution are instantly mirrored on the user's graphical interface ("Session Logs") and in the execution terminal.
- Error handling cleanly dumps stack traces into the central logging mechanism instead of crashing silently.

## Implementation Details

### 1. Mandatory Dependencies
Ensure and utilize the following imports:
```python
import sys
from loguru import logger
```

### 2. Streamlit UI Binding
Implement a custom log handler that pushes formatted strings directly into a Streamlit placeholder block. Instantiate this class before executing the core logic:

```python
class StreamlitLogHandler:
    def __init__(self, container):
        self.container = container
        self.log_content = ""

    def write(self, message):
        if message.strip():
            self.log_content += f"{message}\n"
            self.container.code(self.log_content)
```

### 3. Dual-Output Configuration
Clear all default `loguru` handlers before your logic blocks catch or emit anything. 

1. **UI Output:** Link an empty Streamlit container (`st.empty()`) in the designated UI space (e.g., a "Session Logs" subheader) to `StreamlitLogHandler`. Use the explicit format.
2. **Terminal Output:** Re-target standard error `sys.stderr` with green parsing for time and cyan text for the payload.

```python
# 1. Create the visual container in the app
log_container = st.empty()
handler = StreamlitLogHandler(log_container)

# 2. Reset loguru defaults
logger.remove()

# 3. Add graphical interface sink
logger.add(handler, format="{time:HH:mm:ss} | <level>{level: <8}</level> | {message}", colorize=True)

# 4. Add colorized console system sink
logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>")
```

### 4. Required Tracing Taxonomy
Throughout the script, substitute `print()` with `logger` calls that strictly map to the situation:

- `logger.info("...")`: Start of overarching processes, general state verifications.
- `logger.debug("...")`: Fine-grained loop details or variable tracking.
- `logger.warning("...")`: Non-fatal anomalies or negative condition findings (e.g., 0 results from an API).
- `logger.error("...")`: Specific external call failures, API rejections, or corrupted payloads.
- `logger.exception("...")`: Inside `try-except` blocks; loguru automatically builds and appends the traceback.
- `logger.success("...")`: Explicit marking for successful completion of a major milestone.
