# Branching Convention for SCS Repository

Branches must be:

- Short-lived  
- Tied to a specific Issue  
- Descriptively named  
- Deleted after merge  

This keeps the git history clean and avoids long-lived diverging branches.

---

# 1. Naming Pattern

issue--short-description

### Examples

issue-12-meta-spec-overview
issue-08-update-readme
issue-19-standards-tier-template
issue-24-fix-typo

---

# 2. Rules

### ✔ One branch per Issue  
Avoid combining unrelated tasks.

### ✔ Branch from `main`  
Before creating a branch:

git checkout main
git pull

### ✔ Keep changes small  
Each branch should represent one logical unit of work.

### ✔ Delete branch after merge  
GitHub will offer to delete it automatically after PR merge.

---

# 3. Why Use This Model?

- Clean history  
- Easy reviews  
- No merge conflicts  
- Predictable naming  
- Perfect for both human and AI workflow  
- Enables clear mapping between Issue → Branch → PR  

---

Follow this convention for all contributions.