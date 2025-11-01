# Framework 6: Disambiguation Principles

**Core Principle**: When multiple agents seem to fit equally well, use these principles to distinguish best choice.

## Principle 1: Domain Ownership Trumps All

**When in doubt, domain ownership is the strongest signal.**

Domain boundaries are deliberately designed. Agents have developed expertise in their domains. Respect those boundaries even when technical capability suggests alternatives.

**Example**: "Update agent list in CLAUDE.md"
- Technical capability: Many agents can edit Markdown files
- Domain ownership: CLAUDE.md is Claude Code configuration
- Domain owner: **claude-code**
- **Decision**: claude-code (domain ownership wins)

**Why This Principle**: Domain owners understand:
- Structure and conventions of their domain
- Implications of changes in their domain
- Common pitfalls in their domain
- How their domain integrates with others

**Application**: Always check domain first. If domain has clear owner, that's usually your answer.

---

## Principle 2: Closest Expertise Match

**When agents overlap in capability, choose the one whose expertise is closest match to work type.**

**Example**: "Fix bug in auth.py where login fails with 500 error"

**Agents That Could Technically Do This**:
- debugger (expertise: investigation, root cause analysis)
- code-implementer (expertise: implementation, code writing)

**Analysis**:
- Is root cause known? → No, "login fails with 500 error" doesn't specify why
- Is this investigation work? → Yes, need to discover why
- **Closest expertise**: debugger (investigation is their specialization)
- **Decision**: debugger

**Alternative Scenario**: "Fix known bug in auth.py where missing null check causes 500 error"
- Is root cause known? → Yes, "missing null check" is specific
- Is this investigation work? → No, straightforward implementation
- **Closest expertise**: code-implementer (implementation is their specialization)
- **Decision**: code-implementer

**Why This Principle**: Agent whose expertise most closely matches work type will do highest quality work in least time.

---

## Principle 3: Least Assumptions

**When task is ambiguous or vague, choose agent that makes fewest assumptions about what's wanted.**

**Example**: "Improve code quality in payment.py"

**What "improve" could mean**:
- Add comments and documentation
- Restructure for better organization
- Fix bugs
- Optimize performance
- Add error handling
- All of the above?

**Agents That Could Handle This**:
- code-reviewer (assumption: you want feedback on issues)
- code-implementer (assumption: you want new code added)
- debugger (assumption: there are bugs to fix)

**Least Assumptions**:
- **code-reviewer**: Provides feedback on what could be improved, doesn't change code
- **Others**: All assume specific type of improvement and make changes

**Decision**: code-reviewer (least invasive, provides information that clarifies what "improve" means)

**Why This Principle**: Vague tasks benefit from starting with feedback. code-reviewer's output clarifies what improvements are needed, then you can delegate to appropriate specialist (code-implementer, debugger) with clear direction.

**Sequential Pattern**: Ambiguous request → code-reviewer (clarify) → specific agent (implement)

---

## Principle 4: Workload Balance

**When two agents are equally qualified, consider recent task distribution to avoid overloading one agent.**

**Why This Principle**:
- No agent should monopolize all work
- Distributed workload suggests healthy use of specializations
- Prevents systematic overuse of one agent (the original problem with code-implementer)
- Better task distribution means agents stay within their expertise zones

**When to Apply**: Only as tie-breaker. Don't sacrifice expertise match for workload balance. But when expertise is equal, workload balance is reasonable consideration.

---

## Combining Principles

**The Hierarchy**:
1. **Domain Ownership** (strongest signal)
2. **Closest Expertise** (when domain doesn't fully determine)
3. **Least Assumptions** (when task is ambiguous)
4. **Workload Balance** (when all else is equal)

**Example Application**: "Update schema validation in `.claude/docs/schemas/agent-schema.json`"

**Check Each Principle**:
1. **Domain Ownership**: `.claude/docs/schemas/**` - Could be agent-architect (agent schemas) or claude-code (Claude Code schemas). Let's check further.
2. **Closest Expertise**: "agent-schema.json" specifically → agent schemas → agent-architect has deepest expertise in agent-related artifacts
3. **Decision**: agent-architect (domain + expertise align)

**No Need for Principles 3 & 4**: Clear answer from domain and expertise.
