# SCS 0.1 — Terminology  
**Version:** 0.1 (Draft)  
**Status:** Work in Progress  
**Last Updated:** 2025-11-17  

---

## 1. Purpose

This document defines the terminology used throughout the Structured Context Specification (SCS).  
Terms defined here are considered **normative** for all SCS documents unless explicitly stated otherwise.

Clear terminology ensures that humans, tools, and AI agents interpret SCS consistently.

---

## 2. Core Concepts

### **2.1 Context**
Information that describes the structure, behavior, intent, constraints, responsibilities, or requirements of a system.

Context includes:
- architecture  
- requirements  
- compliance expectations  
- operational constraints  
- performance goals  
- security posture  
- design intent  
- domain concepts  

SCS treats context as a first-class artifact.

---

### **2.2 Structured Context**
Context represented in a **machine-readable**, **human-readable**, and **version-controlled** form.

Structured context is:
- explicit  
- precise  
- hierarchical  
- linkable  
- analyzable  
- AI-interpretable  

SCDs (Structured Context Documents) are the units of structured context.

---

### **2.3 Structured Context Document (SCD)**  
A **self-contained, typed, versioned document** that represents a coherent slice of system context.

An SCD includes:
- metadata  
- descriptive fields  
- requirements or constraints  
- relationships to other SCDs  
- references to standards or domains  

SCDs are the foundational building blocks of SCS.

---

### **2.4 SCD Type**
Each SCD belongs to exactly one of the three SCS tiers:

1. **Meta-Tier** — system-level semantics and conceptual framing  
2. **Standards-Tier** — imported or codified compliance/spec standards  
3. **Project-Tier** — system-specific context for the project

The SCD type determines:
- semantic role  
- schema used  
- allowed references  
- placement in bundles  

---

### **2.5 SCD Bundle**
A collection of SCDs across one or more tiers that together represent the complete contextual definition of a system.

Bundles:
- organize SCDs  
- define boundaries  
- are versioned as a whole  
- serve as the unit of analysis for tools  
- act as the **context contract** for a project  

Bundles are typically stored as directories or YAML aggregate files.

---

### **2.6 Identifier**
A unique, stable identifier assigned to each SCD, used for:

- cross-SCD linking  
- external references  
- traceability  
- versioning  
- tool interoperability  

Identifiers should follow SCS naming conventions (defined in future versions).

---

### **2.7 Relationship**
A typed connection between SCDs.

Examples include:
- *depends-on*  
- *constrains*  
- *extends*  
- *refines*  
- *satisfies*  
- *conflicts-with*  

Relationships support reasoning, impact analysis, and governance.

---

### **2.8 Constraint**
Any requirement, limit, rule, or boundary imposed on the system.

Examples:
- security constraints  
- architectural constraints  
- performance thresholds  
- compliance rules  
- data retention limits  

Constraints may originate from project needs or external standards.

---

### **2.9 Requirement**
An obligation, behavior, or condition the system must fulfill.

Requirements may be:
- functional  
- non-functional  
- compliance-driven  
- architectural  
- operational  

SCDs may define or reference requirements.

---

### **2.10 Capability**
A unit of system functionality or behavior.

Capabilities describe:
- what the system can do  
- the roles involved  
- affected domains  
- relationships to requirements  

Capabilities are often organized in Meta- or Project-Tier SCDs.

---

### **2.11 Domain**
A conceptual area relevant to the system.

Domains help structure:
- vocabulary  
- object models  
- constraints  
- responsibilities  

Standards (e.g., CHAI, HIPAA) may define their own domains.

---

## 3. Tiers

### **3.1 Meta-Tier**
Defines system-wide semantics, roles, cross-cutting structures, and conceptual framing.

Guides:
- how teams speak about the system  
- what concepts mean  
- how context is expressed  

The meta-tier is foundational.

---

### **3.2 Standards-Tier**
Represents external standards, including:

- regulatory requirements  
- certification frameworks  
- interoperability standards  
- organizational policies  

Examples:
- HIPAA  
- CHAI  
- SOC2  
- ISO 27001  
- NIST 800-53  

Standards-tier SCDs serve as contracts imported into a project.

---

### **3.3 Project-Tier**
Defines the actual system being built.

Project-tier SCDs include:
- architecture  
- modules  
- data flows  
- performance expectations  
- security posture  
- requirements  
- constraints  
- compliance mappings  

This tier is unique per project.

---

## 4. Governance and Traceability

### **4.1 Traceability**
The ability to follow a concept or requirement:

- from definition  
- to implementation  
- to verification  
- to governance evidence  

Traceability is achieved through SCD identifiers, relationships, and bundles.

---

### **4.2 Provenance**
Metadata describing the origin, authorship, changes, and decisions behind an SCD or bundle.

Provenance supports:
- auditing  
- compliance review  
- reproducibility  
- accountability  

---

### **4.3 Context Contract**
A versioned SCD bundle that defines the authoritative context of a system.

It is used by:
- human contributors  
- AI agents  
- governance systems  
- auditors  

The contract evolves through version-controlled change.

---

## 5. AI-Native Concepts

### **5.1 AI Agent**
Any AI system participating in the project lifecycle, including:

- code assistants  
- evaluators  
- governance agents  
- analysis tools  
- documentation assistants  

AI agents consume and produce structured context.

---

### **5.2 Human Contributor**
Any human involved in the definition, development, or governance of a system.

Humans and AI collaborate through shared structured context.

---

### **5.3 Autonomic Governance**
Continuous, AI-driven evaluation of a system’s:

- compliance  
- architecture  
- constraints  
- quality attributes  
- changes over time  

Autonomic governance relies on SCDs and bundles.

---

## 6. Documents in This Specification

### **6.1 Specification**
Authoritative normative documents that define SCS.

Found in the `/spec/` directory.

---

### **6.2 Schema**
Machine-readable definitions for SCD structure.

Found in the `/schema/` directory.

---

### **6.3 Template**
Starter SCD documents for human authors.

Found in the `/templates/` directory.

---

### **6.4 Example**
Concrete, realistic SCD bundles demonstrating SCS use.

Found in the `/examples/` directory.

---

## 7. Feedback

All terminology feedback should be submitted via GitHub Issues for review and incorporation.