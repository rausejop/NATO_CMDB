# P5: System Architecture & Design Definition

## 1. System Architecture Document (SAD)
The application follows a **Modular Monolith** pattern:
- **Data Layer:** SQLAlchemy ORM models representing the NATO asset hierarchy.
- **Business Logic:** CRUD and relationship processing handled within modular view scripts.
- **Presentation Layer:** Streamlit-powered interactive interface with custom CONFIANZA23 CSS.

## 2. Design Definition (DDD)
The domain is modelled after ITIL v4 SACM.
- **Aggregates:** Location (Zone/Country/Site), Enclave (Accreditation/Network), Asset (CI/Relationship).
- **Services:** Export Engine, Logic Mapping, Geospatial Rendering.

## 3. Architectural Decision Records (ADRs)
- **ADR-001: Choice of Streamlit.** Selected for rapid prototyping and high interactivity; tested with 15k+ records using DataFrame virtualization.
- **ADR-002: Local SQLite.** chosen over enterprise DBs to maintain NATO enclave isolation; robust against 100MB+ metadata footprints.
- **ADR-003: Mermaid.js integration.** Utilized for dynamic relationship mapping; optimized for enclave-level views (~150 nodes).
- **ADR-004: Standardized Naming Logic.** Implementation of `NSCYSHB1P001` hostname format to ensure unique asset identification across decentralized enclaves.

## 4. Database Schema (P5-DB)
Refer to the [ER Diagram](file:///c:/_CONFIANZA23/PRODUCTOS/31_ENCLAVE/README.md#database-architecture-er-diagram) for detailed attribute mapping and relationship cardinality.
