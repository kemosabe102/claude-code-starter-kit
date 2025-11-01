# Agent Selection Scenarios

Detailed examples of applying the seven frameworks to real tasks.

## Example 1: "Fix the failing login tests"

**Apply Frameworks**:
1. **Domain**: `tests/**` (testing domain)
2. **Work Type**: "Fix" + "failing" → Investigation or implementation?
   - Is cause known? Not stated.
   - Assume unknown → Investigation work
3. **Agent Expertise**: debugger (investigation specialist)
4. **Multi-Agent?**: Not needed initially (can add if debugging reveals implementation issues)
5. **Context**: Test failure output will provide context
6. **Decision**: debugger

**Alternative Scenario**: "Fix the failing login tests (missing null check in LoginService)"
- Cause is known ("missing null check")
- Work type: Implementation (apply known fix)
- **Decision**: code-implementer

---

## Example 2: "Create payment processing feature"

**Apply Frameworks**:
1. **Domain**: `packages/**` (main codebase)
2. **Work Type**: Creation (new feature)
3. **Agent Expertise**: code-implementer... but wait
4. **Multi-Agent?**: Check criticality
   - Payment processing → HIGH CRITICALITY
   - Security-sensitive domain
   - **Multi-agent required**
5. **Context**: Need security research
6. **Pattern**: Sequential pipeline
   - researcher-web (OWASP payment patterns)
   - researcher-library (payment SDK best practices)
   - code-implementer (secure implementation)
   - test-creator (comprehensive test design)
   - test-executor (test validation)
   - code-reviewer (security-focused review)
7. **Decision**: Multi-agent sequential pipeline

---

## Example 3: "Update CLAUDE.md with new agent list"

**Apply Frameworks**:
1. **Domain**: `CLAUDE.md` (Claude Code configuration)
2. **Domain Specialist**: claude-code
3. **Work Type**: Update (modification)
4. **Disambiguation**: Could others edit Markdown? Yes, technically
   - **But domain ownership principle**: claude-code owns CLAUDE.md
5. **Decision**: claude-code (domain ownership)

---

## Example 4: "Analyze patterns in authentication code"

**Apply Frameworks**:
1. **Domain**: `packages/**` likely (main codebase)
2. **Work Type**: Investigation (analysis, pattern discovery)
3. **Multi-file?**: Probably (authentication code spans files)
4. **Agent Expertise**: researcher-codebase (pattern discovery specialist)
5. **Context**: This IS context gathering
6. **Decision**: researcher-codebase

**Why not code-implementer?**: Work type is investigation, not creation.
**Why not debugger?**: Not fixing failures, discovering patterns.

---

## Example 5: "Create intent-analyzer agent in `.claude/agents/intent-analyzer.md`"

**Framework Analysis**:
- Keywords: "create" (suggests code-implementer)
- Domain signal: `.claude/agents/**` path
- Domain owner: agent-architect
- **Decision**: agent-architect (domain ownership trumps keyword)

**Why domain matters**: agent-architect has expertise in:
- Prompt engineering patterns
- Agent simulation and evaluation
- 9-criteria quality matrix
- Workflow integration patterns

code-implementer lacks this specialized agent design knowledge.

---

## Example 6: "Implement user authentication with tests and documentation"

**Wrong Approach**: Assign code-implementer for everything

**Right Approach**: Decompose by domain
- T001 [test-creator] Create test suite in `tests/auth/`
- T002 [code-implementer] Implement authentication in `packages/auth/`
- T003 [test-executor] Validate tests pass
- T004 [code-reviewer] Security-focused review
- T005 [spec-enhancer] Document authentication flow in `docs/auth-spec.md`

**Why**: Each domain specialist produces higher quality in their area than generalist approach.

---

## Example 7: "Improve code quality in payment.py"

**Ambiguous Task Analysis**:
- What does "improve" mean?
  - Add comments?
  - Restructure?
  - Fix bugs?
  - Optimize performance?
  - All of above?

**Least Assumptions Principle**:
- code-reviewer: Provides feedback, doesn't change code (least invasive)
- code-implementer: Assumes you want new code added
- debugger: Assumes bugs to fix

