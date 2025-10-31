# OODA Loop Framework

**Purpose**: Comprehensive decision-making framework for multi-agent orchestration and task execution.

**Applies To**: Orchestrators (Claude Code primary), worker agents, and agent creation workflows.

**Version**: 1.0.0

---

## Overview

### What is OODA?

**OODA** = **O**bserve, **O**rient, **D**ecide, **A**ct

Originally developed by military strategist John Boyd, the OODA loop is a decision-making framework that emphasizes rapid, iterative learning and adaptation. In multi-agent systems, it provides a structured approach to:

1. **Gathering information** (Observe)
2. **Assessing context and understanding** (Orient)
3. **Selecting optimal approaches** (Decide)
4. **Executing and validating** (Act)

### Why OODA for Multi-Agent Systems?

**Benefits**:
- **Prevents premature action** - Forces context gathering before implementation
- **Reduces rework** - Investing in Orient phase prevents expensive mistakes
- **Enables delegation** - Clear framework for when to delegate vs. execute directly
- **Improves quality** - Structured validation at each phase
- **Facilitates learning** - Iterative loops improve agent performance over time

**Critical Insight**: **Orient phase determines success** - 80% of failures come from insufficient context gathering.

### When to Apply

| Context | Application |
|---------|-------------|
| **Orchestrator** | MANDATORY for all user requests (comprehensive framework) |
| **Worker Agents** | Simplified OODA for task execution (focus on Observe + Act) |
| **Agent Creation** | Full OODA during agent design (agent-architect context) |
| **Research Tasks** | Extended Orient phase with research delegation |

---

## Phase 1: OBSERVE

**Goal**: Understand what is being asked without jumping to solutions.

### Checklist

- [ ] **Read the full request carefully** - Don't skim, internalize the complete context
- [ ] **Identify task type** - Research, implementation, analysis, or combination?
- [ ] **Note key verbs** - "understand", "review", "implement", "explain", "fix", "research"
- [ ] **Count entities** - How many files/components/tasks are involved?
- [ ] **Extract constraints** - Time, scope, quality expectations, dependencies

### Task Type Recognition

| Verb Pattern | Task Type | Typical Next Phase |
|--------------|-----------|-------------------|
| "understand", "explain", "how does" | **Research** | Orient → researcher-lead delegation |
| "implement", "add", "create" | **Implementation** | Orient → complexity assessment |
| "review", "validate", "check" | **Analysis/Review** | Orient → quality framework selection |
| "fix", "debug", "resolve" | **Debugging** | Orient → root cause investigation |
| "refactor", "optimize", "improve" | **Enhancement** | Orient → baseline measurement |

### Entity Count Implications

- **1 file** - Single-file task, potentially simple (direct execution)
- **2-3 files** - Multi-component task, moderate complexity
- **4-10 files** - Cross-domain task, likely needs agent delegation
- **10+ files** - Architectural task, requires planning and coordination

### Examples

**Example 1**: "Research async validation patterns in Pydantic v2"
- **Task Type**: Research (verb: "research")
- **Entities**: 1 topic (Pydantic v2 async validation)
- **Constraints**: None specified (assume comprehensive research)
- **Key Insight**: Multi-source research needed

**Example 2**: "Fix the authentication bug in user_service.py"
- **Task Type**: Debugging (verb: "fix")
- **Entities**: 1 file (user_service.py)
- **Constraints**: Single bug, localized fix
- **Key Insight**: May need to understand auth flow beyond single file

**Example 3**: "Implement user profile editing across frontend and backend"
- **Task Type**: Implementation (verb: "implement")
- **Entities**: 2+ domains (frontend + backend = multiple files)
- **Constraints**: Cross-domain coordination required
- **Key Insight**: Needs architecture planning and multi-agent coordination

---

## Phase 2: ORIENT (MOST CRITICAL)

**Goal**: Assess context quality and gather information needed for confident decision-making.

⚠️ **This phase determines success** - Invest time here to prevent expensive rework in Act phase.

### Context Assessment Priority

**1. Check Auto-Loaded Docs FIRST** (already in context):

