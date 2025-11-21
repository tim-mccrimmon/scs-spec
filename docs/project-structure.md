# Recommended Project Structure for SCS

**Version**: 0.1
**Last Updated**: 2025-11-21

---

## Overview

This document defines the **recommended directory structure** for projects using the Structured Context Specification (SCS). This structure provides clear conventions for organizing bundles, SCDs, and project code in a way that supports both human understanding and tool automation.

**Important**: This structure is **recommended but not required**. Teams may adapt it to their needs, but following these conventions will ensure compatibility with SCS tooling and best practices.

---

## Complete Structure

```
project-name/
├── README.md
├── .gitignore
│
├── src/                              # Application source code
│   └── ...
│
├── tests/                            # Application tests
│   └── ...
│
├── docs/                             # Project documentation
│   └── ...
│
├── context/                          # SCS Context (all SCDs)
│   ├── meta/                         # Meta-tier SCDs
│   │   ├── roles.yaml
│   │   ├── capabilities.yaml
│   │   ├── domains.yaml
│   │   └── concerns.yaml
│   │
│   ├── standards/                    # Standards-tier SCDs
│   │   ├── hipaa-privacy-rule.yaml
│   │   ├── hipaa-security-rule.yaml
│   │   └── hipaa-breach-notification.yaml
│   │
│   └── project/                      # Project-tier SCDs (38+ SCDs)
│       ├── system-context.yaml
│       ├── tech-stack.yaml
│       ├── integration-map.yaml
│       ├── component-model.yaml
│       ├── authn-authz.yaml
│       ├── data-protection.yaml
│       ├── data-handling.yaml
│       ├── threat-model.yaml
│       └── ... (30+ more project SCDs)
│
├── bundles/                          # Bundle manifests
│   ├── project-bundle.yaml           # Top-level project bundle
│   ├── meta-bundle.yaml              # Meta-tier bundle (imported from SCS)
│   ├── standards-bundle.yaml         # Standards bundle
│   │
│   └── domains/                      # Domain-specific bundles (10 minimum)
│       ├── architecture.yaml
│       ├── security.yaml
│       ├── performance-reliability.yaml
│       ├── usability-accessibility.yaml
│       ├── compliance-governance.yaml
│       ├── data-provenance.yaml
│       ├── testing-validation.yaml
│       ├── deployment-operations.yaml
│       ├── safety-risk.yaml
│       └── ethics-ai-accountability.yaml
│
├── .scs/                             # SCS configuration (optional)
│   └── config.yaml
│
└── .github/                          # CI/CD workflows
    └── workflows/
        └── validate-scs.yml          # SCS validation workflow
```

---

## Bundle Hierarchy

SCS projects organize context using a **4-bundle-type hierarchy**:

```
Project Bundle (type: project)
├── Meta Bundle (type: meta)
├── Standards Bundle (type: standards)
└── Domain Bundles (type: domain × 10+)
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
- **Project bundle** imports all other bundles (meta, standards, domains)
- **Meta bundle** contains foundational vocabulary (imported from SCS spec)
- **Standards bundle** contains compliance requirements
- **Domain bundles** contain project-tier SCDs (2+ SCDs each, no imports allowed)

---

## Directory Descriptions

### `/context/` - All Structured Context Documents

**Purpose**: Contains all SCDs organized by tier.

**Structure**:
```
context/
├── meta/          # Meta-tier: Foundational vocabulary
├── standards/     # Standards-tier: Compliance and regulatory
└── project/       # Project-tier: Specific system being built
```

**Conventions**:
- One SCD per file
- YAML format (`.yaml` extension preferred over `.yml`)
- Filename matches SCD name portion of ID
  - SCD ID: `scd:meta:roles` → File: `context/meta/roles.yaml`
  - SCD ID: `scd:project:system-context` → File: `context/project/system-context.yaml`
- Use kebab-case for multi-word names: `tech-stack.yaml`, `component-model.yaml`

**Git Management**:
- All SCD files are version controlled in git
- DRAFT SCDs live in working branches
- Versioned SCDs are tagged with bundle versions

---

### `/context/meta/` - Meta-Tier SCDs

**Purpose**: Defines universal semantics, vocabulary, and foundational concepts. Typically **imported from SCS specification** rather than created from scratch.

**Standard Contents** (provided by SCS):
- `roles.yaml` - System roles and trust levels
- `capabilities.yaml` - System capabilities
- `domains.yaml` - Domain concepts and boundaries
- `concerns.yaml` - Cross-cutting concerns

**Note**: Most projects import the standard meta bundle from SCS rather than defining their own meta-tier SCDs.

**Example SCD Structure**:
```yaml
# context/meta/roles.yaml
id: scd:meta:roles
type: meta
title: "System Roles"
version: "1.0.0"
description: "Standard role definitions for structured context"
content:
  roles:
    - id: role:admin
      name: "Administrator"
      description: "System administrator with full access"
    - id: role:user
      name: "Standard User"
      description: "Regular system user"
