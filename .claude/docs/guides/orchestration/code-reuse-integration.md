# Code Reuse & Technical Debt Reduction Workflow

**Purpose**: Workflow integration patterns for code reuse framework application during planning and implementation phases.

**Framework Reference**: `.claude/docs/guides/planning/code-reuse-framework.md`

---

## Core Principles

1. **Prefer Extend Over Create**: Default to extending existing components
2. **Prefer Modify Over Replace**: Incremental enhancement over wholesale replacement
3. **Mandatory Cleanup**: Every replacement generates cleanup tasks (T9XX series)
4. **Component Almanac First**: Always check `docs/00-project/COMPONENT_ALMANAC.md` before planning

---

## Planning Phase Code Reuse Steps

### 1. Plan-Enhancer Phase
- Read Component Almanac
- Identify reuse/extend/replace opportunities
- Document existing components in business value propositions
- Flag replacement scenarios for cleanup task generation
- Include "Technical Debt Reduction Value" in success metrics

### 2. Architecture-Enhancer Phase
- Populate "Existing Code Analysis" section
  - Component Almanac Reference Check table
  - Build vs Extend vs Replace Decision Matrix
  - Integration Complexity Analysis
- Populate "Technical Debt & Cleanup Tasks" section
  - Obsolete Code Removal table (file paths, effort)
  - Deprecated Components tracking
  - Tech Debt Investigation Needs (tech-debt-investigator)
  - Cleanup Task Summary (P1/P2/P3 prioritization)
- Enhance "Integration Points" with existing component mapping
- ENFORCE: Prefer extend over create principle

### 3. Architecture-Review Phase
- Score Code Reuse Effectiveness (15% weight)
  - 5: >80% reuse, zero duplication
  - 4: 60-80% reuse, minimal duplication
  - 3: 40-60% reuse, acceptable duplication
  - 2: 20-40% reuse, significant duplication
  - 1: <20% reuse, reinventing the wheel
- Score Cleanup & Debt Reduction (7% weight)
  - 5: Complete cleanup, comprehensive metrics
  - 4: Good cleanup coverage
  - 3: Basic cleanup tasks
  - 2: Incomplete cleanup
  - 1: No cleanup tasks
- Flag "Reinventing the Wheel" as CRITICAL anti-pattern
- Validate cleanup task completeness for all replacements

### 4. Technical-PM Phase (Optional)
- Calculate development time savings
  - Reuse Savings = Build Hours - Integration Hours
  - Extension Savings = Build Hours - (Extend + Migration Hours)
  - Replacement Savings = Maintenance Savings - (Migration + Cleanup Hours)
- Validate >50% time savings threshold
- Include code reuse in cost-benefit analysis

---

## Task Generation Phase Code Reuse Steps

**/tasks command**:
- Parse "Technical Debt & Cleanup Tasks" section
- Generate cleanup task series:
  - T9XX: Cleanup tasks [C] (obsolete code removal)
  - T8XX: Tech debt investigation [I] (complex areas)
  - Priority-based ordering:
    - P1 Cleanup: Before implementation (blocks new code)
    - Implementation tasks
    - P2/P3 Cleanup: After implementation (debt reduction)
- Generate integration tasks for extended components

---

## Implementation Phase Code Reuse Steps

**code-implementer agent**:
- Check Component Almanac before implementation
- Search codebase with Grep/Glob for existing functionality
- Prefer extending existing patterns
- Execute cleanup tasks [C] as specified

**refactorer agent**:
- Extract reusable patterns to shared modules
- Consolidate duplicated code
- Update Component Almanac when creating new reusable components

**test-runner agent**:
- Validate cleanup (no old references remain via grep)

---

## Time Savings Calculation

- **Reuse**: Typically 80-95% time savings
- **Extension**: Typically 60-80% time savings
- **Replacement**: Often negative savings (expensive)
- **Threshold**: Reuse/Extension must save >50% to justify new implementation

---

## Cleanup Task Prioritization

- **P1 (Immediate)**: Blocking issues, security vulnerabilities, conflicts with new code
- **P2 (This Sprint)**: Active usage, technical debt reduction
- **P3 (Backlog)**: Dead code, documentation cleanup

---

## Planning Workflow Coordination Patterns

**Optimized Planning Flow with Code Reuse & Parallel Execution (Recommended)**:
```
/spec → spec-enhancer (creates SPEC.md with embedded Planning Recommendations) → /plan →
  Component Almanac check → read metadata → create plan files →
  [Plan-Enhancer × N in parallel] (business context + code reuse opportunities) →
  [Architecture-Enhancer × N in parallel] (technical content + cleanup tasks) →
  Architecture-Review (validates code reuse + cleanup completeness) →
  Complete PLAN.md → /tasks → [Task-Creator × N in parallel] → Combined tasks.md
```

**Performance**: 3-5x faster than sequential processing for multi-component features

**Quality-Enhanced Planning Flow (Optional)**:
```
/spec → spec-enhancer → spec-reviewer (quality validation) → /plan →
  Component Almanac check → read metadata → create plan files →
  Plan-Enhancer (business + reuse) →
  Technical-PM (business review + reuse ROI) →
  Architecture-Enhancer (technical + cleanup) →
  Architecture-Review (validates reuse + cleanup) →
  Complete PLAN.md → /tasks
```

**Planning Phase Coordination**:
- spec-enhancer embeds Planning Recommendations (component breakdown, complexity, estimates) directly in SPEC.md
- spec-reviewer (optional) provides quality validation before planning
- /plan reads Component Almanac and embedded metadata instead of performing analysis from scratch
- Plan-Enhancer enhances plan files with business context from SPEC + identifies code reuse opportunities
- Technical-PM (optional) provides business alignment review + validates code reuse ROI (time savings)
- Architecture-Enhancer populates technical content for complete plans + generates cleanup tasks for replacements
- Architecture-Review validates plans + scores code reuse effectiveness (15% weight) + cleanup completeness (7% weight)
- /tasks generates T9XX cleanup tasks and T8XX tech debt investigation tasks from plan
- Clean handoff with embedded planning data, validated content, and comprehensive cleanup planning
