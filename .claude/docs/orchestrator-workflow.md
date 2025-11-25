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

### Common Scenarios (Examples)

These are examples of how agents might be selected based on their descriptions. Claude Code automatically matches tasks to agents.

- `.claude/agents/**` - Agent architecture work
- `.claude/**` (other) - Claude Code framework work
- `docs/**/SPEC.md` - Specification work
- `docs/**/PLAN.md` - Planning work
- `packages/**` - Application code work
- `tests/**` - Testing work
- Research/analysis - Information gathering
- Kubernetes ops - Deployment operations
- Git operations - Version control

Actual agent selection is automatic based on agent descriptions and task requirements.

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

**Core Approach**: Trust agent descriptions for automatic selection. Claude Code matches tasks to agents based on their descriptions.

**How Selection Works**:

1. **Agent Descriptions Drive Selection**
   - Each agent has a description with clear trigger conditions
   - Claude Code reads these descriptions and matches them to tasks
   - Well-written descriptions enable accurate automatic selection

2. **When Creating Agents**
   - Write clear "Use when..." or "Proactively use for..." triggers
   - Include specific domain keywords and technologies
   - Use action-oriented language
   - Declare the agent's role and expertise explicitly

3. **Multi-Agent Coordination**
   - Sequential: Dependencies between steps, different expertise needed
   - Parallel: Independent tasks that can run simultaneously
   - Research-then-act: Gather context before implementation
   - Discovery Pattern: Multi-agent ORIENT exploration when context insufficient

4. **Coordination Limits**
   - Parallel agents: Max 5 simultaneously
   - Sequential: Coordinate dependencies carefully
   - File modifications: Coordinate to avoid conflicts

**Best Practices**:
- ✅ Trust automatic agent selection based on descriptions
- ✅ Write clear, specific task descriptions
- ✅ Decompose multi-domain tasks into logical steps
- ✅ Use parallel execution for independent tasks
- ❌ Don't override automatic selection without good reason
- ❌ Don't ignore domain boundaries
- ❌ Don't force single agent across multiple domains

---

### Discovery Pattern (ORIENT Phase Exploration)

**When to Use**: Context_Quality <0.7 OR ambiguous agent selection OR security-critical domains

**Pattern**: Spawn 2-3 exploration agents in parallel during ORIENT to gather multi-perspective context before selecting execution agent in DECIDE phase.

**Spawning Strategy** (single message with multiple Task calls):

1. **Always include**: context-readiness-assessor (primary CQ calculator)
2. **Add domain specialist**: Based on file paths or task domain
3. **Add researcher**: researcher-codebase (patterns), researcher-web (external), or researcher-library (docs)
4. **Optional**: hypothesis-former (multiple approach options)

**Example Coordination**:
```python
# Single message with 3 parallel Task calls
Task(agent="context-readiness-assessor",
     prompt="Assess Context_Quality for OAuth2 API implementation")
Task(agent="researcher-codebase",
     prompt="Find existing authentication patterns in codebase")
Task(agent="researcher-web",
     prompt="Research OAuth2 best practices for Python APIs")
```

**CQ Consolidation**:
- Use weighted averaging: context-readiness-assessor (0.50) + specialists (0.35) + researcher (0.15)
- Check consensus: Strong (±0.10), Weak (>0.20), Conflict (>0.30)
- Gate decision: CQ ≥0.85 → PROCEED | CQ <0.85 → Iterate (max 2 rounds)

**After Consolidation**:
- If CQ ≥0.85: Proceed to DECIDE (select execution agent)
- If CQ <0.85: Spawn targeted follow-up agents (max 2 rounds total)
- If 2 rounds exhausted: Escalate to user with consolidated findings

**Cost Management**: +60-120s latency, +100-200k tokens. Reserve for ambiguous/security-critical tasks. Standard agent selection should resolve 70-80% of cases without Discovery Pattern.

**See**: CLAUDE.md Discovery Pattern section for complete workflow, examples, and triggers

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