provenance:
  created_by: "scs-spec-maintainers@ohana.ai"
  created_at: "2025-01-15T10:00:00Z"
  rationale: "SCS 0.1 standard role definitions"
```

---

### `/context/standards/` - Standards-Tier SCDs

**Purpose**: Represents external standards, regulations, and compliance requirements interpreted for the project.

**Typical Contents**:
- `hipaa-privacy-rule.yaml` - HIPAA privacy requirements
- `hipaa-security-rule.yaml` - HIPAA security requirements
- `soc2-*.yaml` - SOC2 control interpretations
- `gdpr-*.yaml` - GDPR requirements
- `pci-dss-*.yaml` - PCI DSS requirements

**Note**: Some standards may be imported from external bundles (e.g., SOC2) while others are project-specific interpretations (e.g., HIPAA).

**Example SCD Structure**:
```yaml
# context/standards/hipaa-privacy-rule.yaml
id: scd:standards:hipaa-privacy-rule
type: standards
title: "HIPAA Privacy Rule Requirements"
version: "1.0.0"
description: "HIPAA Privacy Rule requirements applicable to this project"
content:
  standard_name: "HIPAA Privacy Rule"
  requirements:
    - id: "164.502(a)"
      title: "Uses and Disclosures of PHI"
      description: "A covered entity may not use or disclose PHI except as permitted"
provenance:
  created_by: "compliance-team@medtech.com"
  created_at: "2025-11-01T09:30:00Z"
  rationale: "HIPAA privacy requirements for medication adherence system"
```

---

### `/context/project/` - Project-Tier SCDs

**Purpose**: Describes the specific system being built - architecture, features, security implementations, etc.

**Organization**: 38+ SCDs organized across 10 domain areas (see [Minimum Project SCDs](minimum-project-scds.md) for complete list).

**Example Categories**:

**Architecture** (4 SCDs):
- `system-context.yaml` - System boundaries and external systems
- `tech-stack.yaml` - Technology choices and rationale
- `integration-map.yaml` - External system interfaces
- `component-model.yaml` - Component structure and interactions

**Security** (4 SCDs):
- `authn-authz.yaml` - Authentication and authorization
- `data-protection.yaml` - Encryption and key management
- `data-handling.yaml` - Data classification and retention
- `threat-model.yaml` - Identified threats and mitigations

**Performance & Reliability** (4 SCDs):
- `response-time.yaml` - Latency targets and SLOs
- `availability.yaml` - Uptime targets and redundancy
- `fault-tolerance.yaml` - Error handling and resilience
- `scalability.yaml` - Scaling strategy and capacity

(See [Minimum Project SCDs](minimum-project-scds.md) for remaining 7 domains with 26+ SCDs)

**Example SCD Structure**:
```yaml
# context/project/system-context.yaml
id: scd:project:system-context
type: project
title: "System Context and Boundaries"
version: "1.0.0"
description: "Defines system boundary, external systems, and key interactions"
content:
  system_name: "Medication Adherence System"
  system_boundary:
    description: "Mobile app for medication tracking and reminders"
    components:
      - "Mobile App (iOS/Android)"
      - "Backend API"
      - "Database"
      - "Notification Service"
    external_systems:
      - name: "EHR System"
        interface: "HL7 FHIR API"
      - name: "SMS Gateway"
        interface: "Twilio API"
relationships:
  - type: depends-on
    target: scd:meta:roles
  - type: satisfies
    target: scd:standards:hipaa-security-rule
provenance:
  created_by: "architecture-team@medtech.com"
  created_at: "2025-11-01T10:00:00Z"
  rationale: "Initial system context for medication adherence system"
```

---

### `/bundles/` - Bundle Manifests

**Purpose**: Contains bundle manifests that organize and version SCDs. Bundles are **container documents** (manifests) that reference SCDs but are NOT SCDs themselves.

**Structure**:
```
bundles/
├── project-bundle.yaml          # Top-level orchestrator (type: project)
├── meta-bundle.yaml             # Foundational vocabulary (type: meta)
├── standards-bundle.yaml        # Compliance requirements (type: standards)
└── domains/                     # Domain-specific bundles (type: domain)
    ├── architecture.yaml
    ├── security.yaml
    ├── performance-reliability.yaml
    ├── usability-accessibility.yaml
    ├── compliance-governance.yaml
    ├── data-provenance.yaml
    ├── testing-validation.yaml
    ├── deployment-operations.yaml
    ├── safety-risk.yaml
    └── ethics-ai-accountability.yaml
