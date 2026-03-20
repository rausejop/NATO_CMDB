# P2: Technical & Configuration Management

## 1. Systems Engineering Management Plan (SEMP)
The project utilizes a modular architecture based on Streamlit (Frontend) and SQLAlchemy ORM (Data Layer). The methodology focuses on high observability and secure data handling.

## 2. Configuration Management Plan (CMP)
### Configuration Items (CIs)
CIs are managed in a hierarchical structure to ensure dependency tracking:
- **Zone:** Geographic region.
- **Country:** Member or partner nation.
- **Location:** Operational site (e.g., Brunssum).
- **Enclave:** Security boundary with 3-letter code (e.g., HB1, HB2 for NR; HB3, HB4 for NS).
- **Network:** VLAN/Subnet (3 standard subnets per enclave).
- **Device:** Hardware/Virtual asset following the `NSCYSHB1P001` convention.

### Baselines
- **Functional Baseline:** Defined in the `MASTER_PROMPT.txt`.
- **Product Baseline:** Final code repository with P1-P7 silos.

## 3. ITIL v4 Service Design
The tool is designed to support the **Service Asset and Configuration Management (SACM)** practice. 

### Criticality and Status
Each CI tracks:
- **Status:** Active, Planned, Under Repair, Decommissioned.
- **Impact Relationships:** N:M dependencies between technical assets for impact analysis during incidents.

## 4. Risk Management (Technical)
- Utilization of `loguru` for granular event tracing and incident forensics.
- Validation of path safety using `pathlib` to prevent injection vulnerabilities.
