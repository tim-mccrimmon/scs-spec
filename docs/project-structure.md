# Recommended Project Structure for SCS

**Version**: 0.1
**Last Updated**: 2025-11-20

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
│   │   ├── hipaa.yaml
│   │   ├── soc2.yaml
│   │   └── iso27001.yaml
│   │
│   └── project/                      # Project-tier SCDs
│       ├── system-context.yaml
│       ├── tech-stack.yaml
│       ├── component-model.yaml
│       ├── deployment-model.yaml
│       ├── threat-model.yaml
│       ├── security-controls.yaml
│       ├── auth-model.yaml
│       ├── decision-framework.yaml
│       ├── approval-process.yaml
│       ├── performance-requirements.yaml
│       ├── test-strategy.yaml
│       └── ... (more project SCDs)
│
├── bundles/                          # Bundle definitions
│   ├── project-bundle.yaml           # Master project bundle
│   │
│   └── domains/                      # Domain-specific bundles
│       ├── architecture.yaml
│       ├── security.yaml
│       ├── governance.yaml
│       ├── performance.yaml
│       └── compliance.yaml
│
├── .scs/                             # SCS configuration (optional)
│   └── config.yaml
│
└── .github/                          # CI/CD workflows
    └── workflows/
        └── validate-scs.yml          # SCS validation workflow
```

---

## Directory Descriptions

### `/context/` - All Structured Context Documents

**Purpose**: Contains all SCDs organized by tier.

**Structure**:
```
context/
├── meta/          # Meta-tier: System-wide definitions
├── standards/     # Standards-tier: External standards and regulations
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

**Purpose**: Defines universal semantics, vocabulary, and foundational concepts for the system.

**Typical Contents**:
- `roles.yaml` - System roles and trust levels
- `capabilities.yaml` - System capabilities
- `domains.yaml` - Domain concepts and boundaries
- `concerns.yaml` - Cross-cutting concerns

**Example SCD Structure**:
```yaml
# context/meta/roles.yaml
id: scd:meta:roles
type: meta
title: "System Roles"
version: "1.0.0"
description: "Defines all roles within the system and their trust levels"
content:
  roles:
    - id: role:admin
      name: "Administrator"
      description: "System administrator with full access"
      responsibilities:
        - "Manage system configuration"
        - "Manage user accounts"
      trust_level: "high"
    - id: role:user
      name: "Standard User"
      description: "Regular system user"
      responsibilities:
        - "Access permitted resources"
      trust_level: "standard"
provenance:
  created_by: "governance-team@company.com"
  created_at: "2025-11-20T10:00:00Z"
  rationale: "Initial role definitions for project authorization model"
```

---

### `/context/standards/` - Standards-Tier SCDs

**Purpose**: Represents external standards, regulations, and compliance requirements.

**Typical Contents**:
- `hipaa.yaml` - HIPAA requirements and controls
- `soc2.yaml` - SOC2 requirements
- `gdpr.yaml` - GDPR requirements
- `iso27001.yaml` - ISO 27001 controls
- `pci-dss.yaml` - PCI DSS requirements
- `nist.yaml` - NIST framework controls

**Note**: Many standards-tier SCDs may be imported from external bundles (e.g., `scs-registry`) rather than created from scratch.

**Example SCD Structure**:
```yaml
# context/standards/hipaa.yaml
id: scd:standards:hipaa-164.312
type: standards
title: "HIPAA Security Rule - Technical Safeguards"
version: "1.0.0"
description: "HIPAA 164.312 technical safeguard requirements"
content:
  standard_name: "HIPAA"
  standard_version: "164.312"
  requirements:
    - id: "164.312(a)(2)(iv)"
      title: "Encryption and Decryption"
      description: "Implement a mechanism to encrypt and decrypt electronic protected health information"
      category: "Access Control"
    - id: "164.312(d)"
      title: "Person or Entity Authentication"
      description: "Implement procedures to verify that a person or entity seeking access to electronic protected health information is the one claimed"
      category: "Authentication"
provenance:
  created_by: "compliance-team@company.com"
  created_at: "2025-11-20T10:00:00Z"
  rationale: "HIPAA technical safeguards applicable to healthcare system"
```

---

### `/context/project/` - Project-Tier SCDs

**Purpose**: Describes the specific system being built - architecture, features, security implementations, etc.

**Typical Contents** (organized by domain concern):

**Architecture**:
- `system-context.yaml` - System boundaries and external systems
- `tech-stack.yaml` - Technology choices and rationale
- `component-model.yaml` - Component structure and interactions
- `deployment-model.yaml` - Deployment architecture
- `data-flow.yaml` - Data flow and integration patterns

