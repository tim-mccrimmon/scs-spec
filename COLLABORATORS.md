# Collaborator Guide

**For Repository Owner: Managing Collaborators on GitHub Free Tier**

---

## Adding Collaborators

### Step 1: Invite Collaborators

1. Go to your repository on GitHub
2. Click **Settings** → **Collaborators**
3. Click **Add people**
4. Enter their GitHub username or email
5. Choose access level:
   - **Read**: Can view and clone
   - **Write**: Can push to branches, open PRs
   - **Admin**: Can modify settings (be careful!)

**Recommendation**: Start with **Write** access for contributors

---

## Setting Up Branch Protection (Free Tier)

GitHub Free has **limited** branch protection, but you can still protect `main`:

### Step 1: Protect Main Branch

1. Go to **Settings** → **Branches**
2. Click **Add branch protection rule**
3. Branch name pattern: `main`
4. Enable these (free tier options):
   - ✅ **Require pull request before merging**
   - ✅ **Require conversation resolution before merging**
   - ❌ ~~Require approvals~~ (Pro/Team only)
   - ❌ ~~Require status checks~~ (Limited on free)

**This prevents direct pushes to main** - all changes must go through PRs.

---

## Workflow for Collaborators

### Collaborator Workflow

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/scs-spec.git
   ```

2. **Create issue for their work**
   - Go to Issues → New Issue
   - Choose appropriate template
   - Describe what they're working on

3. **Create branch** (following BRANCHING_CONVENTION.md)
   ```bash
   git checkout -b issue-123-add-example
   ```

4. **Make changes**
   - Follow CONTRIBUTING.md
   - Follow style guidelines
   - Test their work

5. **Commit changes**
   ```bash
   git add .
   git commit -m "Add healthcare example bundle

   - Created example bundle for HIPAA-compliant API
   - Includes meta, standards, and project tiers
   - Validates against schemas

   Closes #123"
   ```

6. **Push to their branch**
   ```bash
   git push -u origin issue-123-add-example
   ```

7. **Open Pull Request**
   - GitHub will prompt to create PR
   - Fill out PR template
   - Request review (you'll be auto-assigned via CODEOWNERS)

8. **Address feedback**
   - Make requested changes
   - Push updates to same branch
   - Respond to comments

9. **Merge** (you do this after approval)

---

## Managing Contributions

### Your Review Process

1. **Automated checks** (when you set up CI):
   - YAML validation
   - Schema validation
   - Relationship checks

2. **Your manual review**:
   - Does it follow CONTRIBUTING.md?
   - Is the quality good?
   - Does it align with spec vision?
   - Is provenance filled out?

3. **Request changes** or **Approve**

4. **Merge** when ready

### Merge Strategies

**Recommended for free tier**:
- **Squash and merge** - Keeps history clean
- Merge commit message should be clear

---

## Setting Expectations with Collaborators

### What You Should Tell New Collaborators

**Welcome message template**:

```markdown
Welcome to the SCS project! 🎉

Before you start contributing:

1. **Read these docs** (in order):
   - CONTRIBUTING.md - How to contribute
   - GOVERNANCE.md - How the project is governed
   - CODE_OF_CONDUCT.md - Community standards

2. **For your first contribution**:
   - Start with something small (typo fix, example, documentation)
   - Open an issue first to discuss
   - Follow the PR template carefully

3. **For major changes**:
   - Open a GitHub Discussion first
   - If it's a spec change, you'll need an RFC (see rfcs/README.md)
   - Get feedback before writing code

4. **Communication**:
   - GitHub Issues for bugs/features
   - GitHub Discussions for questions/ideas
   - Tag @timmccrimmon if you need maintainer input

5. **Be patient**:
   - I review PRs within 1 week typically
   - Follow-up if you haven't heard in a week
   - Remember this is an open source project (volunteer time)

