# Agent Descriptions Update Guide

**Purpose**: Clarify agent purposes and boundaries
**Date**: 2025-10-03
**Status**: Recommended updates to agent descriptions

## Updated Agent Descriptions

### Code Review Agents

#### code-reviewer
**Current**: "Principle-driven code review specialist"
**Updated**: "Code quality reviewer - provides feedback WITHOUT modifying files. Focuses on security, standards, and best practices. Use for PR reviews and quality gates."
**Key Point**: Read-only reviewer, no modifications

#### handle-code-review
**Current**: "Handles code review feedback"
**Updated**: "Code review response handler - ingests review feedback and APPLIES changes. Full implementation capabilities. Use AFTER code-reviewer to fix issues."
**Key Point**: Implements fixes based on review feedback

### Planning Agents

#### plan-enhancer
**Current**: "Enhances plans with business context"
**Updated**: "Business context enhancer for plans - MODIFIES plan files to add business goals, user value, and requirements. Fast startup. Use after plan creation."
**Key Point**: Modifies files, business focus

#### architecture-enhancer
**Current**: "Enhances technical architecture"
**Updated**: "Technical architecture enhancer - MODIFIES plan files to add technical details, patterns, and implementation guidance. Use for technical content."
**Key Point**: Modifies files, technical focus

#### technical-pm
**Current**: "Technical PM review"
**Updated**: "Business alignment reviewer - REVIEWS plans for business value WITHOUT modifying. Generates reports. Read-only. Use for validation."
**Key Point**: Review only, no modifications

#### architecture-review
**Current**: "Architecture review"
**Updated**: "Technical architecture reviewer - REVIEWS plans for technical quality WITHOUT modifying. Generates reports. Read-only. Use for validation."
**Key Point**: Review only, no modifications

### Implementation Agents

#### code-implementer
**Current**: "Implementation specialist"
**Updated**: "Feature implementation specialist - writes production code following plans and specifications. Primary coding agent."
**Clear**: ✅ Already good

#### debugger
**Current**: "Debugging specialist"
**Suggested**: "Problem diagnosis specialist - analyzes failures, identifies root causes, and fixes bugs. Use when tests fail or issues arise."
**Rename to**: `debug-assistant` (future)

#### refactorer
**Current**: "Refactoring specialist"
**Suggested**: "Code refactoring specialist - improves code structure WITHOUT changing behavior. Use for cleanup and optimization."
**Rename to**: `refactor-assistant` (future)

### Testing Agents

#### test-runner
**Current**: "Test automation specialist"
**Updated**: "Test creation and execution specialist - writes and runs tests, ensures coverage, validates functionality."
**Clear**: ✅ Already good

### Specification Agents

#### spec-enhancer
**Current**: "Specification enhancement specialist"
**Updated**: "Specification creator and enhancer - creates comprehensive specs from requirements, adds planning metadata. Primary spec agent."
**Clear**: ✅ Already good

#### spec-reviewer
**Current**: "Specification review specialist"
**Updated**: "Specification quality reviewer - validates specs WITHOUT modifying. Checks clarity, completeness, testability. Read-only."
**Key Point**: Review only

## Description Template

Use this template for consistency:

```
[Primary function] - [modification capability]. [Specific focus areas]. [When to use].

Examples:
"Code quality reviewer - provides feedback WITHOUT modifying files. Focuses on security, standards, and best practices. Use for PR reviews."

"Technical architecture enhancer - MODIFIES plan files to add technical details. Focuses on patterns, integration, and implementation. Use after plan creation."
```

## Key Phrases to Use

### For Reviewers (Read-Only)
- "WITHOUT modifying files"
- "Read-only"
- "Generates reports"
- "Provides feedback"
- "Validates"

### For Enhancers/Modifiers
- "MODIFIES files"
- "Implements changes"
- "Creates content"
- "Writes code"
- "Updates directly"

## Boundary Clarifications

### Review vs Enhance
```
REVIEWER: Reads → Analyzes → Reports
ENHANCER: Reads → Modifies → Saves
```

### When to Use Which
```
Need feedback only? → Reviewer
Need changes made? → Enhancer/Handler
Need both? → Reviewer first, then Enhancer
```

## Migration Plan

### Phase 1: Documentation (Now)
- ✅ Document all clarifications
- ✅ Create naming conventions
- ✅ Identify duplications

### Phase 2: Update Descriptions (Next)
- Update agent markdown files
- Add clarifying phrases
- Emphasize boundaries

### Phase 3: Enforcement (Future)
- Add validation hooks
- Prevent capability mismatches
- Enforce naming standards

## Common Confusion Points

### "Which agent for code review?"
- **Just need feedback?** → code-reviewer
- **Need to apply fixes?** → handle-code-review
- **Full cycle?** → code-reviewer → handle-code-review

### "Which agent for plans?"
- **Add business context?** → plan-enhancer
- **Add technical details?** → architecture-enhancer
- **Review business alignment?** → technical-pm
- **Review technical quality?** → architecture-review

### "Can reviewers make changes?"
**NO.** Reviewers are read-only by design. They:
- Cannot modify files
- Cannot write code
- Can only generate reports
- Should only have read tools

## Validation Checklist

When updating descriptions:
- [ ] Clearly states modification capability
- [ ] Uses "WITHOUT modifying" or "MODIFIES"
- [ ] Explains when to use
- [ ] Mentions specific focus areas
- [ ] Distinguishes from similar agents
- [ ] Follows naming conventions

---

**Action**: Update agent descriptions following these guidelines to reduce confusion and improve selection.