Critical documents loaded at startup:
- `orchestrator-workflow.md` - Delegation patterns, OODA coordination
- `agent-selection-guide.md` - Domain-first thinking, 7 frameworks
- `file-operation-protocol.md` - File editing rules
- `research-patterns.md` - Research delegation methodology
- `tool-parallelization-patterns.md` - Optimization patterns

**Why First**: These docs are already in context (zero cost), provide foundational patterns, and answer 80% of common questions.

**2. Assess Context Quality** (self-assessment):

Calculate Context_Quality score (0.0-1.0) using four dimensions:

#### Context Quality Formula

```
Context_Quality = (Domain_Familiarity × 0.40) +
                  (Pattern_Clarity × 0.30) +
                  (Dependency_Understanding × 0.20) +
                  (Risk_Awareness × 0.10)
```

**Dimension Definitions**:

| Dimension | Question | Score Guide |
|-----------|----------|-------------|
| **Domain Familiarity** (0.40) | Do I understand this technology domain? | 1.0 = Expert, 0.5 = Familiar, 0.0 = Unknown |
| **Pattern Clarity** (0.30) | Are there existing patterns to follow? | 1.0 = Clear patterns, 0.5 = Some examples, 0.0 = No patterns |
| **Dependency Understanding** (0.20) | Are integration points clear? | 1.0 = All clear, 0.5 = Some unknowns, 0.0 = Many unknowns |
| **Risk Awareness** (0.10) | Have failure modes been considered? | 1.0 = All risks known, 0.5 = Some risks, 0.0 = Unknown risks |

**Example Calculation**:

Task: "Add async validation to Pydantic models"
- Domain_Familiarity = 0.6 (familiar with Pydantic, less with async patterns)
- Pattern_Clarity = 0.4 (some async examples exist, but not for validation)
- Dependency_Understanding = 0.7 (integration points with existing models clear)
- Risk_Awareness = 0.5 (some risks known: blocking I/O, error handling)

```
Context_Quality = (0.6 × 0.40) + (0.4 × 0.30) + (0.7 × 0.20) + (0.5 × 0.10)
                = 0.24 + 0.12 + 0.14 + 0.05
                = 0.55 (moderate context quality)
```

**3. Classify Task Complexity**

| Complexity Level | Definition | Example |
|------------------|------------|---------|
| **single-file** | Changes confined to 1 file in known domain | Fix typo in README.md |
| **multi-component** | 2-3 related files in same directory/module | Add new API endpoint (route + handler + test) |
| **cross-domain** | 3+ files across multiple directories | User authentication (frontend + backend + db) |
| **architectural** | System-wide changes affecting core abstractions or >5 files | Migrate from sync to async I/O |

**4. Orchestrator Direct Execution** (when no agent available or low agent confidence)

**When to Use**:
- No appropriate agent exists for the task domain
- Available agents have low confidence (<0.5) for this specific task
- Single-file changes in familiar domain (Context_Quality ≥ 0.8) AND no specialist agent

**Decision Logic**:
1. Check for appropriate agent (domain + work type match)
2. If agent exists with confidence ≥ 0.5 → Delegate to agent
3. If no agent OR confidence < 0.5 → Orchestrator handles directly

**Action**: Use Read/Grep/Edit/Write tools directly, reference auto-loaded docs

**Example**:
```
Task: "Add a new field to User model in models/user.py"
- Context_Quality = 0.9 (high - familiar pattern, clear location)
- Agent_Selection_Confidence = 0.0 (no code-implementer agent exists yet)
- Decision: Orchestrator executes directly (no appropriate agent available)
- Action: Read models/user.py, find similar fields, Edit to add new field
```

**Note**: As you build agents with `/create-agent`, this scenario becomes less common. Once a code-implementer agent exists, delegate even simple tasks to maintain consistency.

**5. Complex Context Gathering** (delegate to researcher-lead)

**When to Use**:
- Context_Quality < 0.5 (insufficient understanding)
- Multi-component features spanning 3+ files
- New architectural patterns being introduced
- External integrations or API design
- Security-critical implementations

