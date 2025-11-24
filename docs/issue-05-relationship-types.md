# Issue 05: Review Relationship Types

## Overview

The **SCD-META** specification defines 7 relationship types that SCDs can use to link to other SCDs. These relationships enable traceability, impact analysis, and governance, but we need to ensure they're comprehensive and well-defined.

## Current Rules (from SCD-META)

### Defined Relationship Types

1. **depends-on**
   - Description: This SCD requires another SCD
   - Example: Component SCD depends on Architecture SCD

2. **satisfies**
   - Description: This SCD fulfills requirements from another SCD
   - Example: Auth Service SCD satisfies HIPAA Security Rule SCD

3. **constrains**
   - Description: This SCD imposes constraints on another SCD
   - Example: Security Policy SCD constrains API Design SCD

4. **refines**
   - Description: This SCD provides more detail for another SCD
   - Example: Detailed Module SCD refines High-Level Architecture SCD

5. **extends**
   - Description: This SCD builds upon another SCD
   - Example: Enhanced Component SCD extends Base Component SCD

6. **conflicts-with**
   - Description: This SCD has conflicts with another SCD
   - Example: New Design SCD conflicts with Legacy Architecture SCD

7. **implements**
   - Description: This SCD implements specifications from another SCD
   - Example: Code Module SCD implements Interface Specification SCD

## Questions for Community

### 1. Are These 7 Types Sufficient?
**Question**: Do these relationship types cover all important relationships between SCDs?

**Implications**:

**Sufficient (7 types)**
**Pros**:
- Simple, manageable set
- Covers most common relationships
- Not overwhelming
- Easy to remember

**Cons**:
- May miss important relationships
- May force "shoehorning" into wrong types
- May need more specificity

**Potential Missing Relationships**:

**replaces**
- Description: This SCD replaces/deprecates another SCD
- Use case: Version evolution, deprecation
- Example: New Architecture SCD replaces Old Architecture SCD

**derives-from**
- Description: This SCD is derived from another SCD
- Use case: Templates, cloning, inheritance
- Example: Project Security SCD derives from Standard Security Template

**validates**
- Description: This SCD validates another SCD
- Use case: Test SCDs validating implementation SCDs
- Example: Test Plan SCD validates Feature SCD

**maps-to**
- Description: This SCD maps to another SCD (bidirectional equivalence)
- Use case: Cross-standard mapping, integration
- Example: Internal Control SCD maps to SOC2 Control

**requires-approval-from**
- Description: This SCD requires approval from another SCD/role
- Use case: Governance, compliance
- Example: Architecture Change SCD requires approval from Security Team

**informs**
- Description: This SCD provides context for another SCD (looser than depends-on)
- Use case: Reference, background, context
- Example: Research SCD informs Design SCD

**contradicts**
- Description: This SCD contradicts another SCD (stronger than conflicts-with)
- Use case: Incompatible requirements
- Example: Performance Requirement SCD contradicts Security Requirement SCD

### 2. Relationship Directionality
**Question**: Should all relationships be directional, or should some be bidirectional?

**Current State**: All appear to be directional (A → B)

**Implications**:

**Directional relationships**
**Pros**:
- Clear semantics (source and target)
- Explicit about direction of dependency
- Better for impact analysis
- Clearer causality

**Cons**:
- May need to express both directions
- More relationships to manage
- Redundant information

**Some bidirectional relationships**
**Pros**:
- Less redundancy
- More natural for some relationships (conflicts-with, maps-to)
- Fewer relationships to maintain

**Cons**:
- Mixed semantics (some directional, some not)
- May be confusing
- Harder to validate

**Question for Community**:
- Which relationships should be bidirectional?
- How should tools handle bidirectional relationships?

### 3. Relationship Constraints
**Question**: Should certain relationship types only be allowed between specific tiers?

**Current State**: No tier constraints specified

**Potential Constraints**:

**satisfies**
- Should only go from project → standards?
- Or can meta → standards? standards → standards?

**implements**
- Should only go from project → standards or project → project?
- Or can meta → meta?

**depends-on**
- Can project depend on meta? (probably yes)
- Can meta depend on standards? (probably no)
- Can standards depend on project? (probably no)

**Implications**:

**With tier constraints**
**Pros**:
- Prevents nonsensical relationships
- Clearer semantics
- Better validation
- Enforces architectural layers

**Cons**:
- Less flexible
- May be overly restrictive
- Edge cases may need exceptions

