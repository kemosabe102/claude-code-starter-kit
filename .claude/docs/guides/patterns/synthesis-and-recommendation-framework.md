# Synthesis and Recommendation Framework

**Purpose**: Systematic framework for consolidating overlapping findings from multiple agents into actionable, prioritized recommendations

**Last Updated**: 2025-10-31
**Applies To**: Orchestrator, multi-agent research, multi-agent analysis/review workflows
**Auto-Load**: Referenced by orchestrator-workflow.md for session availability

---

## Overview

### Problem Addressed

When coordinating multiple agents (research, analysis, review), findings often include **overlapping solutions** that:
- Address the same underlying problem
- Propose different approaches with varying trade-offs
- Create confusion about which solution to implement
- Risk overengineering by implementing redundant solutions

**Example Anti-Pattern**:
```markdown
Agent A (code-reviewer): "Add input validation class"
Agent B (tech-debt-investigator): "Refactor validation logic into service layer"
Agent C (researcher-web): "Use Pydantic validators for input checking"

Orchestrator (WRONG): "Implement all three approaches"
→ Result: 3 overlapping validation solutions, technical debt, maintenance burden
```

### When to Apply This Framework

**✅ Use This Framework When**:
- Coordinating 3+ agents (core + dynamic pattern)
- Research workflows (researcher-lead → multiple workers)
- Analysis workflows (code-reviewer, tech-debt-investigator, refactorer)
- Multi-agent reviews (spec-reviewer, technical-pm, architecture-review)
- Findings include multiple solutions to same problem

**❌ Don't Use When**:
- Single agent outputs (no overlap possible)
- Findings are complementary (not overlapping)
- Structured reviews with formal schemas (use review-aggregation-logic.md)

### Scope

**This framework provides**:
1. Overlap detection algorithm (similarity scoring)
2. Trade-off analysis matrix (impact, effort, risk)
3. Recommendation scoring formula (highest impact, lowest change)
4. Structured presentation template
5. Integration guidance for orchestrator

**This framework does NOT handle**:
- Formal review aggregation (see review-aggregation-logic.md)
- Research planning/coordination (see research-patterns.md)
- Quality gate decisions (see review-aggregation-logic.md)

---

## Step 1: Overlap Detection

### Similarity Scoring Algorithm

**Purpose**: Identify solutions addressing the same underlying problem

**Algorithm**:
```python
def detect_overlaps(findings: list[Finding]) -> list[OverlapGroup]:
    """
    Group findings by similarity using keyword matching and problem domain.

    Returns groups of overlapping findings addressing same problem.
    """
    overlap_groups = []

    for finding in findings:
        # Extract problem keywords
        keywords = extract_keywords(finding.description)
        problem_domain = categorize_problem(finding)

        # Check against existing groups
        matched_group = None
        for group in overlap_groups:
            similarity = calculate_similarity(finding, group)
            if similarity > 0.7:  # 70% similarity threshold
                matched_group = group
                break

        if matched_group:
            matched_group.add(finding)
        else:
            overlap_groups.append(OverlapGroup([finding]))

    return overlap_groups

def calculate_similarity(finding: Finding, group: OverlapGroup) -> float:
    """
    Calculate similarity score (0.0-1.0) between finding and group.

    Factors:
    - Keyword overlap (40%)
    - Problem domain match (30%)
    - File/location overlap (20%)
    - Agent type similarity (10%)
    """
    keyword_score = len(set(finding.keywords) & set(group.keywords)) / len(finding.keywords)
    domain_score = 1.0 if finding.domain == group.domain else 0.0
    location_score = 1.0 if finding.location == group.location else 0.5
    agent_score = 1.0 if finding.agent_type == group.primary_agent_type else 0.7

    return (keyword_score * 0.4 +
            domain_score * 0.3 +
            location_score * 0.2 +
            agent_score * 0.1)
```

### Problem Domain Categories

