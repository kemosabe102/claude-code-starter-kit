# Agent Selection Guide

**Framework-based reasoning** for selecting the right agent for any task. Instead of keyword matching or algorithmic rules, these frameworks help understand relationships between file location, work type, and agent expertise.

**Core Problem**: Task-creator overweighted code-implementer using keyword-only matching (e.g., "create" → code-implementer) without understanding domain context. Task to "create intent-analyzer agent in `.claude/agents/intent-analyzer.md`" matched "create" and assigned code-implementer, when agent-architect is domain specialist.

**Solution**: Seven conceptual frameworks guiding reasoning about domain, work type, and expertise matching.

---

## Quick Decision Flow

**Start here for common patterns (80% of cases):**

1. **Check File Paths** → Identify domain
2. **Match Domain to Specialist** (see Domain-Agent Quick Reference below)
3. **If main codebase (`packages/**`, `tests/**`)** → Determine work type (creation, investigation, improvement)
4. **If security-sensitive** → Add research + review steps
5. **If multiple domains** → Decompose into specialist sequences
6. **If ambiguous** → Use Disambiguation Principles (Framework 6)

---

## Domain-Agent Quick Reference

| Domain | Domain Owner | When to Use |
|--------|-------------|-------------|
| `.claude/agents/**` | agent-architect | Agent creation, evaluation, updates |
| `.claude/**` (other) | claude-code | Commands, hooks, schemas, configuration |
| `packages/**` | Varies by work type | See Work Type table below |
| `tests/**` | Varies by work type | See Work Type table below |
| `docs/**/SPEC.md` | spec-enhancer | New specifications |
| `docs/**/PLAN.md` | plan-enhancer, architecture-enhancer | Plan enhancement |
| `docs/**` (review) | spec-reviewer, technical-pm, architecture-review | Validation work |

---

## Work Type Quick Reference (Main Codebase)

| Work Type | Agent | Recognition Keywords |
|-----------|-------|---------------------|
| **Creation** | code-implementer | "create", "build", "implement", "add new feature" |
| **Investigation (unknown cause)** | debugger | "debug", "investigate", "why is it failing", "troubleshoot" |
| **Test Creation** | test-creator | "create tests", "generate tests", "test coverage" |
| **Test Execution** | test-executor | "run tests", "execute tests", "validate execution" |
| **Test Data** | test-dataset-creator | "test data", "fixtures", "test scenarios" |
| **Quality Review** | code-reviewer | "review", "validate quality", "assess", "audit" |
| **Refactoring** | (context-dependent) | "refactor", "restructure", "improve structure" |

---

## Common Scenarios (Quick Lookup)

