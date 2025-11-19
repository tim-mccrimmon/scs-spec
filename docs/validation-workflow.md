# SCS Validation Workflow

**Version**: 0.1
**Last Updated**: 2025-11-19

---

## Overview

Validation ensures that your SCDs and bundles are:
- **Syntactically correct** (valid YAML/JSON)
- **Schema compliant** (match the required structure)
- **Semantically consistent** (relationships are valid, IDs match patterns)
- **Complete** (all required fields present)
- **Governable** (enable autonomic governance)

This guide covers:
- Types of validation
- Validation workflow during development
- CI/CD integration
- Common errors and how to fix them
- Validation tools

---

## Table of Contents

1. [Types of Validation](#types-of-validation)
2. [Validation Workflow](#validation-workflow)
3. [Manual Validation](#manual-validation)
4. [Automated Validation](#automated-validation)
5. [CI/CD Integration](#cicd-integration)
6. [Common Validation Errors](#common-validation-errors)
7. [Validation Checklist](#validation-checklist)
8. [Tools](#tools)

---

## Types of Validation

SCS validation happens at multiple levels:

### Level 1: Syntactic Validation

**What**: Is the file valid YAML or JSON?

**Checks**:
- No syntax errors
- Proper indentation
- Valid data types
- Quotes balanced

**Tools**:
- `yamllint` for YAML files
- `jsonlint` for JSON files
- IDE/editor linters

**Example error**:
```yaml
# Bad: missing colon
id scd:meta:roles
```

**Fix**:
```yaml
# Good
id: scd:meta:roles
```

---

### Level 2: Schema Validation

**What**: Does the SCD match the required schema?

**Checks**:
- All required fields present
- Field types match schema
- ID patterns correct
- No extra fields (if strict mode)

**Tools**:
- JSON Schema validators
- SCS validator tool

**Example error**:
```yaml
# Bad: missing required field 'type'
id: scd:meta:roles
title: "Roles"
# missing: type, version, description, content, provenance
```

**Fix**:
```yaml
# Good: all required fields
id: scd:meta:roles
type: meta
title: "System Roles"
version: "0.1.0"
description: "Defines system roles"
content: { }
provenance: { }
```

---

### Level 3: Semantic Validation

**What**: Do the contents make logical sense?

**Checks**:
- ID patterns match tier (`scd:meta:*`, `scd:project:*`, etc.)
- Type field matches tier in ID
- Relationship targets reference valid SCDs
- No circular dependencies
- Versions follow semver

**Example error**:
```yaml
# Bad: type doesn't match ID tier
id: scd:meta:roles
type: project  # Should be 'meta'
```

**Fix**:
```yaml
# Good: type matches ID tier
id: scd:meta:roles
type: meta
```

---

### Level 4: Relationship Validation

**What**: Are relationships valid and targets exist?

**Checks**:
- Relationship targets exist in bundle
- Relationship types are valid
- No orphaned references
- Dependency graph is acyclic (for `depends-on`)

**Example error**:
```yaml
# Bad: target doesn't exist
relationships:
  - type: satisfies
    target: scd:standards:hipaa-999  # This SCD doesn't exist
```

**Fix**:
```yaml
# Good: target exists in bundle
relationships:
  - type: satisfies
    target: scd:standards:hipaa-164.312  # This SCD exists
```

---

### Level 5: Bundle Validation

**What**: Is the bundle complete and consistent?

**Checks**:
- All SCDs listed in bundle exist
- No duplicate SCD IDs
- At least one meta-tier SCD
- At least one project-tier SCD
- All relationship targets exist within bundle
- Import references are valid

**Example error**:
```yaml
# Bad: bundle references non-existent file
scds:
  - path: context/meta/roles.yaml
    id: scd:meta:roles  # File doesn't exist!
```

**Fix**:
```yaml
# Good: file exists
scds:
  - path: context/meta/roles.yaml  # File exists
    id: scd:meta:roles
```

---

### Level 6: Compliance Validation (Optional)

**What**: Does the bundle satisfy compliance requirements?

**Checks**:
- All standards-tier requirements have `satisfies` relationships
- Required controls are implemented
- No unsatisfied obligations
- Coverage gaps identified

**This is where autonomic governance happens.**

**Example check**:
```
Governance Agent: "Checking HIPAA compliance..."
  ✓ scd:standards:hipaa-164.312(a)(2)(iv) satisfied by scd:project:auth-service
  ✓ scd:standards:hipaa-164.312(d) satisfied by scd:project:encryption-module
  ✗ scd:standards:hipaa-164.308(a)(1) NOT satisfied by any project SCD

Result: NOT COMPLIANT - 1 unsatisfied requirement
```

---

## Validation Workflow

### During Development

**Step 1: Write SCD**
- Copy template
- Fill in fields
- Add relationships

**Step 2: Validate Syntax**
```bash
yamllint context/meta/roles.yaml
```

**Step 3: Validate Schema**
```bash
scs-validate context/meta/roles.yaml
```

**Step 4: Fix Errors**
- Review error messages
- Fix issues
- Re-validate

**Step 5: Add to Bundle**
- Update `bundle.yaml`
- Reference the new SCD

**Step 6: Validate Bundle**
```bash
scs-validate --bundle context/bundle.yaml
```

**Step 7: Commit**
- Only commit when validation passes
- Include validation results in commit message

---

### Before Pull Request

**Checklist**:
- [ ] All SCDs pass syntax validation
- [ ] All SCDs pass schema validation
- [ ] Bundle is complete and consistent
- [ ] All relationship targets exist
- [ ] Provenance is filled out
- [ ] Versions are bumped appropriately
- [ ] CHANGELOG is updated

**Run full validation**:
```bash
# Validate entire bundle
scs-validate --bundle context/bundle.yaml --strict

# Check for common issues
scs-validate --bundle context/bundle.yaml --check-relationships
scs-validate --bundle context/bundle.yaml --check-compliance
```

---

### In CI/CD Pipeline

**On every commit/PR**:
1. Syntax validation (fail fast)
2. Schema validation
3. Relationship validation
4. Bundle completeness check
5. Generate validation report

**See [CI/CD Integration](#cicd-integration) below.**

---

## Manual Validation

### Quick Syntax Check

**YAML**:
```bash
# Using yamllint
yamllint context/**/*.yaml

# Using Python
python -c "import yaml; yaml.safe_load(open('context/meta/roles.yaml'))"

# Using yq
yq eval '.' context/meta/roles.yaml > /dev/null
```

**JSON**:
```bash
# Using jq
jq . schema/scd/meta-scd-template.json > /dev/null

# Using Python
python -c "import json; json.load(open('schema/scd/meta-scd-template.json'))"
```

---

### Visual Inspection Checklist

When manually reviewing an SCD:

**✓ ID Check**:
- [ ] Follows pattern: `scd:<tier>:<name>`
- [ ] Tier matches type field
- [ ] Name is descriptive and unique

**✓ Required Fields**:
- [ ] `id` present and valid
- [ ] `type` matches tier (meta/standards/project)
- [ ] `title` is human-readable
- [ ] `version` follows semver
- [ ] `description` is clear (1-3 sentences)
- [ ] `content` has relevant sections
- [ ] `provenance` has all fields

**✓ Content Quality**:
- [ ] Descriptions are clear and helpful
- [ ] Examples are provided where useful
- [ ] IDs within content follow patterns
- [ ] No placeholder text left in

**✓ Relationships**:
- [ ] All relationships have `type` and `target`
- [ ] Targets exist (or will exist) in bundle
- [ ] Relationship types are appropriate
- [ ] Descriptions explain the relationship

**✓ Provenance**:
- [ ] `created_by` is identifiable
- [ ] Timestamps are ISO8601
- [ ] `rationale` explains why SCD exists
- [ ] Updates are tracked

---

## Automated Validation

### Using the SCS Validator

**Basic validation**:
```bash
# Validate single SCD
scs-validate context/meta/roles.yaml

# Validate all SCDs in directory
scs-validate context/**/*.yaml

# Validate bundle
scs-validate --bundle context/bundle.yaml
```

**Advanced options**:
```bash
# Strict mode (no warnings allowed)
scs-validate --bundle context/bundle.yaml --strict

# Check relationships only
scs-validate --bundle context/bundle.yaml --check-relationships

# Check compliance (requires standards-tier SCDs)
scs-validate --bundle context/bundle.yaml --check-compliance

# Output JSON for tooling
scs-validate --bundle context/bundle.yaml --output json
```

**Expected output**:
```
SCS Validator v0.1.0

Validating bundle: bundle:healthcare-platform

✓ Syntax validation passed (8 files)
✓ Schema validation passed (8 files)
✓ Relationship validation passed
  - 12 relationships validated
  - 0 orphaned references
✓ Bundle completeness passed
  - 3 meta-tier SCDs
  - 2 standards-tier SCDs
  - 3 project-tier SCDs

Warnings:
  ⚠ scd:project:patient-api has no 'satisfies' relationships to standards
  ⚠ scd:meta:capabilities version 0.1.0 is older than scd:meta:roles 1.0.0

Summary:
  8 SCDs validated
  0 errors
  2 warnings

Status: ✓ VALID
```

---

## CI/CD Integration

### GitHub Actions

Create `.github/workflows/validate-scs.yml`:

```yaml
name: Validate SCS Bundle

on:
  pull_request:
    paths:
      - 'context/**'
      - 'bundle.yaml'
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

      - name: Install dependencies
        run: |
          pip install pyyaml jsonschema
          # Install scs-validator when available
          # pip install scs-validator

      - name: Validate YAML syntax
        run: |
          python -m yamllint context/**/*.yaml

      - name: Validate SCS bundle
        run: |
          # Replace with actual validator when available
          python tools/validate.py --bundle context/bundle.yaml

      - name: Check relationships
        run: |
          python tools/validate.py --bundle context/bundle.yaml --check-relationships

      - name: Generate validation report
        if: always()
        run: |
          python tools/validate.py --bundle context/bundle.yaml --output json > validation-report.json

      - name: Upload validation report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: validation-report
          path: validation-report.json
```

---

### GitLab CI

Create `.gitlab-ci.yml`:

```yaml
validate-scs:
  stage: test
  image: python:3.11

  before_script:
    - pip install pyyaml jsonschema

  script:
    - python -m yamllint context/**/*.yaml
    - python tools/validate.py --bundle context/bundle.yaml
    - python tools/validate.py --bundle context/bundle.yaml --check-relationships

  only:
    changes:
      - context/**
      - bundle.yaml

  artifacts:
    reports:
      junit: validation-report.xml
    paths:
      - validation-report.json
```

---

### Pre-commit Hook

Create `.git/hooks/pre-commit`:

```bash
#!/bin/bash

echo "Validating SCS bundle before commit..."

# Validate YAML syntax
if ! yamllint context/**/*.yaml 2>/dev/null; then
  echo "❌ YAML syntax validation failed"
  exit 1
fi

# Validate SCS bundle
if ! scs-validate --bundle context/bundle.yaml; then
  echo "❌ SCS validation failed"
  echo "Fix validation errors before committing"
  exit 1
fi

echo "✓ Validation passed"
exit 0
```

Make it executable:
```bash
chmod +x .git/hooks/pre-commit
```

---

## Common Validation Errors

### Error 1: Missing Required Field

**Error**:
```
ValidationError: Missing required field 'version' in scd:meta:roles
```

**Cause**: Required field not present

**Fix**: Add the missing field
```yaml
version: "0.1.0"
```

---

### Error 2: Invalid ID Pattern

**Error**:
```
ValidationError: ID 'meta:roles' does not match pattern 'scd:<tier>:<name>'
```

**Cause**: ID doesn't follow the required pattern

**Fix**: Add `scd:` prefix
```yaml
# Bad
id: meta:roles

# Good
id: scd:meta:roles
```

---

### Error 3: Type Mismatch

**Error**:
```
ValidationError: Type 'project' does not match tier 'meta' in ID 'scd:meta:roles'
```

**Cause**: The `type` field doesn't match the tier in the ID

**Fix**: Make them consistent
```yaml
# Bad
id: scd:meta:roles
type: project

# Good
id: scd:meta:roles
type: meta
```

---

### Error 4: Orphaned Relationship

**Error**:
```
ValidationError: Relationship target 'scd:standards:hipaa-164.312' not found in bundle
```

**Cause**: Relationship references an SCD that doesn't exist in the bundle

**Fix**: Either add the missing SCD to the bundle or remove the relationship
```yaml
# Option 1: Add to bundle.yaml
scds:
  - path: context/standards/hipaa-security.yaml
    id: scd:standards:hipaa-164.312

# Option 2: Remove relationship
# (delete the relationship referencing the missing SCD)
```

---

### Error 5: Duplicate SCD ID

**Error**:
```
ValidationError: Duplicate SCD ID 'scd:project:auth-service' found in bundle
```

**Cause**: Two SCDs in the bundle have the same ID

**Fix**: Make IDs unique
```yaml
# Change one of them
id: scd:project:auth-service-v2
# or
id: scd:project:oauth-service
```

---

### Error 6: Invalid Semver

**Error**:
```
ValidationError: Version 'v1.0' is not valid semver
```

**Cause**: Version doesn't follow semantic versioning

**Fix**: Use proper semver format
```yaml
# Bad
version: "v1.0"
version: "1"

# Good
version: "1.0.0"
version: "0.1.0"
```

---

### Error 7: Circular Dependency

**Error**:
```
ValidationError: Circular dependency detected:
  scd:project:api -> scd:project:auth -> scd:project:api
```

**Cause**: SCDs depend on each other in a cycle

**Fix**: Restructure dependencies to break the cycle
```yaml
# Identify the cycle
# Refactor to remove circular dependency
# Consider: does api really depend on auth, or vice versa?
```

---

### Error 8: Missing Bundle SCDs

**Error**:
```
ValidationError: Bundle requires at least one meta-tier SCD
```

**Cause**: Bundle doesn't meet minimum requirements

**Fix**: Add required SCDs
```yaml
scds:
  # Add at least one meta-tier SCD
  - path: context/meta/roles.yaml
    id: scd:meta:roles

  # Add at least one project-tier SCD
  - path: context/project/architecture.yaml
    id: scd:project:architecture
```

---

## Validation Checklist

### Before Committing

- [ ] All YAML files have valid syntax
- [ ] All SCDs pass schema validation
- [ ] All required fields are present
- [ ] IDs follow pattern `scd:<tier>:<name>`
- [ ] Type matches tier
- [ ] Versions follow semver
- [ ] Descriptions are clear and helpful
- [ ] Relationships have valid targets
- [ ] Provenance is complete
- [ ] Bundle references all SCDs
- [ ] No duplicate IDs
- [ ] No orphaned relationships

### Before Pull Request

- [ ] All above checks pass
- [ ] Bundle validation passes
- [ ] Relationship validation passes
- [ ] No circular dependencies
- [ ] Versions are bumped appropriately
- [ ] CHANGELOG is updated
- [ ] Validation report is clean

### Before Release

- [ ] All above checks pass
- [ ] Compliance validation passes (if applicable)
- [ ] All standards have satisfying relationships
- [ ] Bundle version is bumped
- [ ] Git tag matches bundle version
- [ ] Release notes are prepared

---

## Tools

### Official SCS Validator

**Status**: In development

**Installation** (future):
```bash
pip install scs-validator
```

**Usage** (future):
```bash
scs-validate --bundle context/bundle.yaml
```

**Features**:
- Schema validation
- Relationship validation
- Compliance checking
- CI/CD integration
- JSON output for tooling

---

### YAML Linters

**yamllint**:
```bash
pip install yamllint
yamllint context/**/*.yaml
```

**yq** (YAML processor):
```bash
# Install via package manager
brew install yq  # macOS
apt-get install yq  # Ubuntu

# Validate YAML
yq eval '.' file.yaml
```

---

### JSON Schema Validators

**Python jsonschema**:
```python
import json
import jsonschema

# Load schema
with open('schema/scd/meta-scd-template.json') as f:
    schema = json.load(f)

# Load SCD (convert YAML to JSON first)
with open('context/meta/roles.yaml') as f:
    scd = yaml.safe_load(f)

# Validate
jsonschema.validate(scd, schema)
```

**ajv** (Node.js):
```bash
npm install -g ajv-cli
ajv validate -s schema/scd/meta-scd-template.json -d context/meta/roles.json
```

---

### IDE Integration

**VS Code**:
- Install "YAML" extension
- Configure JSON Schema association
- Get inline validation and autocomplete

**IntelliJ/PyCharm**:
- Built-in YAML support
- Configure JSON Schema
- Validation on save

**Vim/Neovim**:
- Use `ale` or `coc.nvim`
- Configure YAML linting
- JSON Schema support via LSP

---

## Best Practices

### 1. Validate Early and Often

Don't wait until PR time:
- Validate after creating each SCD
- Validate bundle after updates
- Use pre-commit hooks

### 2. Automate Everything

- CI/CD pipeline validation
- Pre-commit hooks
- IDE linting
- Automated reports

### 3. Treat Warnings Seriously

Warnings often indicate:
- Incomplete implementations
- Missing relationships
- Version inconsistencies
- Future problems

Fix them before they become errors.

### 4. Use Strict Mode in CI

```bash
# Fail on warnings in CI
scs-validate --bundle context/bundle.yaml --strict
```

### 5. Version Check

When bumping versions:
- Validate that changes justify the version bump
- Check for breaking changes
- Update CHANGELOG

### 6. Validate Relationships Explicitly

```bash
# Dedicated relationship check
scs-validate --bundle context/bundle.yaml --check-relationships

# Check for orphans
scs-validate --bundle context/bundle.yaml --check-orphans
```

---

## Next Steps

### You've Learned:
- ✅ Six levels of SCS validation
- ✅ Validation workflow during development
- ✅ CI/CD integration approaches
- ✅ Common errors and how to fix them
- ✅ Validation tools and best practices

### What's Next:

1. **Set Up Validation**
   - Install yamllint
   - Set up pre-commit hooks
   - Configure CI/CD pipeline

2. **Build the Validator**
   - See the [validator implementation](../../tools/scd-validator/)
   - Contribute to validation tooling

3. **Integrate with CEDM**
   - Validation is part of the Governance phase
   - See CEDM book for full methodology

4. **Explore Autonomic Governance**
   - Compliance validation
   - Automated governance agents
   - Continuous monitoring

---

## Resources

- **Specification**: [spec/0.1/](../spec/0.1/)
- **Schemas**: [schema/](../../schema/)
- **Templates**: [templates/](../../templates/)
- **Usage Guide**: [usage-guide.md](usage-guide.md)
- **Examples**: [examples/](../../examples/) (coming soon)

---

## Questions?

- Open an issue on GitHub
- Start a discussion
- See the [FAQ](faq.md)

**Happy validating!**
