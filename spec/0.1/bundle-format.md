# SCS 0.1 — Bundle Format

**Version:** 0.1 (Draft)
**Status:** Work in Progress
**Last Updated:** 2025-11-21

---

## 1. Purpose

The **SCS Bundle** is a manifest document that organizes and references Structured Context Documents (SCDs). Bundles are NOT SCDs themselves—they are container documents similar to Docker manifests or Kubernetes pod specifications.

The Bundle Format defines:

- how SCDs are grouped into logical units
- how bundles reference other bundles (imports)
- how bundle types differ (project, meta, standards, domain)
- how versions and tier boundaries are managed
- how tools load, validate, and reason over context hierarchies

In SCS 0.1, bundles serve as **immutable contracts** for structured context.

---

## 2. What Is an SCS Bundle?

An **SCS Bundle** is:

- A YAML manifest file that lists SCDs and imports other bundles
- A container/organizer (NOT content itself)
- Versioned as an immutable set once locked
- Used by tools as the "active context" for evaluation
- The foundation for AI-assisted development and autonomic governance

**Key Principle**: Bundles are manifests. SCDs are content. They are separate document types.

### Container Analogy

Think of SCS bundles like Docker/Kubernetes containers:

| Docker/K8s | SCS Bundle |
|------------|------------|
| Container manifest (`Dockerfile`, K8s Pod spec) | Bundle YAML file |
| Container image | Versioned bundle |
| Base image (`FROM python:3.11`) | Bundle import (`bundle:meta:1.0.0`) |
| Layers | SCDs |
| `docker-compose.yml` | Project bundle |
| Container registry | SCS Registry (future) |
| Image tags (`:latest`, `:1.0.0`) | Bundle versions (`DRAFT`, `1.0.0`) |

Just as Docker manifests organize layers without being layers themselves, SCS bundles organize SCDs without being SCDs.

---

## 3. Bundle Types

SCS 0.1 defines **four bundle types**:

### 3.1 Project Bundle

**Type**: `project`
**Purpose**: Top-level orchestrator bundle for a complete project
**Cardinality**: 1 per project
**Imports**: MUST import meta, standards, and domain bundles
**SCDs**: Typically empty (all context in imported bundles)

The project bundle is the single entry point for all project context.

**Example**:
```yaml
id: bundle:medication-adherence
type: project
version: "1.0.0"
title: "Medication Adherence System"

imports:
  - bundle:meta:1.0.0
  - bundle:standards:1.0.0
  - bundle:architecture:1.0.0
  - bundle:security:1.0.0
  # ... all domain bundles

scds: []
```

---

### 3.2 Meta Bundle

**Type**: `meta`
**Purpose**: Standard vocabulary and semantic foundations
**Cardinality**: 1 per project (imported from SCS specification)
**Imports**: None (meta is the foundation)
**SCDs**: Meta-tier SCDs (roles, capabilities, domains, concerns)

The meta bundle provides standardized terminology that all projects reference.

**Example**:
```yaml
id: bundle:meta
type: meta
version: "1.0.0"
title: "SCS Meta-Tier Standard Bundle"

imports: []

scds:
  - scd:meta:roles
  - scd:meta:capabilities
  - scd:meta:domains
  - scd:meta:concerns
```

---

### 3.3 Standards Bundle

**Type**: `standards`
**Purpose**: Compliance and regulatory requirements
**Cardinality**: 1 per project
**Imports**: MAY import other standards bundles (e.g., SOC2, ISO27001)
**SCDs**: Standards-tier SCDs (project-specific interpretations)

Standards bundles combine external compliance frameworks with project-specific mappings.

**Example**:
```yaml
id: bundle:standards
type: standards
version: "1.0.0"
title: "Compliance Standards Bundle"

imports:
  - bundle:standards:soc2-type2:2023.1

scds:
  - scd:standards:hipaa-privacy-rule
  - scd:standards:hipaa-security-rule
```

---

### 3.4 Domain Bundle

**Type**: `domain`
**Purpose**: Context for a specific domain or concern area
**Cardinality**: 11+ per project (minimum 11 prescribed domains)
**Imports**: MUST NOT import other bundles
**SCDs**: MUST contain at least 2 project-tier SCDs

Domain bundles organize project-specific context by subject area (architecture, security, etc.).

**Example**:
```yaml
id: bundle:architecture
type: domain
version: "1.0.0"
title: "Architecture Domain Bundle"

imports: []

scds:
  - scd:project:system-context
  - scd:project:tech-stack
  - scd:project:integration-map
  - scd:project:component-model
```

---

## 4. Bundle Hierarchy

Bundles form a three-level hierarchy:

```
Project Bundle (top-level)
├── Meta Bundle (foundation)
├── Standards Bundle (compliance)
└── Domain Bundles (10+ domains)
    ├── Architecture
    ├── Security
    ├── Performance & Reliability
    ├── Usability & Accessibility
    ├── Compliance & Governance
    ├── Data & Provenance
    ├── Testing & Validation
    ├── Deployment & Operations
    ├── Safety & Risk
    └── Ethics & AI Accountability
```

