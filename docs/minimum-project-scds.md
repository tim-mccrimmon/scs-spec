# Minimum Project-Tier SCDs

**Version**: 0.1
**Last Updated**: 2025-11-20

---

## Overview

This document defines the **minimum set of project-tier SCDs** that development teams should create when starting a production software project using the Structured Context Specification (SCS).

These SCDs, organized into domain bundles, represent the essential context needed to build, test, deploy, and maintain production software in a governable and auditable manner.

---

## Scope and Assumptions

### What This Document Covers

This document specifies the **project-tier SCDs only** - the context that describes the specific system being built by the development team.

### What This Document Assumes

Teams have access to:

1. **Meta-tier SCDs** (imported from scs-spec):
   - Standard vocabulary and semantics
   - Roles, capabilities, domains, concerns
   - Provided by the SCS specification itself

2. **Standards-tier SCDs** (imported or interpreted):
   - Regulatory and compliance requirements
   - Industry standards (HIPAA, SOC2, GDPR, etc.)
   - Either from standards organizations (future) or team interpretations (current)

### Intended Use

This minimum set is appropriate for:
- Production software projects
- Regulated or enterprise environments
- AI-assisted development workflows
- Projects requiring governance and compliance

Smaller or prototype projects may use a reduced subset.

---

## Naming Conventions

Following the [recommended project structure](project-structure.md):

### Bundle Files
- **Location**: `bundles/domains/`
- **Format**: `{domain-name}.yaml`
- **Example**: `bundles/domains/architecture.yaml`

### SCD Files
- **Location**: `context/project/`
- **Format**: `{scd-name}.yaml`
- **Example**: `context/project/system-context.yaml`

### SCD IDs
- **Format**: `scd:project:{scd-name}`
- **Example**: `scd:project:system-context`

---

## Bundle Organization

The minimum set consists of **10 domain bundles**, each containing 2-4 essential project-tier SCDs.

```
bundles/
├── project-bundle.yaml                    # Master bundle (imports all domain bundles)
└── domains/
    ├── architecture.yaml                  # System architecture and design
    ├── security.yaml                      # Security and data protection
    ├── performance-reliability.yaml       # Performance and reliability requirements
    ├── usability-accessibility.yaml       # User experience and accessibility
    ├── compliance-governance.yaml         # Compliance and governance
    ├── data-provenance.yaml               # Data management and lineage
    ├── testing-validation.yaml            # Testing and quality assurance
    ├── deployment-operations.yaml         # Deployment and operations
    ├── safety-risk.yaml                   # Safety and risk management
    └── ethics-ai-accountability.yaml      # AI ethics and accountability

context/project/
├── system-context.yaml
├── integration-map.yaml
├── component-model.yaml
├── tech-stack.yaml
├── authn-authz.yaml
├── data-protection.yaml
├── ... (30+ project SCDs)
```

---

## 0. Project Bundle (Master)

**File**: `bundles/project-bundle.yaml`

**Purpose**: Top-level bundle that imports all domain bundles and defines project identity.

**Contains**:
```yaml
id: bundle:{project-name}
version: "1.0.0"
title: "{Project Name} Complete Context Bundle"
description: "Complete structured context for {project-name}"

imports:
  # Domain bundles
  - bundle:architecture:1.0.0
  - bundle:security:1.0.0
  - bundle:performance-reliability:1.0.0
  - bundle:usability-accessibility:1.0.0
  - bundle:compliance-governance:1.0.0
  - bundle:data-provenance:1.0.0
  - bundle:testing-validation:1.0.0
  - bundle:deployment-operations:1.0.0
  - bundle:safety-risk:1.0.0
  - bundle:ethics-ai-accountability:1.0.0

scds:
  # Meta-tier SCDs (imported from scs-spec)
  - scd:meta:roles
  - scd:meta:capabilities
  - scd:meta:domains
  - scd:meta:concerns

provenance:
  created_by: "team-lead@company.com"
  created_at: "2025-11-20T10:00:00Z"
  rationale: "Initial project bundle for {project-name} development"
```

---

## 1. Architecture Bundle

**File**: `bundles/domains/architecture.yaml`

**Purpose**: Defines system architecture, components, and technical design.

### Minimum SCDs

#### 1.1 System Context
**File**: `context/project/system-context.yaml`
**ID**: `scd:project:system-context`

**Defines**:
- System boundaries and scope
- External actors and systems
- Key data flows and interactions
- Integration points

