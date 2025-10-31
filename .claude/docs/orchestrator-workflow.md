# Orchestrator Workflow Documentation

**Purpose**: Meta-documentation explaining orchestration patterns and design philosophy for the Claude Code orchestrator.

**Context Availability**:
- ✅ **Auto-loaded at session startup** - Available to orchestrator throughout the session
- ✅ **Use for orchestrator decisions** - Agent selection, delegation patterns, OODA loop coordination
- ❌ **Not for command file references** - Command files (`.claude/commands/*.md`) should be self-contained

**Audience**:
- **Claude Code orchestrator** - OODA decision-making, agent coordination, workflow execution
- **Humans** - Understanding system architecture, designing new workflows
- **Command designers** - Learning orchestration patterns when creating new `.claude/commands/*.md` files

**Key Principle**: Command files are complete, self-contained instruction sets. When the orchestrator executes a command like `/plan`, it loads only the command file and executes the workflow defined there. This document provides the orchestrator with background knowledge for making decisions, but is not loaded during command execution.

---

# Orchestrator Workflow Management

## Agent Legend & Current Capabilities

**Last Updated**: 2025-10-26
**Overall Workflow Maturity**: Alpha (1.67) - Production Testing Ready with Test Architecture Enhancement

### Critical Agents (Primary Workflow - 80% Weight)

| Agent | Maturity | Grade | Capabilities | Strong At | Limitations |
|-------|----------|-------|--------------|-----------|-------------|
| **spec-enhancer** | v1.0 (Alpha) | B+ | Specification creation, planning metadata generation, research | Context7 research, spec creation with embedded planning data, roadmap development | Large-scale implementation coordination |
| **technical-pm** | v1.2 (Alpha) | A | Business alignment review and structured reporting | Business context review, NFR assessment, requirements traceability analysis, structured report generation | **PERFORMANCE OPTIMIZED**: Now 7 tools (Read+Grep+Research only) - zero file mutations |
| **architecture-review** | v1.3 (Alpha) | B+ | Technical architecture analysis and structured reporting | Technical analysis, production readiness assessment, Technical Review Reports + Edit Plans | **PERFORMANCE OPTIMIZED**: Now 6 tools (Read+Grep+Research only) - zero file mutations |
| **code-implementer** | v0.8 (MVP) | C+ | Code implementation, technical execution | Feature development, API integration | Complex architectural decisions |
| **test-runner** | v0.9 (MVP) | B- | Test creation, validation, quality assurance | Unit testing, validation frameworks | Integration test complexity |
| **code-reviewer** | v1.1 (Alpha) | B+ | Quality gates, security validation, standards compliance | Code standards, security review | Performance optimization |

### Support Agents (Secondary Impact - 20% Weight)

| Agent | Maturity | Grade | Capabilities | Strong At | Limitations |
|-------|----------|-------|--------------|-----------|-------------|
| **architecture-enhancer** | v1.0 (Alpha) | B+ | Technical architecture enhancement, Context7 research, placeholder replacement | Technical content population, research-backed decisions, file modification | Large-scale integration analysis |
| **spec-reviewer** | v1.0 (Alpha) | B+ | Specification quality assessment, peer validation review | Quality scoring, ambiguity detection, improvement recommendations | Complex multi-spec validation, cross-specification consistency |
| **debugger** | v0.7 (MVP) | C | Problem diagnosis, troubleshooting | Error analysis, systematic debugging | Complex integration issues |
| **test-creator** | v1.0 (Alpha) | A- | Test generation, coverage analysis, AAA pattern enforcement | Unit test creation, pytest fixtures, Context7 research for testing patterns | Test execution (use test-executor), application bug fixing (use debugger) |
| **test-executor** | v1.0 (Alpha) | B+ | Test execution, failure categorization, delegation routing | Multi-framework test running (pytest/jest/go test), 12-heuristic failure classification, delegation to debugger/test-creator/code-reviewer | Test creation (use test-creator), application bug fixing (use debugger) |
| **refactorer** | v0.6 (MVP) | C- | Code organization, cleanup, optimization | Structure improvement, cleanup | Large-scale architectural changes |
| **agent-architect** | v1.0 (Alpha) | B | Agent lifecycle management, evaluation | Agent creation, quality assessment | Complex workflow coordination |
| **context-optimizer** | v1.0 (Alpha) | B | Context analysis, optimization planning | Targeted/group/ecosystem token analysis, redundancy detection, flexible scope optimization | Analysis only, no modifications |
| **k8s-deployment** | v1.0 (Alpha) | B+ | Kubernetes deployment orchestration, pod troubleshooting, manifest management | Script-driven Kustomize workflows, event-driven troubleshooting, rollback strategies | Multi-cluster environments, cloud provider integrations |

### Workflow Maturity Calculation

```
Critical Agent Average: (1.0 + 1.2 + 1.3 + 0.8 + 0.9 + 1.1) / 6 = 1.05
Support Agent Average: (1.0 + 1.0 + 0.7 + 1.0 + 1.0 + 0.6 + 1.0 + 1.0 + 1.0) / 9 = 0.92
Overall Maturity = (1.05 + 0.92) × 0.85 = 1.97 × 0.85 = 1.67 (Alpha)
```

**Maturity Stages:**
- **MVP (0-1.5)**: Development environment testing ready, manual oversight required
- **Alpha (1.5-2.5)**: Production testing ready, monitoring required
- **Beta (2.5-3.5)**: Production candidate, standard development workflow
- **GA (3.5+)**: Production ready, critical business workflows

## Agent Performance Optimization

### Performance-Based Agent Selection

