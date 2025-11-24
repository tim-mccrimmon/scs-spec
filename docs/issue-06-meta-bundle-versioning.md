# Issue 06: Review Meta Bundle Versioning Strategy

## Overview

The **meta bundle** is special - it's provided by SCS-Spec and defines the specification language itself. When SCS-Spec updates the META SCDs, we need a clear strategy for versioning and how projects should consume updates.

## Current State

### Meta Bundle Properties
- **ID**: `bundle:meta`
- **Type**: `meta`
- **Version**: `1.0.0`
- **SCDs**:
  - `scd:meta:scd-meta`
  - `scd:meta:bundle-meta`
  - `scd:meta:domain-meta`
  - `scd:meta:validator-meta`

### Current Versioning Rule
- Meta bundle is versioned like any other bundle
- Once versioned (e.g., `1.0.0`), it becomes immutable
- Projects import specific versions: `bundle:meta:1.0.0`

## The Problem

**When SCS-Spec updates META SCDs**, what happens?

**Scenarios**:
1. Fix typo in DOMAIN-META
2. Add new validation level to VALIDATOR-META
3. Add new bundle type to BUNDLE-META
4. Change required fields in SCD-META

**Questions**:
- Is this a new version of the meta bundle?
- How do projects know to upgrade?
- Can projects stay on old versions?
- What's the compatibility story?

## Questions for Community

### 1. Meta Bundle Versioning Cadence
**Question**: How should we version the meta bundle?

**Option A: With SCS Specification Version**
- Meta bundle version matches SCS version
- `bundle:meta:0.1.0` for SCS 0.1
- `bundle:meta:0.2.0` for SCS 0.2
- Major changes to spec = new meta bundle

**Implications**:
**Pros**:
- Clear alignment with spec
- Easy to understand
- Predictable versioning
- One version to track

**Cons**:
- May version too infrequently
- Bug fixes require spec version bump
- Less granular control

**Option B: Independent Semantic Versioning**
- Meta bundle versions independently
- `bundle:meta:1.0.0`, `1.0.1`, `1.1.0`, `2.0.0`
- Can release updates without spec changes

**Implications**:
**Pros**:
- More frequent updates possible
- Can fix bugs quickly
- Granular control
- True semantic versioning

**Cons**:
- Another version to track
- Potential confusion with spec version
- When to increment?

**Option C: Date-Based Versioning**
- `bundle:meta:2025.01.23`
- Clear when it was released

**Implications**:
**Pros**:
- No ambiguity
- Clear timeline
- Easy to see recency

**Cons**:
- Doesn't convey compatibility
- Can't tell if breaking change
- Less semantic meaning

### 2. Project Version Pinning
**Question**: Should projects pin to specific meta bundle versions?

**Option A: Pin to Specific Version (current)**
- `imports: [bundle:meta:1.0.0]`
- Project controls when to upgrade

**Implications**:
**Pros**:
- Stability
- Reproducibility
- No surprise changes
- Project controls timing

**Cons**:
- May get stuck on old versions
- Miss bug fixes
- Miss new features
- Version sprawl across ecosystem

**Option B: Pin to Major Version**
- `imports: [bundle:meta:1.x]`
- Automatically get minor/patch updates

**Implications**:
**Pros**:
- Automatic bug fixes
- Stay more current
- Less version sprawl
- Easier maintenance

**Cons**:
- Less control
- Potential breakage (if semver violated)
- Harder to reproduce
- May surprise projects

**Option C: Always Latest**
- `imports: [bundle:meta:latest]`
- Always use latest meta bundle

**Implications**:
**Pros**:
- Always current
- No upgrade needed
- Get all fixes/features
- Simplest

**Cons**:
- No stability
- May break unexpectedly
- Hard to reproduce
- Not recommended for production

### 3. Backward Compatibility
**Question**: How should we handle backward compatibility?

**Scenarios**:

**Non-breaking changes (patch/minor)**
- Add new optional field to META SCD
- Add new relationship type
- Add new validation level (optional)
- Fix typo/documentation

**Breaking changes (major)**
- Remove required field
- Change ID pattern
- Remove bundle type
- Change validation behavior

**Strategy Options**:

**Option A: Strict Semantic Versioning**
- Patch: Bug fixes only
- Minor: New features, backward compatible
- Major: Breaking changes

**Option B: Spec-Version-Based**
- Meta bundle major version matches spec version
- SCS 0.x → `bundle:meta:0.y.z`
- Breaking changes only on spec major version bump

**Option C: Conservative (always major)**
- Any change to META SCDs = major version bump
- Maximally conservative
- Easier to reason about

### 4. Upgrade Path
**Question**: How should projects upgrade meta bundle versions?

**Challenges**:
- Meta bundle defines the language itself
- Upgrading changes what "valid" means
- May require changes to all SCDs

**Upgrade Scenarios**:

**Scenario 1: Bug Fix (1.0.0 → 1.0.1)**
- Typo fix in DOMAIN-META
- Should be seamless

**Scenario 2: New Feature (1.0.0 → 1.1.0)**
- New validation level added
- Projects can adopt or ignore