**Action**: Delegate to researcher-lead for strategic research coordination

### researcher-lead Workflow

**Delegation Pattern**:

```python
Task(
    agent="researcher-lead",
    prompt="CREATE A RESEARCH PLAN for [objective]"
)
```

**Workflow**:
1. researcher-lead returns `delegation_plans` → Orchestrator spawns workers in parallel
2. Check confidence scores → If gaps exist, iterate (max 3 rounds, 0.85 confidence threshold)
3. Synthesize findings → Proceed to DECIDE phase

**Example**:
```
Task: "Research async validation patterns in Pydantic v2"
- Context_Quality = 0.55 (moderate, Pattern_Clarity low)
- Action: Task(researcher-lead, "CREATE A RESEARCH PLAN for async validation in Pydantic v2")
- researcher-lead delegates to:
  - researcher-library (Pydantic v2 official docs)
  - researcher-web (community patterns, best practices)
  - researcher-codebase (existing validation patterns in our code)
```

### Research Depth Scoping

Context_Quality determines worker allocation:

| Context_Quality | Depth Level | Workers | Time Budget |
|-----------------|-------------|---------|-------------|
| **High** (≥0.8) | Light verification | 1 worker | 5-10 min |
| **Moderate** (0.5-0.79) | Standard depth | 2-3 workers | 10-15 min |
| **Low** (<0.5) | Deep investigation | 3-5 workers | 15-20 min |

### Gate Status

Before proceeding to DECIDE phase, assess gate status:

| Status | Condition | Action |
|--------|-----------|--------|
| **READY** | Context_Quality ≥ 0.5 | Proceed to DECIDE phase |
| **GATHERING** | Context_Quality < 0.5, iterations < 3 | Continue ORIENT with research |
| **BLOCKED** | Context_Quality < 0.5, iterations ≥ 3 | Escalate to user for clarification |

---

## Phase 3: DECIDE

**Goal**: Select optimal approach based on gathered context.

### Agent Selection Framework

**Core Principle**: Domain-first thinking → File location reveals domain → Domain determines specialist agent.

**Process**:
1. **Identify Domain** - Where does this work belong? (`.claude/**`, `src/**`, `tests/**`, `docs/**`)
2. **Match Work Type** - What kind of work? (research, implementation, review, planning)
3. **Assess Confidence** - How well does the agent fit?
4. **Delegate or Report** - High/Medium confidence → delegate | Low confidence → suggest agent creation

### Agent Selection Confidence Formula

```
Agent_Selection_Confidence = (Domain_Match × 0.60) +
                             (Work_Type × 0.30) +
                             (Track_Record × 0.10)
```

**Dimension Definitions**:

| Dimension | Question | Score Guide |
|-----------|----------|-------------|
| **Domain_Match** (0.60) | Does agent's domain match task domain? | 1.0 = Exact match, 0.5 = Adjacent, 0.0 = Mismatch |
| **Work_Type** (0.30) | Does agent's work type match task type? | 1.0 = Exact match, 0.5 = Overlap, 0.0 = Different |
| **Track_Record** (0.10) | Has agent succeeded at similar tasks? | 1.0 = Proven, 0.5 = Unproven, 0.0 = Failed before |

### Confidence Levels & Actions

| Level | Range | Criteria | Action |
|-------|-------|----------|--------|
| **High** | 0.7-1.0 | Domain + work type exact match | Delegate immediately |
| **Medium** | 0.5-0.69 | Domain adjacent OR work type overlap | Delegate with monitoring |
| **Low** | <0.5 | No domain/work type match | Report + recommend new agent |

### Decision Examples

**Example 1**: "Add async validation to Pydantic models"
- Domain: `packages/**` (implementation code)
- Work Type: Implementation (adding new functionality)
- Available Agent: `code-implementer` (domain: `packages/**`, type: Creator)
- Calculation: Domain_Match=1.0, Work_Type=1.0, Track_Record=0.9 → 0.97 (High)
- **Decision**: Delegate to code-implementer immediately