**Common Domains** (for domain matching):
- **Security**: Authentication, authorization, input validation, encryption
- **Performance**: Caching, optimization, database queries, async operations
- **Architecture**: Modularity, coupling, separation of concerns, design patterns
- **Code Quality**: Duplication, complexity, naming, documentation
- **Testing**: Coverage, flakiness, test design, mocking
- **Infrastructure**: Deployment, configuration, monitoring, logging
- **Data**: Validation, transformation, storage, retrieval

### Overlap Detection Example

**Input Findings**:
```yaml
Finding 1 (code-reviewer):
  description: "Add Pydantic model for request validation"
  keywords: [validation, input, pydantic, model]
  domain: security
  location: packages/api/routes.py

Finding 2 (tech-debt-investigator):
  description: "Refactor validation logic into shared validator service"
  keywords: [validation, refactor, service, logic]
  domain: architecture
  location: packages/api/

Finding 3 (researcher-web):
  description: "Use FastAPI dependency injection for validators"
  keywords: [validation, fastapi, dependency, injection]
  domain: architecture
  location: packages/api/
```

**Overlap Detection Result**:
```yaml
OverlapGroup:
  problem: "Input validation approach"
  similarity_score: 0.78
  findings: [Finding 1, Finding 2, Finding 3]
  reason: "All address validation in packages/api/, 78% keyword overlap"
```

---

## Step 2: Trade-off Analysis

### Analysis Matrix

For each solution in an overlap group, evaluate:

| Dimension | Scale | Description |
|-----------|-------|-------------|
| **Impact** | 1-5 | User value, problem solving effectiveness, system improvement |
| **Effort** | 1-5 | Implementation complexity, time required, skill needed |
| **Risk** | L/M/H | Failure likelihood, regression potential, reversibility |
| **Change Scope** | Localized/Module/System | Blast radius, integration complexity |

### Impact Scoring (1-5)

- **5 (Critical)**: Solves major pain point, significant user value, blocks progress
- **4 (High)**: Notable improvement, measurable benefit, enhances quality
- **3 (Medium)**: Moderate improvement, incremental value
- **2 (Low)**: Minor improvement, nice-to-have
- **1 (Minimal)**: Cosmetic change, negligible impact

### Effort Scoring (1-5)

- **5 (Very High)**: >2 weeks, multiple modules, complex integration, new patterns
- **4 (High)**: 1-2 weeks, multiple files, moderate complexity
- **3 (Medium)**: 3-5 days, few files, established patterns
- **2 (Low)**: 1-2 days, single file, straightforward changes
- **1 (Minimal)**: <1 day, trivial changes, no risk

### Risk Assessment (L/M/H)

- **High**: Breaking changes, untested patterns, external dependencies, hard to revert
- **Medium**: Moderate changes, proven patterns, some reversibility
- **Low**: Isolated changes, well-tested patterns, easily reversible

### Change Scope

- **Localized**: Single function/class, no downstream impacts
- **Module**: Single module/package, limited integration points
- **System-wide**: Multiple modules, architectural changes, broad integration

### Pros/Cons Extraction

**Systematic Approach**:
```python
def extract_trade_offs(solution: Solution) -> TradeOffs:
    """
    Extract pros and cons from solution description and agent context.

    Returns structured trade-offs for comparison.
    """
    pros = []
    cons = []

    # Pattern matching for common trade-offs
    if "simple" in solution.description.lower():
        pros.append("Simple implementation")
    if "comprehensive" in solution.description.lower():
        pros.append("Comprehensive solution")
        cons.append("Higher complexity")
    if "refactor" in solution.description.lower():
        cons.append("Requires refactoring existing code")
    if "new pattern" in solution.description.lower():
        cons.append("Team learning curve")
    if "reuse" in solution.description.lower():
        pros.append("Leverages existing code")

    # Agent-specific insights
    if solution.agent == "tech-debt-investigator":
        pros.append("Reduces technical debt")
    if solution.agent == "code-reviewer":
        pros.append("Follows best practices")
    if solution.agent == "researcher-web":
        pros.append("Industry-standard approach")

    return TradeOffs(pros=pros, cons=cons)
```

