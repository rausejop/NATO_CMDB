import streamlit as st
from database.db_manager import SessionLocal
from database.models import ConfigurationItem, Enclave, Location, Network, CIStatus

def show_dashboard():
    db = SessionLocal()
    
    st.subheader("Infrastructure Summary")
    
    # Metrics
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total CIs", db.query(ConfigurationItem).count())
    col2.metric("Active Enclaves", db.query(Enclave).count())
    col3.metric("Locations", db.query(Location).count())
    col4.metric("Networks", db.query(Network).count())
    
    # Breakdown by Status
    st.divider()
    st.write("### CI Status Breakdown")
    status_counts = {}
    for status in CIStatus:
        status_counts[status.value] = db.query(ConfigurationItem).filter_by(status=status).count()
    
    st.bar_chart(status_counts)
    
    # Critical Infrastructure Alerts (ITIL)
    st.divider()
    st.write("### ⚠️ Service Health Notifications")
    critical_cis = db.query(ConfigurationItem).filter_by(status=CIStatus.UNDER_REPAIR).all()
    if critical_cis:
        for ci in critical_cis:
            st.error(f"CI {ci.hostname} is UNDER REPAIR at {ci.network.enclave.location.name}")
    else:
        st.success("All systems operational. No critical incidents reported.")
    
    db.close()