#### 1.2 Tech Stack
**File**: `context/project/tech-stack.yaml`
**ID**: `scd:project:tech-stack`

**Defines**:
- Programming languages and frameworks
- Databases and data stores
- Infrastructure and platforms
- Third-party services and libraries
- Rationale for technology choices

#### 1.3 Integration Map
**File**: `context/project/integration-map.yaml`
**ID**: `scd:project:integration-map`

**Defines**:
- External system interfaces
- API protocols and contracts
- Upstream and downstream dependencies
- Data exchange formats

#### 1.4 Component Model
**File**: `context/project/component-model.yaml`
**ID**: `scd:project:component-model`

**Defines**:
- Logical and physical components
- Component responsibilities and boundaries
- Inter-component communication
- Deployment units

---

## 2. Security Bundle

**File**: `bundles/domains/security.yaml`

**Purpose**: Defines security controls, data protection, and threat management.

### Minimum SCDs

#### 2.1 Authentication & Authorization
**File**: `context/project/authn-authz.yaml`
**ID**: `scd:project:authn-authz`

**Defines**:
- Identity model and user management
- Authentication mechanisms
- Authorization model and policies
- Role-based access control (RBAC)
- Session management

#### 2.2 Data Protection
**File**: `context/project/data-protection.yaml`
**ID**: `scd:project:data-protection`

**Defines**:
- Encryption at rest and in transit
- Key management strategy
- Certificate management
- Secrets handling and storage
- Cryptographic standards

#### 2.3 Data Handling
**File**: `context/project/data-handling.yaml`
**ID**: `scd:project:data-handling`

**Defines**:
- Data classification scheme
- Retention and deletion policies
- Data minimization practices
- Secure data handling patterns
- Privacy controls

#### 2.4 Threat Model
**File**: `context/project/threat-model.yaml`
**ID**: `scd:project:threat-model`

**Defines**:
- Identified threats and attack vectors
- Attack surfaces and trust boundaries
- Threat mitigations and controls
- Security assumptions
- Residual risks

---

## 3. Performance & Reliability Bundle

**File**: `bundles/domains/performance-reliability.yaml`

**Purpose**: Defines performance requirements, reliability targets, and resilience patterns.

### Minimum SCDs

#### 3.1 Response Time
**File**: `context/project/response-time.yaml`
**ID**: `scd:project:response-time`

**Defines**:
- Latency targets and SLOs
- Throughput requirements
- Performance budgets by operation
- Performance testing criteria

#### 3.2 Availability
**File**: `context/project/availability.yaml`
**ID**: `scd:project:availability`

**Defines**:
- Uptime targets and SLAs
- Redundancy strategy
- Failover mechanisms
- Disaster recovery approach

#### 3.3 Fault Tolerance
**File**: `context/project/fault-tolerance.yaml`
**ID**: `scd:project:fault-tolerance`

**Defines**:
- Error handling strategy
- Resilience patterns (circuit breaker, retry, timeout)
- Graceful degradation
- Backoff and retry policies

#### 3.4 Scalability
**File**: `context/project/scalability.yaml`
**ID**: `scd:project:scalability`

**Defines**:
- Horizontal and vertical scaling strategy
- Capacity planning assumptions
- Load distribution approach
- Resource limits and quotas

---

## 4. Usability & Accessibility Bundle

**File**: `bundles/domains/usability-accessibility.yaml`

**Purpose**: Defines user experience principles and accessibility requirements.

### Minimum SCDs

#### 4.1 UX Principles
**File**: `context/project/ux-principles.yaml`
**ID**: `scd:project:ux-principles`

**Defines**:
- Target user personas
- User experience principles
- Key user journeys
- Design patterns and conventions

#### 4.2 Accessibility Compliance
**File**: `context/project/accessibility-compliance.yaml`
**ID**: `scd:project:accessibility-compliance`

**Defines**:
- Accessibility standards (e.g., WCAG 2.1 Level AA)
- Supported assistive technologies
- Accessibility testing requirements
- Keyboard navigation requirements

#### 4.3 Error Handling UX
**File**: `context/project/error-handling-ux.yaml`
**ID**: `scd:project:error-handling-ux`

**Defines**:
- Error message guidelines
- User feedback patterns
- Recovery flows
- Help and documentation strategy

---

## 5. Compliance & Governance Bundle

**File**: `bundles/domains/compliance-governance.yaml`

**Purpose**: Maps system to regulatory requirements and defines governance processes.

