# Orchestrator Workflow Documentation

**Purpose**: Core orchestration patterns and design philosophy for Claude Code orchestrator.

**Context Availability**:
- ✅ **Auto-loaded at session startup** - Available throughout session
- ✅ **Use for orchestrator decisions** - Agent selection, delegation patterns, OODA loop coordination
- ❌ **Not for command file references** - Command files (`.claude/commands/*.md`) are self-contained

**Audience**:
- **Claude Code orchestrator** - OODA decision-making, agent coordination, workflow execution
- **Humans** - Understanding system architecture, designing workflows
- **Command designers** - Learning orchestration patterns for `.claude/commands/*.md` files

**Key Principle**: Command files are complete, self-contained instruction sets. This document provides orchestrator background knowledge for decisions, but is not loaded during command execution.

---

## Quick Reference

### Agent Performance Tiers
- **🟢 Fast (<30s)**: spec-reviewer, technical-pm - Prefer for initial analysis
- **🟡 Medium (1-2min)**: plan-enhancer, architecture-enhancer - Targeted modifications
- **🔴 Slow (3+min)**: None (after optimization)

### Delegation Patterns
- **Parallel**: Multiple independent files, different agents on different files
- **Sequential**: `.claude/` directory modifications, dependent workflows, shared state
- **Multi-agent**: Complex tasks requiring specialized expertise (research → implement → test → review)

### Common Scenarios (Quick Reference)
- `.claude/agents/**` → agent-architect
- `.claude/**` (other) → claude-code
- `docs/**/SPEC.md` + creation → spec-enhancer
- `docs/**/SPEC.md` + validation → spec-reviewer
- `docs/**/PLAN.md` + business → plan-enhancer
- `docs/**/PLAN.md` + technical → architecture-enhancer
- `packages/**` + "implement" → code-implementer
- `packages/**` + "debug" → debugger
- `packages/**` + "refactor" → refactorer
- `tests/**` + "create tests" → test-runner
- Research/analysis → researcher-* agents
- Kubernetes ops → k8s-deployment
- Git operations → git-github

**See Complete References**:
- `guides/orchestration/agent-capabilities.md` - Full agent matrix + maturity
- `guides/orchestration/parallel-execution-patterns.md` - Parallel vs sequential rules
- `guides/agents/agent-selection-guide.md` - Domain-first frameworks + 30+ scenarios

---

## Core Orchestration Patterns

### Verification-First Delegation Protocol

When delegating to sub-agents:

1. **PRE-DELEGATION**: Verify preconditions and prepare context
2. **INITIAL ATTEMPT**: Delegate to appropriate sub-agent with current context
3. **VERIFICATION**: Verify expected outputs exist and meet quality standards
4. **ANALYSIS**: If failure or incomplete, analyze what was missing
5. **SECOND ATTEMPT**: Retry with enhanced context OR try different sub-agent
6. **ESCALATION**: If still unsuccessful, provide human summary of attempts and recommendations

**Verification Checkpoints**:
- **After File Creation**: Files exist, size > 0, structure matches template
- **After Content Enhancement**: Sections populated, quality meets standards, cross-references valid
- **After Technical Analysis**: Decisions documented, patterns specified, integration points defined

### Agent Selection Protocol

**Core Approach**: Framework-based reasoning (80% of cases), DCS calculation for novel scenarios (20%).

**Framework-Based Selection** (Most Tasks):

1. **Apply Domain-First Thinking** - File path reveals domain
   - `.claude/agents/**` → agent-architect
   - `.claude/**` (non-agents) → claude-code
   - `docs/**/SPEC.md` → spec-enhancer or spec-reviewer
   - `docs/**/PLAN.md` → plan-enhancer or architecture-enhancer
   - `packages/**` → Continue to work type recognition

2. **Recognize Work Type** - Within domain, what kind of work?
   - Creation (implement, build) → code-implementer
   - Investigation (debug, discover why) → debugger or researcher-codebase
   - Improvement (refactor, optimize) → refactorer
   - Validation (review, audit) → code-reviewer

3. **Apply Disambiguation** - If ambiguous:
   - Domain ownership (strongest signal)
   - Closest expertise
   - Least assumptions
   - Workload balance

4. **Delegate** to selected agent

**DCS Calculation** (Complex/Novel Tasks):

1. **Calculate DCS** - Per `confidence-based-delegation-framework.md`:
   - Task_Complexity (40%): file count, tool calls, expertise, integration
   - Agent_Fit (30%): domain match, capability alignment, experience
   - Context_Quality (20%): information completeness, clarity
   - Cost_Benefit (10%): time savings, quality improvement

2. **Check Multi-Agent Indicators**:
   - Sequential pipeline: Dependencies between steps, different expertise
   - Parallel validation: Multiple perspectives, independent reviews
   - Research-then-act: Context gathering before implementation

3. **Determine Pattern** - Sequential, parallel, or research-then-act

4. **Delegate** - Agent sequence or parallel agents (max 5 simultaneously)

**Anti-Patterns**:
- ❌ Don't default to code-implementer for unclear tasks
- ❌ Don't ignore domain boundaries (`.claude/**` → NOT code-implementer)
- ❌ Don't use keyword matching without context
- ❌ Don't force single agent across multiple domains
- ✅ Do respect domain ownership as strongest signal
- ✅ Do consider work type within domains
- ✅ Do apply disambiguation when multiple agents fit
- ✅ Do decompose multi-domain tasks into specialist sequences