**Without tier constraints**
**Pros**:
- Maximum flexibility
- Projects decide what makes sense
- Simpler specification

**Cons**:
- Could create confusing relationships
- May violate architectural principles
- Harder to reason about

### 4. Relationship Cardinality
**Question**: Should we limit how many relationships an SCD can have?

**Current State**: No limits

**Implications**:

**No limits (current)**
**Pros**:
- Maximum expressiveness
- Real dependencies can be complex
- No artificial constraints

**Cons**:
- Could become overwhelming
- May indicate poor SCD decomposition
- Hard to visualize
- Performance issues

**With limits**
**Pros**:
- Encourages better decomposition
- Easier to understand
- Better performance
- Clearer dependencies

**Cons**:
- Arbitrary limits feel wrong
- May be too restrictive
- Complex systems need complex relationships

### 5. Relationship Metadata
**Question**: Should relationships have additional metadata beyond type, target, and description?

**Current Fields**:
- `type` (required)
- `target` (required)
- `description` (optional)

**Potential Additional Fields**:

**strength**
- Values: critical, important, optional
- Use case: Impact analysis, prioritization

**version_constraint**
- Values: Version requirements for target
- Use case: Compatibility checking

**validated**
- Values: true/false
- Use case: Tracking which relationships have been verified

**rationale**
- Values: Why this relationship exists
- Use case: Governance, documentation

**created_at / created_by**
- Values: Provenance for relationship
- Use case: Audit trail

**Implications**:

**More metadata**
**Pros**:
- Richer semantics
- Better governance
- More context
- Supports advanced tooling

**Cons**:
- More complex
- More maintenance
- May be overkill
- Increases overhead

### 6. Relationship Validation
**Question**: How should we validate relationships?

**Current State**: Basic validation (target exists)

**Potential Validation Rules**:

**Existence**
- Target SCD must exist ✅ (current)

**Accessibility**
- Target SCD must be in the same bundle or imported bundle

**Acyclicity**
- No circular relationships (A → B → A) for certain types (depends-on)

**Type constraints**
- Certain relationships only between certain tiers

**Mutual exclusivity**
- Can't have both depends-on and conflicts-with to same target

**Implications**:

**Strict validation**
**Pros**:
- Catches errors early
- Ensures consistency
- Better quality
- Clearer semantics

**Cons**:
- More restrictive
- May block legitimate uses
- More complex validation
- Slower validation

**Loose validation**
**Pros**:
- More flexible
- Faster validation
- Simpler implementation

**Cons**:
- May allow invalid relationships
- Harder to reason about
- Could cause runtime issues

---

## ✅ DECISIONS MADE FOR v0.1 IMPLEMENTATION

**Date**: 2025-11-24
**Status**: Decided for initial validator implementation

### 1. Relationship Types - KEEP CURRENT 7

**Decision**: Keep the 7 existing relationship types. No additions for v0.1.

**The 7 types:**
1. **depends-on** - This SCD requires another SCD
2. **satisfies** - This SCD fulfills requirements from another SCD
3. **constrains** - This SCD imposes constraints on another SCD
4. **refines** - This SCD provides more detail for another SCD
5. **extends** - This SCD builds upon another SCD
6. **conflicts-with** - This SCD has conflicts with another SCD
7. **implements** - This SCD implements specifications from another SCD

**Deferred additions**: replaces, derives-from, validates, maps-to, requires-approval-from, informs, contradicts
- Can be added in future versions based on real usage patterns
- Projects can use existing types as workarounds for now

**Rationale**: Current 7 are comprehensive for most use cases. Don't over-specify before seeing real-world usage.

---

### 2. Relationship Directionality - ALL DIRECTIONAL

**Decision**: All relationships are directional (source → target).

**Example:**
```yaml
# In scd:project:auth
relationships:
  - type: depends-on
    target: scd:meta:roles
    description: "Auth system depends on role definitions"
```

This means: `scd:project:auth` → `scd:meta:roles` (directional)

**If bidirectional needed**: Create two relationships
```yaml
# In SCD A
relationships:
  - type: depends-on
    target: scd:B

# In SCD B
relationships:
  - type: depends-on
    target: scd:A
```

**Rationale**: Clear semantics, explicit about dependency direction, easier to validate

**Validator behavior**: Treats all relationships as directional

---

### 3. Tier Constraints - ENFORCED

