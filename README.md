# Structured Context Specification (SCS)

**Making AI safe for production software development.**

---

## The Problem

AI has entered the software development cycle — but without structured context, it's **ungovernable, untraceable, and legally indefensible**.

**Without structured context:**
- ❌ You can't prove what context the AI saw when generating code
- ❌ You can't demonstrate compliance with HIPAA, SOC2, or other regulations
- ❌ Multiple AI tools (for dev, security, architecture, compliance) produce conflicting outputs
- ❌ No audit trail connecting decisions to humans
- ❌ AI-generated code becomes a liability in regulated environments

**In regulated industries (healthcare, finance, government), this makes AI essentially unusable in production systems that matter.**

---

## The Solution

**The Structured Context Specification (SCS)** provides a machine-readable framework for capturing, organizing, and governing all system context in a way that is:

- **Human-readable** and reviewable
- **Machine-readable** for AI and tools
- **Versionable** in git
- **Enforceable** through validation
- **Governable** through autonomic agents
- **Legally defensible** with complete provenance

SCS makes **context a first-class, version-controlled artifact** — not ephemeral input that disappears after use.

---

## Why This Matters

### 1. Legal Protection & Indemnification

**Without SCS**: "The AI generated it based on... um... a prompt?"

**With SCS**: "The AI operated within documented constraints (scd:meta:architecture), satisfied HIPAA requirements (scd:standards:hipaa-164.312), and was validated against our security contract. Here's the provenance record showing human approval."

### 2. Compliance on Launch Day

**Traditional approach**: Ship product → Start compliance work (6-12 months) → Maybe get certified

**With SCS**: Continuous compliance validation during development → **Certified on launch day**

**Economic impact**: Saves millions in post-facto compliance work and delayed market entry.

### 3. Multi-AI Coordination

As teams add AI assistants for development, security, architecture, and compliance, coordination becomes chaos without shared context.

**SCS provides**: A single source of truth that all AI tools consume, preventing conflicts and ensuring alignment.

### 4. Autonomic Governance

**Autonomic governance agents** (operating over your SCD bundle) can:
- Continuously validate compliance with standards
- Detect missing mappings and gaps
- Answer "Are we HIPAA compliant?" in real-time
- Perform impact analysis ("What breaks if we change this?")
- Generate audit reports automatically

**All without meetings.**

### 5. Complete Accountability

Every SCD includes provenance:
```yaml
provenance:
  created_by: tim@company.com
  created_at: 2025-11-19T10:00:00Z
  rationale: "Changed encryption to AES-256 per CSO requirement for HIPAA"
```

**AI can't hide behind "the algorithm." Humans can't claim "nobody told me."**

---

## What is SCS?

SCS defines **Structured Context Documents (SCDs)** organized into three tiers:

### Meta-Tier: The Semantic Foundation
Defines the "language" your system speaks:
- Roles and capabilities
- Domain concepts
- Cross-cutting concerns
- Architectural patterns

### Standards-Tier: External Obligations
Represents compliance frameworks as importable contracts:
- HIPAA, SOC2, GDPR, ISO standards
- Can be shared via scs-registry
- Updates flow to all users

### Project-Tier: Your Actual System
Describes what you're building:
- Architecture and components
- Features and requirements
- Security implementations
- Links to standards via relationships

**Relationships between SCDs create a queryable knowledge graph** that enables autonomic governance.

---

## What You Get

This repository contains:

✅ **Complete specification** (spec/0.1/) - 8 normative documents
✅ **JSON Schemas** (schema/) - For validation
✅ **YAML Templates** (templates/) - Quick-start files
✅ **Comprehensive guides** (docs/) - Usage, validation, tutorials
✅ **Validation tools** (tools/) - SCD validator
✅ **Professional governance** (GOVERNANCE.md) - RFC process, versioning
✅ **Collaboration infrastructure** - Issue templates, PR process, CODEOWNERS