**Example 2**: "Research async validation patterns in Pydantic v2"
- Domain: Cross-domain (research, not implementation)
- Work Type: Research (multi-source investigation)
- Available Agent: `researcher-lead` (domain: cross-domain, type: Planner)
- Calculation: Domain_Match=1.0, Work_Type=1.0, Track_Record=0.8 → 0.94 (High)
- **Decision**: Delegate to researcher-lead for research plan creation

**Example 3**: "Optimize SQL query performance in database layer"
- Domain: `packages/database/**`
- Work Type: Enhancement (optimization)
- Available Agents: code-implementer (Creator), code-reviewer (Reviewer)
- Best Match: None (no optimizer agent)
- Calculation: Domain_Match=0.5, Work_Type=0.3, Track_Record=0.0 → 0.39 (Low)
- **Decision**: Report to user + recommend creating `database-optimizer` agent

### Complete Framework Reference

**See**: `.claude/docs/guides/agents/agent-selection-guide.md` for:
- 7 frameworks (domain-first thinking, work type recognition, expertise mapping)
- 30+ scenario examples with decision rationale
- Complete decision trees and disambiguation principles

---

## Phase 4: ACT

**Goal**: Execute the selected approach and validate outcomes.

### Execution Checklist

- [ ] **Delegate to appropriate agents** based on DECIDE phase
- [ ] **Track progress with TodoWrite** for multi-step tasks (3+ steps)
- [ ] **Verify outputs before reporting** to user
- [ ] **Communicate clearly and concisely** (no unnecessary verbosity)

### Delegation Patterns

**Single Agent**:
```python
Task(
    agent="code-implementer",
    prompt="Add async validation to User model in packages/models/user.py"
)
```

**Parallel Multi-Agent** (independent tasks):
```python
# Single message with multiple Task calls
Task(agent="code-implementer", prompt="...")
Task(agent="test-runner", prompt="...")
Task(agent="doc-writer", prompt="...")
```

**Sequential Multi-Agent** (dependencies):
```python
# Step 1
result_1 = Task(agent="researcher-codebase", prompt="...")

# Step 2 (depends on result_1)
result_2 = Task(agent="code-implementer", prompt=f"Use {result_1.findings}...")

# Step 3 (depends on result_2)
result_3 = Task(agent="test-runner", prompt=f"Test {result_2.implementation}...")
```

### Progress Tracking

**When to Use TodoWrite**:
- Tasks with 3+ distinct steps
- Complex workflows with potential blocking dependencies
- Multi-agent coordination requiring state management

**Todo Structure**:
```json
{
  "todos": [
    {
      "content": "Research async validation patterns",
      "activeForm": "Researching async validation patterns",
      "status": "completed"
    },
    {
      "content": "Implement async validation in User model",
      "activeForm": "Implementing async validation",
      "status": "in_progress"
    },
    {
      "content": "Write tests for async validation",
      "activeForm": "Writing tests",
      "status": "pending"
    }
  ]
}
```

### Output Verification

**Before reporting to user**:
1. **Validate agent outputs** - Check status, confidence scores, evidence
2. **Verify file operations** - Read back modified files to confirm changes
3. **Assess quality** - Does output meet user's expectations?
4. **Identify gaps** - Are there missing pieces or follow-up needs?

### Communication Standards

**Concise Reporting**:
- ✅ "Implemented async validation in User model. Added 3 validation methods with error handling."
- ❌ "I successfully completed the task of implementing async validation patterns in the User model by adding three new validation methods including error handling capabilities..."

**Evidence-Based**:
- Include file paths and line numbers
- Show key code snippets when relevant
- Provide confidence scores for decisions
- Document trade-offs made

---

## Complete OODA Examples

### Example 1: Research Task

**User Request**: "Research async validation patterns in Pydantic v2"

**OBSERVE**:
- Task Type: Research (verb: "research")
- Entities: 1 topic (Pydantic v2 async validation)
- Constraints: None specified (assume comprehensive)
- **Conclusion**: Multi-source research needed

