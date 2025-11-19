# Pull Request Checklist

Use this checklist before submitting or merging a Pull Request.

---

# ✔ Before Opening the PR

### 1. Linked Issue
- [ ] Does the PR reference the Issue it resolves?
  Example:  

  Closes #12

### 2. Correct Branch
- [ ] Is the work done on a properly named branch (see Branching Convention)?

### 3. Scope
- [ ] Does the PR contain only one unit of work?
- [ ] Are unrelated changes avoided?

### 4. Files Updated
- [ ] Are all relevant documents updated?
- [ ] Are no unnecessary files modified?

---

# ✔ During Review

### 5. Description
- [ ] Is the PR description clear and complete?

### 6. Changes Explained
- [ ] Does the PR explain *why* changes were made?

### 7. Feedback Incorporated
- [ ] Have all review comments been handled?

---

# ✔ Before Merging

### 8. Tests/Validation (if applicable)
- [ ] Does the content render correctly?  
- [ ] No broken links, syntax errors, or YAML errors?

### 9. status-context.yaml (if needed)
- [ ] Does project state need updating?
- [ ] If so, update `status-context.yaml` in the PR.

### 10. Final Check
- [ ] Everything works?  
- [ ] No leftover debugging text or commented-out drafts?  

---

# ✔ After Merge

- [ ] Branch deleted  
- [ ] Issue closed (auto closes if referenced)  
- [ ] Local repo updated (`git pull`)  

---

This checklist ensures clean, traceable contributions to the SCS project.