---

## Repository Structure

```
scs-spec/
├── spec/0.1/              # Normative specification
│   ├── overview.md
│   ├── core-model.md
│   ├── meta-tier.md
│   ├── project-tier.md
│   ├── standards-tier.md
│   ├── bundle-format.md
│   ├── governance-and-compliance.md
│   └── terminology.md
├── schema/                # JSON Schemas for validation
│   ├── scd/               # Meta, project, standards schemas
│   └── bundles/           # Bundle schema
├── templates/             # YAML starter files
│   ├── scd/               # SCD templates
│   └── bundles/           # Bundle templates
├── docs/                  # Guides and tutorials
│   ├── getting-started.md
│   ├── usage-guide.md
│   ├── validation-workflow.md
│   ├── SCD_overview.md
│   └── faq.md
├── tools/                 # Validation and tooling
│   └── scd-validator/
├── rfcs/                  # RFC process for major changes
├── VISION.md              # Complete vision and value proposition
├── GOVERNANCE.md          # Governance model
├── CONTRIBUTING.md        # How to contribute
└── PROGRESS.yaml          # Current status
```

---

## Quick Start

### 1. Clone This Repo

```bash
git clone https://github.com/tim-mccrimmon/scs-spec.git
cd scs-spec
```

### 2. Read the Documentation

**New to SCS? Start here:**
1. [VISION.md](VISION.md) - Why SCS matters
2. [spec/0.1/overview.md](spec/0.1/overview.md) - High-level introduction
3. [docs/getting-started.md](docs/getting-started.md) - Create your first SCD
4. [docs/usage-guide.md](docs/usage-guide.md) - Complete tutorial

**Building tools? Focus on:**
1. [schema/](schema/) - JSON Schemas
2. [templates/](templates/) - YAML templates
3. [spec/0.1/core-model.md](spec/0.1/core-model.md) - Core concepts
4. [docs/validation-workflow.md](docs/validation-workflow.md) - Validation guide

### 3. Create Your First SCD

```bash
# Copy a template
cp templates/scd/meta_scd_template.yaml my-scd.yaml

# Edit it (follow the guide in docs/usage-guide.md)

# Validate it (when validator is ready)
scs-validate my-scd.yaml
```

### 4. Build a Bundle

```bash
# Copy bundle template
cp templates/bundles/minimal-project-bundle.yaml my-bundle.yaml

# Reference your SCDs in the bundle
# Validate the bundle
scs-validate --bundle my-bundle.yaml
```

---

## Who Is This For?

### Industries
- **Healthcare** - HIPAA compliance, patient safety
- **Finance** - SOC2, PCI-DSS, regulatory oversight
- **Government** - NIST standards, security clearances
- **Critical Infrastructure** - Safety, traceability
- **Any regulated industry** - Where accountability matters

### Roles
- **CTOs** - Integrate AI safely without regulatory risk
- **Chief Security Officers** - Enforce security across AI-assisted development
- **Chief Architects** - Maintain architectural integrity with AI in the loop
- **Developers** - Use AI productively without creating tech debt
- **Compliance Officers** - Prove adherence to standards
- **Auditors** - Trace and validate system decisions

### Project Types
- **AI-native development** - Using AI assistants/agents
- **Regulated systems** - HIPAA, SOC2, GDPR compliance required
- **Complex architectures** - Need clear documentation and governance
- **Multi-team projects** - Coordination and alignment critical

---

## Key Features

### ✅ Three-Tier Model
Separates universal semantics (meta), external obligations (standards), and project specifics (project)

### ✅ Relationship Graph
SCDs form a knowledge graph enabling impact analysis, compliance checking, and dependency tracking

### ✅ Version Control Friendly
YAML/JSON formats work with git, enabling full change history and provenance

### ✅ Autonomic Governance
AI agents operate over bundles to continuously validate compliance and detect issues

