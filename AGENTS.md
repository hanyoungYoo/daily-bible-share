# AGENTS.md

This document defines the engineering rules that AI agents (e.g., Codex) must follow when contributing to this repository.

---

# 1. Branch & Merge Policy

- Never push directly to `main`.
- All changes must go through Pull Requests.
- This repository uses **Squash Merge only**.
- PR title becomes the final commit message on `main`.

PR titles must follow Conventional Commits - check .github/pull_request_template.md

---

# 3. Code Quality Rules

Before submitting changes, ensure:

- Code passes lint (ruff)
- Tests pass (pytest)
- No debug prints or temporary code
- No commented-out unused code

Do not introduce unnecessary abstractions.

Keep implementations simple and readable.

---

# 4. Security Rules (Critical)

- Never expose secrets in code.
- Never commit API keys.
- Use environment variables for:
  - OPENAI_API_KEY
  - ESV_API_KEY
- Share token generation must:
  - Use secure randomness
  - Avoid predictable patterns
- Always validate permissions for host-only actions.

---

# 5. Bible License Constraints

This project uses:

- Korean: 개역한글 (1961 edition)
- English: ESV (via API)

Agents must:

- Never modify original Bible text.
- Preserve copyright notices.
- Avoid storing restricted Bible text if API terms prohibit caching.
- Avoid embedding full copyrighted Bible text in source files.

---

# 6. External API Handling

When calling external APIs (e.g., ESV):

- Handle timeouts.
- Handle rate limits.
- Fail gracefully.
- Log structured errors.

Never assume API success.

---

# 7. Database & Migration Rules

- Any model change must include migration.
- Avoid destructive schema changes without justification.
- Ensure backward compatibility when possible.

---

# 8. Testing Requirements

New logic must include tests when:

- Business logic is introduced.
- Permission rules change.
- Token logic changes.
- API parsing logic changes.

Avoid testing trivial getters/setters.

---

# 9. Pull Request Expectations

PR must include:

- Clear summary
- Testing instructions
- If relevant:
  - Security impact
  - Migration impact
  - License impact

Keep PRs small and focused.

If PR has a potential to leak any personal information(i.e., credentials), never push it.

---

# 10. Design Philosophy

Prefer:

- Explicit over implicit
- Simple over clever
- Clear domain boundaries
- Deterministic behavior

Avoid:

- Over-engineering
- Premature optimization
- Global state

---

# 11. When in Doubt

If a change affects:

- Authentication
- Token generation
- Bible content handling
- External API usage

Add extra explanation in the PR.

Security and license compliance are higher priority than convenience.


---

# 12. Documentation

Also think of documentation. Ask if the change is documented somewhere. If the documentation is needed, add a documentation for the change. Especially, check README file. The file is for comprehensive guide for users. If the change affects user behavior, update the document
