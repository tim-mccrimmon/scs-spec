README.md

Structured Context Specification (SCS)

An Open Standard for AI-Native Context Engineering

⸻

1. What Is the Structured Context Specification?

The Structured Context Specification (SCS) defines an open, machine-readable standard for expressing the minimal, authoritative operating environment that AI agents and human developers need in order to reason, build, test, and govern software systems.

SCS provides consistent formats, schemas, and guidelines for expressing Structured Context—compact, deterministic YAML/JSON bundles that fit directly into an LLM’s context window and serve as the project’s “always-loaded world.”

⸻

2. Why SCS Exists — The White-Room Problem

When an AI agent begins a task, it enters the equivalent of a blank white space—
no architecture, no constraints, no integrations, no compliance rules, no purpose.

Like Neo stepping into the white construct in The Matrix, the agent has no world to operate within unless we create one.

Structured Context loads that world.

It defines the purpose, boundaries, actors, components, constraints, quality attributes, and non-negotiables that form the system’s operating environment.
This operating world must be:
	•	compact
	•	deterministic
	•	machine-readable
	•	versioned
	•	always present in the context window

SCS describes exactly how that world is structured.

⸻

3. Structured Context: The Operating Environment

Structured Context is the compact, precisely defined set of truths that must always be present in an LLM’s working memory for agents to operate safely and consistently.

It includes high-level architecture, integrations, constraints, domain rules, quality attributes, and compliance expectations—expressed in concise YAML/JSON and minimal Mermaid diagrams.

Structured Context is designed to consume 25–35% of the available context window, leaving room for conversation, instructions, task details, and chain-of-thought.

👉 Learn more:
docs/01-structured-context.md

⸻

4. Context Engineering: Engineering the Operating World

Context Engineering is the discipline of designing and structuring the world that AI agents and developers build within.

It defines:
	•	project intent and purpose
	•	boundaries and constraints
	•	architecture and integrations
	•	non-negotiable rules
	•	compliance and governance parameters

Context Engineering uses Structured Context as its primary output.
SCS defines the standard for expressing it.

👉 Learn more:
docs/02-context-engineering.md

⸻

5. Why Not Just Use RAG?

RAG is excellent for retrieving large, historical, or reference information.
But RAG is:
	•	slow
	•	expensive
	•	probabilistic
	•	inconsistent
	•	non-deterministic across agents

And therefore not suitable for defining the operating environment agents must load on every prompt.

System context must be:
	•	instantaneous
	•	deterministic
	•	always-present
	•	compact
	•	schema-driven
	•	version-controlled

This is why Structured Context belongs in the context window, and why SCS exists.

👉 Learn more:
docs/03-context-vs-rag.md

⸻

6. The Intent Phase: Worldbuilding

In AI-native development, the Intent Phase becomes the world-building phase—the work of engineering the environment that development will take place in.

Leaders (CTO, CSO, Compliance, Architecture) play a crucial role here.
They help define the essential truths that become Structured Context.

👉 Learn more:
docs/05-intent-phase-worldbuilding.md

⸻

7. The SCS Meta-Model (Light Overview)

The SCS specification is organized using a layered meta-model:
	•	Meta Layer – universal categories and rules
	•	Standards Layer – reusable compliance/regulatory/context requirements
	•	Project Layer – the world for a specific solution
	•	Category Bundles – organized collections of SCDs
	•	SCDs (Structured Context Documents) – atomic units of context

This structure ensures consistency, interoperability, and agent comprehension.

👉 Learn more:
docs/06-meta-model-overview.md

⸻

8. SCDs & Category Bundles

An SCD (Structured Context Document) is the smallest unit of Structured Context—an atomic, machine-readable definition of some aspect of the operating world.

SCDs are grouped into Category Bundles (Architecture, Security, Domain, Integration, Performance, Compliance, etc.).
Category Bundles roll up into a Project Bundle—the contract for the system.

👉 Learn more:
docs/07-scd-and-category-bundles.md
👉 See examples:
examples/minimal-project/

⸻

9. XP.ai & Autonomic Governance

Structured Context is the foundation for XP.ai (hybrid human + AI development teams).
It provides the world all agents work within.

It also enables Autonomic Governance:
	•	continuous compliance
	•	architectural drift detection
	•	standards alignment
	•	automated checklists
	•	multi-agent consistency

👉 Learn more:
docs/08-xp-ai-and-governance.md

⸻

10. Repository Structure

```bash
structured-context-spec/
├─ README.md
├─ docs/
├─ spec/
├─ examples/
├─ community/
└─ tools/
```

⸻

11. Quickstart

Clone the repo and explore the minimal example:

```bash
git clone https://github.com/your-org/structured-context-spec.git
cd structured-context-spec/examples/minimal-project
```

See a complete project bundle with SCDs:

```bash
examples/minimal-project/
├─ project-bundle.yaml
└─ categories/
   ├─ architecture/
   ├─ security/
   └─ ...
```

Validate an SCD (example tool):

```bash
python tools/validate-scd.py examples/minimal-project/categories/architecture/system-context.scd.yaml
```

⸻

12. Contributing

We welcome contributors from architecture, AI, security, compliance, standards bodies, and the broader engineering community.

Start here:

👉 community/CONTRIBUTING.md
👉 GitHub Discussions (Open to All)

⸻

13. Roadmap

See upcoming releases, discussion topics, and open tasks:

👉 community/ROADMAP.md

⸻

14. License

Apache-2.0
(Open, permissive, enterprise-friendly.)

⸻

