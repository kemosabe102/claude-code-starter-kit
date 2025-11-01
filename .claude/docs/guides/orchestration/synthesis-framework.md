# Result Synthesis & Consolidation Framework

**Purpose**: Systematic approach for consolidating overlapping findings from multiple agents to avoid redundant recommendations and overengineering.

**Framework Document**: `.claude/docs/guides/synthesis-and-recommendation-framework.md`

---

## When to Apply

- Multi-agent research (researcher-lead → multiple workers)
- Multi-agent analysis (code-reviewer, tech-debt-investigator, refactorer)
- Multi-agent reviews (3+ core + 0-2 dynamic agents pattern)
- Any scenario with 3+ findings addressing similar problems

---

## Core Process

### 1. Overlap Detection (Similarity >0.7)
- Group findings by problem domain and keywords
- Identify solutions addressing same underlying issue
- Example: 3 agents suggest different validation approaches

### 2. Trade-off Analysis
- Score each solution: Impact (1-5), Effort (1-5), Risk (L/M/H), Change Scope
- Extract pros/cons systematically
- Consider user context (team skills, time constraints, existing patterns)

### 3. Recommendation Scoring
- **Formula**: `Score = (Impact × 0.6) / (Effort × Risk_Multiplier × Change_Multiplier)`
- Higher score = better impact-to-effort ratio
- Tie-breaking: Prefer lower effort, lower risk, simpler solution

### 4. Structured Presentation
- Problem statement with agent attribution
- Solutions sorted by score (highest first)
- Trade-offs, pros/cons for each solution
- Clear recommendation with rationale
- Explanation of why other solutions discarded

---

## Integration with Multi-Agent Workflows

### After Research Completion
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

### After Multi-Agent Analysis
```
code-reviewer + tech-debt-investigator + refactorer → Complete
  ↓
Orchestrator synthesizes:
  ├─ Group overlapping recommendations
  ├─ Score solutions (impact vs effort)
  └─ Present consolidated recommendations with clear winner
```

### After Multi-Agent Review
```
spec-reviewer + technical-pm + architecture-review → Complete
  ↓
Use review-aggregation-logic.md for quality gates
Use synthesis-and-recommendation-framework.md for overlapping recommendations
```

---

## Example Synthesis

### Without Synthesis (Current Anti-Pattern)
```markdown
Findings:
- Agent A: "Add input validation class"
- Agent B: "Refactor validation into service layer"
- Agent C: "Use Pydantic validators"

Orchestrator: "Implement all three approaches" ❌
→ Result: Overengineered, redundant validation solutions
```

### With Synthesis (Correct Approach)
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

---

## Best Practices

### Do's ✅
- Always detect overlaps before presenting findings
- Score objectively using the formula
- Show trade-offs transparently (don't just pick a winner)
- Prefer simplicity when scores are close (<0.1 difference)
- Attribute solutions to agents for transparency
- Explain why discarded solutions weren't chosen

### Don'ts ❌
- Don't present all overlapping solutions without consolidation
- Don't recommend multiple solutions addressing same problem
- Don't ignore effort/risk in favor of high impact alone
- Don't guess trade-offs - extract from agent findings systematically
- Don't overengineer - prefer localized over system-wide changes

---

## Relationship to Other Frameworks

### synthesis-and-recommendation-framework.md (General overlap consolidation)
- **Use for**: Research findings, analysis recommendations, general multi-agent coordination
- **Focus**: Overlap detection, trade-off analysis, impact/effort scoring

### review-aggregation-logic.md (Structured reviews)
- **Use for**: Formal reviews (spec-reviewer, technical-pm, architecture-review)
- **Focus**: Quality gates, structured validation, machine-readable parsing

### research-patterns.md (Research coordination)
- **Use for**: researcher-lead → worker delegation, compression strategies
- **Focus**: Planning, worker allocation, source quality

### Integration Flow
```
research-patterns.md → Coordinate research workers
  ↓
Workers return findings
  ↓
synthesis-and-recommendation-framework.md → Consolidate overlapping findings
  ↓
Present structured synthesis to user
```
