# Framework 5: Context-Aware Selection

**Core Principle**: Visible task description may not contain all context needed to do work well. Sometimes gathering context IS the first task.

## The "What Don't I Know?" Check

Before assigning implementation agent, mentally check:

**Questions to Ask**:
- How many related files might this change touch?
- Are there existing patterns in codebase I should follow?
- What dependencies exist that could be affected?
- Is this potentially duplicating functionality that already exists?
- Do I understand full scope of this change?

**If Answers Are "I Don't Know"**: Consider starting with **researcher-codebase** to gather context, then delegate to implementation agent with enriched understanding.

---

## The Single-File Assumption Trap

**Anti-Pattern**: Task mentions one file → assume it's simple one-file change → assign implementation agent directly

**Reality Check**:
- Changing `packages/auth/login.py` might affect:
  - 10 other files that import it
  - Test files that verify its behavior
  - Config files that reference it
  - Other modules that depend on its interface

**The Hidden Complexity**: What looks like one-file task might have "context radius" of many related files.

**Decision Framework**:

- **1 file, truly isolated** (utility function, new module):
  - Direct to implementation agent

- **1 file + context of 5-10 related files**:
  - researcher-codebase first (understand dependencies)
  - Then implementation agent with context

- **2-4 files mentioned in task**:
  - researcher-codebase for synthesis (understand relationships)
  - Then implementation agent

- **5+ files mentioned**:
  - researcher-codebase for pattern discovery (find common themes)
  - Possibly multiple implementation agents in parallel

**Why This Matters**: Implementation without context often leads to:
- Breaking existing functionality
- Inconsistent patterns with rest of codebase
- Duplicating utilities that already exist
- Missing edge cases that existing code handles

---

## The Security Context Trigger

**Automatic Research Requirement**: Certain domains require research before implementation, regardless of file count or apparent simplicity.

**High-Risk Domains**:
- Authentication/Authorization
- Payment processing
- External API integration
- Data privacy/PII handling
- Cryptography
- Input validation/sanitization

**Required Pattern**: researcher-web (OWASP/security best practices) → implementation agent → code-reviewer (security lens)

**Why Automatic**: Security mistakes are expensive. Even experienced developers miss security issues. Research establishes right patterns before writing vulnerable code.

**Example**: "Implement password reset in `packages/auth/reset.py`"
1. **researcher-web** - Research OWASP authentication patterns, password reset best practices
2. **code-implementer** - Implement with security patterns
3. **code-reviewer** - Security-focused review

Even if reset.py is single new file, security context requires research-then-implement.

---

## Context Quality Assessment

**High Context Quality** (can proceed directly):
- Task includes detailed requirements
- Patterns are explicitly specified
- Dependencies are listed
- Examples are provided
- Clear acceptance criteria

**Low Context Quality** (gather context first):
- Task is vague ("improve auth")
- No patterns specified
- Unknown dependencies
- No examples
- Ambiguous success criteria

**Recognition Pattern**: If you're uncertain about approach or scope, context gathering is the first task.