**Performance Tiers** (by startup time):
- **🟢 Fast (<30s)**: spec-reviewer (Read+Grep only), technical-pm (Read+Grep+Research only) - Prefer for initial analysis and review
- **🟡 Medium (1-2min)**: plan-enhancer (Read+Edit), architecture-enhancer (Read+Edit+Context7) - Use for targeted modifications
- **🔴 Slow (3+min)**: None after technical-pm optimization

### Performance Optimization Results

#### Technical-PM Agent Optimization Complete
**Previous State**: 11 tools including heavy external services (Write, Bash, WebSearch, WebFetch, Context7)
**Previous Impact**: 5+ minute startup time, blocked workflow progression
**Root Cause Resolved**: Agent was configured as creator/editor but used primarily as reviewer
**Solution Applied**: Optimized to Read+Grep+Research tools (reviewer role only), achieved significant startup improvement

**Optimization Changes**:
1. **Removed Creator Tools**: Write, Edit, MultiEdit (no longer needed for review-only role)
2. **Kept Research Tools**: WebSearch, WebFetch, Context7 (for recommendation quality)
3. **Removed Shell Access**: Bash (no execution needed for review)
4. **Optimized Tool Set**: Read (plan analysis), Grep (content search), Research tools (recommendation enhancement)

#### Architecture-Review Agent Optimization Complete
**Previous State**: 10 tools including file mutation capabilities (Read, Write, Edit, MultiEdit, Glob, Grep, WebFetch, WebSearch, Context7)
**Previous Impact**: Slower startup due to file mutation tools, unclear review vs enhancement boundary
**Root Cause Resolved**: Agent was configured for both review and enhancement but should focus solely on analysis
**Solution Applied**: Converted to review-only with Read+Grep+Research tools, generates Technical Review Reports + Technical Edit Plans

**Optimization Changes**:
1. **Removed File Mutation Tools**: Write, Edit, MultiEdit (zero file mutations enforced)
2. **Enhanced Review Capabilities**: Added embedded schemas for Technical Review Report and Technical Edit Plan
3. **Kept Analysis Tools**: Read (plan analysis), Glob/Grep (pattern discovery), Research tools (Context7, WebSearch, WebFetch)
4. **Clear Handoff Design**: Technical Edit Plans provide actionable enhancement instructions for architecture-enhancer consumption
5. **Performance Improvement**: Faster startup time from fewer tools, clearer separation of concerns
6. **Zero Mutation Enforcement**: Agent now strictly prohibited from file modifications

**Performance Impact**: Expected 70% startup time reduction while maintaining review quality

### Performance-Aware Delegation Strategy

**Orchestrator Optimization Rules**:
1. **Fast Agents First**: Always delegate to spec-reviewer before heavier agents
2. **Parallel Independent Work**: Launch multiple agents simultaneously when processing different files
3. **Sequential for .claude/ Directory**: File locking issues require sequential execution for `.claude/` modifications
4. **Progress Feedback**: Provide human updates during heavy agent initialization
5. **Fallback Patterns**: Light agent alternatives for time-sensitive operations

## Parallel Agent Execution

### Capability & Benefits

**Claude Code supports launching multiple sub-agents simultaneously** in a single message with multiple Task tool calls.

**Benefits**:
- **3-5x faster processing** for multi-component features
- **Better resource utilization** - parallel work instead of sequential bottlenecks
- **No file conflicts** when agents work on different files
- **Scales efficiently** to 10+ components without timeout concerns

### When to Use Parallel Execution

**✅ Use Parallel Execution For**:
- Multiple plan files → parallel plan-enhancer agents (different files)
- Multiple plan files → parallel architecture-enhancer agents (different files)
- Multiple plan files → parallel task-creator agents (different files)
- Independent research tasks → parallel web-researcher agents
- Multiple component implementations → parallel code-implementer agents (different files)

**❌ Use Sequential Execution For**:
- Modifying files in `.claude/` directory (file locking issues)
- Agents that coordinate or share state
- When one agent's output feeds into the next agent's input
- Single file modifications by multiple agents

### Parallel Execution Pattern

**Pattern**:
```
Single message with multiple Task tool calls:

Task 1: agent-type for file-1.md
Task 2: agent-type for file-2.md
Task 3: agent-type for file-3.md

All run simultaneously, orchestrator waits for all to complete.
```

**Example from /plan command**:
```
Launch 3 plan-enhancer agents in parallel:
- Task(plan-enhancer, file=core-PLAN.md)
- Task(plan-enhancer, file=analysis-PLAN.md)
- Task(plan-enhancer, file=integration-PLAN.md)

Result: 2 minutes instead of 6 minutes sequential (3x faster)
```

### Critical Constraint: .claude/ Directory

**File Locking Issue**: The `.claude/` directory has file watcher or locking mechanisms that prevent concurrent modifications.

**Solution**: Always use **sequential execution** when modifying files in `.claude/`:
- `.claude/agents/*.md` - Create/modify agents sequentially
- `.claude/commands/*.md` - Update commands sequentially
- `.claude/docs/*.md` - Update documentation sequentially
- `.claude/hooks/*.py` - Modify hooks sequentially

**Safe for Parallel**: User files outside `.claude/` directory:
- `docs/01-planning/specifications/*/plans/*.md` ✅
- `docs/01-planning/specifications/*/tasks/*.md` ✅
- `src/**/*.py` ✅
- `tests/**/*.py` ✅

### Performance Metrics

**Measured Improvements** (3-component feature):
- Sequential plan enhancement: ~6 minutes (2 min per plan × 3 plans)
- Parallel plan enhancement: ~2 minutes (all 3 plans simultaneously)
- **Performance gain**: 3x faster

