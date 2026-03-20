# Zero-Auth LLM Access (The g4f Pattern)

## Role: Strategic AI Integration Engineer

## Objective:
Integrate Large Language Model (LLM) capabilities into applications without requiring end-user API keys or complex cloud authentication, lowering friction for local/MVP tools.

## Core Strategy: `g4f` (GPT4Free) Integration

### 1. Library Management:
- **Dependency:** Add `g4f` to `requirements.txt`.
- **Imports:** `import g4f`.

### 2. Execution Pattern:
- **Multi-Provider Support:** Always treat LLM access as fragile. Implement "Waterfall Fallbacks":
    ```python
    try:
        # Priority: Gemini
        response = g4f.ChatCompletion.create(model=g4f.models.gemini, messages=msgs)
    except:
        # Secondary: GPT-3.5
        response = g4f.ChatCompletion.create(model="gpt-3.5-turbo", messages=msgs)
    ```
- **Streamlit Handling:** LLM operations are blocking. Wrap in `with st.spinner("AI is thinking...")` and use `st.error` for total connection failures.

### 3. Safe Prompting:
- Use "Strict Output" instructions: "ONLY return requested data", "DO NOT include preamble", "Format as JSON/Plaintext".

### 4. Ethical & Performance Use:
- **Usage:** Ideal for Low-Risk MVP features (correction, summarization, translation).
- **Latency:** Expect 5-20 seconds per call. Always use `st.session_state` to prevent re-triggering the LLM on every Streamlit rerun.

## Implementation Context:
- Targeting Desktop/Local-First applications (Project Act_TSLCB_2026).
- Standard for CONFIANZA23 Rapid Prototyping (TRL 5-6).
