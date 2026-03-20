import streamlit as st
from database.db_manager import init_db
from views.inventory import show_inventory
from views.visualization import show_relationships
from views.mapping import show_map
from views.exports import show_exports
from views.dashboard import show_dashboard

# Page Config
st.set_page_config(
    page_title="NATO Enclave CMDB Manager | CONFIANZA23 Inteligencia y Seguridad, S.L.",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize Database
init_db()

# Corporate CSS Styling (HTML Injection)
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

# Sidebar Layout
with st.sidebar:
    # 1. Company Logo
    st.image("skills/Logo_CONFIANZA23.png", use_container_width=True)
    
    # 2. Title & Controls
    st.title("🌍 NATO CMDB")
    menu = st.radio(
        "Navigation",
        ["Dashboard", "Inventory Management", "Relationship Mapping", "Geospatial View", "Exports & Reports"]
    )
    
    # 3. Visual Separator
    st.divider()
    
    # 4. About Section
    st.markdown("### 👨‍💻 About \nNATO Enclave Configuration Management Database (CMDB) for secure infrastructure global tracking.\n\nDeveloped by **CONFIANZA23 Inteligencia y Seguridad, S.L.**")
    
    # 5. Pro-Tip
    st.info("💡 **Pro-Tip:** Use the Relationship Map to visualize complex dependency chains between enclaves and devices.")

st.sidebar.caption("ITIL v4 & PRINCE2 compliant")

# Routing
if menu == "Dashboard":
    show_dashboard()
    
elif menu == "Inventory Management":
    show_inventory()
    
elif menu == "Relationship Mapping":
    show_relationships()
    
elif menu == "Geospatial View":
    show_map()
    
elif menu == "Exports & Reports":
    show_exports()