**Decision**: code-reviewer first (clarify what improvements needed)

**Sequential Pattern**: code-reviewer (identify issues) → code-implementer (implement fixes based on feedback)

---

## Example 8: "Add caching to API endpoints"

**Context-Aware Analysis**:
- Unfamiliar with existing caching patterns?
- Risk of duplicating functionality?

**Research-Then-Act Pattern**:
1. **researcher-codebase** - Discover existing caching patterns
2. **code-implementer** - Implement using discovered patterns

**Why research first**: Without context, might implement caching differently from existing patterns, creating inconsistency.

---

## Example 9: "Update User model in `packages/models/user.py`"

**Single-File Assumption Trap**:
- Looks simple: one file
- Reality check:
  - How many files import User model?
  - What's impact radius?

**Better Approach**:
1. **researcher-codebase** - Analyze User model dependencies
2. **code-implementer** - Update with full understanding of impact

**Why**: Model changes affect all importers. Context prevents breaking changes.

---

## Example 10: "Fix bug in auth.py where login fails with 500 error"

**Closest Expertise Analysis**:
- Is root cause known? No, "500 error" doesn't specify why
- Work type: Investigation (need to discover cause)
- **Decision**: debugger (investigation specialist)

**Alternative**: "Fix bug in auth.py where missing null check causes 500 error"
- Root cause known: "missing null check"
- Work type: Implementation (apply known fix)
- **Decision**: code-implementer

**Key Insight**: Same file, same symptom (500 error), different agent based on whether root cause is known.

---

## Example 11: "Analyze authentication code for security vulnerabilities"

**Read-Only Mode Analysis**:
- Domain: `packages/**` (auth code)
- Work type: Analysis (security assessment)
- Mode: Read-only (no fixes, just report)
- **Decision**: code-reviewer (security analysis expertise) OR debugger (pattern analysis)

**Why not code-implementer**: Work type is analysis, not implementation.

**Domain specialist in read-only mode** more appropriate than generic researcher-codebase for security-specific analysis.

---

## Example 12: "Create tests for new feature"

**Work Type Distinction**:
- "Create tests" = Writing test code
- "Run tests" = Executing test suite
- "Fix failing tests (unknown)" = Debugging
- "Fix failing tests (known)" = Implementation

**Decision**: test-creator (test generation specialist)

**Why not**:
- test-executor: Runs tests, doesn't create them
- debugger: Investigates failures, doesn't create tests
- code-implementer: Creates features, not test suites

---

## Example 13: "Review implementation plan quality"

**Parallel Validation Pattern**:
- Same artifact (plan)
- Multiple perspectives needed
- No dependencies between reviews

**Multi-Agent Approach**:
- **technical-pm** (parallel) - Business alignment, ROI, strategic fit
- **architecture-review** (parallel) - Technical feasibility, NFRs, production readiness
- **tech-debt-investigator** (parallel) - Duplicate detection, cleanup needs

**Orchestrator synthesizes**: Combines perspectives into comprehensive assessment.

---

## Example 14: "Update schema validation in `.claude/docs/schemas/agent-schema.json`"

**Disambiguation Principles**:
1. **Domain Ownership**: `.claude/docs/schemas/**` - Could be agent-architect or claude-code
2. **Closest Expertise**: "agent-schema.json" → agent schemas specifically
   - agent-architect has deepest expertise in agent-related artifacts
3. **Decision**: agent-architect

**Why not claude-code**: While claude-code owns `.claude/**` generally, agent-architect has specialized agent schema knowledge.

---

## Example 15: "Implement password reset in `packages/auth/reset.py`"

**Security Context Trigger**:
- Domain: Authentication (high-risk)
- File count: One file
- **Automatic research requirement**: Security-sensitive domain

**Required Pattern**:
1. **researcher-web** - OWASP authentication patterns, password reset best practices
2. **code-implementer** - Implement with security patterns
3. **code-reviewer** - Security-focused review

**Why**: Even single-file auth work requires research-then-implement-then-review. Security mistakes are expensive.