| Scenario | Decision | Rationale |
|----------|----------|-----------|
| "Fix failing tests" (unknown cause) | debugger | Investigation work |
| "Fix failing tests" (known cause) | code-implementer | Implementation work |
| "Create payment feature" | Multi-agent pipeline | Security-critical requires research → implement → review |
| "Update CLAUDE.md" | claude-code | Domain ownership (Claude Code config) |
| "Analyze auth patterns" | researcher-codebase | Pattern discovery across files |
| "Create agent in `.claude/agents/`" | agent-architect | Agent lifecycle domain |
| "Improve code quality" (vague) | code-reviewer first | Least assumptions (clarify what's needed) |
| "Add caching to API" (unfamiliar) | researcher-codebase → code-implementer | Research-then-act pattern |

---

## Seven Frameworks Overview

**For detailed methodology, see individual framework files:**

### Framework 1: Domain-First Thinking
**Core Principle**: File location reveals domain. Domain determines specialist.

**Primary Domains**:
- `.claude/agents/**` → agent-architect
- `.claude/**` (other) → claude-code
- `packages/**`, `tests/**` → Work type determines (Framework 2)
- `docs/**` → Document type determines (SPEC, PLAN, review)
- Cross-domain → researcher-*, tech-debt-investigator, git-github

**See**: `selection/framework-1-domain-first.md`

---

### Framework 2: Work Type Recognition
**Core Principle**: Within same domain, different work types require different specialists.

**Primary Work Types**:
- **Creation**: Bringing something new into existence → code-implementer
- **Investigation**: Understanding failures/patterns → debugger, researcher-codebase
- **Improvement**: Enhancing existing code → context-dependent
- **Analysis (read-only)**: Assessment without changes → domain specialist in read-only mode

**See**: `selection/framework-2-work-type.md`

---

### Framework 3: Agent Expertise Mapping
**Core Principle**: Match task to agent whose expertise best fits. Technical capability ≠ domain expertise.

**Key Insight**: A generalist can edit any Markdown file. A specialist has developed:
- Deep patterns specific to their domain
- Templates and structures ensuring quality
- Knowledge of pitfalls
- Understanding of best practices

**See**: `selection/framework-3-expertise.md`

---

### Framework 4: Multi-Agent Decision Framework
**Core Principle**: Some tasks too complex or critical for single agent.

**Patterns**:
- **Sequential Pipeline**: Step 1 → Step 2 → Step 3 (dependencies)
- **Parallel Validation**: Multiple perspectives on same artifact
- **Research-Then-Act**: Context gathering → specialist action

**When to Use Multi-Agent**:
- Spans multiple domains
- Security-critical
- Needs validation checkpoints
- Unfamiliar domain requiring research

**See**: `selection/framework-4-multi-agent.md`

---

### Framework 5: Context-Aware Selection
**Core Principle**: Visible task may not contain all context needed. Sometimes gathering context IS the first task.

**The "What Don't I Know?" Check**:
- How many related files?
- Existing patterns to follow?
- Dependencies affected?
- Duplicating functionality?

**Security Context Trigger**: Auth, payments, PII → Automatic research requirement

**See**: `selection/framework-5-context-aware.md`

---

### Framework 6: Disambiguation Principles
**Core Principle**: When multiple agents fit equally well, use these principles.

**The Hierarchy**:
1. **Domain Ownership** (strongest signal)
2. **Closest Expertise** (when domain doesn't fully determine)
3. **Least Assumptions** (when task is ambiguous)
4. **Workload Balance** (when all else is equal)

**See**: `selection/framework-6-disambiguation.md`

---

### Framework 7: Anti-Patterns to Avoid
**Core Principle**: Learn from common mistakes.

**Seven Anti-Patterns**:
1. Default to most familiar agent
2. Ignore domain boundaries
3. Single agent for cross-domain tasks
4. Keyword matching without context
5. Ignore security context
6. Assume simple based on file count
7. Default to code-implementer when uncertain

**See**: `selection/framework-7-anti-patterns.md`

---

## Decision Tree

```
START
  ↓
Check file paths → Identify domain(s)
  ↓
Single domain with clear specialist?
  ├─ YES → Use domain specialist
  └─ NO → Continue
      ↓
  Main codebase domain?
    ├─ YES → Identify work type (Framework 2)
    │         ├─ Creation → code-implementer
    │         ├─ Investigation → debugger or researcher-codebase
    │         ├─ Testing → test-creator, test-executor, test-dataset-creator
    │         └─ Review → code-reviewer
    └─ NO → Cross-domain work?
              ├─ Research → researcher-*
              ├─ Git ops → git-github
              └─ Debt analysis → tech-debt-investigator
  ↓
Security-sensitive?
  ├─ YES → Add: researcher-web → [agent] → code-reviewer
  └─ NO → Continue
  ↓
Multiple domains involved?
  ├─ YES → Decompose into specialists (Framework 4)
  └─ NO → Continue
  ↓
Context sufficient?
  ├─ NO → Start with researcher-codebase
  └─ YES → Proceed with selected agent
  ↓
Still ambiguous?
  └─ Apply Disambiguation Principles (Framework 6)
```

---

## Read-Only Analysis Mode

**Any domain specialist can operate in read-only mode** for analysis within their expertise area.

**Recognition**: Task includes "analyze", "investigate", "assess", "review" + no file modifications expected

**Examples**:
- agent-architect → Analyze agent definitions for duplication
- debugger → Analyze authentication failure patterns
- code-reviewer → Security vulnerability assessment
- technical-pm → Business alignment review

**See Framework 3** for complete read-only specialist mapping.

---

## Integration with Other Frameworks

**This guide complements**:
- **Delegation Confidence Scoring (DCS)** - Use this guide for common patterns (80%), DCS for novel/complex scenarios (20%)
- **Orchestrator Workflow** - Informs agent selection within orchestrator's coordination patterns
- **Research Patterns** - Research-then-act pattern integrates with researcher-lead delegation

**When to Use This Guide vs DCS**:
- **This guide**: Common patterns, known domains, standard work types
- **DCS calculation**: Novel scenarios, unclear confidence, complex multi-factor decisions

Both enforce domain boundaries and avoid keyword-only matching.

---

## Examples in Practice

**For 15 detailed scenario walkthroughs**, see:
`examples/agents/agent-selection-scenarios.md`

**Quick examples**:

**Example 1**: "Fix the failing login tests"
- Domain: `tests/**`
- Work type: Investigation (cause unknown)
- Decision: debugger

**Example 2**: "Create payment processing feature"
- Domain: `packages/**`
- Security-critical: YES
- Pattern: researcher-web → researcher-library → code-implementer → test-creator → test-executor → code-reviewer
- Decision: Multi-agent sequential pipeline

**Example 3**: "Update CLAUDE.md with new agent list"
- Domain: Claude Code configuration
- Domain owner: claude-code
- Decision: claude-code (domain ownership)

---

## Note for researcher-lead Agent

This document is primary reference for agent→domain mappings when creating research plans.

**Key Capability**: ANY agent can perform read-only research within their domain of expertise. Beyond researcher-* family, consider domain specialists for targeted analysis:

**Analysis Without Implementation Examples**:
- agent-architect → Analyze agent definitions, prompt quality in `.claude/agents/**`
- debugger → Analyze test failure patterns, bug patterns in `packages/**`, `tests/**`
- tech-debt-investigator → Analyze code quality, duplication, technical debt (any domain)
- code-reviewer → Analyze code quality, standards compliance (read-only)

**Worker Selection Principle**:
- Match domain expertise to research objective
- Prefer domain specialist over generic researcher-* when expertise aligns
- Example: "Analyze authentication patterns" → debugger (auth domain expert) rather than researcher-codebase

**Reference Framework 1** (Domain-First Thinking) and **Framework 3** (Agent Expertise Mapping) for comprehensive domain → agent mappings.

---

## References

**Framework Deep Dives**:
- `selection/framework-1-domain-first.md` - Domain boundaries and recognition patterns
- `selection/framework-2-work-type.md` - Creation, investigation, improvement work types
- `selection/framework-3-expertise.md` - Agent specializations and read-only workers
- `selection/framework-4-multi-agent.md` - Sequential, parallel, research-then-act patterns
- `selection/framework-5-context-aware.md` - Context quality assessment and triggers
- `selection/framework-6-disambiguation.md` - Four disambiguation principles
- `selection/framework-7-anti-patterns.md` - Seven anti-patterns with examples

**Examples & Scenarios**:
- `examples/agents/agent-selection-scenarios.md` - 15 detailed scenario walkthroughs

---

## Core Takeaway

Agent selection is about understanding **domain, work type, and expertise alignment**—not keyword matching or defaults.

**Apply these frameworks** and agent selection becomes clear in 80% of cases. For remaining 20% (novel, complex scenarios), use DCS calculation.

**Remember**: Respecting domain boundaries and matching expertise produces better work than defaulting to most familiar agent.