**Scaling**:
- 5 components: 5x faster with parallel vs sequential
- 10 components: 10x faster with parallel vs sequential
- Limited only by Claude Code's concurrent agent capacity

## Orchestrator Sub-Agent Management Protocol

### Verification-First Delegation Protocol

When delegating to sub-agents, orchestrator follows verification-first protocol:

1. **PRE-DELEGATION**: Verify preconditions and prepare context
2. **INITIAL ATTEMPT**: Delegate to appropriate sub-agent with current context
3. **VERIFICATION**: Verify expected outputs exist and meet quality standards
4. **ANALYSIS**: If failure or incomplete, analyze what was missing
5. **SECOND ATTEMPT**: Retry with enhanced context OR try different sub-agent
6. **ESCALATION**: If still unsuccessful, provide human summary of attempts and recommendations

### Verification Checkpoints

**After File Creation Tasks**:
- Verify files exist at expected locations
- Check file size > 0 (not empty)
- Validate file structure matches expected template

**After Content Enhancement Tasks**:
- Verify specific sections were populated
- Check content quality meets minimum standards
- Validate cross-references and traceability

**After Technical Analysis Tasks**:
- Verify technical decisions are documented
- Check architecture patterns are specified
- Validate integration points are defined

### Sub-Agent Coordination Patterns

**Sub-Agents as Specialized Tools:**
- **Planner**: Strong at research, architecture, strategic thinking
- **Technical-PM**: Strong at business alignment review, NFR assessment, requirements traceability analysis, structured reporting
- **Architecture-Review**: Strong at technical validation, integration analysis, production readiness, quality gates
- **code-implementer**: Strong at code implementation, technical execution
- **Test-Runner**: Strong at validation, quality assurance, automation
- **Code-Reviewer**: Strong at quality gates, security, standards compliance
- **Debugger**: Strong at problem diagnosis, troubleshooting
- **Refactorer**: Strong at code organization, refactoring, cleanup
- **Agent-Architect**: Strong at agent lifecycle, prompt engineering
- **Researcher-Lead**: Strong at research orchestration, multi-source coordination, complex information synthesis
- **Researcher-Codebase**: Strong at code analysis, pattern discovery, architecture investigation
- **Researcher-Web**: Strong at web/documentation research, best practices discovery, source quality assessment
- **Researcher-Library**: Strong at Context7-based library documentation research, official API references, version-specific patterns, framework docs (15:1 compression ratio, <15s performance, Alpha maturity - Production Ready)
- **k8s-deployment**: Strong at Kubernetes deployment orchestration, pod troubleshooting, manifest management, script-driven Kustomize workflows, event-driven troubleshooting, rollback strategies

**Coordination Rules:**
- Only orchestrator can delegate to sub-agents
- Sub-agents cannot call other sub-agents directly
- All sub-agent communication flows through orchestrator
- Orchestrator maintains context and state across sub-agent interactions
- **Orchestrator can launch multiple sub-agents in parallel** when no file conflicts exist
- **Parallel execution recommended** for independent file processing (plan enhancement, task generation)

## Agent Selection Protocol

**Core Approach**: Use framework-based reasoning for common patterns, DCS calculation for novel scenarios.

### Framework-Based Selection Process

**For Most Tasks** (80% of cases):

1. **Apply Domain-First Thinking** - What domain is this task in based on file paths?
   - Consult `.claude/docs/guides/agent-selection-guide.md` Domain-First Framework
   - Domain usually provides clear agent selection
   - Examples:
     - `.claude/agents/**` → agent-architect
     - `.claude/**` (non-agents) → claude-code
     - `docs/**/SPEC.md` → spec-enhancer or spec-reviewer
     - `docs/**/PLAN.md` → plan-enhancer or architecture-enhancer
     - `packages/**` → Continue to work type recognition

2. **Recognize Work Type** - Within domain, what kind of work is this?
   - Creation (implement, build) → code-implementer
   - Investigation (debug, discover why) → debugger or researcher-codebase
   - Improvement (refactor, optimize structure) → refactorer
   - Validation (review, audit) → code-reviewer
   - Consult Work Type Recognition Framework in agent-selection-guide.md

3. **Apply Disambiguation** - If still ambiguous, use principles:
   - Domain ownership (strongest signal - domain owner gets priority)
   - Closest expertise (agent whose expertise best matches work type)
   - Least assumptions (when vague, choose agent that assumes least)
   - Workload balance (avoid overloading one agent)
   - Consult Disambiguation Principles in agent-selection-guide.md

4. **Delegate** to selected agent

**For Complex/Novel Tasks** (20% of cases):

1. **Calculate DCS** per `docs/01-planning/custom/confidence-based-delegation-framework.md`
   - Task_Complexity (40%): file count, tool calls, domain expertise, integration points
   - Agent_Fit (30%): domain match, capability alignment, experience
   - Context_Quality (20%): information completeness, clarity
   - Cost_Benefit (10%): time savings, quality improvement

2. **Check Multi-Agent Indicators** - Does complexity or criticality suggest multiple agents?
   - Sequential pipeline: Dependencies between steps, different expertise needed
   - Parallel validation: Multiple perspectives valuable, independent reviews
   - Research-then-act: Context gathering before implementation
   - Consult Multi-Agent Decision Framework in agent-selection-guide.md

3. **Determine Pattern** - Sequential pipeline, parallel validation, or research-then-act?

4. **Delegate** to agent sequence or parallel agents (max 5 simultaneously)

### Integration of Frameworks and DCS

**Framework thinking complements DCS quantification**:
- **Frameworks** (80% of cases): Fast, intuitive reasoning for common patterns
  - Domain boundaries are clear
  - Work types are recognizable
  - Agent expertise alignment is obvious
  - Quick reference tables apply