```

**Bundle Types**: See [Bundle Format Specification](../spec/0.1/bundle-format.md) for complete details.

---

### `/bundles/project-bundle.yaml` - Project Bundle

**Type**: `project`
**Purpose**: Top-level orchestrator that imports all other bundles (meta, standards, domains).

**Example Structure**:
```yaml
id: bundle:medication-adherence
type: project
version: "1.0.0"
title: "Medication Adherence System - Complete Context Bundle"
description: >
  Complete structured context bundle for the Medication Adherence system.

imports:
  # Foundation
  - bundle:meta:1.0.0
  - bundle:standards:1.0.0

  # Domain bundles (10 prescribed)
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

scds: []  # All SCDs are in imported bundles

provenance:
  created_by: "project-lead@medtech.com"
  created_at: "2025-11-01T09:00:00Z"
  updated_by: "project-lead@medtech.com"
  updated_at: "2025-11-20T14:00:00Z"
  rationale: "Version 1.0.0 release - complete context contract for development"
```

**Notes**:
- Project bundle typically has empty `scds` array (all context in imported bundles)
- Imports meta, standards, and all domain bundles
- Once versioned, this bundle is immutable

---

### `/bundles/meta-bundle.yaml` - Meta Bundle

**Type**: `meta`
**Purpose**: Standard vocabulary and semantic foundations. Usually **imported from SCS specification** rather than created per-project.

**Example Structure**:
```yaml
id: bundle:meta
type: meta
version: "1.0.0"
title: "SCS Meta-Tier Standard Bundle"
description: >
  Standard meta-tier bundle containing foundational vocabulary and semantics
  for structured context. Imported by all SCS projects.

imports: []  # Meta is the foundation - imports nothing

scds:
  - scd:meta:roles
  - scd:meta:capabilities
  - scd:meta:domains
  - scd:meta:concerns

provenance:
  created_by: "scs-spec-maintainers@ohana.ai"
  created_at: "2025-01-15T10:00:00Z"
  rationale: "SCS 0.1 standard meta-tier bundle"
```

**Notes**:
- Provided by SCS specification
- Projects import this bundle rather than creating their own
- Contains standard vocabulary all projects use

---

### `/bundles/standards-bundle.yaml` - Standards Bundle

**Type**: `standards`
**Purpose**: Compliance and regulatory requirements. May import external standards bundles (e.g., SOC2) and contain project-specific standards SCDs (e.g., HIPAA).

**Example Structure**:
```yaml
id: bundle:standards
type: standards
version: "1.0.0"
title: "Medication Adherence System - Standards Bundle"
description: >
  Standards and compliance requirements for the Medication Adherence system.

imports:
  # External standards bundles
  - bundle:standards:soc2-type2:2023.1

scds:
  # Project-specific standards interpretations
  - scd:standards:hipaa-privacy-rule
  - scd:standards:hipaa-security-rule
  - scd:standards:hipaa-breach-notification

provenance:
  created_by: "compliance-team@medtech.com"
  created_at: "2025-11-01T09:30:00Z"
  updated_by: "compliance-team@medtech.com"
  updated_at: "2025-11-15T16:00:00Z"
  rationale: "Standards bundle for healthcare compliance"
```

**Notes**:
- May import external standards bundles (SOC2, ISO27001, etc.)
- Contains project-specific standards-tier SCDs
- Flexible structure based on project compliance needs

---

### `/bundles/domains/` - Domain Bundles

**Type**: `domain` (all domain bundles)
**Purpose**: Each domain bundle contains project-tier SCDs for a specific concern area.
**Count**: Minimum 10 prescribed domains (projects may add more)

**Key Constraints**:
- Domain bundles MUST have `imports: []` (no imports allowed)
- Domain bundles MUST contain at least 2 SCDs
- Domain bundles contain ONLY project-tier SCDs

#### Architecture Bundle Example

```yaml
# bundles/domains/architecture.yaml
id: bundle:architecture
type: domain
version: "1.0.0"
title: "Medication Adherence System - Architecture Bundle"
description: "Architecture domain bundle defining system boundaries and components"

imports: []  # Domain bundles cannot import other bundles

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

#### Security Bundle Example

