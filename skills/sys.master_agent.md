# CONFIANZA23 Core Software Blueprint (Master Agent)

## Context
You are the Master AI Agent responsible for generating, managing, and unifying the architecture of web applications for "CONFIANZA23 Inteligencia y Seguridad, S.L.". 
You orchestrate multiple specialized standard skills (Frontend, Logging, Data Display, Data Export, Error Handling) to ensure absolute uniformity, security, and usability across all corporate software.

## Preconditions
1. The developer environment uses Python and Streamlit.
2. An appropriate application objective is provided by the user.
3. The individual sub-skills are available or have their rules internalized by the agent.

## Constraints & Rules
- **MUST** enforce the `CONFIANZA23 Corporate Style` frontend design explicitly.
- **MUST** enforce the dual-output real-time `CONFIANZA23 Logging Style` using `loguru`.
- **MUST** render heavy operations or analytics interactively using the `CONFIANZA23 UI Updates & Styling` progress bars and conditional DataFrames.
- **MUST** allow downloading generated tables in 4 formats using the `CONFIANZA23 Export Standards`.
- **MUST** catch and handle all external and internal exceptions gracefully via `CONFIANZA23 Defenses`.
- **NEVER** skip styling, leave unhandled `try-except`, use raw `print()` statements, or output unthemed Streamlit apps.

## Postconditions
- Any Python file generated under this Master Prompt represents a fully compliant, production-ready, TRL-6+ (Technology Readiness Level) minimum viable product for CONFIANZA23.

## Implementation Details (Standard Blueprint)

```python
import streamlit as st
import pandas as pd
import requests
import json
import sys
from loguru import logger

# 1. Page Configuration & CSS
st.set_page_config(
    page_title="{App_Title} | CONFIANZA23 Inteligencia y Seguridad, S.L.",
    page_icon="{Emoji}",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. CSS Injection
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1f2937; padding: 20px; border-radius: 12px; border: 1px solid #374151; color: #f9fafb !important; }
    .stMetric * { color: #f9fafb !important; }
    .stDataFrame { border-radius: 12px; overflow: hidden; }
    h1, h2, h3 { background: linear-gradient(90deg, #3b82f6, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
</style>
""", unsafe_allow_html=True)

# 3. Streamlit Log Handler
class StreamlitLogHandler:
    def __init__(self, container):
        self.container = container
        self.log_content = ""
    def write(self, message):
        if message.strip():
            self.log_content += f"{message}\\n"
            self.container.code(self.log_content)

# 4. Core Business Logic Wrapper
def fetch_data(param):
    logger.info(f"Starting fetch operation for {param}")
    try:
        # Business logic goes here...
        pass
    except Exception as e:
        logger.exception(f"Unhandled exception during fetch: {e}")
        return []

# 5. Main Application Loop
def main():
    st.title("{Emoji} {App_Title}")
    st.subheader("{App_Subtitle}")
    
    with st.sidebar:
        st.image("Logo_CONFIANZA23.png", width='stretch')
        st.header("{Emoji} Settings")
        user_input = st.text_input("Enter Data")
        st.divider()
        st.markdown("### 👨‍💻 About \n{Brief tool description}.\n\nDeveloped by **CONFIANZA23 Inteligencia y Seguridad, S.L.**")
        st.info("💡 **Pro-Tip:** {Usage Hint}.")
        
    top_container = st.container()

    if user_input:
        st.divider()
        st.subheader("📋 Session Logs")
        
        log_container = st.empty()
        handler = StreamlitLogHandler(log_container)
        logger.remove()
        logger.add(handler, format="{time:HH:mm:ss} | <level>{level: <8}</level> | {message}", colorize=True)
        logger.add(sys.stderr, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{message}</cyan>")
        
        progress_bar = st.progress(0)
        results = []
        
        for i in range(10):
            results.append({"ID": f"Result-{i}", "Category": "A", "Status": "Passed"})
            progress_bar.progress((i + 1) / 10)
        logger.success("Operation completed safely.")
        
        with top_container:
            st.divider()
            st.subheader("📉 Process Metrics")
            col1, col2, col3 = st.columns(3)
            col1.metric("Total Extracted", len(results))
            
            st.subheader("Results Table")
            df = pd.DataFrame(results)
            st.dataframe(df, use_container_width=True)
            
            # Export Buttons
            csv = df.to_csv(index=False).encode('utf-8')
            md = df.to_csv(index=False, sep="|").encode('utf-8')
            xml = df.copy()
            xml.columns = [str(c).replace(' ', '_') for c in xml.columns]
            xml = xml.to_xml(index=False).encode('utf-8')
            json_data = df.to_json(orient='records', indent=4).encode('utf-8')

            exp_col1, exp_col2, exp_col3, exp_col4 = st.columns(4)
            exp_col1.download_button("Export CSV", csv, "export.csv", "text/csv")
            exp_col2.download_button("Export MD", md, "export.md", "text/markdown")
            exp_col3.download_button("Export XML", xml, "export.xml", "application/xml")
            exp_col4.download_button("Export JSON", json_data, "export.json", "application/json")
    else:
        st.info("🚀 Please enter data and execute to begin.")
        st.image("https://images.unsplash.com/photo-1550751827-4bd374c3f58b?auto=format&fit=crop&q=80&w=2070", width="stretch")

if __name__ == "__main__":
    main()
```
