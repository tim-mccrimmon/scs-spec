# SCS v0.1 Design Decisions

**Date**: 2025-11-24
**Status**: Canonical Reference
**Purpose**: Comprehensive documentation of all architectural and validation decisions for SCS v0.1

---

## Table of Contents

1. [Overall Philosophy](#overall-philosophy)
2. [SCD Structure Rules](#scd-structure-rules)
3. [Bundle Organization Rules](#bundle-organization-rules)
4. [Domain Requirements](#domain-requirements)
5. [Validation Rules](#validation-rules)
6. [Relationship Types](#relationship-types)
7. [Meta Bundle Versioning](#meta-bundle-versioning)
8. [Validator Implementation](#validator-implementation)
9. [Quick Reference](#quick-reference)

---

## Overall Philosophy

### Core Principle

**"Strict by Default, Flexible by Configuration"**

SCS v0.1 provides strict, production-ready defaults while enabling flexibility through configuration. This approach:
- Ensures quality and consistency out of the box
- Provides clear best practices
- Allows customization for unique requirements
- Supports progressive adoption

### Position on Spectrum

```
<-------- More Rules ----------------------- Fewer Rules -------->
   Prescriptive                                            Flexible
        |                        |                              |
      Rails                   SCS v0.1                   JavaScript
   (Convention)          (Strict + Escape Hatches)    (Do Whatever)
```

**SCS sits at**: "Opinionated with Escape Hatches"

### Key Principles

1. **Opinionated Defaults** - Make the right thing easy, the wrong thing hard (but not impossible)
2. **Clear Escape Hatches** - No feature should be a dead end
3. **Production-Ready Defaults** - Defaults should work for production systems
4. **Progressive Adoption** - Can start minimal and grow stricter

---

## SCD Structure Rules

### 1. ID Pattern - STRICT

**Rule**: SCD IDs MUST follow the pattern `scd:(meta|standards|project):<name>`

**Pattern**: `^scd:(meta|standards|project):[a-zA-Z0-9._-]+$`

**Valid examples:**
- `scd:meta:scd-meta`
- `scd:project:system-context`
- `scd:standards:hipaa-security-rule`
- `scd:project:my-org.auth-service` (organizational prefix in name portion)

**Invalid examples:**
- `meta:roles` (missing `scd:` prefix)
- `scd:project:my context` (spaces not allowed)
- `scd:foo:test` (invalid tier)

**Validator behavior**: ERROR if ID doesn't match pattern

---

### 2. Type-Tier Matching - STRICT

**Rule**: The `type` field MUST match the tier in the `id` field

**Valid:**
```yaml
id: scd:meta:roles
type: meta  # ✓ Matches
```

**Invalid:**
```yaml
id: scd:meta:roles
type: project  # ✗ Doesn't match
```

**Validator behavior**: ERROR if type doesn't match tier

**Rationale**: Prevents confusion, ensures consistency

---

### 3. Versioning - STRICT DICHOTOMY

**Rule**: Version field MUST be either `DRAFT` or strict semantic version (`X.Y.Z`)

**Pattern**: `^(\d+\.\d+\.\d+|DRAFT)$`

**Valid:**
- `version: "DRAFT"` (mutable, working state)
- `version: "1.0.0"` (immutable, locked state)
- `version: "2.3.1"`

**Invalid:**
- `version: "v1.0"` (no 'v' prefix)
- `version: "1.0"` (must be X.Y.Z)
- `version: "1.0.0-beta.1"` (no pre-release in v0.1)
- `version: "latest"`

**Validator behavior**: ERROR if version doesn't match pattern

---

### 4. Immutability - ENFORCED

**Rule**: Once an SCD is versioned (e.g., `1.0.0`), it becomes immutable

**Implications:**
- Changes require creating a new version (1.0.1, 1.1.0, 2.0.0)
- Immutability enforced through git workflow and tooling
- Validator ensures versioned SCDs pass strict validation

**DRAFT vs VERSIONED:**
- `version: "DRAFT"` - Mutable, can be edited freely
- `version: "1.0.0"` - Immutable, create new version for changes

---

### 5. Independent Versioning - CONFIRMED

**Rule**: Each SCD versions independently of bundles and other SCDs

**Implications:**
- SCD can be at version 2.3.1 while containing bundle is at 1.0.0
- Each SCD has its own version lifecycle
- Bundle version is separate from SCD versions

---

## Bundle Organization Rules

### Core Architectural Rule: Bundles XOR SCDs

**CRITICAL RULE**: A bundle MUST contain imports (references to other bundles) OR scds (references to SCDs), but NOT both.

**This is the XOR constraint**: `(imports AND NOT scds) OR (scds AND NOT imports)`

**Rationale**:
- Clear separation between aggregators (bundles) and containers (SCDs)
- Simpler mental model: leaf nodes vs branch nodes
- Consistent pattern across all bundle types

---

### 1. Project Bundle - IMPORTS ONLY

**Rule**: Project bundles MUST have empty `scds` array. They organize via `imports` only.

**Valid:**
```yaml
id: bundle:my-project
type: project
version: "1.0.0"
imports:
  - bundle:meta:0.1.0
  - bundle:standards:1.0.0
  - bundle:architecture:1.0.0
  - bundle:security:1.0.0
scds: []  # Must be empty
```

**Invalid:**
```yaml
id: bundle:my-project
type: project
imports: [bundle:meta:0.1.0]
scds: [scd:project:global-policy]  # ✗ Not allowed
```

**Validator behavior**: ERROR if project bundle contains SCDs

**Bundle role**: Branch node (aggregator/orchestrator)

---

### 2. Meta Bundle - SCDS ONLY

**Rule**: Meta bundles MUST have empty `imports` array. They contain meta-tier SCDs only.

**Valid:**
```yaml
id: bundle:meta
type: meta
version: "0.1.0"
imports: []  # Must be empty
scds:
  - scd:meta:scd-meta
  - scd:meta:bundle-meta
  - scd:meta:domain-meta
  - scd:meta:validator-meta
```

**Minimum**: 1 SCD required

**Validator behavior**: ERROR if meta bundle has imports

**Bundle role**: Leaf node (content container)

---

### 3. Domain Bundle - SCDS ONLY, NO IMPORTS

**Rule**: Domain bundles MUST have empty `imports` array. They contain project-tier SCDs only.

**Valid:**
```yaml
id: bundle:architecture
type: domain
version: "1.0.0"
imports: []  # Must be empty
scds:
  - scd:project:system-context
  - scd:project:tech-stack
  - scd:project:component-model
```

**Minimum**: 1 SCD required (changed from 2 based on XOR architecture)

**Validator behavior**: ERROR if domain bundle has imports

**Bundle role**: Leaf node (content container)

**Rationale**: Enables domain independence and parallel development

---

### 4. Standards Bundle - FOLLOWS XOR RULE

**Rule**: Standards bundles are either aggregators OR containers, not both.

**Option A: Aggregator standards bundle**
```yaml
id: bundle:standards
type: standards
version: "1.0.0"
imports:
  - bundle:standards:hipaa:1.0.0
  - bundle:standards:soc2:2023.1
scds: []  # Aggregator - no SCDs
```

**Option B: Leaf standards bundle**
```yaml
id: bundle:standards:hipaa
type: standards
version: "1.0.0"
imports: []  # Leaf - no imports
scds:
  - scd:standards:hipaa-privacy-rule
  - scd:standards:hipaa-security-rule
```

**Minimum**: None specified (can be 0 if aggregator, 1+ if leaf)

**Validator behavior**: ERROR if standards bundle has both imports AND scds

---

### 5. Cross-Domain Relationships - ALLOWED

**Rule**: Domain bundles CAN reference SCDs from other domain bundles via relationships

**Example:**
```yaml
# In bundle:security
id: scd:project:auth-service
relationships:
  - type: depends-on
    target: scd:project:system-context  # In bundle:architecture
    description: "Auth depends on system boundary definition"
```

**Validator behavior**:
- **Standalone domain bundle validation**: WARN about unresolved cross-bundle relationship targets
- **Complete project bundle validation**: ERROR if relationship targets don't exist

**Rationale**: Domains interact in real systems, better traceability

---

### 6. SCD Uniqueness - GLOBALLY UNIQUE

**Rule**: SCD IDs must be unique across the entire loaded bundle set (project bundle + all imported bundles)

**Validation**: When project bundle loads all imports, validator checks for duplicate SCD IDs

**Validator behavior**: ERROR if duplicate SCD IDs found across loaded bundles

**Rationale**: Prevents ambiguity in relationships and references

---

## Domain Requirements

### 1. Prescribed Domains - 10 REQUIRED BY DEFAULT

**Rule**: Default completeness rules require all 10 prescribed domains

**The 10 prescribed domains:**
1. **Architecture** - System structure, components, boundaries
2. **Security** - Threat models, auth, data protection
3. **Performance & Reliability** - Performance, scalability, availability
4. **Usability & Accessibility** - UX, accessibility, interaction patterns
5. **Compliance & Governance** - Regulatory compliance, audit, governance
6. **Data & Provenance** - Data models, flow, governance, provenance
7. **Testing & Validation** - Testing strategy, QA, verification
8. **Deployment & Operations** - Deployment, monitoring, incident response
9. **Safety & Risk** - Safety requirements, risk assessment, hazard analysis
10. **Ethics & AI Accountability** - Ethical considerations, AI governance, bias

**Customization**: Projects can create `.scs/completeness-rules.yaml` to require fewer domains

**Validator behavior**: ERROR (by default) if project doesn't have all 10 domains

---

### 2. Minimum SCDs per Domain - 1 SCD

**Rule**: Domain bundles must have minimum 1 SCD (structural requirement)

**Validator behavior**: ERROR if domain bundle has 0 SCDs

**Recommended SCDs**: Completeness rules define recommended SCDs per domain (guidance, not strict enforcement)

**Changed from**: Originally 2 SCDs minimum, reduced to 1 based on XOR architecture enabling fine-grained bundles

---

### 3. Additional Domains - ALLOWED

**Rule**: Projects MAY add additional domain bundles beyond the prescribed 10

**Examples of additional domains:**
- Internationalization (i18n)
- Legal (licensing, contracts)
- Business Continuity
- Integration
- Cost Management
- Industry-specific domains (clinical workflows, trading systems, etc.)

---

### 4. Completeness Validation - CONFIGURABLE

**Default behavior**: Strict validation requiring all 10 domains

**Customization paths:**
1. **Project-specific rules**: Create `.scs/completeness-rules.yaml`
2. **Skip validation**: Use `--skip-completeness` flag
3. **Custom rules file**: Use `--completeness-rules path/to/rules.yaml`

**Rule priority:**
1. Explicit `--completeness-rules` flag (highest)
2. Project-specific `.scs/completeness-rules.yaml`
3. Default validator rules (fallback)

---

## Validation Rules

### The 6 Validation Levels

**Level 1: Syntactic Validation**
- Check: Is the file valid YAML or JSON?
- Severity: ERROR
- When: Always

**Level 2: Schema Validation**
- Check: Does the SCD/bundle match the required JSON Schema?
- Severity: ERROR
- When: Always

**Level 3: Semantic Validation**
- Check: Do the contents make logical sense? (type-tier matching, valid semver, etc.)
- Severity: ERROR
- When: Always

**Level 4: Relationship Validation**
- Check: Are relationships valid and do targets exist?
- Severity: ERROR (or WARNING for unresolved cross-bundle refs in standalone validation)
- When: Always

**Level 5: Bundle Validation**
- Check: Is the bundle complete and consistent?
- Severity: ERROR
- When: Always

**Level 6: Completeness/Compliance Validation**
- Check: Does the bundle satisfy completeness requirements?
- Severity: CONFIGURABLE (default: ERROR)
- When: Unless skipped with `--skip-completeness`

---

### Validation Execution Order

**Sequential with dependencies:**
```
Level 1 (Syntax) → MUST pass before proceeding
  ↓
Level 2 (Schema) → MUST pass before proceeding
  ↓
Level 3 (Semantic) + Level 4 (Relationship) → Can run concurrently
  ↓
Level 5 (Bundle) → Requires 1-4 to pass
  ↓
Level 6 (Completeness) → Requires 5 to pass
```

**Error reporting**: Show ALL errors within each level, stop at first failing level

---

### DRAFT vs VERSIONED Mode

**DRAFT mode (version: "DRAFT"):**
- ✅ Validates: Syntax (L1), Schema (L2), Semantic (L3)
- ⚠️ Warns: Incomplete relationships (L4), Incomplete bundles (L5)
- ⏭️ Skips: Completeness validation (L6) unless explicitly enabled

**VERSIONED mode (version: "X.Y.Z"):**
- All levels run with strict ERROR severity

**Rationale**: Catch structural problems early, but allow iteration on completeness

---

### Validation Flags

```bash
# Standard validation
scs-validate --bundle bundle.yaml

# Skip completeness
scs-validate --bundle bundle.yaml --skip-completeness

# Extra strict (warnings become errors)
scs-validate --bundle bundle.yaml --strict

# Custom completeness rules
scs-validate --bundle bundle.yaml --completeness-rules my-rules.yaml

# JSON output for CI/CD
scs-validate --bundle bundle.yaml --output json
```

---

## Relationship Types

### The 7 Relationship Types

1. **depends-on** - This SCD requires another SCD
2. **satisfies** - This SCD fulfills requirements from another SCD
3. **constrains** - This SCD imposes constraints on another SCD
4. **refines** - This SCD provides more detail for another SCD
5. **extends** - This SCD builds upon another SCD
6. **conflicts-with** - This SCD has conflicts with another SCD
7. **implements** - This SCD implements specifications from another SCD

**No additions for v0.1** - Can be expanded in future versions

---

### Relationship Properties

**Directionality**: All relationships are directional (source → target)

**Metadata fields:**
- `type` (required) - One of the 7 types
- `target` (required) - SCD ID
- `description` (optional but recommended) - Why this relationship exists

**No additional metadata in v0.1** (strength, version_constraint, etc. can be added later)

---

### Tier Constraints

**Rule**: Relationships must follow tier constraint rules defined in `relationship-rules.yaml`

**Examples:**

**satisfies** - Project satisfies standards (compliance)
- Allowed: project → standards
- Not allowed: meta → standards, standards → project

**depends-on** - Layers depend on same level or foundation
- Allowed: project → (meta, project), standards → (meta, standards), meta → meta
- Not allowed: standards → project, meta → standards

**implements** - Project implements specs or standards
- Allowed: project → (project, standards)
- Not allowed: meta → project

**Validator behavior**: ERROR if relationship violates tier constraints

---

### Relationship Validation (Level 4)

**Checks performed:**
1. **target_exists** (ERROR) - Relationship target SCD must exist in loaded bundles
2. **tier_constraints** (ERROR) - Relationship must follow tier constraint rules
3. **no_self_reference** (ERROR) - SCD cannot have relationship to itself
4. **acyclic_depends_on** (WARNING) - Circular depends-on relationships detected

**Context-aware validation:**
- Standalone bundle: WARN if target not in bundle (may be in another bundle)
- Complete project bundle: ERROR if target doesn't exist anywhere

---

## Meta Bundle Versioning

### 1. Versioning Cadence - ALIGNED WITH SCS SPEC

**Rule**: Meta bundle version matches SCS specification version

**Versioning scheme:**
- SCS 0.1 → `bundle:meta:0.1.0`
- SCS 0.2 → `bundle:meta:0.2.0`
- SCS 1.0 → `bundle:meta:1.0.0`

**Rationale**: Meta bundle IS the spec language definition, clear alignment

---

### 2. Version Pinning - SPECIFIC VERSION REQUIRED

**Rule**: Projects MUST pin to specific meta bundle version

**Required pattern**: `bundle:meta:X.Y.Z`

**Valid:**
```yaml
imports:
  - bundle:meta:0.1.0  # ✓ Specific version
```

**Invalid:**
```yaml
imports:
  - bundle:meta:0.x      # ✗ No ranges
  - bundle:meta:latest   # ✗ No latest
  - bundle:meta          # ✗ No version
```

**Validator behavior**: ERROR if meta bundle import lacks specific version

---

### 3. Semantic Versioning - STRICT

**Rule**: Meta bundle follows strict semantic versioning

**Version changes:**
- **Patch** (0.1.0 → 0.1.1): Bug fixes, typos, documentation only - Backward compatible
- **Minor** (0.1.0 → 0.2.0): New features, backward compatible
- **Major** (0.1.0 → 1.0.0): Breaking changes - NOT backward compatible

**Examples:**
| Change | Version | Compatible? |
|--------|---------|-------------|
| Fix typo | Patch | Yes |
| Add relationship type | Minor | Yes |
| Add optional field | Minor | Yes |
| Change ID pattern | Major | No |
| Remove bundle type | Major | No |

---

### 4. Version Synchronization

**Rule**: All META SCDs version together with the meta bundle

**Structure:**
```yaml
# bundle:meta:0.1.0
version: "0.1.0"  # Bundle version (canonical)
scds:
  - scd:meta:scd-meta          # version: "0.1.0"
  - scd:meta:bundle-meta       # version: "0.1.0"
  - scd:meta:domain-meta       # version: "0.1.0"
  - scd:meta:validator-meta    # version: "0.1.0"
```

**Rationale**: Simpler reasoning - "I'm on meta bundle 0.1.0" vs tracking 4 SCD versions

---

### 5. Version Checking

**Rule**: Validator checks meta bundle version and warns about mismatches

**Behavior:**
- Info: Shows which meta bundle version is being used
- Warning: If newer version available
- Error: If version too old (unsupported)

**Validation uses rules for the specified meta bundle version**

---

## Validator Implementation

### Rules Directory Structure

```
tools/scd-validator/
├── rules/
│   └── v0.1.0/                       # Versioned with validator
│       ├── scd-rules.yaml            # SCD structure rules
│       ├── bundle-rules.yaml         # Bundle type rules
│       ├── relationship-rules.yaml   # Relationship rules
│       └── completeness-rules.yaml   # Completeness rules (strict default)
└── src/
    └── scs_validator/
```

### Project Configuration

```
my-project/
├── .scs/                             # SCS configuration directory
│   └── completeness-rules.yaml      # Custom rules (optional)
├── context/
│   ├── meta/
│   ├── standards/
│   └── project/
└── bundles/
```

### Rule Loading Priority

1. Explicit `--completeness-rules` flag (highest priority)
2. Project-specific `.scs/completeness-rules.yaml`
3. Default validator `rules/v0.1.0/completeness-rules.yaml` (fallback)

---

## Quick Reference

### Valid SCD Example

```yaml
id: scd:project:system-context
type: project
title: "System Context and Boundaries"
version: "1.0.0"
description: "Defines the system boundaries and external integrations"

content:
  system_boundary: "..."
  external_systems: [...]
  integration_points: [...]

relationships:
  - type: depends-on
    target: scd:meta:roles
    description: "System context depends on role definitions"
  - type: satisfies
    target: scd:standards:hipaa-privacy-rule
    description: "System boundaries satisfy HIPAA privacy requirements"

provenance:
  created_by: "alice@company.com"
  created_at: "2025-01-15T10:00:00Z"
  updated_by: "bob@company.com"
  updated_at: "2025-01-20T14:30:00Z"
  rationale: "Updated to include new external integration with Lab system"
```

### Valid Bundle Examples

**Project Bundle:**
```yaml
id: bundle:medication-adherence
type: project
version: "1.0.0"
title: "Medication Adherence Platform"
description: "AI-powered medication adherence monitoring system"

imports:
  - bundle:meta:0.1.0
  - bundle:standards:1.0.0
  - bundle:architecture:1.0.0
  - bundle:security:1.0.0
  - bundle:performance-reliability:1.0.0
  # ... all 10 domain bundles

scds: []  # Empty - all SCDs in imported bundles

provenance:
  created_by: "project-lead@company.com"
  created_at: "2025-01-10T09:00:00Z"
```

**Domain Bundle:**
```yaml
id: bundle:architecture
type: domain
version: "1.0.0"
title: "Architecture Domain Bundle"
description: "System architecture and design decisions"

imports: []  # Domain bundles don't import

scds:
  - scd:project:system-context
  - scd:project:tech-stack
  - scd:project:component-model
  - scd:project:integration-map

provenance:
  created_by: "architect@company.com"
  created_at: "2025-01-12T11:00:00Z"
```

### Validation Command Quick Reference

```bash
# Basic validation
scs-validate --bundle bundles/project-bundle.yaml

# Skip completeness for development
scs-validate --bundle bundles/project-bundle.yaml --skip-completeness

# Use custom completeness rules
scs-validate --bundle bundles/project-bundle.yaml \
  --completeness-rules .scs/completeness-rules.yaml

# Extra strict mode
scs-validate --bundle bundles/project-bundle.yaml --strict

# JSON output for CI/CD
scs-validate --bundle bundles/project-bundle.yaml --output json

# Validate standalone domain bundle
scs-validate --bundle bundles/domains/architecture.yaml
# (Will warn about cross-bundle relationship targets)

# Validate complete project
scs-validate --bundle bundles/project-bundle.yaml
# (Will error if relationship targets don't exist)
```

---

## Document Metadata

**Version**: 0.1.0
**Last Updated**: 2025-11-24
**Related Documents**:
- Issue 01-07 in `/docs/issue-*.md`
- `.private/bundle-implementation-questions-ANSWERED.md`
- `context/meta/*.yaml` (META SCDs)
- `schema/bundles/scd-bundle-schema.json`

**Status**: CANONICAL - This document represents the authoritative design decisions for SCS v0.1

---

## Change History

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-24 | 0.1.0 | Initial canonical design decisions document |

