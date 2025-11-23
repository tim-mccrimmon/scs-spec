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
- **Minimum SCDs per domain**: 1
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
**Question**: Is requiring 1 SCD per domain sufficient?

**Current Rule**: Minimum 1 SCD per domain

**Implications**:

**1 SCD minimum**
**Pros**:
- Not overly restrictive
- Allows for simple domains
- Easy to satisfy
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

**Alternative: 2-3 SCD minimum**
**Pros**:
- Ensures more comprehensive coverage
- Forces deeper thinking
- Better documentation

**Cons**:
- May be too restrictive
- Creates busywork
- Some domains may legitimately need only 1 SCD

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
