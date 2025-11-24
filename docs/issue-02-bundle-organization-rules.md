# Issue 02: Review Bundle Organization Rules

## Overview

The **BUNDLE-META** specification defines how bundles organize SCDs, the four bundle types, and their constraints. These rules determine how projects structure their context and how teams can work together.

## Current Rules (from BUNDLE-META)

### Bundle Type Rules

#### Project Bundle (type: project)
- **MUST** import meta, standards, and domain bundles
- SCDs **typically empty** (all context in imported bundles)
- **Cardinality**: 1 per project

#### Meta Bundle (type: meta)
- **MUST NOT** import other bundles (`imports: []`)
- Contains meta-tier SCDs only
- **Cardinality**: 1 per project (imported from SCS-Spec)

#### Standards Bundle (type: standards)
- **MAY** import other standards bundles
- Contains standards-tier SCDs only
- **Cardinality**: 1 per project

#### Domain Bundle (type: domain)
- **MUST NOT** import other bundles (`imports: []`)
- **MUST** contain at least 1 project-tier SCD
- **Cardinality**: 10+ per project

### Bundle Hierarchy Rule
```
Project Bundle (top-level)
├── Meta Bundle (foundation)
├── Standards Bundle (compliance)
└── Domain Bundles (10+ domains)
```

### Validation Rules
- All SCD references MUST resolve to actual files
- All bundle imports MUST resolve to actual files
- NO circular imports
- SCD IDs MUST be unique within bundle

## Questions for Community

### 1. Project Bundle Content
**Question**: Should project bundles be allowed to contain SCDs directly, or should they always just import?

**Current Rule**: "SCDs typically empty"

**Implications**:

**Option A: Empty (imports only)**
**Pros**:
- Clear separation of concerns
- Forces organization into domains
- Cleaner hierarchy
- Easier to reason about

**Cons**:
- What if you have SCDs that don't fit into domains?
- Less flexible
- May force artificial categorization
- Where do "cross-domain" SCDs go?

**Option B: Allow SCDs in project bundle**
**Pros**:
- More flexible
- Can handle cross-domain SCDs
- Easier for small projects
- Natural place for project-wide SCDs

**Cons**:
- Less clear organization
- May encourage poor organization
- Harder to validate
- When should you use project bundle vs. domain bundles?

### 2. Domain Bundle Import Restriction
**Question**: Is the "no imports" rule for domain bundles too restrictive?

**Current Rule**: Domain bundles MUST NOT import other bundles

**Implications**:

**Pros (no imports)**:
- Domain independence
- Parallel development
- Clear boundaries
- No circular dependencies

**Cons (no imports)**:
- Domains may need shared context
- Can't reuse across domains
- May force duplication
- What about domain-specific standards?

**Potential Issues**:
- What if the security domain needs to reference architecture SCDs?
- Should domains share a "common" bundle?
- How do cross-domain concerns work?

### 3. Domain Bundle Relationships
**Question**: Should domain bundles be allowed to reference SCDs from other domain bundles via relationships?

**Current Rule**: Not explicitly addressed

**Implications**:

**Allow cross-domain relationships**
**Pros**:
- More realistic (domains do interact)
- Better traceability
- Can model dependencies
- More expressive

**Cons**:
- Creates coupling between domains
- May break parallel development
- Validation becomes complex
- Circular relationship risk

**Disallow cross-domain relationships**
**Pros**:
- Clean separation
- True independence
- Simpler validation
- Parallel development guaranteed

**Cons**:
- Unrealistic (domains do interact)
- Can't model real dependencies
- May force artificial workarounds

### 4. Minimum Bundle Set
**Question**: Should we require 1 project, 1 meta, 1 standards, and 10 domain bundles for ALL projects?

**Current Rule**: Production projects MUST include this minimum set

**Implications**:

**Pros (strict minimum)**:
- Ensures comprehensive coverage
- Prevents overlooking concerns
- Standard structure
- Easier tooling

**Cons (strict minimum)**:
- May be overkill for simple projects
- Creates overhead for small teams
- Could discourage adoption
- Some domains may not be relevant

**Potential Issues**:
- Should we have a "minimal viable" tier for small projects?
- Can domains be optional for certain project types?
- What about proof-of-concepts or experiments?

### 5. Standards Bundle Imports
**Question**: Should standards bundles be allowed to import other standards bundles?

**Current Rule**: Standards bundles MAY import other standards bundles

**Implications**:

**Pros (allow imports)**:
- Can compose standards (HIPAA + SOC2)
- Reuse standard definitions
- Build on existing work
- Hierarchical standards

**Cons (allow imports)**:
- Complexity
- Version conflicts
- Circular dependency risk
- Which version wins?

**Potential Issues**:
- How do we handle conflicting standards?
- Should there be limits on import depth?
- What about standard "profiles" or "baselines"?

### 6. Bundle Uniqueness
**Question**: Should SCD IDs be unique across ALL bundles or just within a bundle?

**Current Rule**: Unique within bundle

**Implications**:

**Unique within bundle only**
**Pros**:
- Different bundles can have same ID
- Domain independence
- Easier for large projects
- Teams don't collide

**Cons**:
- Potential ambiguity
- How do relationships work across bundles?
- Naming conflicts
- Which SCD wins?

**Unique globally (across all bundles)**
**Pros**:
- No ambiguity
- Clear references
- Simpler validation
- Better traceability

**Cons**:
- Hard to enforce
- Teams must coordinate
- Limits flexibility
- Organizational overhead

