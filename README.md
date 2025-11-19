# Structured Context Specification (SCS)

The Structured Context Specification (SCS) defines a **machine-readable way to describe context** for systems, projects, and standards.

It is designed so that:

- Humans can write and review specifications in Markdown/YAML.
- Tools and AI agents can **validate, reason over, and generate** artifacts (code, configs, governance evidence) from a single, versioned source of truth.
- Standards bodies, governance teams, and project teams can all use the **same structure** to describe intent and constraints.

This repository contains the **core SCS spec**, reference schemas, templates, and validation tools.  
Concrete examples and implementations live in sibling repos (e.g., `scs-reference-implementation`, `scs-registry`, etc.).

---

## Repository Structure

At a glance:

- **`spec/`** – The normative SCS specification (versioned).
- **`schema/`** – JSON Schemas for SCDs and SCD bundles.
- **`templates/`** – YAML templates for creating new SCDs and minimal bundles.
- **`docs/`** – Human-oriented guides (overview, getting started, FAQ, usage, validation workflow).
- **`tools/`** – Helper tools (e.g., SCD validator).
- **Root files** – Governance, contribution, and progress tracking (e.g., `PROGRESS.yaml`).

### `spec/`

The **normative spec** lives under `spec/0.1/` (current working version):

- `overview.md` – High-level introduction to SCS and its goals.
- `core-model.md` – The core concepts: SCD, bundle, tiers, identifiers, lifecycle.
- `meta-tier.md` – Structure and semantics for the meta tier (cross-cutting definitions).
- `project-tier.md` – Structure and semantics for project-level SCDs.
- `standards-tier.md` – Structure and semantics for standards-level SCDs.
- `governance-and-compliance.md` – How SCS supports auditability, governance, and autonomic compliance.
- `bundle-format.md` – How to assemble SCDs into bundles and how they are versioned.
- `terminology.md` – Glossary and definitions.

Version history for the spec lives in:

- `spec/CHANGELOG.md`

### `schema/`

Machine-level definitions:

- `schema/scd/meta-scd-template.json` – JSON Schema for meta-tier SCDs.
- `schema/scd/project-scd-template.json` – JSON Schema for project-tier SCDs.
- `schema/scd/standards-scd-template.json` – JSON Schema for standards-tier SCDs.
- `schema/bundles/scd-bundle-schema.json` – JSON Schema for SCD bundles.

> These schemas are what tools and AI agents should use to **validate** SCDs and bundles.

### `templates/`

Starter files for humans and tools:

- `templates/scd/meta_scd_template.yaml` – YAML starter for meta-tier SCDs.
- `templates/scd/project_scd_template.yaml` – YAML starter for project-tier SCDs.
- `templates/scd/standard_scd_template.yaml` – YAML starter for standards-tier SCDs.
- `templates/bundles/minimal-project-bundle.yaml` – Minimal bundle illustrating how to group SCDs for a single project.

> If you’re creating your first SCD or bundle, **start here**.

### `docs/`

Guides and explanatory material:

- `docs/SCD_overview.md` – What an SCD is, and how it fits into the SCS model.
- `docs/getting-started.md` – “Hello, SCS” – creating your first SCD and bundle.
- `docs/usage-guide.md` – How to use SCS in a project or organization.
- `docs/validation-workflow.md` – How to validate SCDs/bundles with the tooling.
- `docs/notes_on_meta_layer.md` – Deeper notes on the meta tier.
- `docs/faq.md` – Common questions and answers about SCS.
- `docs/SCS_tools_Initial_concepts.md` – Early concepts for the toolchain.

### `tools/`

- `tools/scd-validator/` – CLI or script(s) for validating SCDs and bundles against the JSON Schemas.
  - `tools/scd-validator/README.md` – How to install and use the validator.

---

## Progress & Governance

- `PROGRESS.yaml` – A machine-readable snapshot of the current state of this repo (what’s done, what’s in progress, what’s next).  
  This is intended to help both humans and AI agents quickly understand “where we are.”
- `GOVERNANCE.md` – High-level governance model for this spec.
- `BRANCHING_CONVENTION.md` – Branch naming and workflow.
- `PULL_REQUEST_CHECKLIST.md` – Checklist for contributors before opening a PR.
- `CONTRIBUTING.md` – How to contribute, expectations, and workflow.
- `CODE_OF_CONDUCT.md` – Expected behavior in this community.
- `LICENSE.md` – License for this repository.

---

## Who Is This For?

SCS is intended to be used by:

- **Standards bodies / governance teams** – To publish machine-readable specifications and checklists.
- **Project teams** – To define intent, constraints, and compliance targets as structured context.
- **Tooling & AI agents** – To validate, interpret, and act on structured context.

If you are:

- A **new contributor**, start with:
  1. `spec/0.1/overview.md`
  2. `docs/SCD_overview.md`
  3. `docs/getting-started.md`

- A **tooling/AI engineer**, focus on:
  1. `schema/`
  2. `templates/`
  3. `tools/scd-validator/`
  4. `spec/0.1/core-model.md` and `bundle-format.md`

---

## Quick Start

1. **Clone this repo**

```bash
git clone https://github.com/tim-mccrimmon/scs-spec.git
cd scs-spec
```

2. **Create a new SCD** (example: project-tier SCD)

```bash
cp templates/bundles/minimal-project-bundle.yaml my_project_bundle.yaml
# Reference your SCD(s) in the bundle
```

4. **Validate your SCD** / bundle
See docs/validation-workflow.md and tools/scd-validator/README.md for details.

## Status

The current working version of the spec is 0.1 and is still evolving.
For current focus and next steps, see:

`PROGRESS.yaml`

If you have questions, suggestions, or want to collaborate, please open an issue or pull request.