### Trade-off Analysis Example

**Solution A: Pydantic Model Validation**
```yaml
Impact: 4/5
  - Solves validation problem completely
  - Type safety + runtime validation
  - Clear error messages
Effort: 2/5
  - Add Pydantic models to existing routes
  - ~1-2 days, single file changes
  - Well-documented pattern
Risk: Low
  - Pydantic is proven, widely used
  - No breaking changes
  - Easy to test and revert
Change Scope: Localized
  - Limited to API routes
  - No downstream impacts
Pros:
  - Simple implementation
  - Type safety
  - Clear error messages
  - Industry standard
Cons:
  - Adds dependency (Pydantic)
  - Requires model definitions
```

**Solution B: Shared Validator Service**
```yaml
Impact: 3/5
  - Solves validation problem
  - Reusable across modules
  - But adds abstraction layer
Effort: 4/5
  - Create new service layer
  - Refactor existing validation
  - ~1-2 weeks, multiple files
  - New pattern for team
Risk: Medium
  - New pattern, team learning curve
  - Integration complexity
  - Harder to test
Change Scope: Module
  - Affects multiple routes
  - New service layer
  - Moderate integration
Pros:
  - Reusable validation logic
  - Centralized control
  - Reduces duplication
Cons:
  - Higher complexity
  - Refactoring burden
  - Team learning curve
  - Overengineered for current need
```

**Solution C: FastAPI Dependency Injection**
```yaml
Impact: 3/5
  - Solves validation problem
  - Follows FastAPI patterns
  - But more complex setup
Effort: 3/5
  - Set up dependency injection
  - ~3-5 days, moderate complexity
  - FastAPI-specific pattern
Risk: Medium
  - Framework-specific approach
  - Less portable
  - Moderate testing complexity
Change Scope: Module
  - Affects route structure
  - Dependency setup
Pros:
  - FastAPI native pattern
  - Testable dependencies
  - Flexible injection
Cons:
  - Framework lock-in
  - More complex than Pydantic alone
  - Requires DI understanding
```

---

## Step 3: Recommendation Scoring

### Scoring Formula

```
Score = (Impact × Impact_Weight) / (Effort × Risk_Multiplier × Change_Multiplier)

Where:
  Impact_Weight = 0.6 (prioritize user value)
  Risk_Multiplier:
    - Low = 1.0
    - Medium = 1.5
    - High = 2.0
  Change_Multiplier:
    - Localized = 1.0
    - Module = 1.5
    - System-wide = 2.0
```

### Scoring Examples

**Solution A: Pydantic Model Validation**
```
Score = (4 × 0.6) / (2 × 1.0 × 1.0)
      = 2.4 / 2.0
      = 1.20
```

**Solution B: Shared Validator Service**
```
Score = (3 × 0.6) / (4 × 1.5 × 1.5)
      = 1.8 / 9.0
      = 0.20
```

**Solution C: FastAPI Dependency Injection**
```
Score = (3 × 0.6) / (3 × 1.5 × 1.5)
      = 1.8 / 6.75
      = 0.27
```

**Result**: Solution A (1.20) is the clear winner - highest impact with lowest effort/risk.

### Tie-Breaking Rules

If scores are within 0.1 of each other:
1. **Prefer lower effort** (faster to market)
2. **Prefer lower risk** (safer bet)
3. **Prefer simpler solution** (easier maintenance)
4. **Prefer agent expertise** (code-reviewer > tech-debt-investigator > researcher-web for code quality)

---

## Step 4: Structured Presentation

### Presentation Template

