# P3: Concept of Operations (ConOps)

## 1. Operational Framework
The NATO Enclave CMDB Manager is designed to provide a unified topographic and logical view of secure infrastructure. 

### User Groups:
- **IT Service Desk:** Use the dashboard for monitoring asset health and identifying under-repair items.
- **Network Architects:** Utilize relationship mapping for impact analysis and planning infrastructure changes.
- **Security Auditors:** Access CMDB data to verify accreditation levels and asset locations.

## 2. Operational Scenarios
- **Scenario A: Incident Impact.** When a core network switch fails (e.g., `NR-CYS-HB1-SW-01`), the architect uses the Relationship Mapping view to identify all dependent assets following the `NR-CYS-HB1-*-*` pattern.
- **Scenario B: Accreditation Audit.** The auditor filters the export center for all `NSCYSHB3*` assets to verify their physical location and accreditation compliance in the Secret Enclave.

## 3. Stakeholder Requirements (StRS)
- **R3.01:** The system shall maintain persistent storage of all assets via a local database.
- **R3.02:** The interface shall allow for hierarchical navigation: Zone → Country → Location → Enclave → Network → CI.
- **R3.03:** The visualization engine shall represent 1:N and N:M relationships clearly.
