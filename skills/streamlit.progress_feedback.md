# Advanced Progress & Feedback Management

## Role: UX & Interaction Engineer

## Objective:
Provide real-time, granular feedback for long-running operations in Python/Streamlit applications to prevent perceived application hangs.

## Implementation Patterns:

### 1. Download Progress (yt-dlp):
- **Extracción de Datos:** Usar `ydl_hook` para capturar no solo el porcentaje, sino también `eta` (tiempo restante) y `speed` (velocidad).
- **Cómputo:** Convertir la velocidad a unidades legibles (MB/s) y formatear el ETA en segundos o minutos.
- **UI Labeling:** En Streamlit, usar el parámetro `text` de `st.progress` para mostrar strings dinámicos: `📥 Descargando | ETA: 12s | 4.5 MB/s`.

### 2. Processing States:
- **Transición:** Diferenciar claramente entre las fases de "Descarga" (basada en red) y "Inferencia/Transcripción" (basada en CPU/computación).
- **Indicadores Visuales:** Usar `st.spinner` para procesos cuya duración exacta no se conoce (como Whisper o Gemini), pero informando al usuario de la fase actual.
- **Metadatos Iniciales:** Obtener la duración del video antes de empezar para setear expectativas en el usuario.

### 3. Static UI Containers (st.empty):
- **Problem:** Dynamic messages (info/warning) inside loops create multiple widgets, cluttering the UI.
- **Solution:** Initialize an empty container outside the loop: `status_placeholder = st.empty()`.
- **Usage:** Inside the loop/callback, update the container: `status_placeholder.info("Current Step...")`. This overwrites the previous content instead of appending.
- **Clean ending:** Use the placeholder for a final success message: `status_placeholder.success("Done!")`.

## Best Practices:
- **Cleanliness:** Use `st.empty()` for transient status messages and `st.progress` for numerical progress.
- **Separation:** Pass the UI objects (placeholders) from the main app to the logic functions to decouple business logic from UI rendering.
- **Robustness:** ALWAYS wrap progress and status updates in `try/except` blocks. In Python 3.14/Streamlit environments, background threads can lose context unexpectedly; the core business logic MUST continue even if the UI feedback fails.

## Context: Act_TSLCB_2026 / CONFIANZA23 Standards