**ORIENT**:
- Auto-loaded docs: Check research-patterns.md for delegation methodology
- Context_Quality calculation:
  - Domain_Familiarity = 0.6 (know Pydantic, less familiar with async patterns)
  - Pattern_Clarity = 0.3 (few async validation examples)
  - Dependency_Understanding = 0.5 (unclear how async affects existing models)
  - Risk_Awareness = 0.6 (some async risks known)
  - **Context_Quality = 0.55** (moderate)
- Task Complexity: Cross-domain (research)
- **Conclusion**: Delegate to researcher-lead (Context_Quality < 0.8, multi-source needed)

**DECIDE**:
- Domain: Cross-domain research
- Work Type: Research
- Agent: researcher-lead
- Agent_Selection_Confidence: Domain_Match=1.0, Work_Type=1.0, Track_Record=0.9 → **0.97 (High)**
- **Decision**: Delegate to researcher-lead immediately

**ACT**:
```python
result = Task(
    agent="researcher-lead",
    prompt="CREATE A RESEARCH PLAN for async validation patterns in Pydantic v2. Focus on official documentation, best practices, and integration with existing synchronous validators."
)
```

### Example 2: Implementation Task

**User Request**: "Add a new `email_verified` field to the User model"

**OBSERVE**:
- Task Type: Implementation (verb: "add")
- Entities: 1 file (User model, likely `models/user.py`)
- Constraints: Single field addition
- **Conclusion**: Simple single-file change

**ORIENT**:
- Auto-loaded docs: Check file-operation-protocol.md for edit patterns
- Context_Quality calculation:
  - Domain_Familiarity = 1.0 (know User model structure)
  - Pattern_Clarity = 1.0 (existing fields provide clear pattern)
  - Dependency_Understanding = 0.8 (may need migration script)
  - Risk_Awareness = 0.9 (minimal risk, standard operation)
  - **Context_Quality = 0.94** (high)
- Task Complexity: Single-file
- **Conclusion**: High context quality, check for appropriate agent

**DECIDE**:
- Domain: `packages/models/**`
- Work Type: Implementation (code modification)
- Check for agent: code-implementer agent?
  - **Agent_Selection_Confidence = 0.0** (no code-implementer exists in starter kit)
- **Decision**: Orchestrator executes directly (no appropriate agent available)
- **Note**: If code-implementer existed with confidence ≥ 0.5, would delegate even for this simple task

**ACT**:
```python
# Read User model
user_model = Read("packages/models/user.py")

# Add new field following existing pattern
Edit(
    file_path="packages/models/user.py",
    old_string="email: str",
    new_string="email: str\n    email_verified: bool = False"
)

# Verify change
verify = Read("packages/models/user.py")
# Confirm field added correctly
```

**Evolution Path**: Once you create a code-implementer agent, this same request would delegate:
```python
Task(
    agent="code-implementer",
    prompt="""Add `email_verified` field to User model in packages/models/user.py.

Context: Pattern analysis shows existing boolean fields use `= False` default.
Follow existing pattern: email_verified: bool = False"""
)
```

### Example 3: Cross-Domain Implementation

**User Request**: "Implement user profile editing across frontend and backend"

**OBSERVE**:
- Task Type: Implementation (verb: "implement")
- Entities: 2+ domains (frontend + backend = multiple files)
- Constraints: Cross-domain coordination required
- **Conclusion**: Multi-component architectural task

**ORIENT**:
- Auto-loaded docs: Check orchestrator-workflow.md for multi-agent coordination
- Context_Quality calculation:
  - Domain_Familiarity = 0.7 (know both frontend and backend, but integration unclear)
  - Pattern_Clarity = 0.5 (some profile editing patterns exist, but not comprehensive)
  - Dependency_Understanding = 0.4 (API contract unclear, frontend-backend sync unknown)
  - Risk_Awareness = 0.6 (state management, validation, security concerns)
  - **Context_Quality = 0.59** (moderate)
- Task Complexity: Cross-domain (3+ files, frontend + backend + API)
- **Conclusion**: Need research + planning before implementation

**DECIDE**:
- Domain: Cross-domain (frontend + backend)
- Work Type: Implementation + Planning
- Approach: Research existing patterns → Plan implementation → Delegate to specialists
- **Decision**: Multi-phase approach with researcher-codebase → planning → delegation

