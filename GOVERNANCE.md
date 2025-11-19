# SCS Governance

**Version**: 0.1
**Last Updated**: 2025-11-19
**Status**: Active

---

## Overview

This document defines how the Structured Context Specification (SCS) is governed, how decisions are made, and how the community can contribute.

The governance model is designed to be:
- **Transparent**: All decisions and discussions are public
- **Inclusive**: Community input is welcomed and valued
- **Efficient**: Clear processes prevent bureaucracy
- **Evolutionary**: Governance will mature as the project grows

---

## Current Phase: Benevolent Maintainer (v0.x)

While SCS is in early development (version 0.x), governance follows a **Benevolent Maintainer** model:

- **Tim McCrimmon** (`tim@ohanaconsulting.ai`) serves as primary maintainer with final decision authority
- Community input is welcomed and encouraged via GitHub Issues and Discussions
- The maintainer makes final decisions on all changes to the specification
- This lightweight approach allows rapid iteration while establishing the specification's foundation

**This governance model will evolve as the project matures.** See [Future Governance](#future-governance) below.

---

## Roles & Responsibilities

### Maintainer

**Current Maintainer**: Tim McCrimmon

**Responsibilities**:
- Review and merge pull requests
- Make final decisions on specification changes
- Ensure quality and consistency of the spec
- Manage releases and versioning
- Steward the project's vision and direction
- Respond to issues and discussions in a timely manner
- Update governance as project evolves

**Authority**:
- Final say on all changes to the specification
- Can accept, reject, or request changes to proposals
- Can designate trusted contributors as reviewers

### Contributors

**Anyone can be a contributor** by:
- Opening issues to report problems or suggest improvements
- Participating in discussions
- Submitting pull requests
- Creating examples, tutorials, or tools
- Helping other community members

**Recognition**: Significant contributors will be acknowledged in CONTRIBUTORS.md and release notes.

### Community

**Everyone is part of the SCS community**, including:
- Users implementing SCS
- Tool developers
- Standards bodies
- Organizations adopting CEDM
- Anyone interested in Context Engineering

---

## Contribution Process

### Minor Changes

**Definition**: Typos, clarifications, formatting, small examples, documentation improvements

**Process**:
1. **Fork the repository** and create a branch
2. **Make your changes** following the [contribution guidelines](CONTRIBUTING.md)
3. **Submit a pull request** with clear description
4. **Maintainer reviews** (typically within 1 week)
5. **Merge if approved**, or request changes

**Timeline**: Most minor changes are reviewed within 1 week and merged within 2 weeks.

---

### Major Changes

**Definition**: New concepts, breaking changes, significant additions, architectural shifts

**Examples**:
- Adding a new SCD tier
- Changing core schema structure
- Adding new required fields
- Modifying relationship semantics
- Substantial additions to the specification

**Process**:
1. **Open a GitHub Discussion** in the "Ideas" category
   - Describe the proposal
   - Explain the motivation (what problem does this solve?)
   - Outline potential approaches
   - Invite community feedback

2. **Community feedback period** (minimum 2 weeks)
   - Community discusses pros/cons
   - Maintainer provides initial feedback
   - Proposal may be refined based on discussion

3. **Write an RFC** (if proposal is viable)
   - Use the [RFC template](rfcs/0000-template.md)
   - Provide detailed specification
   - Address alternatives and drawbacks
   - Include examples

4. **Submit RFC as pull request** to `rfcs/` folder
   - Name: `rfcs/NNNN-short-title.md` (maintainer assigns number)
   - Additional discussion on the PR
   - Refinements based on feedback

5. **Maintainer decision** (within 4 weeks of RFC PR)
   - **Accept**: RFC is merged, implementation can proceed
   - **Reject**: RFC is closed with explanation
   - **Defer**: Good idea but not ready; revisit later
   - **Request Changes**: Needs modification before acceptance

6. **Implementation** (if accepted)
   - RFC is merged to `rfcs/` folder
   - Specification can be updated in subsequent PR
   - Changes are documented in CHANGELOG
   - Included in next versioned release

**Timeline**: Major changes typically take 6-12 weeks from initial discussion to merged specification update.

---

## RFC Process

### What is an RFC?

**RFC** stands for "Request for Comments" - a detailed proposal for significant changes to SCS.

RFCs provide:
- A structured way to propose major changes
- Opportunity for thorough community review
- Documentation of design decisions and tradeoffs
- Historical record of why things are the way they are

**Inspired by**: The Rust RFC process, adapted for specification governance.

### RFC Template

All RFCs must follow the [RFC template](rfcs/0000-template.md).

**Required sections**:
- **Summary**: One-paragraph explanation
- **Motivation**: Why is this needed?
- **Guide-level explanation**: How will users understand this?
- **Reference-level explanation**: Technical details
- **Drawbacks**: Why should we NOT do this?
- **Alternatives**: What other approaches were considered?
- **Unresolved questions**: What needs further discussion?

### RFC Lifecycle

```
Proposed → Under Review → Accepted/Rejected/Deferred
             (2+ weeks)
                ↓
             Accepted
                ↓
          Implemented → Merged into Spec
```

### RFC Numbering

- RFCs are numbered sequentially: 0001, 0002, 0003, etc.
- The maintainer assigns the number when the RFC PR is opened
- The number remains even if the RFC is rejected (preserves history)

### Active RFCs

See [rfcs/README.md](rfcs/README.md) for a list of active, accepted, and rejected RFCs.

---

## Version Policy

SCS follows **semantic versioning** adapted for specifications:

### Version Format: `MAJOR.MINOR.PATCH`

**MAJOR** (e.g., 1.0.0 → 2.0.0):
- Breaking changes to the specification
- Changes that require updating existing SCDs
- Removal of required fields or tier types
- Significant restructuring

**MINOR** (e.g., 1.0.0 → 1.1.0):
- New features that are backwards compatible
- New optional fields or relationship types
- New tier types (if backwards compatible)
- Clarifications and refinements

**PATCH** (e.g., 1.0.0 → 1.0.1):
- Typo fixes
- Documentation improvements
- Clarifications with no semantic changes
- Examples and non-normative content

### Version 0.x (Pre-1.0)

**While SCS is version 0.x**:
- The spec is considered **draft** and **unstable**
- Breaking changes are allowed in MINOR versions (0.1 → 0.2)
- This allows rapid iteration to get the fundamentals right
- Early adopters should expect changes

**Version 1.0** will be released when:
- The core model is proven in real-world use
- Multiple implementations exist
- The community agrees the spec is stable
- Breaking changes will be rare and carefully managed

### Release Process

1. **Changes accumulate** in the main branch
2. **CHANGELOG is updated** with all changes
3. **Version number is bumped** according to semver
4. **Git tag is created** (`v0.2.0`, `v1.0.0`, etc.)
5. **GitHub Release** is published with release notes
6. **Announcement** is posted to discussions and social media

**Release frequency**:
- 0.x: Every 2-3 months or as major features are ready
- 1.x+: Every 6-12 months for minor, as needed for patch

---

## Decision Making

### Decision Authority

**During 0.x (Benevolent Maintainer phase)**:
- The maintainer (Tim McCrimmon) makes final decisions
- Community input heavily influences decisions
- Rationale is always provided for rejections

**Future (1.0+)**:
- Steering committee will use consensus decision-making
- Maintainer retains tie-breaking authority
- See [Future Governance](#future-governance)

### Decision Criteria

Decisions are based on:
1. **Alignment with SCS vision**: Does it support the core goals?
2. **Real-world need**: Is there demonstrated demand?
3. **Backwards compatibility**: Does it break existing implementations?
4. **Complexity**: Is the benefit worth the added complexity?
5. **Community consensus**: What does the community think?
6. **Maintainability**: Can it be sustained long-term?

### Disagreement Resolution

If you disagree with a decision:
1. **Respectfully state your case** in the relevant discussion/PR
2. **Provide evidence** (use cases, examples, data)
3. **Propose alternatives** with rationale
4. **Accept the final decision** gracefully

The maintainer will:
- Consider all perspectives
- Provide clear rationale for decisions
- Be open to reversing decisions if new information emerges

---

## Intellectual Property

### Copyright

All contributions to SCS are:
- Copyright © 2025 Timothy McCrimmon and Contributors
- Licensed under Apache License 2.0

### Contributor License

By contributing to SCS, you agree that:
- Your contributions are your original work
- You have the right to submit the contribution
- Your contributions are licensed under Apache 2.0
- You grant rights to use, modify, and distribute your contributions

### Trademarks

**"SCS" (Structured Context Specification)** and **"CEDM" (Context Engineering Development Method)** are trademarks of Ohana Consulting LLC.

**Use of trademarks**:
- ✅ You MAY use "SCS" to describe implementations that comply with the specification
- ✅ You MAY say your tool "supports SCS" or "validates SCS bundles"
- ❌ You MAY NOT use "SCS" in a way that implies official endorsement
- ❌ You MAY NOT create competing specifications called "SCS"

**Reasonable use** is always permitted for descriptive purposes.

---

## Community Standards

All community members must follow the [Code of Conduct](CODE_OF_CONDUCT.md).

**Summary**:
- Be respectful and inclusive
- Welcome newcomers
- Focus on what's best for the community
- Show empathy and kindness
- Accept constructive criticism gracefully

**Violations** should be reported to tim@ohanaconsulting.ai and will be addressed promptly.

---

## Communication Channels

### GitHub

**Primary venue** for all project activity:
- **Issues**: Bug reports, feature requests, questions
- **Discussions**: Ideas, proposals, general discussion
- **Pull Requests**: Code and spec contributions

### Email

For private matters: tim@ohanaconsulting.ai

### Social Media

Announcements and community engagement:
- Twitter/X: (TBD)
- LinkedIn: (TBD)

### Mailing List

(Future) A low-volume mailing list for major announcements will be established.

---

## Future Governance

As SCS matures and the community grows, governance will evolve:

### Version 1.0 Transition

**When SCS reaches 1.0**, governance will transition to:

**Steering Committee** (3-5 members):
- Tim McCrimmon (chair, tie-breaking vote)
- 2-4 community members with significant contributions
- Terms: 2 years, staggered
- Decisions by consensus, chair breaks ties

**Core Contributors**:
- Recognized contributors with commit access
- Can approve minor changes
- Major changes still require RFC process

**Working Groups** (as needed):
- Focus on specific areas (tooling, compliance, education)
- Make recommendations to steering committee

### Foundation Consideration

**After 2+ years of stable operation**, consider:
- Joining an existing foundation (e.g., Linux Foundation)
- Creating a standalone SCS Foundation
- Remaining independent with formal governance

**Criteria for foundation**:
- Multiple major organizational adopters
- Funding available for operations
- Need for legal entity (contracts, trademarks, events)

---

## Governance Evolution

**This governance document is a living document.**

Changes to governance follow the same RFC process as specification changes.

**History**:
- 2025-11-19: Initial governance model (Benevolent Maintainer)
- (Future updates will be recorded here)

---

## Questions?

If you have questions about governance:
- Open a GitHub Discussion in the "Meta" category
- Email the maintainer: tim@ohanaconsulting.ai
- Review past governance discussions and RFCs

**Thank you for contributing to SCS!**

Building the infrastructure for trustworthy AI-native development is a community effort. We're grateful for your participation.
