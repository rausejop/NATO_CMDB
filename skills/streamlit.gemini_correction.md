# AI Correction & Semantic Enrichment

## Role: AI Linguistic Specialist

## Objective:
Process raw text (transcriptions, logs, notes) to improve readability, grammar, and structure using high-level LLMs like Google Gemini.

## Technical Execution (The "No-Key" Pattern):

### 1. Access Strategy (`g4f` Integration):
- **Library:** Use `g4f` (GPT4Free) to access Gemini and other LLMs without API keys.
- **Reliability:** Implement provider fallbacks using dynamic model references. Instead of string names, use `g4f.models.gemini` for primary and `g4f.models.default` for fallback to ensure the provider choice is handled by the library.
- **Performance:** LLM calls are slow (5-15s). Always wrap in `st.spinner` and cache results in `st.session_state`.

### 2. Prompt Engineering for Correction:
- **Core Prompt:** "Correct punctuation, orthography, and coherence. NO introductions. NO conclusions. ONLY the resulting text. Maintain all technical keywords and original meaning."
- **Context Awareness:** If the source is a transcription, prompt for "removing typical filler words (um, ah) and fixing sentence flow".

### 3. UI Implementation Patterns:
- **Comparison View:** Use `st.tabs(["Original", "Corrected"])` or `st.columns(2)` for immediate feedback.
- **Independent Exports:** Provide separate download buttons (`st.download_button`) for both versions to allow the user to choose or keep both.

## Implementation Guardrails:
- Ensure `g4f` is in `requirements.txt`.
- Handle "Empty Text" or "API Timeout" errors gracefully with user-facing warnings.

## Context: Act_TSLCB_2026 / CONFIANZA23 Standards
