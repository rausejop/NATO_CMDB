import streamlit as st
import folium
from streamlit_folium import st_folium
from database.db_manager import SessionLocal
from database.models import Location, Enclave

def show_map():
    st.subheader("🌍 NATO Enclave Global Distribution")
    
    db = SessionLocal()
    locations = db.query(Location).all()
    
    if not locations:
        st.info("No locations found. Add some in Inventory Management.")
        return

    # Create map centered at Europe/Atlantic
    m = folium.Map(location=[45, 0], zoom_start=2)
    
    for loc in locations:
        enclaves = db.query(Enclave).filter_by(location_id=loc.id).all()
        enclave_list = ", ".join([e.name for e in enclaves])
        
        popup_text = f"<b>{loc.name}</b><br>Country: {loc.country.name}<br>Enclaves: {enclave_list or 'None'}"
        
        folium.Marker(
            [loc.latitude, loc.longitude],
            popup=popup_text,
            tooltip=loc.name,
            icon=folium.Icon(color="blue", icon="info-sign")
        ).add_to(m)
        
    st_folium(m, width=1000, height=600)
    
    db.close()