---

## Enhanced Workflow Execution Patterns

**🚀 Workflow Optimization**: spec-enhancer embeds Planning Recommendations directly in SPECs, eliminating duplicate analysis between /spec and /plan phases. Reduces planning overhead by ~50% while maintaining traceability.

### Phase 1: Specification Creation & Planning Metadata
- spec-enhancer creates SPEC.md with embedded Planning Recommendations
- Planning metadata: component breakdown, complexity assessment, sprint estimates
- Orchestrator reads embedded planning metadata (no separate analysis needed)
- Source: Feature descriptions via /spec command or roadmap items

### Phase 2: Plan File Creation & Business Enhancement
- Orchestrator creates plan files from embedded Planning Recommendations
- Delegate to plan-enhancer for business section population (fast startup)
- Alternative: technical-pm for business alignment review (review-only role)
- Input: SPEC.md with embedded metadata + newly created plan templates
- Output: Enhanced plans with business context, requirements traceability
- Verification: Business sections populated, requirements mapped

### Phase 3: Technical Architecture Enhancement
- **Primary**: architecture-enhancer for focused technical content (single file enhancement)
- **Alternative**: architecture-review for multi-plan integration analysis (cross-plan coordination)
- Input: Plan files with business context from plan-enhancer
- Output: Complete PLAN.md ready for implementation
- Verification: Technical decisions documented, architecture patterns specified

### Phase 4: Implementation
- Delegate to code-implementer for feature development using complete plans
- If blocked, delegate to debugger for problem analysis
- If architectural issues, delegate to architecture-review for design review

### Phase 5: Testing & Validation
- Delegate to test-runner for comprehensive validation
- If tests fail, delegate to debugger for failure analysis
- If persistent failures, delegate to architecture-review for technical assessment

### Phase 6: Quality Review
- Delegate to code-reviewer for security and standards validation
- If issues found, delegate to code-implementer for fixes
- If architectural concerns, delegate to architecture-review for design review

### Phase 7: Cleanup & Optimization
- Delegate to refactorer for code organization and optimization
- If structural issues, delegate to architecture-review for redesign
- If quality concerns, delegate to code-reviewer for final validation

---

## Specialized Workflows

### Git Workflow Integration
- **Primary**: git-github (intelligent file grouping, commit execution, CI monitoring)
- **Workflow**: `/git prepare` → Validation → File Grouping → Human Decision → `/git commit` → Execute Commits → Monitor CI (optional)
- **See**: `.claude/commands/git.md` for complete workflow

### Context & Performance Management
- **Primary**: context-optimizer (targeted/group/ecosystem token analysis, redundancy detection)
- **Scope**: Individual agents, agent groups (patterns), or full ecosystem
- **Performance**: 2-3min for single agent vs 60-85min for full ecosystem (6-28x faster targeted)
- **Triggers**: Ecosystem token usage >85%, agent redundancy, MCP tool bloat, performance degradation
- **See**: `.claude/agents/context-optimizer.md` for capabilities and targeting

---

## Escalation Patterns

### When to Use Human Escalation
- Strategic decisions requiring business judgment
- Scope changes affecting project goals
- Technical decisions with significant architectural impact
- Persistent failures across multiple sub-agent attempts

### When to Use Sub-Agent Escalation
- Missing technical expertise (try different specialist)
- Research needs (delegate to spec-enhancer)
- Quality issues (delegate to reviewer)
- Implementation problems (delegate to debugger)

### When to Use Approach Changes
- Current strategy not working after 2 attempts
- Different technical approach might be more effective
- Context has changed since initial attempt
- Alternative patterns identified through research

---

## Workflow State Management

### Execution State Tracking
- Current phase and active sub-agent
- Previous attempts and outcomes
- Context accumulated across sub-agent interactions
- Blockers and resolution strategies applied

### Progress Validation
- Sub-agent output validation against schemas
- Progress against original objectives
- Quality gates and milestone completion
- Readiness for next phase transition

### Context Continuity
- Preserve context across sub-agent delegations
- Maintain decision history and rationale
- Track research findings and application
- Document lessons learned for future iterations

---

## Specialized Guides (Progressive Disclosure)

For detailed patterns, consult specialized guides:

**Agent Management**:
- `guides/orchestration/agent-capabilities.md` - Full agent matrix, maturity tracking, capability mapping
- `guides/agents/agent-selection-guide.md` - 7 frameworks, 30+ scenarios, decision trees

**Execution Optimization**:
- `guides/orchestration/parallel-execution-patterns.md` - Parallel vs sequential rules, performance optimization
- `guides/orchestration/code-reuse-integration.md` - Code reuse workflows, technical debt reduction

**Research & Synthesis**:
- `guides/orchestration/research-coordination.md` - researcher-lead patterns, iterative research workflows
- `guides/orchestration/synthesis-framework.md` - Multi-agent result consolidation, overlap detection

**Planning & Quality**:
- `guides/planning/code-reuse-framework.md` - Extend > create principles, cleanup task generation
- `guides/synthesis-and-recommendation-framework.md` - Trade-off analysis, scoring formulas
- `guides/review-aggregation-logic.md` - Multi-agent review consolidation

---

**This workflow document provides the orchestrator with systematic patterns for coordinating sub-agents while maintaining the 2-attempt rule and ensuring efficient progression through complex development workflows.**
