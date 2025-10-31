# Feature Specification: [FEATURE NAME]

**Feature Branch**: `[###-feature-name]`
**Created**: [DATE]
**Status**: Draft
**Input**: User description: "$ARGUMENTS"
**Reference Guide**: [path to guide file if provided via file:, else "None"]
**Guide Type**: [technical_implementation_guide | architecture_decision | best_practices | workflow_description | "N/A"]

## Execution Flow (main)
```
1. Parse user description from Input OR extract from Reference Guide
   → If empty and no guide: ERROR "No feature description provided"
2. Extract key concepts from description or guide
   → Identify: actors, actions, data, constraints, technical approaches
3. For each unclear aspect:
   → Mark with [NEEDS CLARIFICATION: specific question]
4. Fill User Scenarios & Testing section
   → If no clear user flow: ERROR "Cannot determine user scenarios"
5. Generate Functional Requirements
   → Each requirement must be testable
   → Mark ambiguous requirements
6. Identify Key Entities (if data involved)
7. If Reference Guide provided: Populate Reference Documentation section
8. Run Review Checklist
   → If any [NEEDS CLARIFICATION]: WARN "Spec has uncertainties"
   → If implementation details found: ERROR "Remove tech details"
9. Return: SUCCESS (spec ready for planning)
```

---

## Reference Documentation

**This section is populated when a guide file is referenced via `file:` argument**

### Source Guide
- **File**: [absolute path to guide file]
- **Purpose**: [extracted purpose/overview from guide]
- **Key Concepts**: [list of main concepts from guide]

### Extracted Business Requirements
[Business goals and user value extracted from guide]

**Example**:
- Enable developers to efficiently navigate and understand codebases
- Support impact analysis for code changes with <30 second response time
- Provide dependency mapping capabilities with 95%+ accuracy

### Extracted User Scenarios
[User workflows and scenarios from guide]

**Example**:
1. **Initial Discovery** - Developer searches for all code mentioning a specific function
2. **Dependency Mapping** - Developer needs to understand what code depends on a module
3. **Impact Analysis** - Developer determines what will break if code changes

### Technical Approaches & Patterns
[Implementation patterns, algorithms, and approaches from guide - these inform HOW during planning]

**Example**:
- **Primary Approach**: Three-layer search strategy (Quick → Smart → Deep)
- **Tools**: ripgrep, grep, find, tree-sitter, ctags, language servers
- **Workflows**: discovery, dependency_mapping, impact_analysis, semantic_search
- **Memory Structure**: Per-file cache + global dependency graph
- **Optimization Techniques**: Bloom filters, parallel search, early termination, smart caching

### Performance & Quality Targets
[Non-functional requirements extracted from guide]

**Example**:
| Operation | Target | Accuracy |
|-----------|--------|----------|
| Initial search | < 1 second | 100% |
| Dependency mapping | < 5 seconds | 95%+ |
| Full impact analysis | < 30 seconds | 95%+ |

**Quality Philosophy**: "95% quickly beats 100% slowly"

### Guide Reference for Planning
**IMPORTANT**: This guide file should be consulted during `/plan` and `/tasks` phases for detailed implementation guidance. Each component plan should reference relevant sections of this guide.

**For Planners**: Review [guide file path] sections on:
- [List key sections relevant to planning, e.g., "Smart Traversal Algorithm", "Memory Structure", "Efficiency Tricks"]

---

## ⚡ Quick Guidelines
- ✅ Focus on WHAT users need and WHY (business value and outcomes)
- 🎯 Include WHERE and WITH WHAT CONSTRAINTS (platform, architecture, technical boundaries)
- ❌ Avoid detailed HOW implementation (no specific code structure, function names, detailed algorithms)
- 👥 Written for both business stakeholders AND technical planners
- 💰 Budget constraint: <$100/month for all external APIs
- 📊 Risk awareness: Identify and score major risks using P×I×E
- 🔄 Sequencing: Consider component dependencies for phased delivery

### Business vs Technical Specification Boundary
**DO Include (Platform & Constraints)**:
- Target platform (Claude Code, Python, Kubernetes, etc.)
- Architectural constraints (must use X protocol, integrate with Y system)
- Non-functional requirements (performance, scalability, reliability targets)
- Technology choices that ARE the requirement (e.g., "must be Claude Code command")
- Reference to technical implementation guides (when provided)

**DO NOT Include (Implementation Details)**:
- Specific code structure or class hierarchies
- Detailed algorithm implementations
- Function names or variable naming conventions
- Low-level technical decisions better made during planning

**Note**: When a Reference Guide is provided, technical approaches ARE captured in the Reference Documentation section for planning phase consumption, but they remain separate from business requirements.

---

## Pain Point Alignment

### Target Pain Points
<!-- Reference: docs/00-project/CUSTOMER-PAIN-POINTS-EXTERNAL.md -->

| Pain Point ID | Description | How This Feature Helps | Impact Score |
|---------------|-------------|----------------------|--------------|
| [ID] | [Description] | [Specific mitigation] | [High/Medium/Low] |

**Pain Point Alignment Score:** [0.0-1.0] (Target: ≥0.4) [✅/❌]

**Calculation:**
- [Pain Point]: Weight=[1-5], Coverage=[0-1], Impact=[1-5] = [score]
- Total Score = (sum of scores) / (sum of weights)