- **DCS calculation** (20% of cases): Quantified confidence for novel scenarios
  - Unprecedented task types
  - Ambiguous domain boundaries
  - Multiple agents equally qualified
  - High-stakes decisions requiring justification

**Both approaches**:
- Enforce domain boundaries (critical for accuracy)
- Prevent code-implementer overweighting
- Avoid brittle keyword matching
- Consider context and expertise, not just technical capability

### Decision Flow

**Start Here**: Every agent selection begins with domain-first thinking

```
User Request → Extract file paths → Identify domain(s)
  ↓
Domain Clear? (80% yes)
  ├─ YES → Apply framework
  │   ├─ Single domain specialist (e.g., .claude/agents/** → agent-architect)
  │   └─ Main codebase → Recognize work type → Select specialist
  │
  └─ NO → Calculate DCS (20%)
      ├─ Novel task type
      ├─ Ambiguous domain
      └─ Multiple candidates with similar DCS scores → Apply disambiguation principles
```

**Key Principle**: Understand the task's domain and work type, then match to agent expertise. This produces better selection than pattern matching keywords or defaulting to familiar agents.

**Anti-Pattern Prevention**:
- ❌ Don't default to code-implementer for unclear tasks
- ❌ Don't ignore domain boundaries (`.claude/**` → NOT code-implementer)
- ❌ Don't use keyword matching without context ("create" alone doesn't determine agent)
- ❌ Don't force single agent across multiple domains
- ✅ Do respect domain ownership as strongest signal
- ✅ Do consider work type within domains
- ✅ Do apply disambiguation when multiple agents fit
- ✅ Do decompose multi-domain tasks into specialist sequences

### Quick Reference for Common Scenarios

**Immediate Answers** (no calculation needed):
- `.claude/agents/**` → agent-architect
- `.claude/**` (other) → claude-code
- `docs/**/SPEC.md` + creation → spec-enhancer
- `docs/**/SPEC.md` + validation → spec-reviewer
- `docs/**/PLAN.md` + business → plan-enhancer
- `docs/**/PLAN.md` + technical → architecture-enhancer
- `packages/**` + "implement" → code-implementer
- `packages/**` + "debug" (unknown cause) → debugger
- `packages/**` + "refactor" → refactorer
- `tests/**` + "create tests" → test-runner
- `tests/**` + "fix failing tests" (unknown) → debugger
- Research/analysis (any domain) → researcher-* agents
- Kubernetes deployment/troubleshooting → k8s-deployment
- Git operations → git-github
- Security scanning → sast-scanner

**See Complete Guide**: `.claude/docs/guides/agent-selection-guide.md` for:
- 7 complete frameworks (domain, work type, expertise, multi-agent, context, disambiguation, anti-patterns)
- 30+ scenario examples with reasoning
- Real-world selection walkthroughs
- Common mistakes to avoid

### Example: Applying the Protocol

**Scenario**: "Create payment processing feature with tests and docs"

**Step 1 - Domain-First Thinking**:
- File paths span: `packages/**` (implementation), `tests/**` (testing), `docs/**` (documentation)
- Observation: Multi-domain task

**Step 2 - Recognize Multi-Agent Need**:
- Complexity: High (payment processing is security-critical)
- Domains: 3 different (packages, tests, docs)
- Decision: Sequential pipeline required

**Step 3 - Decompose with Domain Specialists**:
- T001 [researcher-web] Research OWASP payment security patterns (security context)
- T002 [researcher-library] Research payment SDK best practices (library patterns)
- T003 [code-implementer] Implement payment processing in `packages/payments/` (creation)
- T004 [test-runner] Create test suite in `tests/payments/` (validation)
- T005 [code-reviewer] Security-focused review (quality gate)
- T006 [spec-enhancer] Document payment flow in `docs/payments-spec.md` (documentation)

**Rationale**:
- Domain-first thinking identified multi-domain work
- Security context triggered research-first pattern
- Each step uses domain specialist (not forcing code-implementer to do everything)
- Sequential dependencies: research → implement → test → review → document

### Enhanced Workflow Execution Patterns

**🚀 Workflow Optimization**: spec-enhancer now embeds Planning Recommendations directly in SPECs, eliminating duplicate analysis between /spec and /plan phases. This reduces planning overhead by ~50% while maintaining full traceability.

**Phase 1: Specification Creation & Planning Metadata Generation**
- spec-enhancer creates SPEC.md files with embedded Planning Recommendations section
- Planning metadata includes: component breakdown, complexity assessment, sprint estimates
- Orchestrator reads embedded planning metadata (no separate analysis needed)
- Source: Feature descriptions via /spec command or roadmap items

**Phase 2: Plan File Creation & Business Context Enhancement**
- Orchestrator creates plan files from embedded Planning Recommendations using component breakdown table
- Delegate to plan-enhancer for business section population (fast startup with Read+Edit)
- Alternative: technical-pm for business alignment review and structured reporting (review-only role)
- Input: SPEC.md with embedded planning metadata + newly created plan templates
- Output: Enhanced plan files with business context, requirements traceability
- Verification: Confirm business sections populated and requirements mapped

**Phase 3: Technical Architecture Enhancement**
- **Primary**: Delegate to architecture-enhancer for focused technical content population (optimized for single file enhancement)
- **Alternative**: Delegate to architecture-review for comprehensive multi-plan integration analysis (when cross-plan coordination needed)
- Input: Plan files with business context from plan-enhancer
- Output: Complete PLAN.md files ready for implementation with technical architecture
- Verification: Confirm technical decisions documented and architecture patterns specified

**Phase 4: Implementation**
- Delegate to code-implementer for feature development using complete plans
- If blocked, delegate to debugger for problem analysis
- If architectural issues, delegate back to architecture-review for design review

