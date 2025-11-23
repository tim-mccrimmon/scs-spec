# Issue 04: Review Validation Rules

## Overview

The **VALIDATOR-META** specification defines 6 levels of validation and when/how they should be applied. These rules determine what "valid" means and how strictly projects must adhere to the specification.

## Current Rules (from VALIDATOR-META)

### Validation Levels

#### Level 1: Syntactic Validation
- **Check**: Is the file valid YAML or JSON?
- **Severity**: ERROR
- **When**: During editing, before commit

#### Level 2: Schema Validation
- **Check**: Does the SCD match the required schema?
- **Severity**: ERROR
- **When**: After writing SCD, before adding to bundle

#### Level 3: Semantic Validation
- **Check**: Do the contents make logical sense?
- **Severity**: ERROR
- **When**: With schema validation

#### Level 4: Relationship Validation
- **Check**: Are relationships valid and do targets exist?
- **Severity**: ERROR
- **When**: After updating bundle, before commit

#### Level 5: Bundle Validation
- **Check**: Is the bundle complete and consistent?
- **Severity**: ERROR
- **When**: Before pull request, in CI/CD

#### Level 6: Compliance Validation
- **Check**: Does the bundle satisfy compliance requirements?
- **Severity**: WARNING/ERROR - "depends on project policy"
- **When**: Before release, in governance reviews

### Validation States

#### DRAFT State
- **Mode**: Permissive
- **Behavior**: Warnings instead of errors, allows incomplete SCDs
- **Use case**: Active development, iteration

#### VERSIONED State
- **Mode**: Strict
- **Behavior**: All errors must be fixed, no incomplete SCDs
- **Use case**: Locked bundles, production use

## Questions for Community

### 1. Compliance Validation Severity
**Question**: Should Level 6 (Compliance) be ERROR or WARNING by default?

**Current Rule**: "depends on project policy"

**Implications**:

**Option A: ERROR by default**
**Pros**:
- Ensures compliance is taken seriously
- Prevents non-compliant releases
- Clear signal that compliance matters
- Better for regulated industries

**Cons**:
- Too restrictive for some projects
- Not all projects have compliance requirements
- May block development unnecessarily
- Projects without standards would fail

**Option B: WARNING by default**
**Pros**:
- More flexible
- Doesn't block development
- Projects can choose to enforce
- Better for experimental projects

**Cons**:
- Compliance may be ignored
- Inconsistent enforcement
- May not be taken seriously
- Dangerous for regulated systems

**Option C: Configurable (current)**
**Pros**:
- Maximum flexibility
- Projects decide what's right for them
- Can vary by environment (dev vs. prod)

**Cons**:
- Inconsistent across projects
- Requires configuration
- May be unclear what to choose

### 2. Missing Validation Levels
**Question**: Are there additional validation levels we should include?

**Potential Additional Levels**:

**Level 7: Performance Validation**
- Check: Is the bundle size reasonable? Parse time acceptable?
- Use case: Large projects with hundreds of SCDs

**Level 8: Security Validation**
- Check: No secrets in SCDs, no dangerous patterns
- Use case: All projects

**Level 9: Consistency Validation**
- Check: Cross-SCD consistency, naming conventions, style
- Use case: Large teams, enterprise standards

**Level 10: Coverage Validation**
- Check: Are all domains represented? All standards satisfied?
- Use case: Compliance-heavy projects

**Question for Community**:
- Which additional levels would be valuable?
- Should any be merged with existing levels?

### 3. DRAFT Mode Permissiveness
**Question**: Should DRAFT mode be even more permissive?

**Current Behavior**: Warnings instead of errors, allows incomplete SCDs

**Potential Enhancements**:
- Allow missing required fields (with warnings)
- Allow invalid ID patterns (with warnings)
- Allow broken relationships (with warnings)
- Allow schema violations (with warnings)

**Implications**:

**More permissive DRAFT**
**Pros**:
- Easier early development
- Less friction during iteration
- Can prototype quickly
- Focus on content, not structure

**Cons**:
- May accumulate technical debt
- Harder to transition to VERSIONED
- Could establish bad habits
- Validation becomes less meaningful

**Stricter DRAFT (current)**
**Pros**:
- Catches issues early
- Easier transition to VERSIONED
- Maintains quality throughout
- Better habits

**Cons**:
- More friction during development
- May slow iteration
- Could be frustrating for rapid prototyping

### 4. Validation Order and Dependencies
**Question**: Should validation levels always run in order, or can they run in parallel?

**Current Implication**: Order suggests sequence

**Implications**:

**Sequential (1→2→3→4→5→6)**
**Pros**:
- Fail fast (syntax before schema)
- Logical progression
- Clear error priority
- Easier to fix in order

**Cons**:
- Slower (can't parallelize)
- Must wait for each level
- May hide multiple issues

**Parallel (all at once)**
**Pros**:
- Faster validation
- See all issues at once
- Better for large bundles
- More efficient CI/CD

**Cons**:
- May be overwhelming
- Some errors depend on others
- Harder to prioritize fixes

### 5. Validation in Different Contexts
**Question**: Should validation rules differ based on context?

**Contexts**:
- **Local development**: Most permissive
- **Pre-commit**: Moderate
- **PR/CI**: Strict
- **Production release**: Strictest

**Implications**:

**Context-specific validation**
**Pros**:
- Right level of strictness for each stage
- Less friction in development
- Strong gates for production
- Flexibility where needed

**Cons**:
- More complex
- Inconsistent experience
- May surprise developers
- More configuration

**Uniform validation**
**Pros**:
- Consistent experience
- No surprises
- Simpler to understand
- Less configuration

**Cons**:
- May be too strict for development
- Or too loose for production
- One size doesn't fit all

### 6. Error Reporting
**Question**: How should validation errors be reported?

**Current State**: Not specified

**Options**:

**A: First error only**
- Fast, but may require multiple iterations

**B: All errors at once**
- Complete picture, may be overwhelming

**C: All errors per level, stop at first failing level**
- Balanced approach

**D: Configurable**
- Let projects choose

### 7. Validation Caching
**Question**: Should validation results be cached?

**Implications**:

**Cache validation results**
**Pros**:
- Faster repeated validations
- Better performance for large bundles
- Less CI/CD time

**Cons**:
- Cache invalidation complexity
- May miss changes
- Additional implementation

**No caching**
**Pros**:
- Always accurate
- Simpler implementation
- No cache invalidation issues

**Cons**:
- Slower
- Redundant work
- More CI/CD time

## How to Provide Feedback

Please comment with:
1. **Your validation workflow**: When and how you validate
2. **Pain points**: What's too strict or too loose?
3. **Missing checks**: What should be validated that isn't?
4. **Context-specific needs**: Different validation for dev vs. prod?
5. **Tool integration**: How validation fits into your tools

## Related Files

- `context/meta/validator-meta.yaml` - Full VALIDATOR-META specification
- `docs/validation-workflow.md` - Validation workflow guide
- `tools/scd-validator/` - Validator implementation

## Decision Timeline

- **Feedback period**: 2-4 weeks
- **RFC creation**: After feedback synthesis
- **Implementation**: After RFC approval
