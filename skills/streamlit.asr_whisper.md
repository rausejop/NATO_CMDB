# ASR & Whisper Integration Technical Mastery

## Role: AI Audio Processing Specialist

## Core Knowledge & Lessons:

### 1. Robust Audio Pipeline:
- **Extraction:** Use `yt_dlp` with `format: bestaudio/best`.
- **Naming Convention:** Mandatory use of current Process ID (`os.getpid()`) in temporary filenames to prevent collisions in multi-session environments (e.g., `yt_audio_{pid}_{timestamp}.mp3`).
- **Progress Tracking:** Implement `progress_hooks` in `yt_dlp` to pass download percentages to the UI (e.g., Streamlit `st.progress`).
- **Conversion:** Mandatory use of `ffmpeg`. Convert to `mp3` (192k) for reliable input.

### 2. Optimized Inference (Whisper):
- **CPU Optimization:** When running on CPU, explicitly set `fp16=False` in the `transcribe()` method to avoid `UserWarning` and unnecessary overhead.
- **Model Choice:** Use `base` for local CPU. Requires ~500MB RAM.
- **Memory & Cleanup:** Ensure `os.remove()` is called on audio files within a `finally` block.

### 3. User Experience (UX):
- **Feedback:** For long videos, provide granular status updates ("Downloading...", "Transcribing...", "Cleaning up...").
- **Metadata:** Fetch video duration via `yt_dlp` to give context to the user about expected wait times.

## Implementation Guardrails:
- Always document the FFmpeg dependency.
- Include a progress bar for time-consuming downloads.

## Context: Act_TSLCB_2026