**Phase 5: Testing & Validation**
- Delegate to test-runner for comprehensive validation
- If tests fail, delegate to debugger for failure analysis
- If persistent failures, delegate to architecture-review for technical assessment

**Phase 6: Quality Review**
- Delegate to code-reviewer for security and standards validation
- If issues found, delegate back to code-implementer for fixes
- If architectural concerns, delegate to architecture-review for design review

**Phase 7: Cleanup & Optimization**
- Delegate to refactorer for code organization and optimization
- If structural issues identified, delegate to architecture-review for redesign
- If quality concerns, delegate to code-reviewer for final validation

### Planning Workflow Coordination Patterns

**Optimized Planning Flow with Code Reuse & Parallel Execution (Recommended):**
```
/spec → spec-enhancer (creates SPEC.md with embedded Planning Recommendations) → /plan →
  Component Almanac check → read metadata → create plan files →
  [Plan-Enhancer × N in parallel] (business context + code reuse opportunities) →
  [Architecture-Enhancer × N in parallel] (technical content + cleanup tasks) →
  Architecture-Review (validates code reuse + cleanup completeness) →
  Complete PLAN.md → /tasks → [Task-Creator × N in parallel] → Combined tasks.md
```

**Performance**: 3-5x faster than sequential processing for multi-component features

**Quality-Enhanced Planning Flow (Optional):**
```
/spec → spec-enhancer → spec-reviewer (quality validation) → /plan →
  Component Almanac check → read metadata → create plan files →
  Plan-Enhancer (business + reuse) →
  Technical-PM (business review + reuse ROI) →
  Architecture-Enhancer (technical + cleanup) →
  Architecture-Review (validates reuse + cleanup) →
  Complete PLAN.md → /tasks
```

**Planning Phase Coordination:**
- spec-enhancer embeds Planning Recommendations (component breakdown, complexity, estimates) directly in SPEC.md
- spec-reviewer (optional) provides quality validation before planning
- /plan reads Component Almanac and embedded metadata instead of performing analysis from scratch
- Plan-Enhancer enhances plan files with business context from SPEC **+ identifies code reuse opportunities**
- Technical-PM (optional) provides business alignment review **+ validates code reuse ROI (time savings)**
- Architecture-Enhancer populates technical content for complete plans **+ generates cleanup tasks for replacements**
- Architecture-Review validates plans **+ scores code reuse effectiveness (15% weight) + cleanup completeness (7% weight)**
- /tasks generates T9XX cleanup tasks and T8XX tech debt investigation tasks from plan
- Clean handoff with embedded planning data, validated content, and comprehensive cleanup planning

## Code Reuse & Technical Debt Reduction Workflow

### Code Reuse Framework Integration (New)

**Framework Reference**: `.claude/docs/guides/planning/code-reuse-framework.md`

**Core Principles**:
1. **Prefer Extend Over Create**: Default to extending existing components
2. **Prefer Modify Over Replace**: Incremental enhancement over wholesale replacement
3. **Mandatory Cleanup**: Every replacement generates cleanup tasks (T9XX series)
4. **Component Almanac First**: Always check `docs/00-project/COMPONENT_ALMANAC.md` before planning

**Planning Phase Code Reuse Steps**:

```
1. Plan-Enhancer Phase:
   ├─ Read Component Almanac
   ├─ Identify reuse/extend/replace opportunities
   ├─ Document existing components in business value propositions
   ├─ Flag replacement scenarios for cleanup task generation
   └─ Include "Technical Debt Reduction Value" in success metrics

2. Architecture-Enhancer Phase:
   ├─ Populate "Existing Code Analysis" section
   │  ├─ Component Almanac Reference Check table
   │  ├─ Build vs Extend vs Replace Decision Matrix
   │  └─ Integration Complexity Analysis
   ├─ Populate "Technical Debt & Cleanup Tasks" section
   │  ├─ Obsolete Code Removal table (file paths, effort)
   │  ├─ Deprecated Components tracking
   │  ├─ Tech Debt Investigation Needs (tech-debt-investigator)
   │  └─ Cleanup Task Summary (P1/P2/P3 prioritization)
   ├─ Enhance "Integration Points" with existing component mapping
   └─ ENFORCE: Prefer extend over create principle

3. Architecture-Review Phase:
   ├─ Score Code Reuse Effectiveness (15% weight)
   │  ├─ 5: >80% reuse, zero duplication
   │  ├─ 4: 60-80% reuse, minimal duplication
   │  ├─ 3: 40-60% reuse, acceptable duplication
   │  ├─ 2: 20-40% reuse, significant duplication
   │  └─ 1: <20% reuse, reinventing the wheel
   ├─ Score Cleanup & Debt Reduction (7% weight)
   │  ├─ 5: Complete cleanup, comprehensive metrics
   │  ├─ 4: Good cleanup coverage
   │  ├─ 3: Basic cleanup tasks
   │  ├─ 2: Incomplete cleanup
   │  └─ 1: No cleanup tasks
   ├─ Flag "Reinventing the Wheel" as CRITICAL anti-pattern
   └─ Validate cleanup task completeness for all replacements

4. Technical-PM Phase (Optional):
   ├─ Calculate development time savings
   │  ├─ Reuse Savings = Build Hours - Integration Hours
   │  ├─ Extension Savings = Build Hours - (Extend + Migration Hours)
   │  └─ Replacement Savings = Maintenance Savings - (Migration + Cleanup Hours)
   ├─ Validate >50% time savings threshold
   └─ Include code reuse in cost-benefit analysis
```

**Task Generation Phase Code Reuse Steps**:

