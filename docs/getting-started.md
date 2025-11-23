# Getting Started with the Structured Context Specification (SCS)

This guide walks you through a **minimal end-to-end flow**:

1. Understand the basic concepts.
2. Create your first SCD.
3. Create a bundle.
4. Validate it.

## 1. Prerequisites

You should be comfortable with:

- Reading and editing **YAML** files.
- Basic command-line usage.
- Git fundamentals (cloning a repo, committing changes).

If you’re new to SCS, read these first:

`spec/0.1/overview.md`
`docs/SCD_overview.md`

## 2. Key Concepts (Super Short)

**SCD (Structured Context Document)** – A YAML file that captures structured context for something specific:

- A meta definition (e.g., generic performance metrics).
- A project (e.g., system context, risk register).
- A standard (e.g., CHAI adherence controls, HIPAA baseline).

**Bundle** – A YAML file that **groups one or more SCDs** for a specific purpose:

- A project contract.
- A standards profile.
- A compliance pack.

Tiers:

**Meta tier** – Cross-cutting types and definitions.
**Project tier** – Context for a specific project or system.
**Standards tier** – Context that comes from a standard or regulatory body.

For details, see:

`spec/0.1/core-model.md`
`spec/0.1/meta-tier.md`
`spec/0.1/project-tier.md`
`spec/0.1/standards-tier.md`

## 3. Create Your First SCD

In this example, we’ll create a **project-tier SCD**.

1. **Copy the template:**

```bash
cd scs-spec
cp templates/scd/project_scd_template.yaml examples.my_first_project_scd.yaml
```

2.	Open the file in your editor and fill in the placeholders:

- Give it a clear id (e.g., my_first_project.scd.system_context).
- Set tier: project.
- Set a version, status, and a short summary.
- Fill in at least one meaningful section in the content block.

3.	Save the file.

Tip: It’s fine if your first SCD is incomplete — the goal is to get the structure right.

⸻

## 4. Create a Minimal Bundle

1.	Copy the bundle template:

```bash
cp templates/bundles/minimal-project-bundle.yaml examples.my_first_bundle.yaml
```

2.	Edit examples.my_first_bundle.yaml:

- Set a unique bundle id and name.
- Add your SCD file under the scds: list, e.g.:

```yaml
scds:
  - path: ./examples.my_first_project_scd.yaml
    role: primary_system_context
```

3.	Save the file.

⸻

## 5. Validate Your SCD and Bundle

There are two main validation layers:

1.	YAML & schema validation – Does the file conform to the SCS JSON Schema?
2.	Semantic validation – Are required fields present and consistent?

5.1 Using the SCD Validator

See tools/scd-validator/README.md for full details. A typical flow looks like:

```bash
cd tools/scd-validator
# Install dependencies (example, exact command may vary)
# pip install -r requirements.txt

# Validate a single SCD
./validate_scd.py ../../examples.my_first_project_scd.yaml

# Validate a bundle
./validate_bundle.py ../../examples.my_first_bundle.yaml
```

You should see either:
	•	A success message, or
	•	A list of validation errors (with line/field hints).

⸻

## 6. What Next?

Depending on who you are:

- Project team – Start defining:
- System context SCDs.
- Risk/compliance SCDs.
- Performance and reliability SCDs.
- Then assemble them into a project bundle.
- Standards/governance team – Start from:
- templates/scd/standard_scd_template.yaml
- spec/0.1/standards-tier.md

And model your standard (e.g., CHAI, HIPAA baseline) as an SCD (or a bundle of SCDs).

- Tooling / AI engineers – Integrate:
- schema/ for schema validation.
- templates/ as generation targets.
- SCD bundles into your pipeline as inputs for agents.

For more detailed guidance, see:

- docs/usage-guide.md
- docs/validation-workflow.md
- docs/faq.md
