# Issue 03: Review Domain Requirements

## Overview

The **DOMAIN-META** specification prescribes 10 mandatory domains for production projects. This ensures comprehensive system coverage, but may be too restrictive for certain project types.

## Current Rules (from DOMAIN-META)

### Prescribed Domains

Production projects **MUST** include these 10 domains:

1. **Architecture** - System structure, components, boundaries
2. **Security** - Threat models, auth, data protection
3. **Performance & Reliability** - Performance, scalability, availability
4. **Usability & Accessibility** - UX, accessibility, interaction patterns
5. **Compliance & Governance** - Regulatory compliance, audit, governance
6. **Data & Provenance** - Data models, flow, governance, provenance
7. **Testing & Validation** - Testing strategy, QA, verification
8. **Deployment & Operations** - Deployment, monitoring, incident response
9. **Safety & Risk** - Safety requirements, risk assessment, hazard analysis
10. **Ethics & AI Accountability** - Ethical considerations, AI governance, bias

### Domain Bundle Requirements
- **Minimum domains**: 10
- **Minimum SCDs per domain**: 2
- **Import constraint**: Domain bundles MUST NOT import other bundles
- **SCD tier constraint**: Domain bundles contain only project-tier SCDs
- **Versioning**: Domain bundles MAY version independently

### Additional Domains
- Projects **MAY** add additional domains beyond the 10

## Questions for Community

### 1. Are 10 Domains Too Restrictive?
**Question**: Is requiring 10 domains overkill for small/simple projects?

**Implications**:

**Pros (require 10 domains)**:
- Ensures comprehensive coverage
- Prevents overlooking critical concerns
- Standard structure across all projects
- Forces thoughtful consideration
- Better for governance and compliance

**Cons (require 10 domains)**:
- Overhead for small projects
- Some domains may not be relevant
- Could discourage adoption
- Creates busywork for simple projects
- One-person projects may struggle

**Potential Issues**:
- What about proof-of-concepts?
- Internal tools with limited scope?
- Experimental projects?
- Student/learning projects?

### 2. Should We Have Project Tiers?
**Question**: Should we define different requirements for different project types?

**Potential Tiers**:

**Tier 1: Minimal (3-5 domains)**
- Architecture, Security, Testing
- For: POCs, experiments, internal tools
- No compliance requirements

**Tier 2: Standard (7-8 domains)**
- Add: Performance, Data, Deployment, Compliance
- For: Production services, team projects
- Basic compliance

**Tier 3: Comprehensive (10 domains)**
- All 10 domains required
- For: Critical systems, regulated industries
- Full governance and compliance

**Implications**:

**Pros (tiered approach)**:
- Flexibility for different project sizes
- Lowers barrier to entry
- More realistic for small teams
- Can evolve from tier to tier

**Cons (tiered approach)**:
- More complex specification
- Which tier should you choose?
- May encourage "gaming" the system
- Fragmentation of the standard

### 3. Are the Prescribed Domains Comprehensive?
**Question**: Do the 10 domains cover all critical concerns? Are any missing?

**Potential Missing Domains**:
- **Internationalization (i18n)** - Localization, cultural considerations
- **Legal** - Licensing, contracts, intellectual property
- **Business Continuity** - Disaster recovery, continuity planning
- **Integration** - Third-party integrations, APIs, external systems
- **Cost Management** - Cloud costs, resource optimization

**Question for Community**:
- Are any domains missing?
- Should any be split into multiple domains?
- Should any be combined?

### 4. Domain Granularity
**Question**: Are the domains at the right level of granularity?

**Too Coarse?**
- Should "Data & Provenance" be two domains?
- Should "Safety & Risk" be separate?
- Should "Deployment & Operations" split?

**Too Fine?**
- Should some domains combine?
- Is "Ethics & AI Accountability" too narrow?

**Implications**:

**Coarser domains (fewer, broader)**
**Pros**:
- Fewer bundles to manage
- Simpler structure
- Less overhead
- Easier to understand

**Cons**:
- SCDs may not fit neatly
- Less organized
- Harder to find things
- May mix unrelated concerns

**Finer domains (more, narrower)**
**Pros**:
- Better organization
- Clearer scope
- Easier to find things
- Better separation of concerns

**Cons**:
- More bundles to manage
- More overhead
- Could be overwhelming
- Harder to see big picture

### 5. Domain Relevance
**Question**: Are all domains relevant to all projects?

**Domain Relevance Analysis**:

**Universal (always relevant)**:
- Architecture ✅
- Security ✅
- Testing & Validation ✅
- Deployment & Operations ✅

**Often relevant**:
- Performance & Reliability (most production systems)
- Data & Provenance (most systems handle data)
- Compliance & Governance (depends on industry)

**Sometimes relevant**:
- Usability & Accessibility (not all systems have UIs)
- Safety & Risk (critical for some industries, less for others)
- Ethics & AI Accountability (especially relevant for AI systems)

**Should domains be**:
- **Required**: All 10 always mandatory
- **Conditional**: Some required based on project type
- **Recommended**: Guidance but not mandatory
- **Optional**: Projects choose what's relevant

### 6. Minimum SCDs per Domain
**Question**: Is requiring 2 SCDs per domain sufficient?

**Current Rule**: Minimum 2 SCDs per domain

**Implications**:

**2 SCDs minimum (current)**
**Pros**:
- Ensures more comprehensive coverage
- Prevents token compliance
- Forces deeper thinking
- Better documentation quality