```
/tasks command:
├─ Parse "Technical Debt & Cleanup Tasks" section
├─ Generate cleanup task series:
│  ├─ T9XX: Cleanup tasks [C] (obsolete code removal)
│  ├─ T8XX: Tech debt investigation [I] (complex areas)
│  └─ Priority-based ordering:
│     ├─ P1 Cleanup: Before implementation (blocks new code)
│     ├─ Implementation tasks
│     └─ P2/P3 Cleanup: After implementation (debt reduction)
└─ Generate integration tasks for extended components
```

**Implementation Phase Code Reuse Steps**:

```
code-implementer agent:
├─ Check Component Almanac before implementation
├─ Search codebase with Grep/Glob for existing functionality
├─ Prefer extending existing patterns
└─ Execute cleanup tasks [C] as specified

refactorer agent:
├─ Extract reusable patterns to shared modules
├─ Consolidate duplicated code
└─ Update Component Almanac when creating new reusable components

test-runner agent:
└─ Validate cleanup (no old references remain via grep)
```

**Time Savings Calculation**:
- **Reuse**: Typically 80-95% time savings
- **Extension**: Typically 60-80% time savings
- **Replacement**: Often negative savings (expensive)
- **Threshold**: Reuse/Extension must save >50% to justify new implementation

**Cleanup Task Prioritization**:
- **P1 (Immediate)**: Blocking issues, security vulnerabilities, conflicts with new code
- **P2 (This Sprint)**: Active usage, technical debt reduction
- **P3 (Backlog)**: Dead code, documentation cleanup

## Context & Performance Management

### Context Optimization Capabilities
- **Primary**: context-optimizer (targeted/group/ecosystem token analysis, redundancy detection, optimization planning with ROI)
- **Scope Options**: Analyze individual agents, agent groups (via patterns), or full ecosystem
- **Performance**: 2-3min for single agent vs 60-85min for full ecosystem (6-28x faster targeted analysis)
- **Triggers**:
  - Quick feedback on specific agents (targeted analysis)
  - Group consistency checks (pattern-based analysis)
  - Ecosystem token usage >85% capacity (ecosystem-wide analysis)
  - Agent redundancy detected during lifecycle reviews
  - MCP tool bloat concerns (>50K tokens)
  - Performance degradation investigations
  - Pre-optimization baseline measurements
- **Delegation Strategy**: Use targeted mode for quick feedback, ecosystem mode for comprehensive reviews
- **See**: `.claude/agents/context-optimizer.md` for complete capabilities and targeting examples

## Git Workflow Integration

### Git Operations Agent
- **Primary**: git-github (intelligent file grouping, commit execution, CI monitoring)

**Git Workflow Delegation Pattern**:
- **analyze_changes**: Parse git status, apply FileGrouper heuristics, generate semantic commit groups
- **execute_commits**: Execute git add + commit for approved groups with Conventional Commits messages
- **monitor_ci**: Check GitHub Actions status, parse failures, provide actionable recommendations

**Workflow Execution**:
```
/git prepare → Validation → File Grouping (analyze_changes)
→ Quality Gates → Present Results → Human Decision
→ /git commit → Execute Commits (execute_commits)
→ Optional: Monitor CI (monitor_ci)
```

**See**: `.claude/commands/git.md` for complete git workflow documentation

## Agent Capability Matrix

### Research & Analysis Capabilities
- **Primary**: researcher-lead (complex multi-source research coordination), spec-enhancer (Context7 integration, strategic analysis), technical-pm (business alignment review, structured reporting)
- **Secondary**: researcher-codebase (code analysis), researcher-web (web/doc research), researcher-library (library/API documentation), architecture-review (technical research), debugger (problem analysis), agent-architect (prompt research)
- **Delegation Strategy**: Simple queries handled directly; complex multi-source research delegated to researcher-lead for coordinated worker execution

#### Orchestrator-to-researcher-lead Invocation Pattern

**Purpose**: Clear invocation pattern to ensure researcher-lead returns plans, not executes research

**Invocation Structure**:

**Phase 1: Initial Research Planning**
```
Orchestrator invokes:
  Task(
    agent="researcher-lead",
    prompt="CREATE A RESEARCH PLAN for [objective]"  ← KEY PHRASE
  )

researcher-lead returns:
  {
    "delegation_plans": [
      {"worker_type": "researcher-web", "specific_objective": "...", ...},
      {"worker_type": "researcher-codebase", "specific_objective": "...", ...}
    ]
  }

Orchestrator then spawns workers IN PARALLEL:
  Single message with multiple Task calls:
  - Task(agent="researcher-web", prompt="...")
  - Task(agent="researcher-codebase", prompt="...")
```

**Phase 2: Follow-Up Planning (if needed)**
```
Orchestrator detects gaps:
  - Worker confidence < 0.85
  - Unanswered open_questions

Orchestrator invokes researcher-lead AGAIN:
  Task(
    agent="researcher-lead",
    prompt="CREATE FOLLOW-UP RESEARCH PLAN to address [gaps_summary]"
  )

researcher-lead returns:
  {"delegation_plans": [...]}  ← Targeted, 1-3 workers

Orchestrator spawns targeted workers
```