**Scenario 3: Breaking Change (1.0.0 → 2.0.0)**
- ID pattern changed
- All SCDs need updates

**Question for Community**:
- Should we provide migration tools?
- Should we support multiple meta bundle versions simultaneously?
- How long should we support old versions?

### 5. Meta SCD Individual Versioning
**Question**: Should individual META SCDs have their own versions, separate from the meta bundle?

**Current State**: Each META SCD has a version field

**Implications**:

**Individual versioning**
**Pros**:
- Granular tracking
- Can update one without affecting others
- Clear change history per META SCD

**Cons**:
- More versions to track
- Potential compatibility issues between META SCDs
- When does meta bundle version change?

**Bundle-level versioning only**
**Pros**:
- Simpler
- One version to track
- Clear compatibility
- All META SCDs move together

**Cons**:
- Can't update one without affecting all
- Less granular
- May version unnecessarily

### 6. Validation and Compatibility
**Question**: How do we validate that a project is compatible with a meta bundle version?

**Potential Checks**:

**Meta bundle version check**
- Validator checks if project's meta bundle is too old
- Warns about deprecated versions
- Suggests upgrades

**Feature detection**
- Check if project uses features from specific meta bundle versions
- Warn if using deprecated features

**Automatic migration**
- Tool to upgrade from one meta bundle version to another
- Automatically update SCDs as needed

**Implications**:

**Strict version enforcement**
**Pros**:
- Ensures compatibility
- Prevents issues
- Clear requirements

**Cons**:
- May block valid uses
- Forces upgrades
- Less flexible

**Loose version checking**
**Pros**:
- More flexible
- Projects decide
- Less friction

**Cons**:
- May allow incompatibilities
- Harder to support
- Unclear requirements

---

## ✅ DECISIONS MADE FOR v0.1 IMPLEMENTATION

**Date**: 2025-11-24
**Status**: Decided for initial validator implementation

### 1. Meta Bundle Versioning Cadence - ALIGNED WITH SCS SPEC

**Decision**: Meta bundle version matches SCS specification version.

**Versioning scheme:**
- SCS 0.1 → `bundle:meta:0.1.0`
- SCS 0.2 → `bundle:meta:0.2.0`
- SCS 1.0 → `bundle:meta:1.0.0`

**Example:**
```yaml
# For SCS version 0.1
id: bundle:meta
type: meta
version: "0.1.0"
title: "SCS Meta-Tier Standard Bundle"
```

**Rationale**:
- Clear alignment: "I'm using SCS 0.1, so I use meta bundle 0.1.0"
- Meta bundle IS the spec language definition
- One version to track (not separate from spec)
- Easy to understand and communicate

**Version format**: `MAJOR.MINOR.PATCH` matching SCS spec version

---

### 2. Project Version Pinning - SPECIFIC VERSION

**Decision**: Projects pin to specific meta bundle version.

**Project bundle must specify exact version:**
```yaml
# Project bundle
id: bundle:my-project
type: project
imports:
  - bundle:meta:0.1.0  # Specific version (required)
  - bundle:standards:1.0.0
  - bundle:architecture:1.0.0
```

**NOT allowed:**
- `bundle:meta:0.x` (no range)
- `bundle:meta:latest` (no latest)
- `bundle:meta` (no version)

**Rationale**:
- Stability and reproducibility
- Project controls when to upgrade
- No surprise changes
- Schema enforces version in import pattern

**Validator behavior**: ERROR if meta bundle import lacks specific version

---

### 3. Backward Compatibility - STRICT SEMANTIC VERSIONING

**Decision**: Meta bundle follows strict semantic versioning.

**Version changes:**
- **Patch** (0.1.0 → 0.1.1): Bug fixes, typos, documentation only
  - Example: Fix typo in domain-meta.yaml
  - Backward compatible: YES

- **Minor** (0.1.0 → 0.2.0): New features, backward compatible
  - Example: Add new relationship type, add new validation level
  - Backward compatible: YES
  - Projects on 0.1.0 continue working

- **Major** (0.1.0 → 1.0.0): Breaking changes
  - Example: Change ID pattern, remove bundle type, change required fields
  - Backward compatible: NO
  - Projects must update

**Examples of changes:**
| Change | Version Impact | Compatible? |
|--------|---------------|-------------|
| Fix typo in description | Patch (0.1.0 → 0.1.1) | Yes |
| Add new relationship type | Minor (0.1.0 → 0.2.0) | Yes |
| Add new prescribed domain | Minor (0.1.0 → 0.2.0) | Yes |
| Add optional field to SCD | Minor (0.1.0 → 0.2.0) | Yes |
| Change ID pattern | Major (0.1.0 → 1.0.0) | No |
| Remove bundle type | Major (0.1.0 → 1.0.0) | No |
| Change required fields | Major (0.1.0 → 1.0.0) | No |

**Rationale**: Standard semver is well-understood and predictable

---

### 4. Upgrade Path - MANUAL FOR v0.1

**Decision**: Manual upgrade process for v0.1. Automated tooling deferred to future versions.

