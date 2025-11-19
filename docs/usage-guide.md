# SCS Usage Guide

**Version**: 0.1
**Last Updated**: 2025-11-19

---

## Overview

This guide walks you through practical use of the Structured Context Specification (SCS). You'll learn:
- How to create your first SCD
- How to build a complete bundle
- Best practices for organizing SCDs
- Common patterns and anti-patterns
- How to use relationships effectively

**Prerequisites**: Familiarity with YAML or JSON. Basic understanding of SCS concepts (see [overview.md](../spec/0.1/overview.md)).

---

## Table of Contents

1. [Understanding the Three Tiers](#understanding-the-three-tiers)
2. [Creating Your First SCD](#creating-your-first-scd)
3. [Building a Bundle](#building-a-bundle)
4. [Working with Relationships](#working-with-relationships)
5. [Organizing Your SCDs](#organizing-your-scds)
6. [Versioning SCDs](#versioning-scds)
7. [Common Patterns](#common-patterns)
8. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
9. [Next Steps](#next-steps)

---

## Understanding the Three Tiers

Before creating SCDs, understand what each tier is for:

### Meta-Tier: The Semantic Foundation

**Purpose**: Define the "language" your system speaks

**Contains**:
- Roles (who interacts with the system)
- Capabilities (what the system can do, conceptually)
- Domains (conceptual areas like "clinical", "financial")
- Concerns (cross-cutting issues like security, privacy)

**Think of it as**: The shared vocabulary and concepts that everything else builds on

**Example IDs**:
- `scd:meta:roles`
- `scd:meta:security-concerns`
- `scd:meta:clinical-domain`

---

### Standards-Tier: External Obligations

**Purpose**: Represent external standards and regulations as importable contracts

**Contains**:
- Regulatory requirements (HIPAA, SOC2, GDPR)
- Compliance controls
- Industry standards
- Organizational policies

**Think of it as**: The rules you must follow, made explicit and machine-readable

**Example IDs**:
- `scd:standards:hipaa-164.312`
- `scd:standards:soc2:cc6.6`
- `scd:standards:internal-security-policy`

**Key feature**: These can be shared via the scs-registry so you don't have to reinvent HIPAA compliance

---

### Project-Tier: Your Actual System

**Purpose**: Describe what you're building

**Contains**:
- Architecture and components
- Features and requirements
- Security implementations
- Data flows
- Performance targets
- Links to standards (via relationships)

**Think of it as**: Your system's blueprint, connected to standards and meta-concepts

**Example IDs**:
- `scd:project:architecture`
- `scd:project:auth-service`
- `scd:project:patient-data-flow`

---

## Creating Your First SCD

Let's create a simple meta-tier SCD that defines roles for a healthcare application.

### Step 1: Choose Your Tier and Name

**Decision**: We're defining roles, so this is **meta-tier**

**ID**: `scd:meta:roles`

**Filename**: `context/meta/roles.yaml` (or any organized structure)

---

### Step 2: Copy the Template

Start with the [meta-tier template](../../templates/scd/meta_scd_template.yaml):

```bash
cp templates/scd/meta_scd_template.yaml context/meta/roles.yaml
```

---

### Step 3: Fill in Basic Fields

```yaml
id: scd:meta:roles
type: meta
title: "System Roles and Responsibilities"
version: "0.1.0"
description: >
  Defines the primary roles that interact with the healthcare platform,
  including patients, clinicians, administrators, and system agents.
```

**Key points**:
- `id` must follow pattern: `scd:meta:<name>`
- `type` must be `meta`
- `version` follows semver (start with 0.1.0)
- `description` should be 1-3 sentences

---

### Step 4: Fill in Content

For roles, use the `roles` section:

```yaml
content:
  roles:
    - id: role:patient
      name: "Patient"
      description: >
        End user who receives care. Patients can view their own records,
        schedule appointments, and communicate with care team.
      responsibilities:
        - "Access personal health information"
        - "Schedule and manage appointments"
        - "Communicate with care providers"
      trust_level: "standard"

    - id: role:clinician
      name: "Clinician"
      description: >
        Healthcare provider who delivers care. Clinicians can access patient
        records, create care plans, and prescribe treatments.
      responsibilities:
        - "Access patient health information"
        - "Create and modify care plans"
        - "Prescribe medications"
        - "Document clinical encounters"
      trust_level: "high"

    - id: role:administrator
      name: "System Administrator"
      description: >
        Technical staff who manage the system infrastructure and user access.
      responsibilities:
        - "Manage user accounts and permissions"
        - "Monitor system health"
        - "Configure system settings"
      trust_level: "high"
```

**Delete** sections you don't need (capabilities, domains, concerns).

---

### Step 5: Add Provenance

This tracks who created the SCD and why:

```yaml
provenance:
  created_by: "tim@ohanaconsulting.ai"
  created_at: "2025-11-19T10:00:00Z"
  updated_by: "tim@ohanaconsulting.ai"
  updated_at: "2025-11-19T10:00:00Z"
  rationale: >
    Initial role definitions based on HIPAA privacy rule requirements
    and clinical workflow analysis.
```

**Key points**:
- Use ISO8601 timestamps
- `created_by` and `updated_by` should be identifiable (email, ID)
- `rationale` explains **why** this SCD exists

---

### Step 6: Validate

Check that your YAML is valid:

```bash
# Basic YAML validation
yamllint context/meta/roles.yaml

# Schema validation (once validator exists)
scs-validate context/meta/roles.yaml
```

---

### Complete Example

Here's your complete first SCD:

```yaml
id: scd:meta:roles
type: meta
title: "System Roles and Responsibilities"
version: "0.1.0"
description: >
  Defines the primary roles that interact with the healthcare platform,
  including patients, clinicians, administrators, and system agents.

content:
  roles:
    - id: role:patient
      name: "Patient"
      description: >
        End user who receives care. Can view own records and schedule appointments.
      responsibilities:
        - "Access personal health information"
        - "Schedule and manage appointments"
      trust_level: "standard"

    - id: role:clinician
      name: "Clinician"
      description: >
        Healthcare provider who delivers care and manages patient information.
      responsibilities:
        - "Access patient health information"
        - "Create and modify care plans"
        - "Prescribe medications"
      trust_level: "high"

relationships: []

provenance:
  created_by: "tim@ohanaconsulting.ai"
  created_at: "2025-11-19T10:00:00Z"
  updated_by: "tim@ohanaconsulting.ai"
  updated_at: "2025-11-19T10:00:00Z"
  rationale: >
    Initial role definitions based on HIPAA requirements and clinical workflows.
```

**Congratulations!** You've created your first SCD.

---

## Building a Bundle

A **bundle** is a collection of SCDs that together define your system. Let's build one.

### Typical Bundle Structure

```
my-project/
├── context/
│   ├── meta/
│   │   ├── roles.yaml
│   │   ├── capabilities.yaml
│   │   └── security-concerns.yaml
│   ├── standards/
│   │   ├── hipaa-privacy.yaml
│   │   └── hipaa-security.yaml
│   └── project/
│       ├── architecture.yaml
│       ├── auth-service.yaml
│       └── patient-api.yaml
└── bundle.yaml
```

### Creating a Bundle Manifest

The `bundle.yaml` file lists all SCDs in your bundle:

```yaml
id: bundle:healthcare-platform
version: "0.1.0"
title: "Healthcare Platform Context Bundle"
description: >
  Complete structured context for the HIPAA-compliant healthcare platform.

metadata:
  created_at: "2025-11-19"
  authors:
    - "tim@ohanaconsulting.ai"
  organization: "Ohana Consulting LLC"
  project_phase: "development"

imports:
  # External standards from registry (future)
  # - registry:hipaa:164.312
  # - registry:soc2:cc6.6

scds:
  # Meta-tier SCDs
  - path: context/meta/roles.yaml
    id: scd:meta:roles

  - path: context/meta/capabilities.yaml
    id: scd:meta:capabilities

  - path: context/meta/security-concerns.yaml
    id: scd:meta:security-concerns

  # Standards-tier SCDs
  - path: context/standards/hipaa-privacy.yaml
    id: scd:standards:hipaa-164.308

  - path: context/standards/hipaa-security.yaml
    id: scd:standards:hipaa-164.312

  # Project-tier SCDs
  - path: context/project/architecture.yaml
    id: scd:project:architecture

  - path: context/project/auth-service.yaml
    id: scd:project:auth-service

  - path: context/project/patient-api.yaml
    id: scd:project:patient-api

provenance:
  created_by: "tim@ohanaconsulting.ai"
  created_at: "2025-11-19T10:00:00Z"
  updated_by: "tim@ohanaconsulting.ai"
  updated_at: "2025-11-19T10:00:00Z"
  rationale: >
    Initial bundle for HIPAA-compliant healthcare platform MVP.
```

### Bundle Requirements

**Must have**:
- At least one meta-tier SCD (defines semantics)
- At least one project-tier SCD (defines your system)

**Should have**:
- Standards-tier SCDs if you have compliance requirements

**Optional**:
- Imports from registry (when available)

---

## Working with Relationships

Relationships create the **knowledge graph** that enables autonomic governance.

### Common Relationship Types

| Type | Meaning | Example |
|------|---------|---------|
| `satisfies` | Project implements a standard requirement | `scd:project:auth-service` → `scd:standards:hipaa-164.312(d)` |
| `depends-on` | One component depends on another | `scd:project:patient-api` → `scd:project:auth-service` |
| `implements` | Project implements a meta capability | `scd:project:care-plan-module` → `scd:meta:capability:care-management` |
| `constrains` | One SCD constrains another | `scd:meta:security-concerns` → `scd:project:patient-api` |
| `refines` | Provides more detail | `scd:project:auth-details` → `scd:project:architecture` |
| `extends` | Adds to another SCD | `scd:meta:extended-roles` → `scd:meta:roles` |
| `informed-by` | Decision influenced by | `scd:project:architecture` → `scd:standards:12-factor-app` |

### Adding Relationships

In your project-tier SCD for an auth service:

```yaml
id: scd:project:auth-service
type: project
title: "Authentication & Authorization Service"
version: "0.1.0"

content:
  architecture:
    components:
      - id: component:auth-api
        name: "Auth API"
        description: "OAuth2-based authentication service"

  security:
    security_controls:
      - id: sec:encryption-at-rest
        name: "Data Encryption at Rest"
        method: "AES-256"
        requirement_level: "Required"

relationships:
  # This service satisfies HIPAA encryption requirements
  - type: satisfies
    target: scd:standards:hipaa-164.312(a)(2)(iv)
    description: >
      Auth service encrypts all stored credentials using AES-256,
      satisfying HIPAA's encryption at rest requirement.

  # This service implements the authentication capability
  - type: implements
    target: scd:meta:capability:authentication
    description: >
      Provides OAuth2-based authentication for all system roles.

  # Other services depend on this
  - type: depended-on-by
    target: scd:project:patient-api
    description: >
      Patient API requires authentication from this service.

provenance:
  created_by: "tim@ohanaconsulting.ai"
  created_at: "2025-11-19T11:00:00Z"
  rationale: >
    OAuth2 chosen for standards compliance and token-based access control.
```

### Why Relationships Matter

**Without relationships**:
- "Are we HIPAA compliant?" → Manual audit
- "What breaks if I change auth?" → Guesswork
- "Why do we need encryption?" → Ask someone who remembers

**With relationships**:
- "Are we HIPAA compliant?" → Validator checks all `satisfies` relationships
- "What breaks if I change auth?" → Query `depended-on-by` relationships
- "Why do we need encryption?" → Follow `satisfies` to HIPAA standard

**This is what enables autonomic governance.**

---

## Organizing Your SCDs

### Recommended Directory Structure

```
context/
├── bundle.yaml              # Bundle manifest
├── meta/
│   ├── roles.yaml           # One SCD per major concept
│   ├── capabilities.yaml
│   ├── domains.yaml
│   └── security-concerns.yaml
├── standards/
│   ├── hipaa/
│   │   ├── privacy-rule.yaml
│   │   └── security-rule.yaml
│   ├── soc2/
│   │   └── cc6-logical-access.yaml
│   └── internal/
│       └── security-policy.yaml
└── project/
    ├── architecture.yaml    # High-level system design
    ├── components/
    │   ├── auth-service.yaml
    │   ├── patient-api.yaml
    │   └── care-plan-module.yaml
    ├── data-flows/
    │   └── patient-data-flow.yaml
    └── security/
        └── security-controls.yaml
```

### Organization Principles

**1. One Concept Per SCD**
- ✅ `roles.yaml` contains all roles
- ❌ Don't split roles across multiple files unless there's a clear reason

**2. Group by Tier**
- Keep meta/, standards/, and project/ separate
- Makes it easy to see architectural layers

**3. Subdivide Project Tier**
- Project tier will have the most SCDs
- Group by: components/, data-flows/, security/, requirements/, etc.

**4. Use Meaningful Names**
- ✅ `auth-service.yaml`
- ❌ `project-scd-1.yaml`

**5. Keep Bundle Manifest at Root**
- `bundle.yaml` should be at the top of your context/ folder
- Easy to find, easy to reference

---

## Versioning SCDs

### When to Bump Version

**PATCH** (0.1.0 → 0.1.1):
- Typo fixes
- Clarified descriptions
- Added examples
- No semantic changes

**MINOR** (0.1.0 → 0.2.0):
- Added new roles/capabilities/components
- Added optional fields
- Expanded coverage
- Backwards compatible

**MAJOR** (0.1.0 → 1.0.0):
- Removed roles/capabilities/components
- Changed IDs (breaks relationships)
- Incompatible structural changes
- Breaking changes

### Version in Sync or Independent?

**Bundle version**: Tracks the collection as a whole

**SCD versions**: Track individual SCDs

**They don't have to match!**

Example:
```
bundle.yaml → version: 0.3.0
  ├─ scd:meta:roles → version: 1.0.0 (stable)
  ├─ scd:project:architecture → version: 0.2.0 (still evolving)
  └─ scd:project:new-feature → version: 0.1.0 (brand new)
```

**Best practice**:
- Meta-tier SCDs stabilize faster (0.x → 1.0 early)
- Project-tier SCDs evolve more (stay 0.x longer)
- Bundle version reflects overall maturity

---

## Common Patterns

### Pattern 1: Import Standards from Registry

Instead of writing `scd:standards:hipaa` yourself:

```yaml
# In bundle.yaml
imports:
  - registry:hipaa:164.312  # Official HIPAA SCD from registry
  - registry:soc2:cc6.6     # Official SOC2 SCD from registry
```

Then reference in relationships:

```yaml
# In scd:project:auth-service
relationships:
  - type: satisfies
    target: scd:standards:hipaa-164.312(d)  # From imported registry SCD
```

**Benefits**:
- Don't reinvent compliance requirements
- Updates flow from registry
- Standardized across industry

---

### Pattern 2: Meta-First Development

Start with meta-tier before project-tier:

1. Define roles, capabilities, domains, concerns (meta)
2. Import or create standards (standards)
3. Build project components that reference meta + standards (project)

**Why**: Ensures your project-tier has a solid semantic foundation

---

### Pattern 3: Component SCDs

Instead of one giant `architecture.yaml`, create one SCD per major component:

```
project/
  components/
    ├── auth-service.yaml
    ├── patient-api.yaml
    ├── care-plan-module.yaml
    ├── notification-service.yaml
    └── analytics-engine.yaml
```

Each component SCD:
- Describes one service/module
- Has its own relationships
- Can be versioned independently

**Benefits**:
- Easier to maintain
- Clear ownership
- Parallel development

---

### Pattern 4: Layered Compliance

For multiple compliance frameworks:

```yaml
# scd:project:auth-service
relationships:
  # HIPAA
  - type: satisfies
    target: scd:standards:hipaa-164.312(a)(2)(iv)

  # SOC2
  - type: satisfies
    target: scd:standards:soc2:cc6.1

  # Internal policy
  - type: satisfies
    target: scd:standards:internal:password-policy
```

**Governance agent can check**: "Are we compliant with all three frameworks?"

---

## Anti-Patterns to Avoid

### ❌ Anti-Pattern 1: Kitchen Sink SCD

**Bad**:
```yaml
id: scd:project:everything
# 500 lines covering architecture, security, data flows, requirements...
```

**Why bad**: Impossible to maintain, unclear ownership, massive version churn

**Instead**: Split into focused SCDs

---

### ❌ Anti-Pattern 2: Empty Relationships

**Bad**:
```yaml
relationships: []
# or
relationships:
  - type: related-to
    target: scd:project:something
```

**Why bad**: Defeats the purpose of SCS - no governance graph!

**Instead**: Be explicit about how SCDs connect

---

### ❌ Anti-Pattern 3: Vague Descriptions

**Bad**:
```yaml
description: "Auth stuff"
```

**Why bad**: Not helpful to humans or AI

**Instead**:
```yaml
description: >
  OAuth2-based authentication service providing identity verification
  and access token management for all system roles, implementing
  HIPAA-compliant credential storage.
```

---

### ❌ Anti-Pattern 4: No Provenance

**Bad**:
```yaml
provenance:
  created_by: "someone"
  created_at: "yesterday"
```

**Why bad**: No accountability, no audit trail

**Instead**: Use real identities and ISO timestamps

---

### ❌ Anti-Pattern 5: Copying Standards Wrong

**Bad**: Copying HIPAA text verbatim into your project SCD

**Instead**:
- Create `scd:standards:hipaa` separately
- Reference it via `satisfies` relationships from project SCDs

---

### ❌ Anti-Pattern 6: Skipping Meta Tier

**Bad**: Jumping straight to project-tier without defining meta concepts

**Why bad**: No shared vocabulary, relationships are vague

**Instead**: Start with meta-tier (roles, capabilities, concerns)

---

## Next Steps

### You've Learned:
- ✅ How to create SCDs for all three tiers
- ✅ How to build a bundle
- ✅ How to use relationships
- ✅ How to organize your context/
- ✅ Common patterns and anti-patterns

### What's Next:

1. **Create Your Bundle**
   - Start with meta-tier (roles, capabilities)
   - Add standards (or plan to import from registry)
   - Build project-tier SCDs

2. **Validate Your Bundle**
   - See [validation-workflow.md](validation-workflow.md)
   - Use the SCS validator tool

3. **Integrate with CEDM**
   - SCDs are the "Context" phase of CEDM
   - See the CEDM book for the full methodology

4. **Explore Examples**
   - See `examples/` folder for complete bundles
   - Healthcare, e-commerce, and internal tool examples

5. **Join the Community**
   - Share your SCDs
   - Contribute to the registry
   - Ask questions in GitHub Discussions

---

## Resources

- **Specification**: [spec/0.1/](../spec/0.1/)
- **Templates**: [templates/](../../templates/)
- **Examples**: [examples/](../../examples/) (coming soon)
- **Schema Reference**: [schema/](../../schema/)
- **FAQ**: [faq.md](faq.md)
- **Getting Started**: [getting-started.md](getting-started.md)

---

## Questions?

- Open an issue on GitHub
- Start a discussion
- See the [FAQ](faq.md)

**Happy context engineering!**