Looking forward to your contributions!
```

---

## Roles and Responsibilities

### You (Maintainer)

**Your responsibilities**:
- Review and merge PRs
- Make final decisions on spec changes
- Maintain CODEOWNERS
- Ensure quality standards
- Respond to issues
- Update governance docs
- Manage releases

**Your authority** (per GOVERNANCE.md):
- Final say on all changes
- Can reject PRs with explanation
- Can remove collaborators if needed
- Control over main branch

---

### Collaborators (Contributors)

**Their responsibilities**:
- Follow CONTRIBUTING.md guidelines
- Test their changes
- Write clear commit messages
- Fill out PR templates completely
- Respond to review feedback
- Be respectful (CODE_OF_CONDUCT.md)

**Their limitations** (free tier):
- Can't merge to main (you do this)
- Can't modify settings
- Can't force-push to protected branches

---

## Common Scenarios

### Scenario 1: Someone Submits a PR Without Opening an Issue

**Response**:
```markdown
Thanks for the contribution! For future PRs, please open an issue first
to discuss the change. This helps us align on the approach before you
spend time coding.

For this PR: [review normally or ask them to open issue for discussion]
```

### Scenario 2: Someone Pushes Directly to Main (Before Protection)

**Fix**:
1. Set up branch protection immediately
2. Politely ask them to use PRs going forward
3. If their commit is good, keep it
4. If not, revert and ask for PR

### Scenario 3: Someone Wants to Make a Major Spec Change

**Response**:
```markdown
This looks like a major change to the specification. Per GOVERNANCE.md,
major changes require an RFC.

Please:
1. Open a GitHub Discussion to gauge interest
2. If there's support, write an RFC using rfcs/0000-template.md
3. Submit the RFC as a PR to rfcs/
4. After RFC is accepted, you can implement the change

See rfcs/README.md for the full process.
```

### Scenario 4: Collaborator Abandons PR

**What to do**:
1. Wait 2 weeks
2. Comment: "Are you still working on this?"
3. Wait 1 more week
4. If no response, close PR with kind message:
   ```markdown
   Closing due to inactivity. Feel free to reopen when you're
   ready to continue, or someone else can pick this up.
   ```

### Scenario 5: Someone Violates Code of Conduct

**What to do** (per CODE_OF_CONDUCT.md):
1. Document the violation
2. Email them privately (tim@ohanaconsulting.ai)
3. Warn them (first time)
4. Temporary ban (repeated)
5. Permanent ban (serious/repeated violations)

Always be professional and document everything.

---

## Tools to Help Manage Contributions

### GitHub Features (Free Tier)

**Issues**:
- Use labels (bug, enhancement, question, good-first-issue)
- Use milestones for releases
- Use projects (basic Kanban boards)

**Pull Requests**:
- Review conversations
- Suggest specific changes (GitHub suggests feature)
- Request changes vs Approve

**Discussions**:
- Enable Discussions (Settings → Features)
- Categories: Ideas, Q&A, Show and Tell

**Labels**:
- Create labels for different areas:
  - `spec`: Specification changes
  - `docs`: Documentation
  - `examples`: Example bundles
  - `tools`: Validator/tooling
  - `good-first-issue`: For new contributors
  - `help-wanted`: Open for anyone
  - `needs-rfc`: Requires RFC process

---

## Scaling Over Time

### When You're Ready to Expand

**Add more collaborators**:
- Trusted contributors can become "Core Contributors"
- Update GOVERNANCE.md with their role
- Update CODEOWNERS to include them

**Upgrade to GitHub Team** (if needed):
- Required approvals on PRs
- Better branch protection
- Code review assignments
- **Cost**: $4/user/month

**Form Steering Committee** (per GOVERNANCE.md):
- When project reaches 1.0
- 3-5 trusted community members
- Decisions by consensus

---

## Checklist: Before Inviting First Collaborators

- [ ] Branch protection enabled on `main`
- [ ] CODEOWNERS file exists
- [ ] Issue templates exist
- [ ] PR template exists
- [ ] CONTRIBUTING.md is clear
- [ ] GOVERNANCE.md is complete
- [ ] CODE_OF_CONDUCT.md is in place
- [ ] You've read this guide
- [ ] You're ready to review PRs regularly

---

## Questions?

If you need help managing collaborators:
- Check GitHub Docs: https://docs.github.com/en/repositories
- Ask in a relevant community (r/opensource, etc.)
- Refer to GOVERNANCE.md for project-specific rules

**Remember**: You're the maintainer. You set the standards. It's okay to:
- Say no to contributions that don't fit
- Ask for changes before merging
- Take time to review thoroughly
- Protect the quality and vision of SCS

Your contributors will respect clear, consistent leadership.