```yaml
# bundles/domains/security.yaml
id: bundle:security
type: domain
version: "1.0.0"
title: "Medication Adherence System - Security Bundle"
description: "Security domain bundle defining controls and threat management"

imports: []

scds:
  - scd:project:authn-authz
  - scd:project:data-protection
  - scd:project:data-handling
  - scd:project:threat-model

provenance:
  created_by: "security-team@medtech.com"
  created_at: "2025-11-01T10:15:00Z"
  updated_by: "rachel.kim@medtech.com"
  updated_at: "2025-11-19T09:45:00Z"
  rationale: "Security bundle v1.0.0 - PHI protection controls defined"
```

**All 10 Prescribed Domain Bundles**:
1. **Architecture** - System design and technology stack
2. **Security** - Security controls and data protection
3. **Performance & Reliability** - Performance targets and resilience
4. **Usability & Accessibility** - UX principles and WCAG compliance
5. **Compliance & Governance** - Regulatory mappings and audit requirements
6. **Data & Provenance** - Data models and lineage tracking
7. **Testing & Validation** - Test coverage and QA procedures
8. **Deployment & Operations** - Infrastructure and monitoring
9. **Safety & Risk** - Risk assessment and safety controls
10. **Ethics & AI Accountability** - AI usage policy and bias mitigation

See [Minimum Project SCDs](minimum-project-scds.md) for details on SCDs in each domain.

---

### `/.scs/` - SCS Configuration (Optional)

**Purpose**: Configuration for SCS tooling. Optional but useful for customizing behavior.

**Example Configuration**:
```yaml
# .scs/config.yaml
version: "0.1"

# Path conventions (if different from defaults)
paths:
  context_dir: "context"
  bundles_dir: "bundles"
  schema_dir: "../scs-spec/schema"

# Naming conventions
conventions:
  scd_id_to_path: "context/{tier}/{name}.yaml"
  bundle_id_to_path: "bundles/{name}.yaml"
  domain_bundle_path: "bundles/domains/{name}.yaml"

# Validation settings
validation:
  strict_draft: false           # Lenient validation for DRAFT bundles
  strict_versioned: true        # Strict validation for versioned bundles
  check_relationships: true     # Validate relationship targets exist
  check_circular: true          # Check for circular dependencies
```

---

## File Naming Conventions

### SCD Files

**Convention**: `{name}.yaml` where `{name}` matches the name portion of the SCD ID.

**Mapping**:
```
SCD ID: scd:meta:roles
  → Tier: meta
  → Name: roles
  → File path: context/meta/roles.yaml

SCD ID: scd:project:system-context
  → Tier: project
  → Name: system-context
  → File path: context/project/system-context.yaml
```

**Rules**:
- Use kebab-case for multi-word names: `tech-stack`, `component-model`
- Use `.yaml` extension (preferred) or `.yml`
- Keep names descriptive but concise
- Avoid special characters except hyphen

### Bundle Files

**Convention**:
- Project bundle: `project-bundle.yaml`
- Meta bundle: `meta-bundle.yaml`
- Standards bundle: `standards-bundle.yaml`
- Domain bundles: `bundles/domains/{domain-name}.yaml`

**Examples**:
- `bundles/project-bundle.yaml`
- `bundles/meta-bundle.yaml`
- `bundles/standards-bundle.yaml`
- `bundles/domains/architecture.yaml`
- `bundles/domains/security.yaml`

---

## Integration with Development Projects

### Typical Project Structure

```
my-application/
├── src/                    # Application code
├── tests/                  # Application tests
├── docs/                   # Application docs
├── context/                # SCS context (SCDs)
├── bundles/                # SCS bundles (manifests)
├── .scs/                   # SCS config
├── package.json            # Language-specific config
├── Dockerfile
├── docker-compose.yml
└── README.md
```

**Key Points**:
- SCS context lives alongside application code
- Version controlled together in same repository
- CI/CD validates both code and context
- Context evolves with the application

---

## Container Analogy

SCS bundles work like Docker/Kubernetes containers:

| Docker/K8s | SCS Bundle |
|------------|------------|
| Container manifest | Bundle YAML file |
| `docker-compose.yml` | Project bundle |
| Base image (`FROM`) | Bundle imports |
| Layers | SCDs |
| `:latest` tag | `DRAFT` version |
| `:1.0.0` tag | Semantic version |

Just as Docker manifests organize layers without being layers themselves, **SCS bundles organize SCDs without being SCDs**.

---

## Git Workflow

### Branch Strategy

**DRAFT Bundles** (working state):
```
feature/add-notifications
  ├── Modified: context/project/component-model.yaml
  ├── Modified: context/project/notification-service.yaml (new)
  ├── Modified: bundles/domains/architecture.yaml (version: "DRAFT")
  └── Modified: bundles/project-bundle.yaml (version: "DRAFT")
```

