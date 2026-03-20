import streamlit as st
import streamlit_mermaid as st_mermaid
from database.db_manager import SessionLocal
from database.models import Enclave, Network, ConfigurationItem, Relationship

def show_relationships():
    st.subheader("🕸️ Infrastructure Relationship Mapping")
    
    db = SessionLocal()
    enclaves = db.query(Enclave).all()
    
    if not enclaves:
        st.info("No enclaves found. Add some in Inventory Management.")
        return

    selected_enclave_name = st.selectbox("Select Enclave to Visualize", [f"{e.location.name} > {e.name}" for e in enclaves])
    selected_enclave = next(e for e in enclaves if f"{e.location.name} > {e.name}" == selected_enclave_name)
    
    # Generate Mermaid syntax with Full Hierarchy
    mermaid_code = "graph TD\n"
    
    # Icons
    I_ZONE = "🌐"
    I_COUNTRY = "🚩"
    I_LOC = "📍"
    I_ENC = "🛡️"
    I_NET = "🔌"
    I_CI = "🖥️"

    # Hierarchy Nodes
    loc = selected_enclave.location
    country = loc.country
    zone = country.zone
    
    mermaid_code += f'  Z{zone.id}["{I_ZONE} Zone: {zone.name}"]\n'
    mermaid_code += f'  Z{zone.id} --> CO{country.id}["{I_COUNTRY} Country: {country.name}"]\n'
    mermaid_code += f'  CO{country.id} --> L{loc.id}["{I_LOC} City: {loc.name}"]\n'
    mermaid_code += f'  L{loc.id} --> E{selected_enclave.id}["{I_ENC} Enclave: {selected_enclave.name}"]\n'
    
    networks = db.query(Network).filter_by(enclave_id=selected_enclave.id).all()
    for net in networks:
        mermaid_code += f'  E{selected_enclave.id} --> N{net.id}["{I_NET} {net.name} ({net.subnet})"]\n'
        
        # Limit CIs to avoid Mermaid crashing on large datasets
        cis = db.query(ConfigurationItem).filter_by(network_id=net.id).limit(15).all()
        for ci in cis:
            mermaid_code += f'  N{net.id} --> C{ci.id}["{I_CI} {ci.hostname}"]\n'
        
        total_cis = db.query(ConfigurationItem).filter_by(network_id=net.id).count()
        if total_cis > 15:
            mermaid_code += f'  N{net.id} --> MORE{net.id}["... +{total_cis-15} more CIs"]\n'
            
    # Add N:M Relationships (only for visible CIs in this enclave context)
    visible_ci_ids = [ci.id for net in networks for ci in db.query(ConfigurationItem).filter_by(network_id=net.id).limit(15).all()]
    relationships = db.query(Relationship).filter(Relationship.source_ci_id.in_(visible_ci_ids)).all()
    
    for rel in relationships:
        if rel.target_ci_id in visible_ci_ids:
            mermaid_code += f'  C{rel.source_ci_id} -. {rel.rel_type.value} .-> C{rel.target_ci_id}\n'
            
    st_mermaid.st_mermaid(mermaid_code, height=700)
    with st.expander("Show Mermaid Source"):
        st.code(mermaid_code)
    
    db.close()
