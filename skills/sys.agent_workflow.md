# Comprehensive AI Agent Workflow

Detailed end-to-end workflow for designing, building, and maintaining AI agents at CONFIANZA23.

## Workflow Phases

- **Phase 0: Mindset Shift**: Agents are goal-oriented systems with reasoning, tools, and memory.
- **Phase 1: Purpose & Scope**: Define exact job, user types, use cases, and success criteria (TRL alignment).
- **Phase 2: Agent Behavior**: Define persona, goals, system prompts, thinking structure, and few-shot examples.
- **Phase 3: LLM Strategy**: Choose model by task type (Reasoning vs. Fast). Fallback strategies for SLA.
- **Phase 4: Tooling & Integrations**: Design function-calling schemas, MCP servers, and specialist agents.
- **Phase 5: Basic Memory**: Working memory, episodic conversation history, and RAG retrieval.
- **Phase 6: Orchestration**: State management, triggers, and retry logic for async tool calls.
- **Phase 7: Advanced Memory**: Persistent storage with confidence thresholds to prevent pollution.
- **Phase 8: UI & Delivery**: UX flow design with Human-in-the-Loop (HITL) for high-risk actions.
- **Phase 9: Testing & Evals**: Evaluation datasets to track accuracy, hallucinations, and tool success.
- **Phase 10: Safety & Governance**: Defenses against prompt injection and least-privilege tool permissions.
- **Phase 11: Deployment & Iteration**: Observability, staging environments, and real-time monitoring.

## Token Saver Mode (REQ4.01)
- Ignore `/docs/` during coding sessions.
- Analyze only the active module delta.
- Avoid explanatory prose unless solicited.