```markdown
## Problem: [Clear problem statement]

**Identified By**: [List of agents: code-reviewer, tech-debt-investigator]
**Problem Domain**: [Security/Performance/Architecture/etc.]
**Location**: [File path or component]

---

### Solutions Analysis

#### Solution 1: [Name] ⭐ RECOMMENDED
**Proposed By**: [Agent name]
**Score**: [X.XX] (Highest)

**Approach**: [1-2 sentence description]

**Trade-offs**:
- **Impact**: X/5 - [Brief justification]
- **Effort**: X/5 - [Brief justification]
- **Risk**: [Low/Medium/High] - [Brief justification]
- **Change Scope**: [Localized/Module/System]

**Pros**:
- [Pro 1]
- [Pro 2]
- [Pro 3]

**Cons**:
- [Con 1]
- [Con 2]

---

#### Solution 2: [Name]
**Proposed By**: [Agent name]
**Score**: [X.XX]

**Approach**: [1-2 sentence description]

**Trade-offs**:
- **Impact**: X/5 - [Brief justification]
- **Effort**: X/5 - [Brief justification]
- **Risk**: [Low/Medium/High] - [Brief justification]
- **Change Scope**: [Localized/Module/System]

**Pros**:
- [Pro 1]
- [Pro 2]

**Cons**:
- [Con 1]
- [Con 2]

**Why Not Recommended**: [Clear explanation comparing to Solution 1]

---

#### Solution 3: [Name]
[Same structure as Solution 2]

---

### Recommendation: ✅ Solution 1 ([Name])

**Rationale**:
[2-3 sentences explaining why this solution is best - reference scoring]

**Implementation Priority**: [Immediate/This Sprint/Backlog]

**Discarded Solutions**:
- **Solution 2**: [Brief reason - e.g., "Overengineered for current need"]
- **Solution 3**: [Brief reason - e.g., "Higher risk, similar impact"]
```

### Complete Example

```markdown
## Problem: Input Validation Approach for API Routes

**Identified By**: code-reviewer, tech-debt-investigator, researcher-web
**Problem Domain**: Security + Architecture
**Location**: packages/api/routes.py

---

### Solutions Analysis

#### Solution 1: Pydantic Model Validation ⭐ RECOMMENDED
**Proposed By**: code-reviewer
**Score**: 1.20 (Highest)

**Approach**: Add Pydantic BaseModel classes for request validation with automatic type checking and error messages.

**Trade-offs**:
- **Impact**: 4/5 - Solves validation completely with type safety
- **Effort**: 2/5 - Simple model additions, 1-2 days
- **Risk**: Low - Proven pattern, widely used
- **Change Scope**: Localized - API routes only

**Pros**:
- Simple implementation
- Type safety + runtime validation
- Clear error messages
- Industry standard (FastAPI native)
- Easy to test

**Cons**:
- Adds Pydantic dependency (already in use)
- Requires model definitions (minimal boilerplate)

---

#### Solution 2: Shared Validator Service
**Proposed By**: tech-debt-investigator
**Score**: 0.20

**Approach**: Create centralized validator service layer with reusable validation logic across all modules.

**Trade-offs**:
- **Impact**: 3/5 - Solves validation with reusability
- **Effort**: 4/5 - New service layer, 1-2 weeks refactoring
- **Risk**: Medium - New pattern, integration complexity
- **Change Scope**: Module - Affects multiple routes

**Pros**:
- Reusable validation logic
- Centralized control
- Reduces duplication (future-facing)

**Cons**:
- Higher complexity
- Requires significant refactoring
- Team learning curve
- Overengineered for current scale

**Why Not Recommended**: Much higher effort (4x) for similar impact. Introduces unnecessary abstraction layer given current codebase size. Violates YAGNI principle.

---

#### Solution 3: FastAPI Dependency Injection
**Proposed By**: researcher-web
**Score**: 0.27

**Approach**: Use FastAPI's dependency injection system to inject validators into route handlers.

**Trade-offs**:
- **Impact**: 3/5 - Solves validation with flexibility
- **Effort**: 3/5 - DI setup, 3-5 days
- **Risk**: Medium - Framework-specific, less portable
- **Change Scope**: Module - Route structure changes

**Pros**:
- FastAPI native pattern
- Testable via DI mocking
- Flexible injection points

**Cons**:
- Framework lock-in
- More complex than Pydantic alone
- Requires DI understanding
- Adds indirection

**Why Not Recommended**: Higher complexity than Solution 1 without significant benefit. Pydantic validation (Solution 1) already integrates seamlessly with FastAPI without explicit DI setup.

---

### Recommendation: ✅ Solution 1 (Pydantic Model Validation)

**Rationale**:
Highest score (1.20 vs 0.20/0.27) due to optimal balance of impact and effort. Delivers complete validation solution with type safety in 1-2 days of localized changes. Solutions 2 and 3 introduce unnecessary complexity and higher implementation costs without proportional benefits at current scale.

**Implementation Priority**: This Sprint

**Discarded Solutions**:
- **Solution 2 (Validator Service)**: Overengineered - adds complexity without current need (YAGNI violation)
- **Solution 3 (DI Validators)**: Unnecessary indirection - Pydantic handles this natively in FastAPI
```