**Key Rules**:
- Project bundle imports everything (meta, standards, all domains)
- Meta bundle imports nothing (it's the foundation)
- Standards bundle may import other standards bundles
- Domain bundles import nothing (they contain only SCDs)

---

## 5. Bundle Manifest Format

### 5.1 Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Unique bundle identifier (`bundle:name`) |
| `type` | enum | Bundle type: `project`, `meta`, `standards`, `domain` |
| `version` | string | Semantic version (`1.0.0`) or `DRAFT` |
| `title` | string | Human-readable bundle title |
| `description` | string | Summary of what this bundle represents |
| `imports` | array | List of bundle references with versions |
| `scds` | array | List of SCD references included in this bundle |
| `provenance` | object | Authorship and change history |

### 5.2 Version Format

Versions MUST follow one of these patterns:
- **Semantic version**: `1.0.0`, `2.1.3` (immutable, locked)
- **Draft**: `DRAFT` (mutable, working state)

Once a bundle is versioned (e.g., `1.0.0`), it becomes immutable.

### 5.3 Bundle References

Bundle imports use this format:
```
bundle:<name>:<version>
```

Examples:
- `bundle:meta:1.0.0` - Versioned meta bundle
- `bundle:architecture:1.0.0` - Versioned domain bundle
- `bundle:standards:soc2-type2:2023.1` - External standards bundle

### 5.4 SCD References

SCD references use this format:
```
scd:<tier>:<name>
```

Examples:
- `scd:meta:roles` - Meta-tier SCD
- `scd:standards:hipaa-privacy-rule` - Standards-tier SCD
- `scd:project:system-context` - Project-tier SCD

---

## 6. Complete Example

**Project Bundle** (`bundles/project-bundle.yaml`):
```yaml
id: bundle:medication-adherence
type: project
version: "1.0.0"
title: "Medication Adherence System - Complete Context Bundle"
description: >
  Complete structured context bundle for the Medication Adherence system.

imports:
  - bundle:meta:1.0.0
  - bundle:standards:1.0.0
  - bundle:architecture:1.0.0
  - bundle:security:1.0.0
  - bundle:performance-reliability:1.0.0
  - bundle:usability-accessibility:1.0.0
  - bundle:compliance-governance:1.0.0
  - bundle:data-provenance:1.0.0
  - bundle:testing-validation:1.0.0
  - bundle:deployment-operations:1.0.0
  - bundle:safety-risk:1.0.0
  - bundle:ethics-ai-accountability:1.0.0

scds: []

provenance:
  created_by: "sarah.chen@medtech.com"
  created_at: "2025-11-01T09:00:00Z"
  updated_by: "sarah.chen@medtech.com"
  updated_at: "2025-11-20T14:00:00Z"
  rationale: "Version 1.0.0 release - complete context contract"
```

**Domain Bundle** (`bundles/domains/architecture.yaml`):
```yaml
id: bundle:architecture
type: domain
version: "1.0.0"
title: "Architecture Domain Bundle"
description: >
  Architecture domain bundle defining system boundaries, components,
  technology stack, and integration points.

imports: []

scds:
  - scd:project:system-context
  - scd:project:tech-stack
  - scd:project:integration-map
  - scd:project:component-model

provenance:
  created_by: "architecture-team@medtech.com"
  created_at: "2025-11-01T10:00:00Z"
  updated_by: "mike.johnson@medtech.com"
  updated_at: "2025-11-18T11:30:00Z"
  rationale: "Architecture bundle v1.0.0 - locked for development"
```

---

## 7. Bundle Semantics

### 7.1 Completeness

The project bundle (with all imported bundles) MUST contain every SCD required to define the system.

### 7.2 Source of Truth

The project bundle is the root context used by:
- Code editors and IDEs
- Validators and linters
- Governance engines
- AI code assistants
- Deployment tools

### 7.3 Immutability

Once versioned (e.g., `1.0.0`), a bundle MUST remain immutable. Changes require a new version.

**Lifecycle**:
1. Create bundle in `DRAFT` state
2. Iterate and refine in `DRAFT` mode
3. Lock and version (e.g., `1.0.0`)
4. Bundle becomes immutable contract
5. Future changes create new versions (e.g., `1.1.0`)

### 7.4 Independence

Domain bundles MAY version independently:
- Architecture team locks `bundle:architecture:1.0.0` in Week 3
- Security team locks `bundle:security:1.0.0` in Week 5
- Project bundle references specific versions of each

### 7.5 Cross-Tier Binding

SCDs from different tiers (Meta → Standards → Project) are bound together through the bundle hierarchy.

---

## 8. Directory Structure

Recommended project structure:

```
project-name/
├── bundles/
│   ├── project-bundle.yaml          # Top-level bundle
│   ├── meta-bundle.yaml             # Meta vocabulary (imported)
│   ├── standards-bundle.yaml        # Compliance standards
│   └── domains/
│       ├── architecture.yaml
│       ├── security.yaml
│       ├── performance-reliability.yaml
│       └── ... (10 total domain bundles)
│
├── context/
│   ├── meta/                        # Meta-tier SCDs
│   │   ├── roles.yaml
│   │   ├── capabilities.yaml
│   │   └── ...
│   ├── standards/                   # Standards-tier SCDs
│   │   ├── hipaa-privacy-rule.yaml
│   │   └── ...
│   └── project/                     # Project-tier SCDs
│       ├── system-context.yaml
│       ├── tech-stack.yaml
│       └── ... (38+ SCDs)
│
└── .scs/
    └── config.yaml                  # SCS tooling config
```

---

## 9. Validation Requirements

Tools MUST validate that:

### 9.1 Schema Validation
- Bundle conforms to JSON schema (`schema/bundles/scd-bundle-schema.json`)
- All required fields present
- Field types and patterns correct
- Conditional rules satisfied (e.g., domain bundles have no imports)

### 9.2 Reference Resolution
- All SCD references resolve to actual SCD files
- All bundle imports resolve to actual bundle files
- No circular imports
- SCD identifiers are unique within bundle

### 9.3 Type Consistency
- Bundle `type` matches usage pattern
- Domain bundles contain only project-tier SCDs
- Meta bundles contain only meta-tier SCDs
- Standards bundles contain only standards-tier SCDs

### 9.4 Version Consistency
- Version follows semantic versioning or `DRAFT`
- Imported bundle versions exist
- No conflicting version requirements

Tools MAY also perform:
- Cross-tier semantic checks
- Compliance completeness checks
- Dependency cycle analysis
- Minimum SCD requirements validation

---

## 10. Bundle Lifecycle

### 10.1 DRAFT State

During development, bundles use `version: "DRAFT"`:
- Mutable (can be changed)
- No strict validation (warnings instead of errors)
- Used for active development

### 10.2 VERSIONED State

When ready to lock, bundles receive semantic versions (e.g., `1.0.0`):
- Immutable (cannot be changed)
- Strict validation (all errors must be fixed)
- Serves as binding contract

### 10.3 Versioning Workflow

1. Domain teams create bundles in `DRAFT` state
2. Teams iterate, add SCDs, refine content
3. Teams validate bundle completeness
4. Teams lock bundle with version (e.g., `bundle:security:1.0.0`)
5. Project bundle imports all versioned domain bundles
6. Project bundle locks (e.g., `bundle:project:1.0.0`)
7. Development proceeds against locked contract

---

## 11. Minimum Bundle Set

Production projects MUST include:

**1 Project Bundle** (top-level)
**1 Meta Bundle** (imported from SCS)
**1 Standards Bundle** (project compliance)
**10 Domain Bundles** (minimum prescribed set):
1. Architecture
2. Security
3. Performance & Reliability
4. Usability & Accessibility
5. Compliance & Governance
6. Data & Provenance
7. Testing & Validation
8. Deployment & Operations
9. Safety & Risk
10. Ethics & AI Accountability

Projects MAY add additional domain bundles as needed.

See [Minimum Project SCDs](../../docs/minimum-project-scds.md) for details.

---

## 12. Examples

Complete working examples are available in:
- `examples/bundles/` - Medication Adherence System bundle examples
- `examples/bundles/README.md` - Detailed explanation of example structure

These examples demonstrate:
- All 4 bundle types
- Hierarchical imports
- Domain bundle independence
- Healthcare compliance (HIPAA, SOC2)
- Realistic project structure

---

## 13. Schema Reference

**Bundle Schema**: `schema/bundles/scd-bundle-schema.json`
**SCD Schemas**:
- Meta-tier: `schema/scd/meta-scd-template.json`
- Standards-tier: `schema/scd/standards-scd-template.json`
- Project-tier: `schema/scd/project-scd-template.json`

---

## 14. Future Extensions

Future versions may introduce:
- Bundle inheritance/extension
- Bundle signatures for attestation
- Multi-bundle workspaces
- Dynamic or environment-specific bundles
- Registry-based bundle resolution
- Bundle dependency graph visualization

SCS 0.1 defines the minimal, stable bundle representation.

---

## 15. Related Documentation

- [Bundle Lifecycle](../../docs/bundle-lifecycle.md) - How bundles evolve through development
- [Project Structure](../../docs/project-structure.md) - Recommended directory layout
- [Minimum Project SCDs](../../docs/minimum-project-scds.md) - Required SCD set
- [Validation Workflow](../../docs/validation-workflow.md) - How to validate bundles

---

## 16. Key Takeaways

1. **Bundles are manifests, not content** - They organize and reference SCDs
2. **Four bundle types** - Project, Meta, Standards, Domain
3. **Container model** - Think Docker manifests, not Docker layers
4. **Immutable contracts** - Once versioned, bundles are locked
5. **Hierarchical imports** - Project imports everything else
6. **Domain independence** - Domain bundles can version separately
7. **Type enforcement** - Schema validates bundle type rules

---

## 17. Feedback

Comments and refinements for the Bundle Format should be submitted through:
- [GitHub Issues](https://github.com/tim-mccrimmon/scs-spec/issues)
- [GitHub Discussions](https://github.com/tim-mccrimmon/scs-spec/discussions)