**Cons**:
- May be too restrictive for simple projects
- Some domains may legitimately need only 1 SCD
- More overhead than 1 SCD minimum

**Alternative: 1 SCD minimum**
**Pros**:
- More flexible
- Allows for simple domains
- Easier to satisfy
- Focuses on domain presence

**Cons**:
- Single SCD may be too shallow
- Doesn't ensure comprehensiveness
- May encourage token compliance

**Alternative: No minimum**
**Pros**:
- Maximum flexibility
- Domain can exist without SCDs (placeholder)
- Can build gradually

**Cons**:
- Empty domains are meaningless
- No guarantee of actual content

**Alternative: 3+ SCD minimum**
**Pros**:
- Even more comprehensive coverage
- Forces very thorough documentation
- Higher quality

**Cons**:
- Too restrictive for most projects
- Creates busywork
- May discourage adoption

---

## ✅ DECISIONS MADE FOR v0.1 IMPLEMENTATION

**Date**: 2025-11-24
**Status**: Decided for initial validator implementation

### 1. Are 10 Domains Too Restrictive? - CONFIGURABLE

**Decision**: Default requires all 10 domains (strict). Projects can customize via completeness rules.

**Implementation**:
- Default `completeness-rules.yaml` requires all 10 prescribed domains
- Projects create `.scs/completeness-rules.yaml` to relax requirements
- Can skip completeness validation with `--skip-completeness` flag

**Rationale**: Provides strict production-ready defaults while allowing flexibility for POCs and experiments

---

### 2. Project Tiers - SINGLE STRICT DEFAULT

**Decision**: Ship with single strict default ruleset. No multiple profiles initially.

**Default completeness rules**:
- Requires 1 meta bundle
- Requires 1 standards bundle
- Requires 10 domain bundles (all prescribed)
- Checks for recommended SCDs per domain

**Why not multiple profiles?**
- Simpler for v0.1
- Users can easily customize their own rules
- Avoids bikeshedding about tier definitions
- Can add profiles later if community needs emerge

**Projects that need fewer domains**: Create custom `.scs/completeness-rules.yaml`

---

### 3. Prescribed Domains - KEEP CURRENT 10

**Decision**: Keep the current 10 prescribed domains unchanged.

**The 10 domains:**
1. Architecture
2. Security
3. Performance & Reliability
4. Usability & Accessibility
5. Compliance & Governance
6. Data & Provenance
7. Testing & Validation
8. Deployment & Operations
9. Safety & Risk
10. Ethics & AI Accountability

**Potential additions deferred**: i18n, Legal, Business Continuity, Integration, Cost Management
- Can be added by projects as custom domains (projects MAY add beyond 10)
- Can be added to prescribed list in future versions based on community feedback

**Rationale**: Current 10 provide comprehensive coverage for most projects. Don't expand scope for v0.1.

---

### 4. Domain Granularity - KEEP CURRENT

**Decision**: Keep current domain granularity unchanged.

**No changes to**:
- "Data & Provenance" (stays combined)
- "Safety & Risk" (stays combined)
- "Performance & Reliability" (stays combined)
- All other domains unchanged

**Rationale**: Can be refined based on community feedback. Not critical for validator implementation.

---

### 5. Domain Relevance - HANDLED BY CUSTOMIZATION

**Decision**: All 10 domains required in default rules. Projects customize for their needs.

**Implementation**:
- Universal domains (Architecture, Security, Testing, Deployment): Always in default rules
- Sometimes-relevant domains (Usability, Safety, Ethics): Also in default rules
- Projects without UIs, AI, or safety concerns: Create custom rules excluding irrelevant domains

**Rationale**: Better to start comprehensive and allow opt-out than try to auto-detect relevance

---

### 6. Minimum SCDs per Domain - 1 SCD MINIMUM

**Decision**: Domain bundles must have minimum 1 SCD (structural rule).

**Changed from**: Originally 2 SCDs minimum (see Issue 02 discussion)

**Rationale**:
- XOR architecture enables fine-grained bundles
- Structural minimum of 1 ensures bundle isn't empty
- Completeness rules define recommended SCDs per domain (guidance, not strict enforcement)

**Validator behavior**: ERROR if domain bundle has 0 SCDs

---

### Summary: Domain Rules for v0.1

**Implemented:**
1. ✅ Default requires all 10 prescribed domains
2. ✅ Single strict default ruleset (no tiers/profiles)
3. ✅ Current 10 domains unchanged
4. ✅ Current domain granularity unchanged
5. ✅ Projects customize via `.scs/completeness-rules.yaml`
6. ✅ Minimum 1 SCD per domain bundle (structural)
7. ✅ Recommended SCDs per domain (in completeness rules)

**Deferred to community feedback:**
- Additional prescribed domains (i18n, legal, etc.)
- Domain granularity changes
- Multiple default profiles/tiers

---

## How to Provide Feedback

Please comment with:
1. **Your project context**: Size, industry, compliance requirements
2. **Which domains are most valuable** for your use case
3. **Which domains feel like overhead** or aren't relevant
4. **Missing domains** you need
5. **Should we have different requirements** for different project types?

## Related Files

- `context/meta/domain-meta.yaml` - Full DOMAIN-META specification
- `spec/0.1/bundle-format.md` - Bundle format with domain details
- `examples/bundles/domains/` - Example domain bundles

## Decision Timeline

- **Feedback period**: 2-4 weeks
- **RFC creation**: After feedback synthesis
- **Implementation**: After RFC approval