---

## Step 5: Orchestrator Integration

### Integration Workflow

```python
# Pseudo-code for orchestrator synthesis workflow

def orchestrator_synthesis_workflow(agent_findings: list[AgentFinding]) -> Synthesis:
    """
    Apply synthesis framework to multi-agent findings.

    Returns structured synthesis with recommendations.
    """
    # Step 1: Detect overlaps
    overlap_groups = detect_overlaps(agent_findings)

    # Step 2: For each overlap group, analyze trade-offs
    analyzed_groups = []
    for group in overlap_groups:
        solutions = []
        for finding in group.findings:
            trade_offs = extract_trade_offs(finding)
            score = calculate_recommendation_score(
                impact=finding.impact,
                effort=finding.effort,
                risk=finding.risk,
                change_scope=finding.change_scope
            )
            solutions.append(Solution(
                finding=finding,
                trade_offs=trade_offs,
                score=score
            ))

        # Sort by score (highest first)
        solutions.sort(key=lambda s: s.score, reverse=True)
        analyzed_groups.append(AnalyzedGroup(
            problem=group.problem,
            solutions=solutions,
            recommended=solutions[0]  # Highest score
        ))

    # Step 3: Generate structured presentation
    presentation = generate_synthesis_presentation(analyzed_groups)

    return Synthesis(
        overlap_groups=analyzed_groups,
        presentation=presentation,
        recommendations=[g.recommended for g in analyzed_groups]
    )
```

### When to Apply (Decision Tree)

```
User Request → Orchestrator delegates to multiple agents → Agents complete
  ↓
Check: Are there 3+ findings addressing similar problems?
  ├─ NO → Present findings directly (no synthesis needed)
  └─ YES → Apply Synthesis Framework
      ↓
      Step 1: Overlap Detection (similarity >0.7)
      Step 2: Trade-off Analysis (impact, effort, risk, scope)
      Step 3: Recommendation Scoring (formula)
      Step 4: Structured Presentation (template)
      Step 5: Present synthesis to user
```

### Trigger Conditions

**Automatic Triggers**:
- Multi-agent analysis (3+ core + dynamic agents pattern)
- Research with multiple workers (researcher-lead → workers)
- Code review findings (code-reviewer + tech-debt-investigator + refactorer)
- Architecture review (multiple perspectives)

**Manual Triggers**:
- Orchestrator detects overlap keywords: "similar", "overlap", "redundant", "both", "alternative"
- User request includes: "consolidate", "synthesize", "recommend best approach"

### Integration with Existing Frameworks

