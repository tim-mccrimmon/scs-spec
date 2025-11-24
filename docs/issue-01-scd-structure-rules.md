# Issue 01: Review SCD Structure Rules

## Overview

The **SCD-META** specification defines fundamental rules about how SCDs are structured, identified, and versioned. These rules affect every SCD created in the SCS ecosystem, so they must be practical, enforceable, and not overly restrictive.

## Current Rules (from SCD-META)

### ID Pattern Rule
- **Rule**: IDs MUST follow pattern `scd:(meta|standards|project):<name>`
- **Pattern**: `^scd:(meta|standards|project):[a-zA-Z0-9._-]+$`
- **Examples**:
  - ✅ `scd:meta:scd-meta`
  - ✅ `scd:project:system-context`
  - ❌ `meta:roles` (missing `scd:` prefix)

### Type-Tier Matching Rule
- **Rule**: The `type` field MUST match the tier in the `id`
- **Example**:
  - ✅ `id: scd:meta:roles` with `type: meta`
  - ❌ `id: scd:meta:roles` with `type: project`

### Versioning Rules
- **Rule**: Versions MUST follow semantic versioning (`major.minor.patch`) or be `DRAFT`
- **Examples**:
  - ✅ `version: "1.0.0"`
  - ✅ `version: "DRAFT"`
  - ❌ `version: "v1.0"`
  - ❌ `version: "1.0"`

### Immutability Rule
- **Rule**: Once an SCD is versioned (e.g., `1.0.0`), its content becomes immutable
- **Changes require**: Creating a new version (e.g., `1.0.1` or `1.1.0`)

### Independent Versioning Rule
- **Rule**: Each SCD versions independently of other SCDs and bundles
- **Implication**: An SCD can be at version `2.3.1` while the bundle containing it is at `1.0.0`

## Questions for Community

### 1. ID Pattern Enforcement
**Question**: Is the ID pattern always enforceable? Are there edge cases?

**Implications**:

**Pros (strict enforcement)**:
- Consistent naming across all projects
- Easy to parse and validate
- Clear tier identification
- Tools can rely on pattern

**Cons (strict enforcement)**:
- May not support all naming conventions
- Character restrictions may be limiting
- Could conflict with existing organizational standards

**Potential Issues**:
- What about SCDs that span multiple tiers?
- Should we allow organizational prefixes (e.g., `scd:meta:acme.roles`)?
- Are the allowed characters sufficient for international names?

### 2. Type-Tier Matching
**Question**: Should `type` always match the tier in the `id`? Are there legitimate exceptions?

**Implications**:

**Pros (strict matching)**:
- Prevents confusion and errors
- Makes validation simpler
- Clear semantic consistency
- No ambiguity about SCD tier

**Cons (strict matching)**:
- Redundant information (tier is in both `id` and `type`)
- May be overly restrictive for advanced use cases
- Could SCDs legitimately exist in multiple tiers?

**Potential Issues**:
- What about "bridge" SCDs that map between tiers?
- Should we just remove the `type` field and derive it from `id`?

### 3. Immutability
**Question**: Should versioned SCDs always be immutable? Are there exceptions?

**Implications**:

**Pros (strict immutability)**:
- Guarantees reproducibility
- Enables time-travel debugging
- Clear audit trail
- Builds trust in versioned context

**Cons (strict immutability)**:
- Critical bug fixes require new versions
- Typo fixes require new versions
- May create version proliferation
- What about security vulnerabilities?

**Potential Issues**:
- How do we handle critical security fixes in locked SCDs?
- Should there be a "patch" mechanism that preserves version?
- What about non-semantic fixes (typos, formatting)?

### 4. Semver vs. DRAFT
**Question**: Is the DRAFT/semver dichotomy sufficient? Do we need intermediate states?

**Implications**:

**Pros (simple dichotomy)**:
- Clear distinction between mutable and immutable
- Easy to understand
- Two states are easier to manage than many

**Cons (simple dichotomy)**:
- No "beta" or "rc" versions
- No way to signal "stable but not locked"
- May need more granular lifecycle states

**Potential Issues**:
- Should we support semver pre-release versions (e.g., `1.0.0-beta.1`)?
- What about deprecated SCDs?
- How do we signal "experimental" SCDs?

### 5. Independent Versioning
**Question**: Should SCDs really version completely independently of bundles?

**Implications**:

**Pros (independent versioning)**:
- Maximum flexibility
- Teams can work independently
- No forced version alignment
- Natural evolution of SCDs

**Cons (independent versioning)**:
- Potential version confusion
- Hard to reason about "which version of the system"
- May create compatibility issues
- Bundle version becomes less meaningful

**Potential Issues**:
- Should there be optional version constraints in bundles?
- How do we ensure SCD versions are compatible?
- What's the relationship between bundle version and SCD versions?

---

## ✅ DECISIONS MADE FOR v0.1 IMPLEMENTATION

**Date**: 2025-11-24
**Status**: Decided for initial validator implementation

### 1. ID Pattern Enforcement - STRICT
**Decision**: Enforce pattern `^scd:(meta|standards|project):[a-zA-Z0-9._-]+$` strictly with no exceptions.
- Validator will reject any SCD that doesn't match this pattern
- Organizational prefixes (e.g., `scd:meta:acme.roles`) are supported via the name portion
- Can be reconsidered based on community feedback if edge cases emerge

### 2. Type-Tier Matching - STRICT
**Decision**: The `type` field MUST match the tier in the `id` field. No exceptions.
- Validator will reject SCDs where type doesn't match tier
- Prevents confusion and ensures consistency
- Alternative of removing `type` field can be considered in future versions

### 3. Immutability - ENFORCED
**Decision**: Once an SCD is versioned (e.g., `1.0.0`), it is immutable.
- Changes require creating a new version
- Immutability is enforced through git workflow and tooling
- Validator ensures versioned SCDs pass strict validation

### 4. Semver vs. DRAFT - STRICT DICHOTOMY
**Decision**: Version field must be either `DRAFT` or strict semver (`X.Y.Z`).
- Pre-release versions (e.g., `1.0.0-beta.1`) are NOT supported in v0.1
- No intermediate states beyond DRAFT and versioned
- Pattern: `^(\d+\.\d+\.\d+|DRAFT)$`
- Can add pre-release support in future if community needs it

### 5. Independent Versioning - CONFIRMED
**Decision**: SCDs version independently of bundles and other SCDs.
- Already implemented in current specification
- Each SCD has its own version lifecycle
- Bundle version is separate from contained SCD versions

**Implementation Impact**: All decisions above are implemented in validator rules and will be enforced during validation.

---

## How to Provide Feedback

Please comment with:
1. **Your perspective**: (solo developer / team / enterprise / etc.)
2. **Which rules work well for you** and why
3. **Which rules are problematic** and why
4. **Suggestions for improvement** with rationale
5. **Edge cases** you've encountered or anticipate

## Related Files

- `context/meta/scd-meta.yaml` - Full SCD-META specification
- `spec/0.1/core-model.md` - Core SCS model documentation
- `schema/scd/meta-scd-template.json` - SCD JSON Schema

## Decision Timeline

- **Feedback period**: 2-4 weeks
- **RFC creation**: After feedback synthesis
- **Implementation**: After RFC approval