**Versioned Bundles** (locked state):
```
main branch
  ├── bundles/project-bundle.yaml (version: "1.0.0")
  ├── bundles/domains/architecture.yaml (version: "1.0.0")
  └── Git tag: bundle-v1.0.0
```

### Version Tags

When a bundle is versioned and locked:
```bash
# Tag the bundle version
git tag -a bundle-v1.0.0 -m "Project bundle version 1.0.0 - initial contract"
git push origin bundle-v1.0.0
```

**Tag Convention**: `bundle-v{version}`

### Pull Request Workflow

1. Domain team works in feature branch (DRAFT bundles)
2. Creates PR with context changes
3. CI validates SCDs and bundles
4. Team reviews context changes
5. Merge to main (still DRAFT)
6. When ready to version:
   - Update bundle version numbers (`DRAFT` → `1.0.0`)
   - Update provenance
   - Create git tag
   - Bundle becomes immutable

---

## CI/CD Integration

### GitHub Actions Example

```yaml
# .github/workflows/validate-scs.yml
name: Validate SCS Context

on:
  pull_request:
    paths:
      - 'context/**'
      - 'bundles/**'
  push:
    branches:
      - main

jobs:
  validate:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install SCS validator
        run: |
          pip install scs-validator

      - name: Validate domain bundles
        run: |
          scs-validate bundles/domains/*.yaml

      - name: Validate project bundle
        run: |
          scs-validate bundles/project-bundle.yaml --strict

      - name: Generate validation report
        if: always()
        run: |
          scs-validate bundles/project-bundle.yaml --output json > report.json

      - name: Upload validation report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: validation-report
          path: report.json
```

---

## Versioning Strategy

### Bundle Versions

**Semantic Versioning** applies to bundles:

- **Major (2.0.0)**: Breaking changes, significant restructuring
- **Minor (1.1.0)**: Additive changes, new SCDs, expanded context
- **Patch (1.0.1)**: Corrections, clarifications, non-breaking fixes

**Example Evolution**:
```
DRAFT - Initial work, shared with stakeholders
1.0.0 - First locked version, development begins
1.1.0 - Added notification service (additive change)
1.1.1 - Fixed typo in security control description
2.0.0 - Major architecture change (breaking change)
```

### Domain Bundle Independence

Domain bundles MAY version independently:
- Architecture team locks `bundle:architecture:1.0.0` in Week 3
- Security team locks `bundle:security:1.0.0` in Week 5
- Project bundle references specific versions of each

---

## Quick Start: Creating a New Project

```bash
# 1. Create project structure
mkdir my-project && cd my-project

# 2. Create directories
mkdir -p context/{meta,standards,project}
mkdir -p bundles/domains
mkdir -p .scs

# 3. Copy meta bundle from SCS spec
cp ../scs-spec/examples/bundles/meta-bundle.yaml bundles/

# 4. Create project bundle
cat > bundles/project-bundle.yaml << 'EOF'
id: bundle:my-project
type: project
version: "DRAFT"
title: "My Project Context Bundle"
description: "Complete context for my project"
imports:
  - bundle:meta:1.0.0
scds: []
provenance:
  created_by: "you@company.com"
  created_at: "2025-11-21T10:00:00Z"
  rationale: "Initial project bundle"
EOF

# 5. Initialize git
git init
git add .
git commit -m "Initial SCS structure"

# 6. Validate
scs-validate bundles/project-bundle.yaml
```

---

## Summary

**Key Principles**:
1. **4 bundle types**: Project, Meta, Standards, Domain
2. **Bundles are manifests**: They organize SCDs, they're not SCDs themselves
3. **Hierarchical imports**: Project imports Meta + Standards + Domains
4. **Domain independence**: Domain bundles can version separately
5. **Container model**: Like Docker manifests organizing layers
6. **Immutable contracts**: Once versioned, bundles are locked

**This structure enables**:
- Clear organization and navigation
- Tool automation (validators, AI assistants)
- Team collaboration (domain ownership)
- Version management (git tags)
- CI/CD integration (validation workflows)
- Compliance and auditability

---

## Related Documentation

- [Bundle Format Specification](../spec/0.1/bundle-format.md) - Technical bundle structure
- [Bundle Lifecycle](bundle-lifecycle.md) - How bundles evolve through development
- [Minimum Project SCDs](minimum-project-scds.md) - Required SCD set (38+ SCDs)
- [Validation Workflow](validation-workflow.md) - How to validate your structure

---

## Questions?

- Open an [issue](https://github.com/tim-mccrimmon/scs-spec/issues)
- Start a [discussion](https://github.com/tim-mccrimmon/scs-spec/discussions)
