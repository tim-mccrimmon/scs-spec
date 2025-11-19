# SCS 0.1 — Bundle Format  
**Version:** 0.1 (Draft)  
**Status:** Work in Progress  
**Last Updated:** 2025-11-17  

---

## 1. Purpose

The **SCD Bundle** is the top-level unit of context within a project.  
It defines *the complete set of Structured Context Documents (SCDs)* used to describe, constrain, and govern a system.

The Bundle Format defines:

- how SCDs are grouped  
- how they are referenced  
- how a project declares the SCDs it uses  
- how tools load, analyze, and reason over them  
- how versions and tier boundaries are managed  

In SCS 0.1, the bundle serves as the **authoritative contract** for a project.

---

## 2. What Is an SCD Bundle?

An **SCD Bundle** is:

- a collection of SCD files across all three tiers (Meta → Standards → Project)  
- bound together by a `bundle.yaml` manifest  
- versioned as a set  
- used by tools as the “active context” for evaluation  
- the root context for AI-driven development and autonomic governance  

A project MUST have exactly **one** bundle.

Bundles MAY import SCDs from external sources, libraries, or other repos.

---

## 3. Bundle Directory Structure (Recommended)

SCS does not require a strict directory layout, but the following structure is recommended:

project/
bundle.yaml
scd/
meta/
*.yaml
standards/
*.yaml
project/
*.yaml

Your current repo structure is fully compatible with this model.

---

## 4. Bundle Manifest — `bundle.yaml`

The manifest file (`bundle.yaml`) serves as the single source of truth for which SCDs are included in the bundle.

### 4.1 Required Fields

| Field | Description |
|-------|-------------|
| `id` | Unique bundle identifier |
| `version` | Version of the bundle (not of SCS itself) |
| `title` | Human-readable name |
| `description` | Summary of what this bundle represents |
| `scds` | List of SCD references |
| `imports` | Optional external bundles or libraries |
| `provenance` | Authorship and history |

---

## 5. Bundle YAML — Example (Minimal)

```yaml
id: bundle:example-system
version: "0.1"
title: "Example System Bundle"
description: >
  The complete set of Structured Context Documents
  defining the Example System for version 0.1.

scds:
  - scd:meta:roles
  - scd:meta:capabilities
  - scd:standards:hipaa
  - scd:project:architecture
  - scd:project:security
  - scd:project:data-flow

imports: []

provenance:
  created_by: "timmccrimmon"
  created_at: "2025-11-17T10:00:00Z"
  updated_by: "timmccrimmon"
  updated_at: "2025-11-17T10:00:00Z"
```

---

### 6. Bundle YAML — Example (With External Imports)

```yaml
id: bundle:oh-medapp
version: "1.2"
title: "OH | Medical App Bundle"

description: >
  Structured Context Bundle for Medical Application.
  Includes internal meta definitions plus imported standards.

imports:
  - bundle:scs:standards-library:0.1

scds:
  - scd:meta:roles
  - scd:meta:domains
  - scd:meta:capabilities

  - scd:standards:hipaa-01
  - scd:standards:chai-02

  - scd:project:architecture
  - scd:project:security
  - scd:project:capabilities
  - scd:project:data-flows
```

This supports future scenarios where SCS hosts “libraries” of reusable SCDs.

---

## 7. SCD Reference Format

Bundle entries reference SCDs using:
scd:<tier>:<name>
Where <tier> is one of:

- meta
- standards
- project

Examples:

scd:meta:roles
scd:standards:hipaa
scd:project:architecture

Tools must resolve these references by:
- locating the SCD file
- verifying its schema
- loading it into the bundle context graph

---

## 8. Bundle Semantics

The Bundle defines:

### 8.1 Completeness

The bundle MUST list every SCD required to define the system.

### 8.2 Source of Truth

The bundle is the root context used by:

- editors
- evaluators
- validators
- governance engines
- AI code assistants

### 8.3 Immutability per Version

A bundle version should remain immutable once released.

### 8.4 Cross-Tier Binding

Meta → Standards → Project form a graph only when loaded together through the bundle.

---

## 9. Relationships Across the Bundle

SCD relationships (e.g., depends-on, satisfies) become meaningful only when loaded as part of the bundle.

The bundle establishes:

- the evaluation order
- semantic grounding
- canonical IDs
- global relationship resolution
- the full context graph

Tools SHOULD load SCDs in this order:

1.	Meta-Tier
2.	Standards-Tier
3.	Project-Tier

This ensures:

- vocabulary is defined before it’s used
- obligations exist before mappings
- system structure is defined last

---

10. Bundle Validation Requirements

Tools MUST validate that:

- all SCD references resolve
- SCD schema validation passes
- SCD tier is consistent with reference format
- SCD identifiers are unique
- there are no circular imports
- bundle metadata is valid

Tools MAY also perform:

- cross-tier semantic checks
- compliance completeness checks
- dependency cycle analysis

These are non-normative in SCS 0.1.

---

## 11. Future Extensions

Future versions may introduce:

- modular sub-bundles
- inheritance/extension between bundles
- bundle schemas
- bundle signatures for attestation
- multi-bundle workspaces
- dynamic or environment-specific bundles
- runtime bundle variants

SCS 0.1 defines the minimal, stable bundle representation.

---

## 12. Feedback

Comments and refinements for the Bundle Format should be submitted through GitHub Issues.