**Decision**: Enforce tier constraints for relationships via relationship-rules.yaml

**Constraint examples:**
```yaml
# relationship-rules.yaml
relationship_types:
  - type: "satisfies"
    allowed_tiers:
      - from: "project"
        to: "standards"
    # Project satisfies standards (compliance)
    # NOT allowed: meta → standards, standards → project

  - type: "depends-on"
    allowed_tiers:
      - from: "project"
        to: ["meta", "project"]
      - from: "standards"
        to: ["meta", "standards"]
      - from: "meta"
        to: ["meta"]
    # Layers depend on same level or foundation
    # NOT allowed: standards → project, meta → standards

  - type: "implements"
    allowed_tiers:
      - from: "project"
        to: ["project", "standards"]
    # Project implements project specs or standards
```

**Rationale**: Prevents nonsensical relationships, enforces architectural layering

**Validator behavior**: ERROR if relationship violates tier constraints

---

### 4. Cardinality Limits - NO LIMITS

**Decision**: No limits on number of relationships per SCD.

**Rationale**:
- Real systems can be complex with many dependencies
- Don't artificially constrain
- Can add warnings later if an SCD has excessive relationships (e.g., >50)

**Deferred**: Optional warnings for unusually high relationship counts

---

### 5. Relationship Metadata - KEEP SIMPLE

**Decision**: Relationships have 3 fields only for v0.1.

**Required fields:**
```yaml
relationships:
  - type: "depends-on"        # required
    target: "scd:meta:roles"  # required
    description: "Why this relationship exists"  # optional but recommended
```

**No additional fields**: strength, version_constraint, validated, rationale, etc.
- Can be added in future versions if needed
- Keep it simple for v0.1

**Rationale**: Don't over-engineer. See what community needs before adding complexity.

---

### 6. Relationship Validation - LEVEL 4

**Decision**: Validate relationships at Level 4 with these checks:

**Validation rules:**
```yaml
relationship_validation:
  - check: "target_exists"
    severity: "error"
    description: "Relationship target SCD must exist in loaded bundles"
    applies_to: "all"

  - check: "tier_constraints"
    severity: "error"
    description: "Relationship must follow tier constraint rules"
    applies_to: "all"

  - check: "no_self_reference"
    severity: "error"
    description: "SCD cannot have relationship to itself"
    applies_to: "all"

  - check: "acyclic_depends_on"
    severity: "warning"
    description: "Circular depends-on relationships detected"
    applies_to: ["depends-on"]
    note: "A → B → C → A creates circular dependency"
```

**Validator behavior:**
- When validating standalone bundle: WARN if relationship target not in bundle (may be in another bundle)
- When validating complete project bundle: ERROR if relationship target doesn't exist anywhere
- ERROR if tier constraints violated
- ERROR if self-reference detected
- WARNING if circular depends-on detected

**Rationale**: Comprehensive validation prevents broken references and architectural violations

---

### Summary: Relationship Rules for v0.1

**Implemented:**
1. ✅ 7 relationship types (depends-on, satisfies, constrains, refines, extends, conflicts-with, implements)
2. ✅ All relationships directional
3. ✅ Tier constraints enforced via relationship-rules.yaml
4. ✅ No cardinality limits
5. ✅ Simple metadata: type, target, description
6. ✅ Level 4 validation: target exists, tier constraints, no self-ref, warn on cycles

**Validator implementation:**
- Loads relationship types from `relationship-rules.yaml`
- Validates at Level 4 (Relationship Validation)
- Enforces tier constraints
- Detects circular dependencies
- Cross-bundle relationship resolution

**Deferred to future versions:**
- Additional relationship types (replaces, validates, maps-to, etc.)
- Relationship metadata (strength, version constraints, etc.)
- Cardinality warnings

---

## How to Provide Feedback

Please comment with:
1. **Which relationship types you use most** and how
2. **Missing relationship types** you need
3. **Relationship constraints** that would help (or hurt)
4. **Real-world examples** of complex relationships
5. **Tooling needs** for relationship visualization/analysis

## Related Files

- `context/meta/scd-meta.yaml` - Full SCD-META with relationship types
- `spec/0.1/core-model.md` - Core model with relationship semantics
- `docs/usage-guide.md` - Usage guide with relationship examples

## Decision Timeline

- **Feedback period**: 2-4 weeks
- **RFC creation**: After feedback synthesis
- **Implementation**: After RFC approval
