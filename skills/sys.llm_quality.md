# LLM Validation & Quality (AQS Framework)

Standards for measuring and ensuring the quality of AI agent outputs.

## Agent Quality Score (AQS)
- **Rubrics**: Evaluate Truthfulness, Safety (GRC), and Goal Alignment.
- **Metric**: Use F-beta (beta=2) to prioritize **Recall** over Precision.
- **Thresholds**:
    - **AQS > 0.50**: Private Beta release.
    - **AQS > 0.80**: Production-ready.

## Discovery & Testing
- **Synthetic Frontier Dataset**: Generate 72+ test cases covering User Profiles, Flow, Multimodality, and Features if real data is absent.
- **LLM-as-a-Judge**: Automated scoring using strict evaluation rubrics.
- **Coverage Analysis**: Map results across all 4 dimensions to identify reasoning blind spots.
