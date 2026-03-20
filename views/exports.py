import streamlit as st
import pandas as pd
import json
import dicttoxml
from database.db_manager import SessionLocal
from database.models import ConfigurationItem, Network, Enclave, Location

def show_exports():
    st.subheader("📊 Data Export & Reporting")
    
    db = SessionLocal()
    cis = db.query(ConfigurationItem).all()
    
    if not cis:
        st.info("No data available to export.")
        return

    # Data transformation for export
    data_list = []
    for ci in cis:
        data_list.append({
            "hostname": ci.hostname,
            "device_type": ci.device_type,
            "status": ci.status.value,
            "network": ci.network.name,
            "vlan": ci.network.vlan,
            "enclave": ci.network.enclave.name,
            "accreditation": ci.network.enclave.accreditation.value,
            "location": ci.network.enclave.location.name,
            "ip": ci.ip_address,
            "cpu": ci.cpu,
            "ram_gb": ci.ram_gb,
            "disk_gb": ci.disk_gb,
            "os": ci.os
        })
    df = pd.DataFrame(data_list)
    
    st.write("### Filter Data")
    type_filter = st.multiselect("Filter by Type", df['device_type'].unique(), default=df['device_type'].unique())
    status_filter = st.multiselect("Filter by Status", df['status'].unique(), default=df['status'].unique())
    
    filtered_df = df[(df['device_type'].isin(type_filter)) & (df['status'].isin(status_filter))]
    st.dataframe(filtered_df, use_container_width=True)
    
    st.divider()
    st.write("### Export Formats")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # CSV
    csv_data = filtered_df.to_csv(index=False).encode('utf-8')
    col1.download_button("📥 CSV", csv_data, "nato_cmdb_export.csv", "text/csv")
    
    # JSON
    json_data = json.dumps(filtered_df.to_dict(orient='records'), indent=2)
    col2.download_button("📥 JSON", json_data, "nato_cmdb_export.json", "application/json")
    
    # XML
    xml_data = dicttoxml.dicttoxml(filtered_df.to_dict(orient='records'), custom_root='NATO_CMDB', attr_type=False)
    col3.download_button("📥 XML", xml_data, "nato_cmdb_export.xml", "application/xml")
    
    # Markdown
    md_data = filtered_df.to_markdown(index=False)
    col4.download_button("📥 MD", md_data, "nato_cmdb_export.md", "text/markdown")
    
    # TXT
    txt_data = filtered_df.to_string(index=False)
    col5.download_button("📥 TXT", txt_data, "nato_cmdb_export.txt", "text/plain")
    
    db.close()
