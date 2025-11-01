# Framework 7: Anti-Patterns to Avoid

**Core Principle**: Learn from common mistakes to develop better selection intuition. Knowing what NOT to do is as valuable as knowing what to do.

## Anti-Pattern 1: Default to Most Familiar Agent

**Mistake**: Always choosing code-implementer because it's used most often or appears most frequently in task histories.

**Why It's Wrong**:
- Familiarity ≠ Best Fit
- Each agent exists because they bring specialized expertise
- Defaulting to one agent ignores value of specialization
- Creates original problem (code-implementer overweighting)

**Real Example**: "Review code quality in auth module"
- Familiar choice: code-implementer (it does lots of things)
- Right choice: code-reviewer (specialized in quality review)

**Better Approach**: Let domain and work type guide selection based on expertise match, not habit or frequency of use.

**Self-Check**: "Am I choosing this agent because it's the right expertise, or because it's the one I think of first?"

---

## Anti-Pattern 2: Ignore Domain Boundaries

**Mistake**: Using code-implementer for `.claude/agents/**` work because "it can edit Markdown files" or "it writes code and prompts are kind of like code."

**Why It's Wrong**:
- Technical capability (editing .md files) ≠ Domain expertise (agent prompt engineering)
- code-implementer hasn't developed agent-architect's expertise in:
  - Prompt engineering patterns
  - Agent evaluation criteria
  - Simulation-driven development
  - Anthropic's best practices
- Ignoring boundaries produces lower quality work

**Real Example**: "Create sentiment-analyzer agent in `.claude/agents/sentiment-analyzer.md`"
- Wrong: code-implementer (can edit .md files)
- Right: agent-architect (domain specialist for agent lifecycle)

**Better Approach**: Domain boundaries are hard boundaries. They exist for a reason. Respect specializations regardless of file format.

**Self-Check**: "Am I choosing based on file type capability, or based on domain expertise?"

---

## Anti-Pattern 3: Single Agent for Cross-Domain Tasks

**Mistake**: "Implement user authentication with tests and documentation" → assign to code-implementer for everything.

**Why It's Wrong**:
- Forces one agent to work across multiple domains:
  - `packages/**` (implementation) - code-implementer's domain
  - `tests/**` (testing) - test-creator's and test-executor's domain
  - `docs/**` (documentation) - documentation agents' domain
- Each part gets lower quality than using specialist
- Documentation specialists know specification structure better than code-implementer
- test-creator knows test design patterns better than code-implementer
- test-executor knows test execution patterns better than code-implementer

**Better Approach**: Decompose cross-domain tasks into specialist sequences.

**Correct Decomposition**:
- T001 [test-creator] Create test suite in `tests/auth/`
- T002 [code-implementer] Implement authentication in `packages/auth/`
- T003 [test-executor] Validate tests pass
- T004 [code-reviewer] Security-focused review
- T005 [spec-enhancer] Document authentication flow in `docs/auth-spec.md`

**Self-Check**: "Does this task span multiple domains? Should I decompose it?"

---

## Anti-Pattern 4: Keyword Matching Without Context

**Mistake**: Task contains "create" → automatically assign code-implementer without considering what's being created or where.

**Why It's Wrong**:
- "Create SPEC.md" and "Create auth.py" both contain "create"
- But they need different specialists:
  - "Create SPEC.md" → spec-enhancer (documentation domain)
  - "Create auth.py" → code-implementer (main codebase domain)
- Keywords are hints, not rules
- Context (domain, work type) matters more than individual words

**Real Example**:
- "Create agent evaluation in `.claude/agents/evaluator.md`"
  - Keyword: "create" (suggests code-implementer)
  - Domain: `.claude/agents/**` (agent lifecycle)
  - Work type: Agent creation
  - **Right choice**: agent-architect (domain + work type override keyword)

**Better Approach**:
1. Don't start with keywords
2. Start with domain (Framework 1)
3. Then work type (Framework 2)
4. Keywords can confirm, but domain/work type determine

**Self-Check**: "Am I pattern matching words, or understanding task's nature?"

---

## Anti-Pattern 5: Ignore Security Context

**Mistake**: Treating authentication, payment processing, or data privacy tasks like any other implementation.

**Why It's Wrong**:
- Security domains have specific patterns and pitfalls
- General implementation agents might not know OWASP guidelines
- Security mistakes are expensive (data breaches, compliance violations, reputation damage)
- "Move fast and break things" doesn't apply to security

**Real Example**: "Implement OAuth login in `packages/auth/oauth.py`"
- Wrong: code-implementer alone (might implement insecurely)
- Right: researcher-web (OWASP patterns) → code-implementer (secure implementation) → code-reviewer (security validation)

**Security Domains Requiring Research**:
- Authentication/Authorization
- Payment processing
- Cryptography
- Session management
- Input validation
- Data privacy/PII
- External API keys/secrets

**Better Approach**: Recognize security context → automatically trigger research-then-implement-then-review pattern.

**Self-Check**: "Is this security-sensitive? Do I need research and additional validation?"

---

## Anti-Pattern 6: Assume Simple Based on File Count

**Mistake**: "Only touching one file, so it's simple" → assign directly to implementation agent without context gathering.

**Why It's Wrong**:
- One file might have 20 dependents
- Changing model file affects all services using it
- Modifying utility affects all callers
- "Simple" based on file count ≠ simple based on impact

**Real Example**: "Update User model in `packages/models/user.py`"
- Looks simple: one file
- Reality: 15 services import User model
- Impact: Need to understand all usages before changing

**Better Approach**: Even for "one file", ask:
- How many files depend on this?
- What's the impact radius?
- Should I gather context first?

If impact is unclear, start with researcher-codebase.

**Self-Check**: "Am I confusing file count with complexity?"

---

## Anti-Pattern 7: No Default Fallback → Default to code-implementer

**Mistake**: "I don't know which agent to use, so I'll default to code-implementer since it's versatile."

**Why It's Wrong**:
- This is exactly how code-implementer became overweighted
- Defaulting to any agent for ambiguous cases hides ambiguity
- Forces agent to work outside their expertise
- Produces lower quality work

**Better Approach**: If agent selection is genuinely ambiguous after applying all frameworks, **mark for manual review** rather than defaulting.

**Return**: "Agent selection ambiguous. Considered agents: X, Y, Z. Disambiguation needed: [specific question]"

**Why This Is Better**:
- Makes ambiguity visible
- Forces clarification of requirements
- Prevents systematic misassignment
- Ensures right agent for actual (clarified) task

**Self-Check**: "Am I defaulting because I'm certain, or because I don't want to say 'I don't know'?"
