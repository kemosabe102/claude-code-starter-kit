# Parallel Execution Patterns

**Purpose**: Guide for parallel vs sequential agent execution strategies for optimal performance.

---

## Capability & Benefits

**Claude Code supports launching multiple sub-agents simultaneously** in a single message with multiple Task tool calls.

**Benefits**:
- **3-5x faster processing** for multi-component features
- **Better resource utilization** - parallel work instead of sequential bottlenecks
- **No file conflicts** when agents work on different files
- **Scales efficiently** to 10+ components without timeout concerns

---

## When to Use Parallel Execution

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

---

## Parallel Execution Pattern

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

---

## Critical Constraint: .claude/ Directory

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

---

## Performance Metrics

**Measured Improvements** (3-component feature):
- Sequential plan enhancement: ~6 minutes (2 min per plan × 3 plans)
- Parallel plan enhancement: ~2 minutes (all 3 plans simultaneously)
- **Performance gain**: 3x faster

**Scaling**:
- 5 components: 5x faster with parallel vs sequential
- 10 components: 10x faster with parallel vs sequential
- Limited only by Claude Code's concurrent agent capacity

---

## Agent Performance Optimization

### Performance Tiers (by startup time)

- **🟢 Fast (<30s)**: spec-reviewer (Read+Grep only), technical-pm (Read+Grep+Research only)
  - Prefer for initial analysis and review
- **🟡 Medium (1-2min)**: plan-enhancer (Read+Edit), architecture-enhancer (Read+Edit+Context7)
  - Use for targeted modifications
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