---

## ✅ DECISIONS MADE FOR v0.1 IMPLEMENTATION

**Date**: 2025-11-24
**Status**: Decided for initial validator implementation

### Core Architectural Rule: Bundles XOR SCDs

**Decision**: A bundle can contain imports (references to other bundles) OR scds (references to SCDs), but not both.

**Rationale**:
- Cleaner architecture with clear separation between aggregators and containers
- Simplifies mental model: bundles are either leaf nodes (contain SCDs) or branch nodes (organize bundles)
- Consistent pattern across all bundle types

**Bundle hierarchy becomes tree-like:**
- **Leaf bundles** (have SCDs, no imports): Meta bundles, Domain bundles, Leaf standards bundles
- **Branch bundles** (have imports, no SCDs): Project bundles, Aggregator standards bundles

---

### 1. Project Bundle Content - IMPORTS ONLY

**Decision**: Project bundles MUST have empty `scds` array. They organize via `imports` only.

```yaml
# Valid project bundle
id: bundle:my-project
type: project
imports: [bundle:meta:1.0.0, bundle:architecture:1.0.0, ...]
scds: []  # Must be empty
```

**Validator behavior**: ERROR if project bundle contains SCDs

---

### 2. Domain Bundle Import Restriction - STRICT NO IMPORTS

**Decision**: Domain bundles MUST NOT import other bundles. They are leaf nodes that contain SCDs only.

```yaml
# Valid domain bundle
id: bundle:architecture
type: domain
imports: []  # Must be empty
scds: [scd:project:system-context, scd:project:tech-stack]
```

**Rationale**:
- Enables domain independence and parallel development
- Clear boundaries between domains
- No circular dependencies possible

**Validator behavior**: ERROR if domain bundle has imports

---

### 3. Domain Bundle Relationships - ALLOWED

**Decision**: Domain bundles CAN reference SCDs from other domain bundles via relationships.

**Rationale**:
- Domains do interact in real systems
- Better traceability across domains
- Already decided in bundle-implementation-questions-ANSWERED.md

**Validator behavior**:
- When validating standalone domain bundle: WARN about unresolved cross-bundle relationship targets
- When validating complete project bundle: ERROR if relationship targets don't exist anywhere in loaded bundles

---

### 4. Minimum Bundle Set - CONFIGURABLE VIA COMPLETENESS RULES

**Decision**: Default completeness rules require all 10 domains. Projects can customize via `.scs/completeness-rules.yaml`

**Default behavior (strict)**:
- Requires 1 meta bundle
- Requires 1 standards bundle
- Requires 10 domain bundles (all prescribed domains)
- Each domain bundle must have minimum 1 SCD
- Checks for required SCDs per domain (architecture needs system-context, tech-stack, etc.)

**Customizable**: Projects can relax rules by creating `.scs/completeness-rules.yaml`

**Validator behavior**:
- Loads completeness rules (project-specific or default)
- Validates against loaded rules
- Can skip with `--skip-completeness` flag

---

### 5. Standards Bundle Imports - FOLLOWS XOR RULE

**Decision**: Standards bundles are either aggregators OR containers, not both.

**Option A: Aggregator standards bundle**
```yaml
id: bundle:standards
type: standards
imports: [bundle:standards:hipaa:1.0.0, bundle:standards:soc2:2023.1]
scds: []  # Aggregator - no SCDs
```

**Option B: Leaf standards bundle**
```yaml
id: bundle:standards:hipaa
type: standards
imports: []  # Leaf - no imports
scds: [scd:standards:hipaa-privacy-rule, scd:standards:hipaa-security-rule]
```

**Rationale**: Consistent with XOR rule, enables hierarchical standards composition

**Validator behavior**: ERROR if standards bundle has both imports AND scds

---

### 6. Bundle Uniqueness - GLOBALLY UNIQUE

**Decision**: SCD IDs must be unique across the entire loaded bundle set (project bundle + all imported bundles).

**Rationale**:
- When all bundles are loaded together, duplicate IDs would be ambiguous
- Relationships need unambiguous targets
- Easier reasoning about the complete context

**Validator behavior**: ERROR if duplicate SCD IDs found across loaded bundles

---

### Summary: Structural Changes

**New rules implemented:**
1. ✅ XOR constraint: Bundles contain (imports XOR scds)
2. ✅ Project bundles: imports only, no SCDs
3. ✅ Domain bundles: SCDs only, no imports
4. ✅ Standards bundles: follows XOR rule (aggregator or leaf)
5. ✅ Completeness validation: configurable via rules files
6. ✅ SCD uniqueness: global across all loaded bundles

**Implementation Impact**:
- Schema updates needed for XOR constraint
- Bundle-meta.yaml updates needed
- Completeness rules framework needed
- Cross-bundle relationship validation needed

---

## How to Provide Feedback

Please comment with:
1. **Your project size/type**: (solo, small team, large org, etc.)
2. **Which rules work for your use case**
3. **Which rules are problematic**
4. **Real-world scenarios** these rules don't handle well
5. **Suggested improvements**

## Related Files

- `context/meta/bundle-meta.yaml` - Full BUNDLE-META specification
- `spec/0.1/bundle-format.md` - Bundle format documentation
- `examples/bundles/` - Example bundle files

## Decision Timeline

- **Feedback period**: 2-4 weeks
- **RFC creation**: After feedback synthesis
- **Implementation**: After RFC approval
