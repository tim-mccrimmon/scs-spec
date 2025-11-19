# Contributing to the SCS Repository

Thank you for contributing to the Structured Context Specification (SCS).  
This repository uses a lightweight, GitHub-native workflow designed for clarity and collaboration.

Before contributing, please review the core rules below.

---

# 1. Use Issues for All Discussions

Before making changes:
- Search for an existing Issue  
- If none exists, create a new Issue  
- Use Issues for questions, proposals, and design debates  

All collaboration happens in Issues.

---

# 2. Create a Task Branch Linked to an Issue

Never commit directly to `main`.

Instead:

1. Find or create an Issue  
2. Create a branch from `main`:

git checkout main
git pull
git checkout -b issue--short-description

Examples:
- `issue-15-standards-scd-template`
- `issue-08-update-readme`

Branches are temporary and deleted after merging.

---

# 3. Make Your Change

Add or update files as needed to complete the task in the Issue.

---

# 4. Submit a Pull Request (PR)

Go to GitHub → **Pull Requests → New Pull Request**.

Your PR must:

- Reference the Issue (e.g., `Closes #15`)  
- Include a clear description  
- Contain work limited to one Issue  

---

# 5. Participate in Review

Respond to comments.  
Make additional commits on the same branch until approval.

---

# 6. Merge and Delete Branch

Once approved, the PR is merged into `main`.

After merge:
- The branch is deleted  
- The Issue closes (if referenced)

---

# 7. Update `status-context.yaml` (If Needed)

If your work affects project state, update the AI alignment file.

---

# 8. Stay in Sync

Always pull latest changes before starting new work:

git checkout main
git pull

---

Thank you for contributing!