**Relationship to review-aggregation-logic.md**:
- Use review-aggregation-logic for **structured reviews** (spec-reviewer, technical-pm, architecture-review)
- Use synthesis-and-recommendation-framework for **general multi-agent findings** (research, analysis, code reviews)
- Complement each other: Review aggregation → Quality gates | Synthesis framework → Overlap consolidation

**Relationship to research-patterns.md**:
- research-patterns handles **worker coordination** (planning, delegation, compression)
- synthesis-and-recommendation-framework handles **result consolidation** (overlap detection, trade-offs, recommendations)
- Sequential flow: Research patterns (coordinate) → Synthesis framework (consolidate)

---

## Examples

### Example 1: Research on Async Validation

**Scenario**: User asks "Research async validation patterns in Pydantic v2"

**Agent Findings**:
```yaml
researcher-web:
  - "Use async validators with @field_validator decorator"
  - "Implement async model validation with validate() method"

researcher-codebase:
  - "Current codebase uses sync validators - need migration"
  - "Refactor validators to async for DB lookups"

researcher-library:
  - "Pydantic v2 recommends async validators for I/O operations"
  - "Use model_validator for complex async validation"
```

**Without Synthesis (Current Behavior)**:
```markdown
Findings from 3 agents:

researcher-web suggests:
- Use async validators with @field_validator
- Implement async validation with validate()

researcher-codebase suggests:
- Current codebase needs migration
- Refactor validators to async

researcher-library suggests:
- Use async validators for I/O
- Use model_validator for complex cases

→ User sees 6 overlapping suggestions, unclear which to implement
```

**With Synthesis Framework**:
```markdown
## Problem: Async Validation Implementation Strategy

**Identified By**: researcher-web, researcher-codebase, researcher-library
**Problem Domain**: Architecture + Performance
**Location**: packages/core/validators.py

---

### Solutions Analysis

#### Solution 1: Incremental Migration with @field_validator ⭐ RECOMMENDED
**Proposed By**: researcher-library + researcher-web
**Score**: 1.33

**Approach**: Start with @field_validator for individual fields with I/O, migrate to model_validator for complex cases later.

**Trade-offs**:
- **Impact**: 4/5 - Enables async DB lookups, improves performance
- **Effort**: 2/5 - Incremental migration, 2-3 days
- **Risk**: Low - Proven pattern, gradual rollout
- **Change Scope**: Localized - Individual validators

**Pros**:
- Incremental migration (low risk)
- Official Pydantic v2 pattern
- Backward compatible (sync validators still work)
- Clear upgrade path

**Cons**:
- Partial async (not all validators migrated immediately)
- Mixed sync/async during transition

---

#### Solution 2: Full Refactor with model_validator
**Proposed By**: researcher-codebase
**Score**: 0.50

**Approach**: Refactor all validators to use async model_validator for centralized validation logic.

**Trade-offs**:
- **Impact**: 3/5 - Centralized validation, but complex migration
- **Effort**: 4/5 - Full refactor, 1-2 weeks
- **Risk**: Medium - Big bang migration, testing burden
- **Change Scope**: Module - All validators

**Pros**:
- Centralized validation logic
- Complex validation patterns supported
- Complete async solution

**Cons**:
- Higher risk (big bang migration)
- Significant effort (2 weeks+)
- All-or-nothing approach
- Blocks other development

**Why Not Recommended**: Much higher effort for marginal benefit over incremental approach. Increases risk with big bang migration.

---

### Recommendation: ✅ Solution 1 (Incremental @field_validator)

**Rationale**:
Score 1.33 vs 0.50 due to lower risk and effort while achieving similar impact. Incremental approach allows validation during migration and provides clear rollback points. Start with high-value I/O validators (user lookups, external APIs) then expand to complex cases if needed.

**Implementation Priority**: This Sprint

**Discarded Solutions**:
- **Solution 2 (Full Refactor)**: Overengineered for immediate needs, high risk
```

### Example 2: Code Quality Improvements

**Scenario**: Multiple agents review authentication code

