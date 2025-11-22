# 07-scd-and-category-bundles.md

*Structured Context Documents & Category Bundles:

The Building Blocks of Engineered Context*

⸻

1. Introduction

Structured Context defines the operating environment that AI agents and human developers must share. But to make context workable—compact, deterministic, version-controlled, and machine-readable—it must be broken into consistent, minimal, composable units.

These units are called Structured Context Documents (SCDs).

SCDs are grouped into Category Bundles, which collectively form the Project Bundle—the complete operating contract for the system.

This chapter explains:
	•	What an SCD is
	•	Why SCDs are atomic
	•	What belongs inside an SCD
	•	What does not belong
	•	What Category Bundles are
	•	Which bundles are required
	•	How SCDs compose into a Project Bundle
	•	How this structure supports XP.ai and governance

Together, they form the backbone of the Structured Context Specification.

⸻

2. What Is an SCD (Structured Context Document)?

An SCD is the atomic unit of Structured Context.
It represents a single, focused, essential truth about the system.

Every SCD is:
	•	atomic — it covers one concept or one boundary
	•	compact — minimal text, no prose
	•	deterministic — unambiguous, explicit
	•	machine-readable — YAML or JSON
	•	schema-driven — validated against SCS schemas
	•	versioned — changes are traceable
	•	load-friendly — optimized for LLM context windows
	•	non-redundant — each truth is declared once

If Structured Context is the operating world,
SCDs are the particles that make up that world.

⸻

3. Why SCDs Must Be Atomic

Atomicity is essential because:
	•	Agents cannot reliably parse large, unstructured documents
	•	Updating a single truth should not require editing unrelated truths
	•	Governance agents must compare specific units across versions
	•	Category Bundles must compose cleanly
	•	Architecture must be decomposable
	•	Compliance must be enforceable
	•	Drift must be detectable
	•	RAG must be able to retrieve larger documents without polluting context
	•	Developers need clarity and maintainability

Atomic documents allow the world to be constructed from small, predictable pieces.

An SCD should answer exactly one question, such as:
	•	“What are the system’s external actors?”
	•	“What are the integration entry points?”
	•	“What is the system’s component model?”
	•	“What are the security invariants?”
	•	“What are the performance minimums?”
	•	“What are the domain definitions?”
	•	“What are the trust boundaries?”

If a document explains more than a single domain truth, it is almost certainly too large.

⸻

4. What Belongs in an SCD

Each SCD contains essential truths only, such as:
	•	key definitions
	•	invariants
	•	constraints
	•	core architecture boundaries
	•	interactions
	•	integration rules
	•	domain primitives
	•	non-negotiable requirements
	•	system relationships
	•	compliance or regulatory obligations (at a high level)
	•	simplified diagrams (Mermaid, textual) when necessary

An SCD must contain only information that agents must know to reason correctly.

Every line must contribute to:
	•	architecture
	•	safety
	•	alignment
	•	consistency
	•	compliance
	•	domain correctness

If it does not affect reasoning or system behavior,
it does not belong in an SCD.

⸻

5. What Does Not Belong in an SCD

SCDs are not documentation and must not include:
	•	long prose
	•	narrative explanations
	•	historical notes
	•	meeting summaries
	•	team discussions
	•	implementation details
	•	source code
	•	full diagrams
	•	logs or traces
	•	extended examples
	•	business cases
	•	opinionated commentary
	•	anything exceeding minimal context needs

All of these belong in:
	•	RAG
	•	design docs
	•	ADRs
	•	team notes
	•	Wiki pages
	•	Product documentation
	•	Story mapping tools

SCDs represent the current authoritative truth, not the reasoning that led to it.

⸻

6. The Structure of an SCD

All SCDs follow a consistent structure:

```yaml
scd:
  id: "architecture.system-context.v1"
  title: "System Context"
  category: "architecture"
  version: "1.0.0"
  description: "Defines external actors and system boundary."
  invariants:
    - "System boundary is fixed at service layer."
    - "External actors cannot bypass the API gateway."
  definitions:
    actors:
      - "Patient Mobile App"
      - "Identity Provider"
      - "EHR Upstream Systems"
  diagram: |
    graph TD
      App --> API_Gateway
      API_Gateway --> Core_Service
  references:
    - "nist.800-63.ial2"
```

Every SCD is:
	•	small
	•	direct
	•	structured
	•	intentional

This structure allows agents and validation tools to interpret context consistently.

⸻

7. What Is a Category Bundle?

A Category Bundle is a collection of related SCDs that represent a major dimension of the system.

Each Category Bundle answers a distinct set of questions.

Common bundles include:

Architecture
	•	system context
	•	integration map
	•	component model
	•	domain structure
	•	trust boundaries

Security
	•	identity model
	•	encryption invariants
	•	access boundaries
	•	risk constraints
	•	threat surfaces

Compliance
	•	regulatory obligations
	•	data residency rules
	•	audit requirements
	•	CHAI / HIPAA / GDPR high-level constraints

Domain
	•	core domain definitions
	•	terminology
	•	domain invariants
	•	entities and relationships (at a high level)

Integration
	•	upstream/downstream systems
	•	protocols
	•	SLAs
	•	data flow summaries

Performance
	•	latency constraints
	•	throughput minimums
	•	scalability assumptions
	•	availability targets

Quality Attributes
	•	reliability goals
	•	fault tolerance boundaries
	•	maintainability requirements

Purpose & Scope
	•	mission
	•	non-goals
	•	constraints
	•	lifecycle assumptions

Category Bundles ensure context is grouped logically and predictably.

⸻

8. The Project Bundle

The Project Bundle is the complete, composed set of SCDs representing the entire operating world of the system.

It is the final artifact of the Intent Phase and the primary input to:
	•	XP.ai teams
	•	multi-agent orchestration
	•	autonomic governance
	•	agent alignment
	•	architecture enforcement
	•	compliance checking
	•	onboarding of new team members

The Project Bundle is the operating contract for the system.

It includes:
	•	required architecture SCDs
	•	required category bundles
	•	optional bundles (as needed)
	•	derived context from standards
	•	optional enhancements for specific needs

The Project Bundle must be compact enough to fit comfortably in the context window (target: ~25–35% use).

⸻

9. How SCDs Compose into a Project Bundle

SCDs → Category Bundles → Project Bundle → Structured Context Window

Composition must be:
	•	deterministic
	•	validated
	•	schema-driven
	•	predictable across versions
	•	free of redundancy
	•	safe for merging and updating

When changes occur:
	•	the affected SCDs update
	•	the bundle revalidates
	•	governance agents detect differences
	•	the world changes in controlled increments

SCDs provide the granularity required for version control and drift detection.

⸻

10. Why This Structure Matters

This layered structure enables:
	•	multi-agent consistency
	•	predictable behavior
	•	stable architecture
	•	accurate code generation
	•	meaningful testing
	•	governance automation
	•	compliance alignment
	•	onboarding clarity

Without SCDs and Category Bundles:
	•	context would be too large,
	•	too vague,
	•	too inconsistent,
	•	too difficult to maintain,
	•	too noisy for agents,
	•	and too fragile for governance.

SCDs provide the engineering precision needed for a compact, reliable operating world.

⸻

11. Summary

SCDs and Category Bundles are the building blocks of Structured Context. Together, they form the scaffolding of the engineered world that AI agents and human developers inhabit.
	•	SCDs are atomic truths.
	•	Category Bundles group related truths.
	•	The Project Bundle composes all truths.
	•	The meta-model ensures consistency.
	•	XP.ai consumes these truths.
	•	Governance systems enforce them.

The result is an engineered operating environment—
the world in which AI-native development becomes safe, reliable, and aligned.

⸻