**Security**:
- `threat-model.yaml` - Identified threats and mitigations
- `security-controls.yaml` - Security control implementations
- `auth-model.yaml` - Authentication and authorization design
- `encryption.yaml` - Encryption approach and key management

**Governance**:
- `decision-framework.yaml` - How decisions are made
- `approval-process.yaml` - Approval workflows
- `risk-management.yaml` - Risk identification and management

**Performance**:
- `performance-requirements.yaml` - Performance criteria and SLAs
- `load-expectations.yaml` - Expected load and scaling requirements

**Testing**:
- `test-strategy.yaml` - Testing approach and coverage
- `test-environments.yaml` - Test environment definitions

**Example SCD Structure**:
```yaml
# context/project/system-context.yaml
id: scd:project:system-context
type: project
title: "System Context and Boundaries"
version: "1.0.0"
description: "Defines the system boundary, external systems, and key interactions"
content:
  system_name: "Healthcare Patient Portal"
  system_boundary:
    description: "Web-based patient portal for accessing medical records"
    components_inside_boundary:
      - "Web Frontend"
      - "API Gateway"
      - "Backend Services"
      - "Database"
    external_systems:
      - name: "EHR System"
        interface: "HL7 FHIR API"
        trust_level: "trusted"
      - name: "Payment Processor"
        interface: "REST API"
        trust_level: "external"
relationships:
  - type: depends-on
    target: scd:meta:roles
    description: "Uses system roles defined in meta tier"
  - type: satisfies
    target: scd:standards:hipaa-164.312
    description: "System design satisfies HIPAA technical safeguards"
provenance:
  created_by: "architecture-team@company.com"
  created_at: "2025-11-20T10:00:00Z"
  rationale: "Initial system context for patient portal development"
```

---

### `/bundles/` - Bundle Definitions

**Purpose**: Contains bundle manifests that organize and version SCDs.

**Structure**:
```
bundles/
├── project-bundle.yaml       # Master project bundle
└── domains/                  # Domain-specific bundles
    ├── architecture.yaml
    ├── security.yaml
    ├── governance.yaml
    ├── performance.yaml
    └── compliance.yaml
```

---

### `/bundles/project-bundle.yaml` - Master Project Bundle

**Purpose**: The **authoritative contract** for the entire project. Imports all domain bundles and defines the complete context.

**Example Structure**:
```yaml
id: bundle:healthcare-patient-portal
version: "1.0.0"
title: "Healthcare Patient Portal - Complete Context Bundle"
description: >
  Complete structured context bundle for the Healthcare Patient Portal project.
  This bundle represents the v1.0 contract for development and includes all
  domain-specific contexts (architecture, security, governance, performance, compliance).

imports:
  - bundle:architecture:1.0.0
  - bundle:security:1.0.0
  - bundle:governance:1.0.0
  - bundle:performance:1.0.0
  - bundle:compliance:1.0.0

scds:
  # Meta-tier SCDs (shared across all domains)
  - scd:meta:roles
  - scd:meta:capabilities
  - scd:meta:domains
  - scd:meta:concerns

provenance:
  created_by: "project-lead@company.com"
  created_at: "2025-11-20T15:00:00Z"
  updated_by: "project-lead@company.com"
  updated_at: "2025-11-20T15:00:00Z"
  rationale: >
    Version 1.0 project bundle approved by all domain teams.
    Represents complete context contract for initial development phase.
```

**Notes**:
- Project bundle imports domain bundles
- Meta-tier SCDs typically listed in project bundle (shared foundation)
- Version represents the contract version, not the software version
- Once versioned and locked, this file is immutable

---

### `/bundles/domains/` - Domain-Specific Bundles

**Purpose**: Each domain team maintains a bundle for their specific concern area.

#### Architecture Bundle Example

```yaml
# bundles/domains/architecture.yaml
id: bundle:architecture
version: "1.0.0"
title: "Architecture Context Bundle"
description: "Complete architectural context for the Healthcare Patient Portal"

scds:
  # Project-tier SCDs owned by architecture team
  - scd:project:system-context
  - scd:project:tech-stack
  - scd:project:component-model
  - scd:project:deployment-model
  - scd:project:data-flow

relationships:
  # Domain bundle can declare cross-SCD relationships
  - type: composition
    from: scd:project:system-context
    to: scd:project:component-model
    description: "System context is decomposed into components"

provenance:
  created_by: "alice@company.com"
  created_at: "2025-11-15T10:00:00Z"
  updated_by: "alice@company.com"
  updated_at: "2025-11-20T14:00:00Z"
  rationale: "Architecture context for v1.0 - approved by architecture team"
```

#### Security Bundle Example

