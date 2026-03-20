# Streamlit Development Guide (CONFIANZA23)

Guidelines for building secure and efficient Streamlit dashboards.

## Streamlit Connect (REQ2.02)

- **Connection Management**: Mandatory use of `st.connection()`. Direct driver instantiation (e.g., `psycopg2.connect`) is forbidden.
- **Secrets Management**: All parameters must reside in `.streamlit/secrets.toml`. No hardcoded credentials.
- **Caching**: Use `ttl` (Time-To-Live) to minimize database load. Default `ttl=3600`.
- **SQL Security**: Use indexed parameters in queries to prevent SQL Injection. No f-strings in SQL.
- **Cloud Storage**: Use `FilesConnection` for S3/GCS with `st.cache_data`.
- **State Persistence**: Utilize `st.session_state` for status and query filtering.
- **UI Performance**: Implement `@st.fragment` for high-frequency data refresh blocks.
- **Error Handling**: Wrap connectivity calls in `st.errors.StreamlitAPIException` blocks.

## Design Aesthetics
- **Branding**: Logos must be placed in the sidebar (top-left) as per corporate standards.
- **Dynamic Feedback**: Use `st.empty()` for real-time status updates without flickering.
- **Visuals**: Premium dark mode gradients and modern iconography are required for TRL 6+ applications.