### ✅ Shared Standards
Import standards-tier SCDs from scs-registry instead of reinventing compliance

### ✅ Tool-Friendly
JSON Schemas enable validation, IDE integration, and automated governance

### ✅ Provenance by Design
Every SCD tracks who, when, why for complete accountability

---

## Part of a Larger Ecosystem

SCS is the specification. Related repositories:

- **scs-registry** - Shared standards-tier SCDs (HIPAA, SOC2, etc.)
- **scs-tools** - Validators, editors, governance agents
- **scs-reference-implementation** - Healthcare example demonstrating CEDM+SCS

**CEDM (Context Engineering Development Method)** is the full methodology for AI-native development. SCS enables the "Context" phase of CEDM.

---

## Current Status

**Version**: 0.1 (Draft)
**Status**: Actively evolving
**Stability**: Use for experimentation and feedback

**Recent progress**: See [PROGRESS.yaml](PROGRESS.yaml) for current focus and next steps.

### What's Complete
✅ Core specification (8 documents)
✅ JSON Schemas for all tiers
✅ YAML templates
✅ Usage and validation guides
✅ Governance model with RFC process

### What's In Progress
⏳ Example SCD bundles
⏳ Basic validator tool
⏳ Reference implementation

### Roadmap to 1.0
- Validate spec with real-world projects
- Build complete tooling suite
- Gather community feedback
- Stabilize schemas and semantics

---

## Getting Involved

### Report Issues
Found a bug or have a suggestion? [Open an issue](https://github.com/tim-mccrimmon/scs-spec/issues/new/choose)

### Propose Changes
- **Minor changes** (typos, examples, clarifications): Submit a PR
- **Major changes** (new concepts, breaking changes): [Open a discussion](https://github.com/tim-mccrimmon/scs-spec/discussions) first, then submit an RFC

See [GOVERNANCE.md](GOVERNANCE.md) for the full process.

### Contribute
Read [CONTRIBUTING.md](CONTRIBUTING.md) for:
- How to contribute
- Coding standards
- PR process
- Branch naming conventions

### Join the Community
- **Discussions**: Ask questions, share ideas
- **Issues**: Report bugs, request features
- **RFCs**: Propose major changes (see [rfcs/](rfcs/))

---

## Governance

SCS follows a **Benevolent Maintainer** model for v0.x:
- Tim McCrimmon serves as primary maintainer
- Community input is welcomed via issues and discussions
- Major changes require an RFC (Request for Comments)
- See [GOVERNANCE.md](GOVERNANCE.md) for complete details

**Code of Conduct**: All contributors must follow our [Code of Conduct](CODE_OF_CONDUCT.md)

---

## License

Apache License 2.0

Copyright © 2025 Timothy McCrimmon and Contributors

See [LICENSE.md](LICENSE.md) for details.

**Trademarks**: "SCS" and "CEDM" are trademarks of Ohana Consulting LLC. See [GOVERNANCE.md](GOVERNANCE.md) for usage guidelines.

---

## Learn More

- **Vision**: [VISION.md](VISION.md) - Complete vision and value proposition
- **Specification**: [spec/0.1/](spec/0.1/) - Normative documentation
- **Guides**: [docs/](docs/) - Tutorials and workflows
- **FAQ**: [docs/faq.md](docs/faq.md) - Common questions
- **Governance**: [GOVERNANCE.md](GOVERNANCE.md) - How the project is governed

---

## Why Now?

AI is accelerating software development, but without structured context, it's also accelerating risk, debt, and compliance failures.

**The question isn't whether to use AI in development — it's whether you'll do it safely and legally.**

SCS provides the infrastructure for **trustworthy, governable, AI-native software development**.

**Join us in building the future of context-aware systems.** 🚀

---

**Questions?** Open an [issue](https://github.com/tim-mccrimmon/scs-spec/issues/new/choose) or [discussion](https://github.com/tim-mccrimmon/scs-spec/discussions).