**Anti-Pattern (Don't Do This)**:
```
❌ WRONG: "Investigate feature 005 readiness"
→ researcher-lead will execute research instead of planning (99.4k tokens, 3m 53s)

✅ CORRECT: "CREATE A RESEARCH PLAN for investigating feature 005 readiness"
→ researcher-lead returns delegation plan (5-10k tokens, <30s)
→ Orchestrator spawns workers from plan
→ Workers execute research in parallel (2-3 minutes total)
```

**Key Insights**:
- Phrase matters: "CREATE A RESEARCH PLAN" triggers planning mode, "Investigate" triggers execution mode
- researcher-lead returns PLANS, orchestrator SPAWNS workers
- Orchestrator SYNTHESIZES results after workers complete
- Iteration: Call researcher-lead again with gaps if needed

#### Iterative Research Workflow (NEW)

**Purpose**: Enable multi-round research when initial findings are incomplete

**Worker Capabilities** (v2.0 - all researchers support iteration):
- **researcher-web**: Returns `open_questions` and `confidence_breakdown` with low_confidence_rationale
- **researcher-codebase**: Returns `open_questions` and `confidence_breakdown` with code-specific factors
- **researcher-library**: Returns `open_questions` and `confidence_breakdown` for documentation gaps

**Iteration Trigger Threshold**: Individual worker confidence < 0.85 OR unanswered open_questions

**Orchestrator Iteration Logic**:
```
1. Initial Research Phase:
   - Orchestrator calls researcher-lead for initial plan
   - researcher-lead returns delegation plan (Phase 1-5)
   - Orchestrator spawns workers based on plan

2. Worker Result Analysis (NEW):
   FOR each completed worker:
     - Check individual confidence score
     - IF confidence < 0.85:
         → Record gap: worker_id + low_confidence_rationale
     - Check open_questions
     - FOR each question:
         → Cross-check: Did any other worker answer this?
         → IF unanswered: Record gap: question + suggested_approach

3. Iteration Decision:
   IF gaps_summary is not empty:
     - Orchestrator calls researcher-lead AGAIN (Phase 6: Follow-Up Planning)
     - Pass gaps_summary (NOT full worker results - token efficient)
     - researcher-lead returns targeted follow-up plan (1-3 workers)
     - Orchestrator spawns follow-up workers
     - REPEAT steps 2-3 until:
         * All workers confidence >= 0.85 AND
         * All open_questions answered OR
         * Max iterations reached (default: 3)
   ELSE:
     - Research complete, synthesize all findings

4. Final Synthesis:
   - Combine findings from all rounds
   - Return comprehensive answer to user
```

**Key Design Principles**:
- **Orchestrator-driven**: Orchestrator checks individual results and decides iteration
- **Stateless planning**: researcher-lead called multiple times, doesn't retain state
- **Token-efficient**: Only gap summaries sent to researcher-lead, not full worker results
- **Individual thresholds**: Each worker evaluated independently (not aggregated confidence)
- **Targeted follow-up**: Follow-up plans address specific gaps with 1-3 workers

**Example Flow**:
```
Round 1:
  User: "Research async validation patterns in Pydantic v2"
  → researcher-lead creates plan (3 workers: web, codebase, library)
  → Orchestrator spawns workers
  → researcher-web returns confidence 0.72 + open_question: "async nested models?"
  → researcher-codebase returns confidence 0.88 (no iteration needed)
  → researcher-library returns confidence 0.90 (no iteration needed)

Orchestrator Detects:
  researcher-web: confidence < 0.85 AND unanswered question
  → gaps_summary: ["Low confidence: async patterns (0.72)", "Unanswered: async nested models"]

Round 2:
  → Orchestrator calls researcher-lead with gaps_summary
  → researcher-lead creates targeted follow-up (1 worker: researcher-library for official docs)
  → Orchestrator spawns researcher-library (targeted)
  → researcher-library returns confidence 0.92 + answers nested models question

Orchestrator Checks:
  All workers confidence >= 0.85: ✓
  All open_questions answered: ✓
  → Research complete, synthesize Round 1 + Round 2 findings
```

**Performance Impact**:
- Initial research: Same as before (10-15 minutes typical)
- Follow-up research: 2-5 minutes per round (targeted, not full re-research)
- Total: 15-25 minutes for 2-round research (vs 10-15 minutes accept-incomplete)

### Strategic Planning Capabilities
- **Primary**: plan-enhancer (business context enhancement, requirements mapping) - **FAST STARTUP**
- **Secondary**: spec-enhancer (technical planning), technical-pm (business alignment review), architecture-review (technical strategy)

### Business Analysis Capabilities
- **Primary**: plan-enhancer (business goals, user value, requirements traceability) - **PERFORMANCE OPTIMIZED**
- **Secondary**: technical-pm (business alignment review, NFR assessment), spec-enhancer (strategic context)

### Implementation Capabilities
- **Primary**: code-implementer (feature development, API integration)
- **Secondary**: refactorer (code structure), debugger (issue resolution)

### Architecture & Technical Design Capabilities
- **Primary**: architecture-enhancer (technical content population, single-file focused), architecture-review (technical validation, integration analysis, production readiness)
- **Secondary**: spec-enhancer (architectural planning), technical-pm (NFR framework assessment)

### Validation & Testing Capabilities
- **Primary**: test-runner (automated testing, validation)
- **Secondary**: code-reviewer (manual review), debugger (failure analysis)

### Quality & Standards Capabilities
- **Primary**: code-reviewer (security, compliance, standards)
- **Secondary**: refactorer (code quality), agent-architect (agent standards)

### Architectural & Strategic Capabilities
- **Primary**: spec-enhancer (specification design, strategic planning)
- **Secondary**: agent-architect (agent architecture), code-reviewer (architectural review)

### Deployment & Operations Capabilities
- **Primary**: k8s-deployment (Kubernetes orchestration, pod troubleshooting, manifest management)
- **Secondary**: code-implementer (manifest modifications), debugger (application-level diagnosis), git-github (configuration PRs)

## Result Synthesis & Consolidation

### Purpose

When coordinating multiple agents (research, analysis, review), findings often include **overlapping solutions** that address the same problem with different approaches. The orchestrator must consolidate these findings to avoid:
- Presenting redundant recommendations
- Overengineering by implementing multiple overlapping solutions
- Confusion about which approach to implement
- Technical debt from conflicting implementations

### Synthesis Framework

**Framework Document**: `.claude/docs/guides/synthesis-and-recommendation-framework.md`

**When to Apply**:
- Multi-agent research (researcher-lead → multiple workers)
- Multi-agent analysis (code-reviewer, tech-debt-investigator, refactorer)
- Multi-agent reviews (3+ core + 0-2 dynamic agents pattern)
- Any scenario with 3+ findings addressing similar problems

**Core Process**:

1. **Overlap Detection** (Similarity >0.7)
   - Group findings by problem domain and keywords
   - Identify solutions addressing same underlying issue
   - Example: 3 agents suggest different validation approaches

2. **Trade-off Analysis**
   - Score each solution: Impact (1-5), Effort (1-5), Risk (L/M/H), Change Scope
   - Extract pros/cons systematically
   - Consider user context (team skills, time constraints, existing patterns)

3. **Recommendation Scoring**
   - Formula: `Score = (Impact × 0.6) / (Effort × Risk_Multiplier × Change_Multiplier)`
   - Higher score = better impact-to-effort ratio
   - Tie-breaking: Prefer lower effort, lower risk, simpler solution

4. **Structured Presentation**
   - Problem statement with agent attribution
   - Solutions sorted by score (highest first)
   - Trade-offs, pros/cons for each solution
   - Clear recommendation with rationale
   - Explanation of why other solutions discarded

### Integration with Multi-Agent Workflows

**After Research Completion**:
```
researcher-lead → Workers complete → Orchestrator receives findings
  ↓
Check: 3+ findings with overlap?
  ├─ YES → Apply Synthesis Framework
  │   ├─ Detect overlaps (similarity scoring)
  │   ├─ Analyze trade-offs (impact, effort, risk)
  │   ├─ Calculate scores (formula)
  │   └─ Present structured synthesis
  └─ NO → Present findings directly
```

**After Multi-Agent Analysis**:
```
code-reviewer + tech-debt-investigator + refactorer → Complete
  ↓
Orchestrator synthesizes:
  ├─ Group overlapping recommendations
  ├─ Score solutions (impact vs effort)
  └─ Present consolidated recommendations with clear winner
```

**After Multi-Agent Review**:
```
spec-reviewer + technical-pm + architecture-review → Complete
  ↓
Use review-aggregation-logic.md for quality gates
Use synthesis-and-recommendation-framework.md for overlapping recommendations
```

### Example Synthesis

**Without Synthesis** (Current Anti-Pattern):
```markdown
Findings:
- Agent A: "Add input validation class"
- Agent B: "Refactor validation into service layer"
- Agent C: "Use Pydantic validators"

Orchestrator: "Implement all three approaches" ❌
→ Result: Overengineered, redundant validation solutions
```

**With Synthesis** (Correct Approach):
```markdown
## Problem: Input Validation Approach

### Solution 1: Pydantic Validators ⭐ RECOMMENDED
**Score**: 1.20 (Highest)
- Impact: 4/5 | Effort: 2/5 | Risk: Low
- Pros: Simple, type-safe, industry standard
- Cons: Requires model definitions (minimal)

### Solution 2: Validation Service
**Score**: 0.20
- Impact: 3/5 | Effort: 4/5 | Risk: Medium
- Why Not: Overengineered for current need (YAGNI violation)

### Solution 3: Validation Class
**Score**: 0.27
- Impact: 3/5 | Effort: 3/5 | Risk: Medium
- Why Not: More complex than Pydantic without benefit

**Recommendation**: Solution 1 (Pydantic) - Highest score, optimal impact/effort ratio
```

### Best Practices

**Do's** ✅:
- Always detect overlaps before presenting findings
- Score objectively using the formula
- Show trade-offs transparently (don't just pick a winner)
- Prefer simplicity when scores are close (<0.1 difference)
- Attribute solutions to agents for transparency
- Explain why discarded solutions weren't chosen

**Don'ts** ❌:
- Don't present all overlapping solutions without consolidation
- Don't recommend multiple solutions addressing same problem
- Don't ignore effort/risk in favor of high impact alone
- Don't guess trade-offs - extract from agent findings systematically
- Don't overengineer - prefer localized over system-wide changes

### Relationship to Other Frameworks

**synthesis-and-recommendation-framework.md** (General overlap consolidation):
- Use for: Research findings, analysis recommendations, general multi-agent coordination
- Focus: Overlap detection, trade-off analysis, impact/effort scoring

**review-aggregation-logic.md** (Structured reviews):
- Use for: Formal reviews (spec-reviewer, technical-pm, architecture-review)
- Focus: Quality gates, structured validation, machine-readable parsing

**research-patterns.md** (Research coordination):
- Use for: researcher-lead → worker delegation, compression strategies
- Focus: Planning, worker allocation, source quality

**Integration Flow**:
```
research-patterns.md → Coordinate research workers
  ↓
Workers return findings
  ↓
synthesis-and-recommendation-framework.md → Consolidate overlapping findings
  ↓
Present structured synthesis to user
```

## Escalation Patterns

### When to Use Human Escalation
- Strategic decisions requiring business judgment
- Scope changes that affect project goals
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

## Workflow State Management

### Execution State Tracking
- Current phase and active sub-agent
- Previous attempts and their outcomes
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
- Track research findings and their application
- Document lessons learned for future iterations

---

**This workflow document provides the orchestrator with systematic patterns for coordinating sub-agents while maintaining the 2-attempt rule and ensuring efficient progression through complex development workflows.**