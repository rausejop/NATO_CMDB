# CONFIANZA23 Corporate Style (Frontend)

## Context
You are an expert Frontend web developer agent specializing in Python and the Streamlit library. 
Your objective is to generate web applications that strictly adhere to the corporate identity, design layout, and aesthetics of "CONFIANZA23 Inteligencia y Seguridad, S.L.".

## Preconditions
1. The target framework is Streamlit (`import streamlit as st`).
2. The agent must have the application title, description, and an appropriate representative emoji.
3. The file `Logo_CONFIANZA23.png` must be available in the local directory.

## Constraints & Rules
- **DO NOT** use default Streamlit light themes without overriding them with corporate CSS.
- **DO NOT** clutter the main screen; always use a sidebar for controls.
- **MUST** use CSS injection (`unsafe_allow_html=True`) precisely as supplied.
- **MUST** follow the rigid layout structure described in Implementation.

## Postconditions
- The resulting `.py` file successfully renders a wide-layout Streamlit app with the CONFIANZA23 dark theme, gradient headers, and a persistent sidebar containing the company logo and "About" section.

## Implementation Details

### 1. Page Configuration
Initialize the application with the following strict settings:
```python
st.set_page_config(
    page_title="{App_Name} | CONFIANZA23 Inteligencia y Seguridad, S.L.",
    page_icon="{Representative_Emoji}",
    layout="wide",
    initial_sidebar_state="expanded"
)
```

### 2. Corporate CSS Styling (HTML Injection)
Inject this exact CSS block early in the script to ensure the corporate dark theme `#0e1117`, metric styling `#1f2937`, and gradient text for headers:
```python
st.markdown("""
<style>
    /* Main background */
    .main { background-color: #0e1117; }
    
    /* Metrics panels */
    .stMetric { 
        background-color: #1f2937; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #374151; 
        color: #f9fafb !important; 
    }
    .stMetric * { color: #f9fafb !important; }
    
    /* Rounded borders for data tables */
    .stDataFrame { border-radius: 12px; overflow: hidden; }
    
    /* Corporate color gradients for all headers */
    h1, h2, h3 { 
        background: linear-gradient(90deg, #3b82f6, #8b5cf6); 
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent; 
    }
</style>
""", unsafe_allow_html=True)
```

### 3. Sidebar Layout
The `with st.sidebar:` block must contain the following sequence:
1. **Company Logo:** `st.image("Logo_CONFIANZA23.png", width='stretch')`
2. **Title & Controls:** Section title (with emoji) followed by interactive widgets.
3. **Visual Separator:** `st.divider()` immediately after controls.
4. **About Section:** `st.markdown("### 👨‍💻 About \n{Brief tool description}.\n\nDeveloped by **CONFIANZA23 Inteligencia y Seguridad, S.L.**")`
5. **Pro-Tip:** `st.info("💡 **Pro-Tip:** {Usage hint}.")`

### 4. Main Panel Layout
1. **Header:** `st.title("{Representative_Emoji} {App_Name}")` followed by `st.subheader("{Description}")`.
2. **Separators:** Use `st.divider()` between major logical UI sections.
3. **Dashboard Panels:** Display state metrics using rows of columns (`col1, col2... = st.columns(N)`) and `st.metric`.
4. **Dynamic Feedback:** For long processes, maintain a static UI using `st.empty()` for status messages and `st.progress()` for progress bars. **DO NOT** let status messages accumulate.
5. **Empty State:** If user action is required before processing (e.g., file upload):
    - Show Call to Action: `st.info("🚀 Please {Required_Action} to begin.")`
    - Show Full-width Decorative Image: `st.image("{High_Quality_Unsplash_URL}", width="stretch")`.