```yaml
# bundles/domains/security.yaml
id: bundle:security
version: "1.0.0"
title: "Security Context Bundle"
description: "Complete security context for the Healthcare Patient Portal"

scds:
  # Project-tier SCDs owned by security team
  - scd:project:threat-model
  - scd:project:security-controls
  - scd:project:auth-model
  - scd:project:encryption

relationships:
  - type: satisfies
    from: scd:project:security-controls
    to: scd:standards:hipaa-164.312
    description: "Security controls satisfy HIPAA requirements"

provenance:
  created_by: "bob@company.com"
  created_at: "2025-11-16T10:00:00Z"
  updated_by: "bob@company.com"
  updated_at: "2025-11-20T14:30:00Z"
  rationale: "Security context for v1.0 - approved by security team"
```

#### Compliance Bundle Example

```yaml
# bundles/domains/compliance.yaml
id: bundle:compliance
version: "1.0.0"
title: "Compliance Context Bundle"
description: "Standards and compliance mappings for Healthcare Patient Portal"

scds:
  # Standards-tier SCDs (owned by compliance team)
  - scd:standards:hipaa-164.312
  - scd:standards:soc2

  # Project-tier SCDs (compliance mappings)
  - scd:project:hipaa-mappings
  - scd:project:audit-evidence
  - scd:project:compliance-controls

relationships:
  - type: maps-to
    from: scd:project:hipaa-mappings
    to: scd:standards:hipaa-164.312
    description: "Project implementations mapped to HIPAA requirements"

provenance:
  created_by: "carol@company.com"
  created_at: "2025-11-17T10:00:00Z"
  updated_by: "carol@company.com"
  updated_at: "2025-11-20T13:00:00Z"
  rationale: "Compliance context for v1.0 - all HIPAA mappings verified"
```

---

### `/.scs/` - SCS Configuration (Optional)

**Purpose**: Configuration for SCS tooling. This is optional but useful for customizing tool behavior.

**Example Configuration**:
```yaml
# .scs/config.yaml
version: "0.1"

# Path conventions (if different from defaults)
paths:
  context_dir: "context"
  bundles_dir: "bundles"
  schema_dir: "../scs-spec/schema"  # Path to SCS schemas

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

# Git integration
git:
  tag_versioned_bundles: true   # Automatically tag versioned bundles
  tag_format: "bundle-v{version}"  # Tag format for bundles
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

**Convention**: `{domain-name}.yaml` for domain bundles, `project-bundle.yaml` for project bundle.

**Examples**:
- `bundles/project-bundle.yaml` - Master project bundle
- `bundles/domains/architecture.yaml` - Architecture domain bundle
- `bundles/domains/security.yaml` - Security domain bundle

---

## Integration with Development Projects

### Typical Project Structure

```
my-application/
├── src/                    # Application code
├── tests/                  # Application tests
├── docs/                   # Application docs
├── context/                # SCS context
├── bundles/                # SCS bundles
├── .scs/                   # SCS config
├── package.json            # Node.js example
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

## Git Workflow

### Branch Strategy

**DRAFT Bundles** (working state):
```
feature/add-payment-processing
  ├── Modified: context/project/component-model.yaml
  ├── Modified: bundles/domains/architecture.yaml (DRAFT)
  └── Modified: bundles/domains/security.yaml (DRAFT)
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

**Tag Convention**: `bundle-v{version}` or `bundle-{bundle-name}-v{version}`

### Pull Request Workflow

1. Domain team works in feature branch (DRAFT bundles)
2. Creates PR with context changes
3. CI validates SCDs and bundles
4. Team reviews context changes
5. Merge to main (still DRAFT)
6. When ready to version:
   - Update bundle version numbers
   - Update provenance
   - Create git tag
   - Lock bundle (prevent further changes to that version)

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
          scs-validate --bundle bundles/domains/architecture.yaml
          scs-validate --bundle bundles/domains/security.yaml
          scs-validate --bundle bundles/domains/governance.yaml
          scs-validate --bundle bundles/domains/compliance.yaml

      - name: Validate project bundle
        run: |
          scs-validate --bundle bundles/project-bundle.yaml --strict

      - name: Generate validation report
        if: always()
        run: |
          scs-validate --bundle bundles/project-bundle.yaml --output json > validation-report.json

      - name: Upload validation report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: validation-report
          path: validation-report.json
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
v0.1.0 - Initial DRAFT, shared with stakeholders
v1.0.0 - First locked version, development begins
v1.1.0 - Added new component (additive change)
v1.1.1 - Fixed typo in security control description
v2.0.0 - Major architecture change (breaking change)
```

### Git Tags for Versions

```bash
# Version 1.0.0 locked
git tag -a bundle-v1.0.0 -m "Project bundle v1.0.0"
git push origin bundle-v1.0.0

# Version 1.1.0 locked
git tag -a bundle-v1.1.0 -m "Project bundle v1.1.0 - added payment component"
git push origin bundle-v1.1.0
```

