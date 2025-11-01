# Framework 4: Multi-Agent Decision Framework

**Core Principle**: Some tasks are too complex or too critical for a single agent. Recognize when multiple perspectives or sequential expertise is needed.

## Complexity Signals

**Single-Agent Indicators**:
- Task scope is clear and contained within one domain
- One type of expertise suffices
- Straightforward file paths indicating single domain
- Low risk if something is missed (not security-critical, not high-impact)

**Multi-Agent Indicators**:
- Task spans multiple domains (e.g., "implement + test + document")
- High criticality (security, payments, authentication, data privacy)
- Multiple perspectives valuable (business validation + technical validation)
- Need for validation checkpoints (implement → review → verify)
- Unfamiliar domain requiring research before action

**Recognition Pattern**: When you see "and" connecting different work types ("implement AND test AND document"), think about whether each needs its own specialist.

---

## The Sequential Pipeline Pattern

**When to Use**: Tasks where later steps depend on earlier steps, and each step requires different expertise.

**Structure**: Step 1 (Agent A) → Step 2 (Agent B) → Step 3 (Agent C)

**Example**: Creating a secure payment feature
1. **researcher-web** - Research OWASP payment security patterns (context gathering)
2. **researcher-library** - Research Stripe SDK best practices (library-specific patterns)
3. **code-implementer** - Implement with researched patterns (creation)
4. **test-creator** - Create comprehensive test suite (generation)
5. **test-executor** - Validate test execution (validation)
6. **code-reviewer** - Security-focused code review (quality gate)

**Why Sequential**: Each step builds on the previous. Can't implement securely without research. Can't test before implementation. Can't review before code exists.

**Recognition Pattern**: Dependencies between steps. Output of step N is input to step N+1.

---

## The Parallel Validation Pattern

**When to Use**: Need multiple independent perspectives on same artifact. All perspectives are equally valuable and can be gathered simultaneously.

**Structure**: All agents review in parallel → Orchestrator synthesizes

**Example**: Reviewing an implementation plan
- **technical-pm** - Business alignment, ROI, strategic fit, requirements coverage
- **architecture-review** - Technical feasibility, NFRs, technology choices, production readiness
- **tech-debt-investigator** - Duplicate detection, cleanup needs, debt implications

**Why Parallel**: Each brings different lens to same plan. Reviews are independent—technical-pm doesn't need to wait for architecture-review.

**Recognition Pattern**: Same input artifact, different evaluation criteria, no dependencies between reviews.

---

## The Research-Then-Act Pattern

**When to Use**: Context is missing or confidence would be low without research. Need to gather information before taking action.

**Structure**: researcher-* (context gathering) → specialist agent (action with context)

**Example**: "Add caching to API endpoints" when unfamiliar with existing caching patterns
1. **researcher-codebase** - Discover existing caching patterns in the codebase
2. **code-implementer** - Implement using discovered patterns (higher confidence, consistent with existing approach)

**Why Research First**: Without research, code-implementer might implement caching differently from existing patterns, creating inconsistency or duplicating utilities.

**Recognition Pattern**:
- Unfamiliar domain or pattern
- Risk of duplicating existing functionality
- Need to understand "how we do this here" before acting

---

## Recognizing When Single Agent Suffices

**Don't default to multi-agent for everything**. Multi-agent adds overhead (time, coordination complexity).

**Use single agent when**:
- Domain is clear and matches agent expertise perfectly
- Task is well-defined with no ambiguity
- Risk is low (not security-critical)
- No cross-domain work involved
- Context is sufficient

**Example**: "Create unit tests for login feature in `tests/auth/test_login.py`"
- Clear domain: `tests/**`
- Clear work type: test creation
- Clear agent: test-creator
- No need for multi-agent (unless feature is security-critical, then add code-reviewer after)
