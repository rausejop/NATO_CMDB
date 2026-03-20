# CONFIANZA23 Export Standards

## Context
You are a Python data developer agent working inside Streamlit.
For all applications generated for "CONFIANZA23 Inteligencia y Seguridad, S.L." handling tabular data, you must empower the business side to export analysis strictly to specific serialized formats.

## Preconditions
1. Final results exist in memory as a `pandas.DataFrame`.
2. Streamlit is active.

## Constraints & Rules
- **MUST** export all processed DataFrame outputs to the user in a minimum of four standard data formats: CSV, Markdown, XML, and JSON.
- **MUST** place export buttons horizontally aligned on a single Streamlit UI row.
- **MUST** enforce the file naming convention, utilizing an application-relevant descriptive string normalized with lowercase terminology and underscores.
- **NEVER** use spaces in XML export column names.

## Postconditions
- Buttons display explicitly as intended, allowing simultaneous generation and delivery of `.csv`, `.md`, `.xml`, and `.json`.

## Implementation Details

### 1. Data Preparation Logic
Convert your base DataFrame into the byte strings required by the Streamlit download widget.
Assume DataFrame variable is `df`:

```python
# 1. Export CSV
csv = df.to_csv(index=False).encode('utf-8')

# 2. Export Markdown (MD)
try:
    md = df.to_markdown(index=False).encode('utf-8')
except ImportError:
    # Graceful degradation fallback if the tabulate package is missing
    md = df.to_csv(index=False, sep="|").encode('utf-8')

# 3. Export XML
# Mandatory constraint: XML column names strictly forbid spaces.
xml_df = df.copy()
xml_df.columns = [str(c).replace(' ', '_') for c in xml_df.columns]
xml = xml_df.to_xml(index=False).encode('utf-8')

# 4. Export JSON
json_data = df.to_json(orient='records', indent=4).encode('utf-8')
```

### 2. Streamlit Button Rendering (Interactive UI)
Align the download components strictly side-by-side using four column containers to conserve vertical real estate.

```python
# Create an evenly distributed layout 
exp_col1, exp_col2, exp_col3, exp_col4 = st.columns(4)

# Define contextual names mapping the tool identity
file_base_identifier = "application_domain_report" # e.g., sbom_audit_report

# Hook buttons
exp_col1.download_button(label="Export CSV", data=csv, file_name=f"{file_base_identifier}.csv", mime="text/csv")
exp_col2.download_button(label="Export MD", data=md, file_name=f"{file_base_identifier}.md", mime="text/markdown")
exp_col3.download_button(label="Export XML", data=xml, file_name=f"{file_base_identifier}.xml", mime="application/xml")
exp_col4.download_button(label="Export JSON", data=json_data, file_name=f"{file_base_identifier}.json", mime="application/json")
```