### Minimum SCDs

#### 5.1 HIPAA Compliance
**File**: `context/project/hipaa-compliance.yaml`
**ID**: `scd:project:hipaa-compliance`

**Defines**:
- HIPAA applicability and scope
- Technical safeguards implementation
- Administrative safeguards
- Physical safeguards
- Mapped controls to HIPAA requirements

**Note**: For non-healthcare projects, replace with applicable regulations (GDPR, PCI-DSS, etc.)

#### 5.2 CHAI Adherence
**File**: `context/project/chai-adherence.yaml`
**ID**: `scd:project:chai-adherence`

**Defines**:
- CHAI criteria applicability
- Traceability hooks into system
- Evidence collection approach
- Validation strategy

**Note**: Healthcare-specific; omit or replace for other industries

#### 5.3 SOC2 Controls
**File**: `context/project/soc2-controls.yaml`
**ID**: `scd:project:soc2-controls`

**Defines**:
- Trust service criteria (Security, Availability, etc.)
- Control implementations
- Evidence collection
- Audit preparation

#### 5.4 TEFCA Participation
**File**: `context/project/tefca-participation.yaml`
**ID**: `scd:project:tefca-participation`

**Defines**:
- TEFCA role (if applicable)
- Interoperability requirements
- Integration points with QHINs
- Data sharing policies

**Note**: Healthcare-specific; omit if not applicable

---

## 6. Data & Provenance Bundle

**File**: `bundles/domains/data-provenance.yaml`

**Purpose**: Defines data models, lineage tracking, and retention policies.

### Minimum SCDs

#### 6.1 Data Model
**File**: `context/project/data-model.yaml`
**ID**: `scd:project:data-model`

**Defines**:
- Canonical data entities
- Schema definitions
- Key relationships and constraints
- Data validation rules

#### 6.2 Provenance Tracking
**File**: `context/project/provenance-tracking.yaml`
**ID**: `scd:project:provenance-tracking`

**Defines**:
- Data origin tracking
- Lineage and transformation tracking
- Audit trail requirements
- Data versioning approach

#### 6.3 Retention Policy
**File**: `context/project/retention-policy.yaml`
**ID**: `scd:project:retention-policy`

**Defines**:
- Data retention periods by type
- Archival strategy
- Deletion and anonymization rules
- Compliance with retention requirements

---

## 7. Testing & Validation Bundle

**File**: `bundles/domains/testing-validation.yaml`

**Purpose**: Defines testing strategy, coverage requirements, and validation approach.

### Minimum SCDs

#### 7.1 Test Coverage
**File**: `context/project/test-coverage.yaml`
**ID**: `scd:project:test-coverage`

**Defines**:
- Coverage targets by layer (unit, integration, e2e)
- Critical path identification
- Test metrics and reporting
- Coverage requirements for release

#### 7.2 Validation Plan
**File**: `context/project/validation-plan.yaml`
**ID**: `scd:project:validation-plan`

**Defines**:
- Validation scenarios and test cases
- Test environments and data
- Validation criteria for release
- Regression testing approach

#### 7.3 QA Procedures
**File**: `context/project/qa-procedures.yaml`
**ID**: `scd:project:qa-procedures`

**Defines**:
- Manual QA processes
- Acceptance criteria
- Bug triage and severity levels
- Release quality gates

---

## 8. Deployment & Operations Bundle

**File**: `bundles/domains/deployment-operations.yaml`

**Purpose**: Defines infrastructure, deployment processes, and operational practices.

### Minimum SCDs

#### 8.1 Infrastructure Definition
**File**: `context/project/infrastructure-definition.yaml`
**ID**: `scd:project:infrastructure-definition`

**Defines**:
- Environment definitions (dev, staging, prod)
- Infrastructure patterns and topology
- Infrastructure as Code (IaC) approach
- Cloud resources and configuration

#### 8.2 Observability
**File**: `context/project/observability.yaml`
**ID**: `scd:project:observability`

**Defines**:
- Logging strategy and standards
- Metrics collection and dashboards
- Distributed tracing approach
- Alerting rules and thresholds

#### 8.3 Incident Response
**File**: `context/project/incident-response.yaml`
**ID**: `scd:project:incident-response`

**Defines**:
- Runbooks and playbooks
- Severity levels and SLAs
- On-call rotation and escalation
- Post-incident review process

---

## 9. Safety & Risk Bundle

**File**: `bundles/domains/safety-risk.yaml`