### ROI Analysis (Hours-Based)

| Activity | Current Time | With Feature | Time Saved | Frequency | Monthly Hours Saved |
|----------|--------------|--------------|------------|-----------|-------------------|
| [Activity] | [time] | [time] | [time] | [freq] | [hours] |

**Total Monthly Time Savings:** [hours]
**Developer Hour Value:** ~$100/hour (internal estimate)
**Effective Monthly Value:** $[amount]

---

## User Scenarios & Testing

### Primary User Story
[High-level narrative describing how users will interact with this feature and what value they derive]

### Acceptance Scenarios

#### Scenario 1: [Scenario Name]
**Given** [initial context and preconditions]
**When** [user action or trigger]
**Then** [expected outcome and success criteria]

#### Scenario 2: [Scenario Name]
**Given** [initial context]
**When** [user action]
**Then** [expected outcome]

---

## Functional Requirements

### Core Requirements (MVP - MUST HAVE)

#### FR-C001: [Requirement Name]
**Description**: [Clear, testable requirement]
**User Value**: [Why this matters to users]
**Acceptance Criteria**:
- [ ] [Specific, measurable criterion]
- [ ] [Specific, measurable criterion]

**Traceability**:
- Pain Point: [ID]
- Scenario: [Scenario reference]
- Guide Reference: [section if applicable]

### Optional Requirements (Future Enhancement)

#### FR-O001: [Requirement Name]
**Description**: [Enhancement beyond MVP]
**User Value**: [Additional value provided]
**Rationale for Optional**: [Why this can wait]

---

## Key Entities & Data Models

### Entity 1: [Entity Name]
**Purpose**: [What this entity represents]
**Key Attributes**:
- `[attribute_name]`: [type] - [description]

**Relationships**:
- [Relationship to other entities]

**Data Source**: [Where this data comes from]
**Guide Reference**: [guide section if applicable, e.g., "Memory Structure - Per-File Cache"]

---

## Technical Expectations & Constraints

### Platform & Technology
- **Platform**: [Claude Code | Python Application | Web Service | Kubernetes]
- **Implementation Type**: [command/agent/hook | worker | endpoint | deployment]
- **Required Tools**: [List from guide if applicable]

### Performance Requirements
[Non-functional requirements - often extracted from Reference Guide]

| Requirement | Target | Measurement |
|-------------|--------|-------------|
| Response time | [target] | [how measured] |
| Throughput | [target] | [how measured] |
| Accuracy | [target] | [how measured] |

### Integration Requirements
- Must integrate with: [existing systems]
- Must follow: [protocols, patterns]
- Must use: [specific technologies if mandated]

### Constraints
- Budget: <$100/month for external APIs
- [Other constraints from business or guide]

---

## Risk Assessment

### Risk Matrix

| Risk ID | Description | P (1-5) | I (1-5) | E (1-5) | Score | Mitigation |
|---------|-------------|---------|---------|---------|-------|------------|
| R-001 | [Risk description] | [prob] | [impact] | [effort] | [P×I×E] | [Mitigation strategy] |

**Risk Score Formula**: P (Probability) × I (Impact) × E (Ease of exploitation/occurrence)
**Threshold**: Risks with score ≥ 50 require explicit mitigation plan

---

## Component Breakdown & Sequencing

### Recommended Components
[High-level component identification - detailed plans created in /plan phase]

1. **[Component Name]**
   - Purpose: [What this component does]
   - Dependencies: [What it depends on]
   - Guide Reference: [relevant guide sections]

### Sequencing Strategy
**Phase 1 (Foundation)**: [Components that must be built first]
**Phase 2 (Core Features)**: [Main functionality]
**Phase 3 (Polish)**: [Enhancements and optimization]

---

## Success Metrics

### Business Metrics
- [Metric]: [Target] - [How measured]

### Technical Metrics
- [Metric]: [Target] - [How measured]

### User Satisfaction
- [Metric]: [Target] - [How measured]

---

## Open Questions & Decisions Needed

### [NEEDS CLARIFICATION: Question Category]
- **Question**: [Specific question]
- **Impact**: [Why this matters]
- **Options**: [Possible answers if known]

---

## Review Checklist

Before marking this spec as ready for planning:

- [ ] All core requirements are testable and measurable
- [ ] Pain point alignment score ≥ 0.4
- [ ] ROI analysis shows clear value
- [ ] User scenarios cover primary use cases
- [ ] Technical constraints are clear (WHAT/WHERE/WHY, not HOW)
- [ ] Risks identified and scored
- [ ] No implementation details (code structure, algorithms, function names)
- [ ] Component sequencing considers dependencies
- [ ] Reference guide properly documented (if applicable)
- [ ] [NEEDS CLARIFICATION] markers address all uncertainties

---

## Notes for Planning Phase

**When proceeding to `/plan`**:
1. Review Reference Guide sections: [list key sections]
2. Component plans should reference specific guide workflows/patterns
3. Technical approaches from guide inform HOW, not dictate it
4. Performance targets from guide become testable acceptance criteria

**Guide File Propagation**:
- This specification includes reference to: [guide file path]
- All component plans should maintain this reference
- Task lists should reference specific guide sections for implementation