**ACT**:
```python
# Phase 1: Research existing patterns
research_result = Task(
    agent="researcher-codebase",
    prompt="Analyze existing profile editing patterns. Find: 1) API endpoints for profile updates, 2) Frontend components for profile forms, 3) Validation patterns used. Return file locations and pattern summary."
)

# Phase 2: Create implementation plan (using research findings)
TodoWrite([
    {"content": "Design API endpoint for profile update", "status": "pending"},
    {"content": "Implement backend profile update handler", "status": "pending"},
    {"content": "Create frontend profile editing component", "status": "pending"},
    {"content": "Add validation on frontend and backend", "status": "pending"},
    {"content": "Write integration tests", "status": "pending"}
])

# Phase 3: Delegate to specialists (parallel where possible)
Task(agent="api-designer", prompt="Design /api/profile/update endpoint based on research...")
Task(agent="code-implementer", prompt="Implement backend profile update handler...")
Task(agent="frontend-implementer", prompt="Create profile editing component...")
```

---

## Integration Patterns

### Orchestrator OODA

**Claude Code (Primary Orchestrator)** uses OODA for:
- Every user request assessment
- Multi-agent coordination decisions
- Research delegation strategies
- Quality gate enforcement

**Key Characteristics**:
- **Comprehensive framework** - All 4 phases with detailed checklists
- **Extended Orient phase** - Invests time in context gathering (80% of effort)
- **Delegation authority** - Can spawn multiple agents in parallel
- **State management** - Tracks progress across multi-step workflows

### Worker Agent OODA (Simplified)

**Worker agents** use simplified OODA for:
- Task-specific execution
- Tool selection decisions
- Output validation

**Key Characteristics**:
- **Observe + Act focus** - Less emphasis on Orient/Decide (orchestrator did this)
- **Domain-specific** - Orient phase checks domain-specific patterns
- **No delegation** - Cannot spawn other agents (orchestrator-only capability)
- **Fast execution** - Optimized for task completion, not planning

**Example (code-implementer)**:
1. **Observe** - Parse implementation requirements, identify files to modify
2. **Orient** - Check code style guide, find similar implementations
3. **Decide** - Select appropriate tools (Read, Edit, Write)
4. **Act** - Implement changes, verify outputs, return structured result

### Agent Creation OODA

**agent-architect** uses OODA for:
- Designing new agents
- Simulating agent behavior
- Selecting tools and frameworks

**Key Characteristics**:
- **Simulation-driven** - Think from target agent's perspective during Orient
- **Research integration** - Uses researcher-* agents for best practices
- **Template compliance** - Decides how to apply agent.template.md structure
- **Quality evaluation** - Acts include self-evaluation against quality matrix

**Example (creating security-scanner agent)**:
1. **Observe** - Requirements: SAST scanning for Python code using Semgrep
2. **Orient** - Research Semgrep patterns, OWASP standards, existing scanner agents
3. **Decide** - Tools: Bash (Semgrep CLI), Read (code context), Write (reports)
4. **Act** - Generate agent definition, create schema, evaluate quality, integrate workflow

---

## Best Practices

### 1. Don't Skip Orient

**Anti-pattern**: Jump from Observe → Act without Orient
```
User: "Fix the bug in user_service.py"
Bad: Read user_service.py → Apply fix immediately
Good: Understand bug context → Check related files → Assess impact → Then fix
```

**Why**: 90% of rework comes from insufficient context in Orient phase.

### 2. Use Context_Quality as Gate

**Pattern**: Calculate Context_Quality before proceeding to Decide
```python
context_quality = assess_context_quality()

if context_quality < 0.5:
    # BLOCKED - need more research
    delegate_to_researcher_lead()
elif context_quality < 0.8:
    # GATHERING - get specific info
    read_relevant_docs()
else:
    # READY - proceed to implementation
    delegate_to_implementer()
```

### 3. Invest in Research Early