**Upgrade process:**
```bash
# Step 1: Update project bundle
# Change: bundle:meta:0.1.0 → bundle:meta:0.2.0

# Step 2: Validate
scs-validate --bundle bundles/project-bundle.yaml

# Step 3: Fix any breaking changes (if major version)

# Step 4: Commit
git add bundles/project-bundle.yaml
git commit -m "Upgrade to meta bundle 0.2.0"
```

**Future tooling** (post-v0.1):
```bash
# Automated upgrade tool (future)
scs-upgrade --from 0.1.0 --to 0.2.0
# Tool analyzes changes, suggests fixes, optionally auto-migrates
```

**Rationale**: Keep validator simple for v0.1. Add upgrade tooling when community needs emerge.

**Deferred**: Automated migration tool, upgrade analysis, breaking change reports

---

### 5. Individual Meta SCD Versioning - TRACKED BUT BUNDLE IS CANONICAL

**Decision**: Both bundle and individual SCD versions exist. Bundle version is what matters.

**Structure:**
```yaml
# bundle:meta:0.1.0
id: bundle:meta
version: "0.1.0"  # ← Bundle version (canonical)

scds:
  - scd:meta:scd-meta          # version: "0.1.0"
  - scd:meta:bundle-meta       # version: "0.1.0"
  - scd:meta:domain-meta       # version: "0.1.0"
  - scd:meta:validator-meta    # version: "0.1.0"

# All META SCDs version together with bundle
```

**Version synchronization:**
- When meta bundle updates to 0.2.0, all META SCDs update to 0.2.0
- Individual SCD versions track history
- Bundle version is what projects reference

**Rationale**:
- Simpler reasoning: "I'm on meta bundle 0.1.0" vs tracking 4 SCD versions
- Clear compatibility: bundle version determines compatibility
- Individual versions useful for change tracking

**Validator behavior**: Uses bundle version for compatibility checking

---

### 6. Version Checking and Compatibility - WARN ABOUT MISMATCHES

**Decision**: Validator checks meta bundle version and warns about mismatches.

**Validator behavior:**
```bash
$ scs-validate --bundle project-bundle.yaml

⚠ Info: Project uses bundle:meta:0.1.0
⚠ Info: Validator supports bundle:meta:0.1.0 - 0.2.0
✓ Validation using meta bundle 0.1.0 rules

Summary: No errors
Status: VALID
```

**If newer version available:**
```bash
$ scs-validate --bundle project-bundle.yaml

⚠ Warning: Project uses bundle:meta:0.1.0
⚠ Warning: Newer version available: bundle:meta:0.2.0
⚠ Warning: Consider upgrading for latest features and bug fixes
   See: https://scs-spec.org/changelog/0.2.0

✓ Validation using meta bundle 0.1.0 rules
Status: VALID
```

**If version too old (unsupported):**
```bash
$ scs-validate --bundle project-bundle.yaml

✗ Error: Project uses bundle:meta:0.1.0
✗ Error: Validator requires bundle:meta:0.3.0 or higher
✗ Error: Please upgrade your meta bundle

Status: FAILED (unsupported version)
```

**Rationale**: Helpful guidance without blocking valid projects on older versions

---

### Summary: Meta Bundle Versioning for v0.1

**Implemented:**
1. ✅ Meta bundle version matches SCS spec version (0.1.0, 0.2.0, 1.0.0)
2. ✅ Projects pin to specific version (`bundle:meta:0.1.0`)
3. ✅ Strict semantic versioning (patch/minor/major)
4. ✅ Manual upgrade process (tooling deferred)
5. ✅ Bundle version is canonical (individual SCD versions tracked)
6. ✅ Validator warns about version mismatches

**Version lifecycle:**
```
SCS 0.1 Released
  └─ bundle:meta:0.1.0 created
       └─ Projects use: bundle:meta:0.1.0

SCS 0.2 Released (new features, backward compatible)
  └─ bundle:meta:0.2.0 created
       ├─ Existing projects on 0.1.0: continue working
       └─ New projects: use 0.2.0

SCS 1.0 Released (breaking changes)
  └─ bundle:meta:1.0.0 created
       ├─ Projects on 0.x.x: must upgrade
       └─ Validator may drop support for old versions
```

**Deferred to future:**
- Automated upgrade tooling
- Breaking change analysis
- Multi-version support in validator

---

## How to Provide Feedback

Please comment with:
1. **Your upgrade philosophy**: Do you pin versions or stay current?
2. **Version sprawl concerns**: Would ecosystem fragmentation be a problem?
3. **Compatibility needs**: How important is backward compatibility?
4. **Migration tooling**: Would you use automated migration tools?
5. **Support expectations**: How long should old versions be supported?

## Related Files

- `examples/bundles/meta-bundle.yaml` - Current meta bundle
- `context/meta/*.yaml` - All META SCDs
- `spec/0.1/bundle-format.md` - Bundle versioning documentation

## Decision Timeline

- **Feedback period**: 2-4 weeks
- **RFC creation**: After feedback synthesis
- **Implementation**: After RFC approval
