import streamlit as st
import pandas as pd
from loguru import logger
from database.db_manager import SessionLocal
from database.models import Zone, Country, Location, Enclave, Network, ConfigurationItem, Relationship, RelationshipType, Accreditation, CIStatus

def show_inventory():
    st.subheader("📦 Configuration Items (CIs)")
    
    db = SessionLocal()
    
    # 1. CI Creation Form
    with st.expander("➕ Add New Configuration Item"):
        # Hierarchical Selection
        zones = db.query(Zone).all()
        selected_zone_name = st.selectbox("Select Zone", [z.name for z in zones], key="zone_sel")
        
        selected_zone = db.query(Zone).filter_by(name=selected_zone_name).first()
        countries = db.query(Country).filter_by(zone_id=selected_zone.id).all()
        selected_country_name = st.selectbox("Select Country", [c.name for c in countries], key="country_sel")
        
        selected_country = db.query(Country).filter_by(name=selected_country_name).first()
        locations = db.query(Location).filter_by(country_id=selected_country.id).all()
        if not locations:
            st.warning("No locations found in this country. Create one first.")
            # Simple form for location if none
            with st.form("new_location"):
                loc_name = st.text_input("New Location Name")
                lat = st.number_input("Lat", value=0.0)
                lon = st.number_input("Lon", value=0.0)
                if st.form_submit_button("Add Location"):
                    new_loc = Location(name=loc_name, latitude=lat, longitude=lon, country_id=selected_country.id)
                    db.add(new_loc)
                    db.flush()
                    
                    # Auto-generate default enclave and network
                    new_enc = Enclave(name="Standard Enclave", accreditation=Accreditation.NU_NR, location_id=new_loc.id)
                    db.add(new_enc)
                    db.flush()
                    
                    new_net = Network(name="Default MGMT", vlan="1", subnet="192.168.1.0/24", enclave_id=new_enc.id)
                    db.add(new_net)
                    
                    db.commit()
                    st.success(f"Location {loc_name} created with default Enclave and Network.")
                    st.rerun()
        else:
            selected_location_name = st.selectbox("Select Location", [l.name for l in locations])
            selected_location = db.query(Location).filter_by(name=selected_location_name, country_id=selected_country.id).first()
            
            enclaves = db.query(Enclave).filter_by(location_id=selected_location.id).all()
            if not enclaves:
                st.warning("No enclaves found. Add an enclave to this location.")
                with st.form("new_enclave"):
                    enc_name = st.text_input("Enclave Name (e.g. NATO HQ)")
                    acc = st.selectbox("Accreditation", [a.name for a in Accreditation])
                    if st.form_submit_button("Add Enclave"):
                        new_enc = Enclave(name=enc_name, accreditation=Accreditation[acc], location_id=selected_location.id)
                        db.add(new_enc)
                        db.commit()
                        st.rerun()
            else:
                selected_enclave_name = st.selectbox("Select Enclave", [e.name for e in enclaves])
                selected_enclave = db.query(Enclave).filter_by(name=selected_enclave_name, location_id=selected_location.id).first()
                
                networks = db.query(Network).filter_by(enclave_id=selected_enclave.id).all()
                if not networks:
                    st.warning("No networks found. Add a network first.")
                    with st.form("new_network"):
                        net_name = st.text_input("Network Name (e.g. Core SW)")
                        vlan = st.text_input("VLAN ID")
                        if st.form_submit_button("Add Network"):
                            new_net = Network(name=net_name, vlan=vlan, enclave_id=selected_enclave.id)
                            db.add(new_net)
                            db.commit()
                            st.rerun()
                else:
                    selected_network_name = st.selectbox("Select Network", [n.name for n in networks])
                    selected_network = db.query(Network).filter_by(name=selected_network_name, enclave_id=selected_enclave.id).first()
                    
                    with st.form("new_ci_form"):
                        st.write("### CI Details")
                        hostname = st.text_input("Hostname")
                        device_type = st.selectbox("Device Type", ["Switch", "Router", "Firewall", "Server", "Laptop", "Desktop"])
                        status = st.selectbox("Status", [s.value for s in CIStatus])
                        
                        col1, col2 = st.columns(2)
                        with col1:
                            cpu = st.text_input("CPU Model")
                            ram = st.number_input("RAM (GB)", min_value=0)
                            ip = st.text_input("IP Address")
                        with col2:
                            disk = st.number_input("Disk (GB)", min_value=0)
                            os = st.text_input("Operating System")
                            mac = st.text_input("MAC Address")
                        
                        if st.form_submit_button("Add Configuration Item"):
                            new_ci = ConfigurationItem(
                                hostname=hostname, device_type=device_type, status=CIStatus(status),
                                cpu=cpu, ram_gb=ram, disk_gb=disk, ip_address=ip, mac_address=mac,
                                os=os, network_id=selected_network.id
                            )
                            db.add(new_ci)
                            db.commit()
                            st.success(f"CI {hostname} added successfully.")
                            st.rerun()
    
    # 2. Relationship Management (N:M)
    st.divider()
    with st.expander("🔗 Manage CI Relationships"):
        st.write("### Link configuration items (Dependencies)")
        cis = db.query(ConfigurationItem).all()
        if len(cis) < 2:
            st.info("Add at least 2 CIs to create relationships.")
        else:
            ci_options = {f"{ci.hostname} ({ci.device_type})": ci.id for ci in cis}
            col1, col2, col3 = st.columns(3)
            with col1:
                source_ci_id = st.selectbox("Source CI (Depends)", list(ci_options.keys()))
            with col2:
                rel_type = st.selectbox("Relationship", [r.value for r in RelationshipType])
            with col3:
                target_ci_id = st.selectbox("Target CI (On)", list(ci_options.keys()))
            
            if st.button("Create Relationship"):
                if source_ci_id == target_ci_id:
                    st.error("A CI cannot have a relationship with itself.")
                else:
                    new_rel = Relationship(
                        source_ci_id=ci_options[source_ci_id],
                        target_ci_id=ci_options[target_ci_id],
                        rel_type=RelationshipType(rel_type)
                    )
                    db.add(new_rel)
                    db.commit()
                    logger.info(f"Relationship created: {source_ci_id} -> {rel_type} -> {target_ci_id}")
                    st.success("Relationship documented.")
                    st.rerun()

    # 3. CI List Table
    st.divider()
    st.subheader("📊 Configuration Items Inventory")
    
    # Advanced Filtering
    col1, col2, col3 = st.columns(3)
    with col1:
        f_country = st.selectbox("Filter Country", ["All"] + [c.name for c in db.query(Country).all()], key="f_c")
    with col2:
        f_location = st.selectbox("Filter Location", ["All"] + [l.name for l in db.query(Location).all()], key="f_l")
    with col3:
        f_enclave = st.selectbox("Filter Enclave", ["All"] + [e.name for e in db.query(Enclave).all()], key="f_e")
    
    query = db.query(ConfigurationItem).join(Network).join(Enclave).join(Location).join(Country)
    if f_country != "All":
        query = query.filter(Country.name == f_country)
    if f_location != "All":
        query = query.filter(Location.name == f_location)
    if f_enclave != "All":
        query = query.filter(Enclave.name == f_enclave)
        
    cis = query.all()
    if cis:
        data = []
        for ci in cis:
            data.append({
                "Hostname": ci.hostname,
                "Type": ci.device_type,
                "Status": ci.status.value,
                "Enclave": ci.network.enclave.name,
                "Location": ci.network.enclave.location.name,
                "Country": ci.network.enclave.location.country.name,
                "IP": ci.ip_address,
                "OS": ci.os
            })
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No matching configuration items found.")
    
    db.close()
