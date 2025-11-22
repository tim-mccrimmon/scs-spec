# 09-faq.md

Frequently Asked Questions (FAQ)

Structured Context Specification (SCS)

⸻

1. What is Structured Context?

Structured Context is a compact, deterministic, machine-readable representation of the essential truths of a system—its purpose, boundaries, constraints, architecture, domain definitions, and non-negotiable rules.

It is not documentation.
It is the operating world that AI agents and human developers must load before reasoning about the system.

It is designed to fit comfortably inside the LLM context window (~25–35%), enabling fast, predictable, aligned reasoning.

⸻

2. How is Structured Context different from documentation?

Documentation is:
	•	narrative
	•	descriptive
	•	long-form
	•	historical
	•	explanatory

Structured Context is:
	•	declarative
	•	minimal
	•	atomic
	•	structured
	•	deterministic
	•	written for machines

Documentation explains what and why.
Structured Context encodes what must be true.

⸻

3. Why not use RAG for system context?

Because RAG is probabilistic, while context must be deterministic.

RAG is excellent for retrieving long-form materials, but it cannot:
	•	guarantee retrieval
	•	ensure consistency
	•	enforce invariants
	•	provide compact truth
	•	synchronize multiple agents
	•	eliminate noise and ambiguity

System context must always be present in the LLM’s working memory.
RAG cannot provide that guarantee.

Structured Context must live inside the context window.

RAG is for extended reference.
Structured Context is for reasoning.

⸻

4. What is an SCD?

An SCD (Structured Context Document) is the atomic unit of Structured Context.

Each SCD:
	•	defines one essential truth
	•	is minimal and compact
	•	is machine-readable (YAML/JSON)
	•	fits into one Category Bundle
	•	is validated via schema
	•	is version-controlled
	•	contains exactly the content required for predictable agent reasoning

Think of SCDs as the “atoms” of the system’s world.

⸻

5. What is a Category Bundle?

A Category Bundle is a collection of SCDs grouped by purpose, such as:
	•	Architecture
	•	Security
	•	Integration
	•	Domain
	•	Compliance
	•	Performance
	•	Quality Attributes
	•	Scope & Purpose
	•	Risk

Category Bundles help structure context into predictable logical segments.

⸻

6. What is the Project Bundle?

The Project Bundle is the composed set of Category Bundles that form the complete engineered world of the system.

It is the primary input to:
	•	XP.ai development
	•	Multi-agent orchestration
	•	Autonomic governance
	•	Architecture enforcement
	•	Compliance automation

The Project Bundle is the operating contract of the system.

⸻

7. Who creates Structured Context?

Structured Context is created during the Intent Phase by:
	•	architects
	•	security officers
	•	domain experts
	•	product owners
	•	developers
	•	AI agent designers
	•	compliance teams

This is a multi-disciplinary effort, because system context spans business, domain, architectural, and compliance boundaries.

⸻

8. When is Structured Context created?

During the Intent Phase, before development begins.

This is where the world of the system is engineered:
	•	purpose
	•	scope
	•	boundaries
	•	architecture
	•	domain models
	•	integration points
	•	constraints
	•	risks
	•	compliance requirements

Once defined, it becomes the working environment for XP.ai teams.

⸻

9. Why is context engineering necessary?

Before AI, humans carried system context implicitly:
	•	in memory
	•	in conversations
	•	in Slack threads
	•	in shared intuition
	•	in tribal knowledge

AI agents do not have implicit understanding.
They require explicit, structured, engineered context.

Without context engineering, AI agents hallucinate architecture and violate boundaries.

With it, they act predictably and correctly.

⸻

10. How does Structured Context support XP.ai?

XP.ai (hybrid human + AI development) relies on:
	•	multiple agents
	•	specialized roles
	•	coordination
	•	shared understanding

Structured Context ensures all agents:
	•	load the same world
	•	follow the same invariants
	•	respect the same constraints
	•	collaborate consistently
	•	maintain architecture and compliance

Without Structured Context, XP.ai collapses.
With Structured Context, XP.ai becomes powerful.

⸻

11. How does Structured Context support autonomic governance?

Autonomic governance uses AI agents to:
	•	monitor system drift
	•	check architecture
	•	validate compliance
	•	enforce boundaries
	•	generate compliance checklists
	•	analyze change impact

These agents compare:
	•	the intended world (Structured Context)
	•	with the actual world (implementation + runtime)

This is only possible when system intent is expressed in structured, machine-readable form.

⸻

12. How small does Structured Context need to be?

The goal is to occupy 25–35% of the LLM context window.

This ensures:
	•	enough room remains for conversation
	•	task-specific data can be included
	•	additional memory can augment the world

Structured Context must remain compact, distilled, essential.

More information belongs in RAG, documentation, or external resources.

⸻

13. What formats are allowed?

Allowed:
	•	YAML
	•	JSON
	•	Lightweight Mermaid diagrams (with strict sizing limits)

Not allowed:
	•	Markdown prose
	•	PDFs
	•	Word documents
	•	Full technical diagrams
	•	Screenshots
	•	Images
	•	Tables with excessive narrative

The format must be compact, deterministic, and easy for machines to parse.

⸻

14. Can SCDs include diagrams?

Yes—minimal Mermaid diagrams are allowed when they provide:
	•	structural clarity
	•	system boundaries
	•	component relationships
	•	integration flows

Diagrams must be:
	•	minimal
	•	textual
	•	compact
	•	free of extraneous detail

Large or heavily visual diagrams belong in design docs, not Structured Context.

⸻

15. How are SCDs versioned?

Every SCD includes:
	•	an ID
	•	a semantic version
	•	a category
	•	a change summary
	•	references (e.g., to standards or other SCDs)

Version control allows:
	•	governance agents to detect drift
	•	teams to review changes easily
	•	project-level context to remain stable
	•	future tooling to support semantic diffs

⸻

16. Is Structured Context intended to replace architecture documents?

No—Structured Context replaces the minimum set of operating definitions needed by agents.

Architectural documents such as:
	•	detailed diagrams
	•	rationale
	•	trade-off studies
	•	ADRs
	•	RFCs
	•	sequence diagrams

…still exist, but live outside the context window.

Structured Context provides the distilled operating truth;
architecture documents provide depth and reasoning.

⸻

17. How does Structured Context scale to large systems?

Through:
	•	atomic SCDs
	•	Category Bundles
	•	the SCS Meta-Model
	•	compact constraints
	•	hierarchical composition

Large systems simply include more SCDs, but each remains minimal and isolated.

⸻

18. How does governance handle change?

When something changes:
	•	update the relevant SCD
	•	revalidate the Category Bundle
	•	recompose the Project Bundle
	•	governance agents detect and report differences
	•	the updated world is loaded for all agents

This creates a controlled, traceable evolution of system intent.

⸻

19. Can organizations create their own Category Bundles?

Yes.

SCS explicitly supports:
	•	custom bundles
	•	organization-specific standards
	•	internal frameworks
	•	reusable compliance bundles
	•	sector-specific domain models

These can be shared, versioned, and reused across projects.

⸻

20. What is the long-term vision for SCS?

SCS aims to standardize:
	•	how system context is represented
	•	how AI-native development operates
	•	how governance becomes machine-verifiable
	•	how standards bodies deliver their requirements
	•	how regulated industries adopt AI safely
	•	how multi-agent teams remain aligned
	•	how complex systems maintain integrity over time

The long-term goal is interoperability across:
	•	organizations
	•	industries
	•	tooling ecosystems
	•	regulatory frameworks

SCS is a foundation for the AI-native future of software engineering.

⸻

