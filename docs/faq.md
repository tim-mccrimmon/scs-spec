# SCS FAQ

### What is an SCD?

An SCD (Structured Context Document) is a YAML document that captures structured context for some scope (meta, project, or standard). It is designed to be:

- Human-readable.
- Machine- and AI-parseable.
- Validatable against a schema.

See: `docs/SCD_overview.md` and `spec/0.1/core-model.md`.

---

### How is SCS different from traditional documentation?

Traditional docs (Word, PDF, wiki pages) are written **for humans** and are often ambiguous or out-of-date.

SCS provides:

- A **strict structure** enforced by JSON Schema.
- A clear separation of tiers (meta, project, standards).
- A format that AI agents and tooling can act on directly.

You can still have narrative docs, but the **source of truth** for context lives in SCDs and bundles.

---

### What is a bundle and why do I need it?

A bundle:

- Groups multiple SCDs together (e.g., all SCDs for a project).
- Is versioned as a single unit.
- Acts as a **contract** between teams, tools, and governance.

Tools can load a bundle and quickly understand the context it represents.

See: `spec/0.1/bundle-format.md`.

---

### How stable is the spec right now?

The current version is **0.1** and still evolving. Breaking changes may occur.  
See `spec/CHANGELOG.md` for details and `PROGRESS.yaml` for current focus.

---

### How do I contribute?

- Read `CONTRIBUTING.md` and `BRANCHING_CONVENTION.md`.
- Check `PULL_REQUEST_CHECKLIST.md`.
- Open an issue or pull request with your proposal.

---

### Where can I see real-world examples?

This repo focuses on the **spec itself**.

Example SCDs and bundles live in:

- `scs-reference-implementation` – a separate repo that shows SCS used in an actual project.
- `scs-registry` – (planned) registry of publicly available SCDs and SCD bundles from standards bodies and projects.

(Repo URLs to be added once public.)