**Agent Findings**:
```yaml
code-reviewer:
  - "Extract authentication logic into separate service"
  - "Add input validation for credentials"

tech-debt-investigator:
  - "High coupling between auth and routes"
  - "Duplicate password validation in 3 places"

refactorer:
  - "Consolidate validation into shared module"
  - "Use dependency injection for auth service"
```

**Overlap Detection**:
```yaml
OverlapGroup 1:
  problem: "Authentication architecture"
  findings: [code-reviewer "extract service", refactorer "use DI"]

OverlapGroup 2:
  problem: "Validation duplication"
  findings: [code-reviewer "add validation", tech-debt "duplicate validation", refactorer "consolidate"]
```

**Synthesis Output**:
```markdown
## Problem 1: Authentication Architecture

### Recommendation: ✅ Extract Auth Service (No DI Yet)
**Score**: 1.40 vs 0.60
- Extract to service: Impact 4/5, Effort 2/5, Risk Low
- Add DI: Impact 3/5, Effort 4/5, Risk Medium
- **Rationale**: Service extraction provides 80% of benefits without DI complexity

---

## Problem 2: Validation Duplication

### Recommendation: ✅ Consolidate with Pydantic Models
**Score**: 1.50 vs 0.30 vs 0.40
- Pydantic models: Impact 5/5, Effort 2/5, Risk Low (already in use)
- Shared module: Impact 4/5, Effort 4/5, Risk Medium (new abstraction)
- Generic validators: Impact 3/5, Effort 3/5, Risk Medium (overengineered)
- **Rationale**: Pydantic already in codebase, eliminates duplication with minimal effort
```

---

## Best Practices

### Do's ✅

1. **Always detect overlaps first** - Don't rush to recommendations
2. **Score objectively** - Use the formula, don't guess
3. **Show your work** - Display trade-offs, don't just pick a winner
4. **Consider user context** - Team skill level, time constraints, existing patterns
5. **Prefer simplicity** - When scores are close, choose simpler solution
6. **Attribute to agents** - Show which agent suggested which solution
7. **Explain discarded options** - Help user understand why not chosen

### Don'ts ❌

1. **Don't present all overlapping solutions** - Consolidate first
2. **Don't ignore effort/risk** - High impact alone doesn't justify high cost
3. **Don't guess trade-offs** - Extract from agent findings systematically
4. **Don't skip scoring** - Gut feelings lead to bias
5. **Don't recommend multiple overlapping solutions** - Pick one, justify it
6. **Don't overengineer** - Prefer localized over system-wide changes
7. **Don't ignore agent expertise** - code-reviewer > generic suggestion

---

## Validation Checklist

**Before presenting synthesis**:
- [ ] Overlap groups identified (similarity >0.7)
- [ ] Trade-offs extracted for each solution
- [ ] Impact, Effort, Risk, Change Scope scored
- [ ] Recommendation scores calculated
- [ ] Solutions sorted by score (highest first)
- [ ] Pros/cons listed for each solution
- [ ] Recommendation rationale explains scoring
- [ ] Discarded solutions have clear "why not" explanation

**Quality Checks**:
- [ ] Recommended solution has highest score OR clear tie-breaking justification
- [ ] No overengineering (prefer simpler when scores close)
- [ ] Change scope matches effort estimate
- [ ] Risk assessment considers team context
- [ ] Agent attributions present

---

## References

- **Review Aggregation**: `.claude/docs/guides/review-aggregation-logic.md` (structured reviews)
- **Research Patterns**: `.claude/docs/guides/research-patterns.md` (worker coordination)
- **Orchestrator Workflow**: `.claude/docs/orchestrator-workflow.md` (agent coordination)
- **Multi-Agent Analysis**: `CLAUDE.md` (3 core + 0-2 dynamic pattern)

---

**Questions or Extensions**:
If this framework is insufficient for specific scenarios, document the gap and propose refinements.
