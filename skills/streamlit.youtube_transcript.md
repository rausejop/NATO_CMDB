# YouTube Transcript Extraction Mastery

## Role: Senior Automation Engineer & AI Specialist

## Objective:
Generate a premium Streamlit application that handles the complete lifecycle of YouTube content extraction: Discovery, Transcription (Official or ASR), and AI Correction.

## Technical Architecture & Lessons Learned:

### 1. Robust Intelligence Engine (`youtube_extractor.py`):
- **Dependencies:** `yt_dlp` (Audio/Metadata), `openai-whisper` (ASR), `youtube-transcript-api` (Official Captions).
- **Official API Bug Mitigation:** Use `get_transcript()` as the primary method. Version 1.2.2+ may have attribute errors with `list_transcripts`; check with `hasattr()` or wrap in comprehensive try-except.

### 🛠️ Strategic Lessons from Mastery lessons:

#### 1. Handling the `list_transcripts` and `get_transcript` attribute errors
Newer versions (1.2.4+) may have deprecated static methods in favor of instance methods.
**Solución Robusta (Adaptador Híbrido):**
1. **Instanciar:** `api = YouTubeTranscriptApi()`
2. **Jerarquía de llamadas:**
    - Intentar estático: `YouTubeTranscriptApi.get_transcript(...)`
    - Fallback a instancia: `api.fetch(...)`
3. **Procesamiento de datos:**
    - Los segmentos pueden ser diccionarios (estilo antiguo) o objetos `FetchedTranscriptSnippet` (estilo nuevo).
    - Usar: `text = segment['text'] if isinstance(segment, dict) else segment.text`

#### 2. Soporte de Idiomas
No todos los videos tienen transcripciones en el idioma solicitado.
**Patrón de Implementación:**
```python
def get_transcript_robust(video_id, preferred=['es', 'en']):
    try:
        return YouTubeTranscriptApi.get_transcript(video_id, languages=preferred)
    except:
        return YouTubeTranscriptApi.get_transcript(video_id)
```

### 2. The Extraction Funnel:
1. **Preferred Official:** Try `es` and `en` first.
2. **Auto-Generated Fallback:** List and fetch auto-captions if manual ones are missing.
3. **ASR (Last Resort):** Use `yt-dlp` + `Whisper` (base model) with `fp16=False` for CPU optimization.

### 3. AI Post-Processing (Correction):
- **Goal:** Transform raw, unpunctuated text into readable prose.
- **Workflow:** Once text is obtained, offer an "AI Correction" phase using Google Gemini (via no-auth methods like `g4f`).
- **Prompting:** Focus on punctuation, orthography, and coherence while preserving the original meaning.

### 4. Intelligent UI (`transcriptor.py`):
- **Feedback:** Use real-time progress bars for `yt-dlp` downloads and info spinners for Whisper/Gemini processing.
- **Dual Display:** Implement `st.tabs` to show "Original" vs "Corrected" versions side-by-side.
- **Labeling:** Badge the source (Official, Auto, ASR) and the correction status.

### 5. Environment & Automation:
- **Requirement:** FFmpeg is mandatory for audio processing.
- **One-Click Setup:** Provide a `build.cmd` using `winget install --id=Gyan.FFmpeg`.

## Contextual Identity:
- **Project:** Act_TSLCB_2026
- **Standards:** TRL 6 / Modular / Self-Healing.