**Access historical versions**:
```bash
# Check out specific bundle version
git checkout bundle-v1.0.0

# View bundle at that version
cat bundles/project-bundle.yaml
```

---

## Required vs. Recommended

### Required (Must Follow)

✅ **File Format**: SCDs must be valid YAML or JSON
✅ **Schema Compliance**: SCDs must validate against tier schemas
✅ **Bundle Structure**: Bundles must include required fields (id, version, title, description, scds, provenance)
✅ **ID Format**: SCD IDs must follow `scd:<tier>:<name>` pattern

### Recommended (Should Follow)

💡 **Directory Structure**: Use `/context/` and `/bundles/` organization
💡 **Naming Convention**: Map SCD IDs to file paths as described
💡 **Domain Bundles**: Organize by domain concerns
💡 **Git Tags**: Tag versioned bundles for easy reference
💡 **CI/CD Validation**: Validate on every PR

### Flexible (May Adapt)

🔧 **Exact directory names**: Can use different names (e.g., `scd/` instead of `context/`)
🔧 **File organization**: Can organize project-tier SCDs differently
🔧 **Tool configuration**: Can customize in `.scs/config.yaml`
🔧 **Bundle granularity**: May have more or fewer domain bundles

---

## Adapting the Structure

Teams may adapt this structure if needed. Common adaptations:

### Alternative: Flat Context Structure

```
context/
├── roles.yaml                    # Meta-tier
├── capabilities.yaml             # Meta-tier
├── hipaa.yaml                    # Standards-tier
├── system-context.yaml           # Project-tier
└── tech-stack.yaml               # Project-tier
```

**Trade-off**: Simpler but harder to navigate with many SCDs

### Alternative: Domain-Oriented Context

```
context/
├── architecture/
│   ├── system-context.yaml
│   ├── tech-stack.yaml
│   └── component-model.yaml
├── security/
│   ├── threat-model.yaml
│   └── security-controls.yaml
└── shared/
    ├── roles.yaml                # Meta-tier
    └── hipaa.yaml                # Standards-tier
```

**Trade-off**: Organized by domain but mixes tiers

### Recommendation

Start with the recommended structure. Adapt only if you have specific needs and understand the trade-offs. Ensure your adaptation is documented in `.scs/config.yaml`.

---

## Quick Start: Creating a New Project

```bash
# 1. Create project structure
mkdir my-project
cd my-project

# 2. Create directories
mkdir -p context/{meta,standards,project}
mkdir -p bundles/domains
mkdir -p .scs

# 3. Create initial meta SCD (example)
cat > context/meta/roles.yaml << 'EOF'
id: scd:meta:roles
type: meta
title: "System Roles"
version: "0.1.0"
description: "System role definitions"
content:
  roles: []
provenance:
  created_by: "you@company.com"
  created_at: "2025-11-20T10:00:00Z"
  rationale: "Initial roles definition"
EOF

# 4. Create project bundle
cat > bundles/project-bundle.yaml << 'EOF'
id: bundle:my-project
version: "0.1.0"
title: "My Project Context Bundle"
description: "Complete context for my project"
imports: []
scds:
  - scd:meta:roles
provenance:
  created_by: "you@company.com"
  created_at: "2025-11-20T10:00:00Z"
  rationale: "Initial project bundle"
EOF

# 5. Initialize git
git init
git add .
git commit -m "Initial SCS structure"

# 6. Validate
scs-validate --bundle bundles/project-bundle.yaml
```

---

## Summary

**Key Principles**:
1. **Separate concerns**: Context lives in `/context`, bundles in `/bundles`
2. **Organize by tier**: Meta, standards, and project SCDs in separate directories
3. **Convention over configuration**: Standard naming maps IDs to paths
4. **Domain ownership**: Each domain team owns a bundle
5. **Version control**: Everything in git, tags for versions
6. **Tool-friendly**: Structure designed for automation

**This structure enables**:
- Clear organization and navigation
- Tool automation (validators, viewers, AI assistants)
- Team collaboration (domain bundles)
- Version management (git tags)
- CI/CD integration (validation workflows)

---

## Related Documentation

- [Bundle Lifecycle](bundle-lifecycle.md) - How bundles evolve through development
- [Bundle Format Specification](../spec/0.1/bundle-format.md) - Technical bundle structure
- [Validation Workflow](validation-workflow.md) - How to validate your structure
- [Getting Started](getting-started.md) - Create your first SCD

---

## Questions?

- Open an [issue](https://github.com/tim-mccrimmon/scs-spec/issues)
- Start a [discussion](https://github.com/tim-mccrimmon/scs-spec/discussions)
- See the [FAQ](faq.md)