**Anti-pattern**: Implement → Realize missing context → Refactor
```
Cost: 10 units (research) + 100 units (implementation) + 50 units (rework) = 160 units
```

**Best practice**: Research → Implement correctly once
```
Cost: 30 units (thorough research) + 100 units (implementation) = 130 units
Savings: 30 units (19% reduction)
```

### 4. Track Multi-Step Workflows

**Pattern**: Use TodoWrite for transparency and state management
```python
# Complex task with dependencies
TodoWrite([
    {"content": "Research patterns", "status": "completed"},
    {"content": "Design API", "status": "in_progress"},
    {"content": "Implement backend", "status": "pending"},
    {"content": "Implement frontend", "status": "pending"},
    {"content": "Write tests", "status": "pending"}
])
```

### 5. Verify Before Reporting

**Pattern**: Read back changes before SUCCESS status
```python
# Make change
Edit(file_path="user.py", old_string="...", new_string="...")

# ALWAYS verify
verification = Read("user.py")
assert new_field in verification, "Field not added correctly"

# Then report
return {"status": "SUCCESS", "evidence": verification}
```

---

## Anti-Patterns to Avoid

### 1. Premature Optimization

**Anti-pattern**: Decide on approach before understanding requirements
```
User: "Make the app faster"
Bad: Immediately start profiling and optimizing
Good: Observe → What's slow? Orient → Measure baseline, identify bottleneck, research solutions
```

### 2. Context-Free Execution

**Anti-pattern**: Execute without domain knowledge
```
User: "Add async validation to Pydantic models"
Bad: Add async def without understanding Pydantic's async patterns
Good: Research Pydantic v2 async support → Understand best practices → Implement correctly
```

### 3. Delegation Without Research

**Anti-pattern**: Delegate to agent without confirming fit
```
Bad: Task(agent="code-implementer", prompt="Research async patterns...")
Good: Task(agent="researcher-lead", prompt="CREATE A RESEARCH PLAN for async patterns...")
```

### 4. Ignoring Confidence Scores

**Anti-pattern**: Proceed despite low confidence
```
Agent_Selection_Confidence = 0.3 (Low)
Bad: Delegate anyway and hope for the best
Good: Report to user: "No suitable agent found. Recommend creating async-validator agent."
```

### 5. Skipping Verification

**Anti-pattern**: Report SUCCESS without verifying changes
```
Bad: Edit(file) → return SUCCESS immediately
Good: Edit(file) → Read(file) to verify → return SUCCESS with evidence
```

---

## Quick Reference Card

### OODA in 60 Seconds

| Phase | Key Question | Action | Time |
|-------|--------------|--------|------|
| **OBSERVE** | What is being asked? | Identify task type, entities, constraints | 5-10 sec |
| **ORIENT** | What context do I need? | Calculate Context_Quality, gather info | 60-80% of time |
| **DECIDE** | What's my approach? | Apply Agent Selection Framework | 5-10 sec |
| **ACT** | Execute & verify | Delegate, track, validate, report | 20-30% of time |

### Context Quality Gate

```
Context_Quality ≥ 0.8 → Handle directly
Context_Quality 0.5-0.79 → Research specific gaps
Context_Quality < 0.5 → Delegate to researcher-lead
```

### Agent Selection

```
Agent_Confidence ≥ 0.7 → Delegate immediately
Agent_Confidence 0.5-0.69 → Delegate with monitoring
Agent_Confidence < 0.5 → Report + recommend new agent
```

---

## Related Documentation

- **`.claude/docs/orchestrator-workflow.md`** - Multi-agent coordination patterns
- **`.claude/docs/guides/agents/agent-selection-guide.md`** - 7 frameworks for agent selection
- **`.claude/docs/guides/patterns/research-patterns.md`** - Research delegation methodology
- **`.claude/docs/guides/patterns/tool-parallelization-patterns.md`** - Parallel execution patterns
- **`.claude/docs/agent-standards-runtime.md`** - Agent runtime behavior and contracts

---

**Framework Version**: 1.0.0
**Last Updated**: 2025-10-31
**Applies To**: All agents in Claude Code Starter Kit ecosystem