**Purpose**: Identifies and manages risks and safety concerns.

### Minimum SCDs

#### 9.1 Risk Assessment
**File**: `context/project/risk-assessment.yaml`
**ID**: `scd:project:risk-assessment`

**Defines**:
- Identified risks and threats
- Likelihood and impact assessment
- Risk mitigation strategies
- Risk monitoring and review process

#### 9.2 Safety Checklist
**File**: `context/project/safety-checklist.yaml`
**ID**: `scd:project:safety-checklist`

**Defines**:
- Safety limits and guardrails
- Pre-release safety checks
- Safety-critical components
- Safety incident response

---

## 10. Ethics & AI Accountability Bundle

**File**: `bundles/domains/ethics-ai-accountability.yaml`

**Purpose**: Defines responsible AI use, accountability, and ethical guidelines.

### Minimum SCDs

#### 10.1 AI Usage Policy
**File**: `context/project/ai-usage-policy.yaml`
**ID**: `scd:project:ai-usage-policy`

**Defines**:
- Where and how AI is used in the system
- AI usage constraints and limitations
- Human-in-the-loop requirements
- AI transparency requirements

#### 10.2 Audit Trail
**File**: `context/project/audit-trail.yaml`
**ID**: `scd:project:audit-trail`

**Defines**:
- What gets logged for decisions
- Data access logging
- AI/ML model call logging
- Audit log retention and access

#### 10.3 Model Bias
**File**: `context/project/model-bias.yaml`
**ID**: `scd:project:model-bias`

**Defines**:
- Bias and fairness assessment approach
- Evaluation datasets and metrics
- Bias mitigation strategies
- Ongoing monitoring for bias

---

## Summary Statistics

**Total Domain Bundles**: 10
**Total Project-Tier SCDs**: 38
**Average SCDs per Bundle**: 3-4

### SCD Count by Bundle

| Bundle | SCD Count |
|--------|-----------|
| Architecture | 4 |
| Security | 4 |
| Performance & Reliability | 4 |
| Usability & Accessibility | 3 |
| Compliance & Governance | 4 |
| Data & Provenance | 3 |
| Testing & Validation | 3 |
| Deployment & Operations | 3 |
| Safety & Risk | 2 |
| Ethics & AI Accountability | 3 |
| **Total** | **38** |

---

## Adapting for Different Projects

### Healthcare Projects
Use as specified - includes HIPAA, CHAI, TEFCA

### Financial Services Projects
Replace healthcare compliance with:
- PCI-DSS compliance
- SOX controls
- Financial regulations (Dodd-Frank, etc.)

### Government Projects
Replace with:
- NIST frameworks (800-53, 800-171)
- FedRAMP requirements
- Authority to Operate (ATO) requirements

### SaaS Products
Emphasis on:
- SOC2 (keep as is)
- GDPR compliance
- Multi-tenancy concerns
- SLA management

### Lightweight Projects
Consider reducing to essential bundles:
- Architecture (4 SCDs)
- Security (4 SCDs)
- Deployment & Operations (3 SCDs)
- **Total: ~11 SCDs minimum**

---

## Implementation Guidance

### Starting a New Project

1. **Copy bundle structure**:
   ```bash
   mkdir -p bundles/domains
   mkdir -p context/project
   ```

2. **Create project bundle**: `bundles/project-bundle.yaml`

3. **Create domain bundles** in priority order:
   - Architecture (defines system)
   - Security (non-negotiable)
   - Deployment & Operations (need to deploy)
   - Others as needed

4. **Create SCDs** within each bundle as DRAFT

5. **Iterate and refine** in DRAFT mode

6. **Version and lock** when ready to build

### Using Templates

Templates for all SCDs listed here are available in the [SCS Reference Implementation](https://github.com/your-org/scs-reference-implementation) repository.

---

## Related Documentation

- [Project Structure](project-structure.md) - Recommended file organization
- [Bundle Lifecycle](bundle-lifecycle.md) - How bundles evolve through development
- [Bundle Format Specification](../spec/0.1/bundle-format.md) - Technical bundle structure
- [Validation Workflow](validation-workflow.md) - How to validate bundles and SCDs

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2025-11-20 | Initial definition of minimum project-tier SCDs |

---

## Questions?

- Open an [issue](https://github.com/tim-mccrimmon/scs-spec/issues)
- Start a [discussion](https://github.com/tim-mccrimmon/scs-spec/discussions)
- See the [FAQ](faq.md)
