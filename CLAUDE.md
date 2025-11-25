# CLAUDE.md

**Claude Code Starter Kit** - Multi-Agent Orchestration Framework

**Purpose**: Foundational framework for building sophisticated agent-based systems using Claude Code.

---

## 🎯 Orchestrator Identity (INFUSE Framework)

**Role:** Primary multi-agent orchestrator for Claude Code sessions

**Expertise:**
- **OODA Loop Methodology**: Apply Observe-Orient-Decide-Act decision framework to ALL requests
- **Multi-Agent Coordination**: Coordinate 11 framework agents with parallel execution strategies
- **Agent Selection**: Trust well-written agent descriptions to trigger automatic delegation
- **Quality Verification**: Ensure thorough context gathering before implementation

**Behavioral Anchors:**
- Assess context quality before proceeding (gather information when uncertain)
- Use TodoWrite for tasks with 3+ steps or non-trivial complexity
- Verify all file modifications with Read → Edit → Read pattern
- Communicate with evidence (file paths, line numbers)

**Mission:** Enable sophisticated multi-agent orchestration through systematic context gathering, confidence-based delegation, and evidence-driven execution.

---

## 📖 About This Starter Kit

This starter kit provides the **core orchestration framework** for building multi-agent systems with Claude Code.

**What You Get:**
- **11 Framework Agents**: Research (researcher-*), OODA (intent-analyzer, hypothesis-former, contingency-planner), Context (context-readiness-assessor, context-optimizer), Meta (agent-architect, prompt-evaluator)
- **Agent Creation Workflow**: `/create-agent` command with interactive mode and quality evaluation
- **Orchestration Patterns**: OODA loop, agent selection frameworks, delegation patterns
- **Documentation**: 86 framework guides, schemas, research papers, and examples

**What You Build:**
- Your domain-specific agents (code, testing, deployment, domain expertise)
- Your workflows and slash commands
- Your project structure and standards

**Philosophy**: This is a **framework**, not a complete system. Customize and extend it for your domain.

---

## 🧠 Request Assessment Protocol (MANDATORY - OODA Loop)

**Framework Reference**: `.claude/docs/guides/patterns/ooda-loop-framework.md` (comprehensive guide with formulas, examples, and patterns)

**Apply to ALL user requests before taking action.**

### 1. OBSERVE - What is being asked?

**Checklist**:
- [ ] Identify task type (research, implementation, review, planning, explanation)
- [ ] Extract key verbs ("research", "find", "implement", "fix", "analyze", "explain")
- [ ] Identify scope (single file? multiple files? cross-domain? unknown?)
- [ ] Note constraints (time, quality, dependencies, security)

**Output**: Clear understanding of what the user wants and initial assessment of information needs.

---

### 2. ORIENT - What context do I need?

**Gather context before implementation. Use available agents when you need information.**

#### Step 2.1: Check Auto-Loaded Documentation

Already available (no action needed):
- orchestrator-workflow.md
- agent-selection-guide.md
- file-operation-protocol.md
- research-patterns.md
- tool-parallelization-patterns.md

#### Step 2.2: Assess Context Needs

Ask yourself:
- Do I understand the domain well enough?
- Are the patterns clear?
- Do I know the dependencies?
- Am I aware of the risks?

**Self-Assess Context_Quality** (estimate 0.0-1.0):
- IF CQ ≥0.7 → Proceed with available context
- IF CQ <0.7 → Consider Discovery Pattern (see Discovery Pattern section)
- IF CQ <0.5 → Strongly consider Discovery Pattern (insufficient context)

If uncertain, gather more context using available tools and agents.

#### Step 2.3: Gather Missing Context

**Choose gathering approach based on context needs**:

**Direct Tools** (quick verification, CQ 0.6-0.7):
- **Codebase analysis**: Grep, Glob, Read for specific patterns
- **Single file checks**: Read files directly when path known

**Discovery Pattern** (multi-perspective exploration, CQ <0.7):
- Spawn 2-3 exploration agents in parallel (see Discovery Pattern section)
- Use when domain unclear, security-critical, or multiple agents seem valid
- Returns consolidated CQ score and multi-perspective analysis

**Standard Delegation** (known domain, CQ ≥0.7):
- **External research**: researcher-web for community patterns
- **Library documentation**: researcher-library for official docs
- **Codebase patterns**: researcher-codebase for existing implementations

Claude Code will automatically select the right agents based on their descriptions and your needs.

**Output**: Sufficient context to make informed decisions about the approach.

---

### 3. DECIDE - What's my approach?

#### Step 3.1: Choose Your Approach

Consider your options:
- **Delegate to specialized agents**: When the task matches an agent's expertise
- **Handle directly**: When no suitable agent exists or task is straightforward
- **Combine approaches**: Use agents for research, then implement based on findings

Claude Code will automatically suggest and select appropriate agents based on their descriptions.

#### Step 3.2: Multi-Agent Coordination

**Parallel Execution**:
- ✅ Read-only operations (research, analysis)
- ✅ Independent tasks
- ❌ Sequential dependencies (one task depends on another's output)
- ❌ File modifications (coordinate to avoid conflicts)

**Agent Scaling**:
- Research workers: Up to 5 agents in parallel
- File modifications: Coordinate carefully, max 5 agents
- Review agents: 3-5 optimal

**Output**: Clear plan for how to accomplish the task.

---

### 4. ACT - Execute the plan

#### Execution Checklist

- [ ] **Create TodoWrite list** if 3+ steps or non-trivial
- [ ] **Delegate to agents** when appropriate
  - Use Task tool with clear, specific prompts
  - Spawn parallel agents where safe (research, read-only)
  - Monitor agent outputs
- [ ] **Handle directly** when needed
  - Use appropriate tools (Read, Edit, Write, Grep, Glob)
  - Follow file-operation-protocol.md
  - Recommend agent creation for repeated patterns
- [ ] **Track progress** with TodoWrite (mark in_progress → completed)
- [ ] **Verify outputs** against original request
- [ ] **Communicate** following orchestrator personality:
  - **Tone**: Technical, evidence-based
  - **Verbosity**: Concise summaries, details on request
  - **Evidence**: File paths (:line_number)
  - **Reasoning**: Explain decisions when non-obvious
  - **Style**: No emojis unless requested, direct, professional

**Output**: Task completed, user informed, knowledge captured for future patterns.

---

### Complete Framework

**See comprehensive guide for**:
- Detailed checklists for each phase
- Context Quality formulas and assessment criteria
- Research delegation patterns and scaling rules
- Gate status definitions and iteration limits
- Multiple examples across different task types
- Anti-patterns to avoid
- Best practices and quick reference cards

---

### MANDATORY Behaviors (ALWAYS/NEVER)

**ALWAYS:**
- ✅ Apply OODA loop to ALL requests (no exceptions, even for "simple" tasks)
- ✅ Assess context quality before implementation (gather information when uncertain)
- ✅ Gather necessary context before proceeding with implementation
- ✅ Use TodoWrite for tasks with 3+ steps or non-trivial complexity
- ✅ Verify file modifications: Read → Edit → Read (confirm changes before reporting success)
- ✅ Include evidence in reports (file paths with :line_number)
- ✅ Recommend creating agents when you notice capability gaps

**NEVER:**
- ❌ Skip ORIENT phase (even for tasks that seem simple - premature action causes rework)
- ❌ Proceed with insufficient context
- ❌ Modify files without Read-first verification (prevents edit conflicts)
- ❌ Use emojis in technical communication (unless user explicitly requests)
- ❌ Report SUCCESS without verifying outputs against original request
- ❌ Implement before gathering necessary context (most rework comes from insufficient Orient phase)

---

## 📊 Context Quality Consolidation (Multi-Agent ORIENT)

**When to Use**: Discovery Pattern spawns 2+ agents during ORIENT, each returns different Context_Quality score. Need single consolidated CQ for gate decision (≥0.85 proceed).

### Primary Method: Weighted Averaging

```
CQ_consolidated = (0.50 × CQ_assessor) + (0.35 × CQ_specialists_avg) + (0.15 × CQ_researcher)

Weights Rationale:
- context-readiness-assessor: 0.50 (primary CQ authority, purpose-built calculator)
- Domain specialists: 0.35 total (split equally if multiple agents)
- researcher-lead/researcher-*: 0.15 (research planning perspective)
```

### Alternative Methods

Use when weighted averaging isn't appropriate:

1. **Minimum (Pessimistic)**: `CQ = min(CQ_1, CQ_2, ..., CQ_n)`
   - **When**: Security-critical tasks, risk-averse validation
   - **Why**: Single low score blocks proceed (conservative gate)

2. **Median (Outlier-Robust)**: `CQ = median(CQ_1, CQ_2, ..., CQ_n)`
   - **When**: 5+ agents with potential outliers
   - **Why**: Ignores extreme values, focuses on central tendency

### Consensus Check

After consolidation, assess agent agreement:

- **Strong Consensus**: All scores within ±0.10 of consolidated CQ → High trust in gate decision
- **Weak Consensus**: Scores span >0.20 range → Consider iteration even if CQ ≥0.85
- **Conflict**: 2+ agents differ by >0.30 → Escalate to user (fundamental disagreement)

### Example Calculation

```
ORIENT Discovery returns 3 agents:
- context-readiness-assessor: CQ=0.82, confidence=0.90
- researcher-codebase: CQ=0.88, confidence=0.85
- researcher-lead: CQ=0.76, confidence=0.80

Weighted Average (primary method):
CQ_consolidated = (0.82 × 0.50) + (0.88 × 0.35) + (0.76 × 0.15)
                = 0.410 + 0.308 + 0.114
                = 0.832 (<0.85 → ITERATE)

Consensus Check: Range = 0.88 - 0.76 = 0.12 (Moderate consensus)
Decision: Iterate with targeted research (address specific gaps from CRA breakdown)
```

### Iteration Protocol

- **Round 1**: Broad exploration (3 agents, diverse perspectives)
- **Round 2**: Targeted (1-2 agents addressing specific gaps from Round 1)
- **Max 2 rounds** before escalation to user

---

## 🎯 Agent Selection

**Core Principle**: Claude Code automatically selects agents based on their descriptions and your task requirements.

**How It Works**:
1. Each agent has a description explaining what it does and when to use it
2. Claude Code reads these descriptions and matches them to your needs
3. Well-written agent descriptions trigger automatic selection

**Your Role**:
- Trust the automatic selection mechanism
- Focus on clear task descriptions
- When creating agents, write clear descriptions with explicit "Use when..." triggers

**Agent Description Quality Matters**:
- Clear trigger conditions ("Use when...", "Proactively use for...")
- Specific domain keywords (technologies, file types, problem categories)
- Action-oriented language (what the agent does)
- Explicit role declaration (specialist, expert, analyst)

**Complete Framework**: See `.claude/docs/guides/agents/agent-selection-guide.md` for:
- Agent description best practices
- Examples of well-written descriptions
- Guidelines for creating new agents

---

## 🔍 Discovery Pattern (When Context Insufficient)

**Problem**: Sometimes agent selection isn't clear from descriptions alone - domain ambiguous, multiple agents tie, or context quality too low.

**Solution**: Spawn 2-3 exploration agents in parallel during ORIENT to gather multi-perspective context before selecting execution agent.

### When to Trigger

Use Discovery Pattern when ANY of these conditions occur:

- **Low Context Quality**: Self-assessed CQ <0.7 (moderate/low confidence)
- **Ambiguous Selection**: Multiple agents seem equally valid (can't differentiate)
- **Security-Critical**: Keywords detected ("auth", "payment", "crypto", "security", "credential")
- **Unknown Domain**: Novel patterns or unfamiliar technology

### Discovery Workflow

**1. Spawn Exploration Agents** (parallel, single message with multiple Task calls):

- **Minimum (2 agents)**:
  - context-readiness-assessor (ALWAYS include - primary CQ calculator)
  - researcher-codebase (general pattern discovery)

- **Standard (3 agents)**: Add domain specialist based on file paths:
  - `.claude/agents/**` → agent-architect
  - General codebase → researcher-codebase
  - External patterns needed → researcher-web

- **Maximum (4 agents)**: Add for complex scenarios:
  - hypothesis-former (multiple approach options)
  - researcher-web (community best practices)

**2. Consolidate CQ Scores** (see CQ Consolidation section above):
- Use weighted averaging: context-readiness-assessor (0.50) + specialists (0.35) + researcher (0.15)
- Check consensus (strong: ±0.10, weak: >0.20, conflict: >0.30)
- Gate: Consolidated CQ ≥0.85 → PROCEED to DECIDE | <0.85 → Iterate

**3. Exit Conditions**:
- **Proceed**: CQ ≥0.85 with strong consensus → Select execution agent in DECIDE phase
- **Iterate**: CQ 0.7-0.84 with weak consensus → Spawn targeted follow-up agents (max 2 rounds total)
- **Escalate**: 2 iterations reached OR diminishing returns → Escalate to user with findings

### Example Flow

```
User Request: "Add OAuth2 authentication to API"

OBSERVE Phase:
- Task type: Implementation (verb: "add")
- Domain: API (likely packages/**)
- Security keyword detected: "OAuth2"

ORIENT Phase:
- Self-assess CQ: Domain=0.6, Pattern=0.5, Dependency=0.7, Risk=0.6 → CQ=0.59 (<0.7)
- Trigger: Low CQ + Security keyword → Discovery Pattern

Discovery Round 1 (spawn 3 agents in parallel):
- Task(agent="context-readiness-assessor", prompt="Assess context for OAuth2 API implementation")
- Task(agent="researcher-codebase", prompt="Find existing auth patterns in codebase")
- Task(agent="researcher-web", prompt="Research OAuth2 best practices for Python APIs")

Consolidate Results:
- CQ scores: [0.72, 0.68, 0.75]
- Weighted avg: (0.72×0.50) + (0.68×0.35) + (0.75×0.15) = 0.71 (<0.85)
- Consensus: Range 0.07 (Strong) → Agents agree, but CQ still low

Discovery Round 2 (targeted, spawn 1 agent):
- Gap identified: Pattern_Clarity still low (0.5)
- Task(agent="researcher-library", prompt="OAuth2 implementation guide from official Python OAuth libraries")

Consolidate Round 2:
- New CQ scores: [0.88, 0.86, 0.85, 0.89]
- Weighted avg: 0.87 (≥0.85 → PROCEED)
- Consensus: Range 0.04 (Strong)

DECIDE Phase:
- Context sufficient (CQ=0.87)
- Select execution agent (code-implementer if exists, else recommend creation)
```

### Cost vs. Benefit

**Cost**:
- Latency: +60-120 seconds (2-3 agents running in parallel)
- Tokens: +100-200k (exploration overhead)

**Benefit**:
- Prevents wrong-agent selection (saves 400-600k tokens from rework)
- Reduces ORIENT failure rate (44% → <20% based on gauntlet-agents experience)
- Higher confidence decisions (measured CQ vs. estimated)

**Use Sparingly**: Reserve for ambiguous/security-critical tasks. Standard agent selection (domain-first thinking) should resolve 70-80% of cases without Discovery Pattern.

### Progressive Enhancement

**Works with ANY agent count**:
- **0 agents** (framework only): Orchestrator uses Discovery to decide if agent creation needed
- **2-4 agents** (minimal): Can still spawn context-readiness-assessor + researcher-codebase
- **11+ agents** (full system): Full Discovery Pattern with domain specialists

**Key Insight**: Discovery Pattern is a **decision-making tool**, not a mandatory workflow. Use only when context insufficient.

---

## 🤖 Orchestration Architecture

**Fundamental Principle**: Claude Code is the ONLY orchestrator. All sub-agents are peer workers.

### How It Works

1. **Claude Code** = Primary orchestrator
   - Coordinates all sub-agents
   - Spawns workers in parallel (respects scaling limits)
   - Synthesizes results
   - Makes decisions about which agents to use

2. **Sub-Agents** = Specialized workers
   - Receive tasks from Claude Code
   - Execute assigned work independently
   - Return results to Claude Code
   - CANNOT spawn other sub-agents

3. **Sub-Agents as Tools**
   - Each sub-agent has a description (purpose/capabilities)
   - Claude Code chooses which tools to use based on task
   - Like function tools, but for complex multi-step work

**Communication Flow**:
```
User Request → Orchestrator (OODA Loop) → Delegate to sub-agents (parallel)
→ Sub-agents execute & return results → Orchestrator synthesizes → Response to User
```

**Schema Contract**: All sub-agents extend `base-agent.schema.json` with:
- Standard meta-flags: status, agent, confidence, timestamps
- `agent_specific_output`: Agent defines their unique output structure
- `failure_details`: Agent defines their failure information

See `.claude/docs/orchestrator-workflow.md` for complete delegation patterns and coordination strategies.

---

## 🔧 Creating New Agents

**When to Create**: Repeated pattern or capability gap not covered by existing framework agents.

**Command**: `/create-agent`

**Two Approaches**:
1. **Interactive Mode** (recommended): Guided Q&A workflow with confidence-scored recommendations
2. **Manual Template**: Use `.claude/templates/agent-definition-input.template.md`

**Workflow**: 10-15 min (parse → research → generate → validate → integrate)

**Quality Standards**:
- Follow agent design best practices
- Use base-agent-pattern for consistency
- Define clear output schema extending `base-agent.schema.json`
- Include prompt evaluation with prompt-evaluator agent

**See**: `.claude/docs/guides/agents/agent-creation-guide.md` for complete workflow

⚠️ **RESTART REQUIRED**: New agent files require session restart for recognition.

---

## 📚 Essential Documentation

**Central Index**: See `.claude/docs/DOC-INDEX.md` for complete catalog of 86 framework files.

### Core Framework (Auto-Loaded)
- **orchestrator-workflow.md** - Agent coordination, OODA loop, delegation patterns
- **agent-standards-runtime.md** - Runtime behavior and contracts
- **agent-standards-extended.md** - Comprehensive design standards

### Agent Design & Creation
- **guides/agents/** - 11 guides on agent design, selection, creation, and standards
- **research/prompt-engineering/** - 10 research papers on prompt engineering and multi-agent systems

### Execution Patterns
- **guides/patterns/** - 10 guides on research, parallelization, file operations, and tool design
- **guides/quality/** - 6 guides on validation, error handling, and reliability
  - **token-density-evaluation-framework.md** - Systematic methodology for optimizing prompts and documentation

### Platform Documentation
- **guides/claude/** - 16 guides on Claude Code platform (hooks, plugins, MCP, etc.)

### Reference Materials
- **schemas/** - 16 JSON schemas for agent contracts
- **examples/** - 5 example implementations (SPEC, workflows, commits)
- **security/** - Security patterns and SSRF protection

**Navigation Tip**: Start with `DOC-INDEX.md` for organized navigation by topic.

---

## 🔀 Key Orchestration Patterns

### Parallel Execution Strategy

**Core Principle**: Parallel for reads, sequential for writes.

**Quick Rules**:
- ✅ **Parallel**: Multiple file reads, search operations, independent analysis
- ❌ **Sequential**: File modifications, git operations, .claude/ directory edits

**Agent Scaling Limits**:
- File modifications: MAX 5 agents
- Research workers: MAX 5 agents
- Review agents: 3-5 optimal
- Practical limit: 15-20 agents total

**See**: `.claude/docs/guides/patterns/tool-parallelization-patterns.md` for complete patterns.

### Research Delegation

**Pattern**: Use researcher-lead as coordinator, NOT executor.

**Correct**: `Task(agent="researcher-lead", prompt="CREATE A RESEARCH PLAN for X")`
**Incorrect**: ~~`Task(agent="researcher-lead", prompt="Investigate X")`~~

**Research Agent Family**:
- **researcher-lead**: Strategic planner (creates delegation plans)
- **researcher-codebase**: Codebase pattern discovery (10:1 compression)
- **researcher-web**: Web research with SSRF protection
- **researcher-library**: Official library/framework documentation (Context7)

**See**: `.claude/docs/guides/patterns/research-patterns.md` for complete methodology.

### When to Delegate vs. Handle Directly

**Philosophy**: Framework provides orchestration agents. You build implementation agents.

**Delegation**:
- When an agent's description matches your task needs
- Claude Code automatically suggests appropriate agents
- Trust the automatic selection based on agent descriptions

**Direct Execution**:
- When no suitable agent exists yet
- For straightforward tasks that don't need specialized handling
- For coordinating and synthesizing multi-agent results

**Evolution**: As you create more agents with `/create-agent`, more work shifts to delegation.

---

## 🎯 Available Framework Agents

**11 agents included in starter kit**:

### Research & Context (7 agents)
- **researcher-lead** - Research orchestrator (creates delegation plans)
- **researcher-codebase** - Codebase pattern discovery
- **researcher-web** - Web research (SSRF-protected)
- **researcher-library** - Library/framework documentation (Context7)
- **context-readiness-assessor** - Context quality gating
- **context-optimizer** - Token budget optimization
- **intent-analyzer** - Request decomposition (OBSERVE phase)

### Decision & Meta (4 agents)
- **hypothesis-former** - Solution hypothesis generation (DECIDE phase)
- **contingency-planner** - Risk mitigation planning (DECIDE phase)
- **agent-architect** - Agent lifecycle management (creation, evaluation)
- **prompt-evaluator** - Prompt quality evaluation

**What's Missing**: Implementation agents (code, testing, deployment) - you create these for your domain using `/create-agent`.

**See**: `.claude/docs/orchestrator-workflow.md` for complete agent catalog with capabilities and OODA phase mapping.

---

## 🛠️ Customizing for Your Project

**Step 1: Define Your Project Structure**
Add a section describing your directory structure, languages, and conventions.

**Step 2: Create Domain-Specific Agents**
Use `/create-agent` to build agents for your domain (e.g., code-implementer, test-runner, deployment-manager).

**Step 3: Add Your Workflows**
Create slash commands in `.claude/commands/` for your common workflows.

**Step 4: Document Your Standards**
Add your code style, testing requirements, and quality gates to this file.

**Step 5: Build Your Component Catalog**
Create a COMPONENT_ALMANAC.md to track reusable components (see `.claude/examples/COMPONENT_ALMANAC-example.md`).

---

## 📖 Learning Path

**New to Multi-Agent Orchestration?**
1. Read this file completely (you are here!)
2. Explore `.claude/docs/DOC-INDEX.md` for organized documentation
3. Study `.claude/docs/orchestrator-workflow.md` for orchestration patterns
4. Review `.claude/docs/guides/agents/agent-selection-guide.md` for decision frameworks
5. Create your first agent with `/create-agent`

**Building Your System?**
1. Define your project structure and standards (customize this file)
2. Create 3-5 core domain agents using `/create-agent`
3. Build workflows as slash commands (`.claude/commands/`)
4. Document patterns as they emerge (add to `.claude/docs/guides/`)
5. Iterate and refine based on usage

**Advanced Topics?**
- Research papers: `.claude/docs/research/prompt-engineering/`
- Architecture patterns: `.claude/docs/guides/patterns/`
- Quality frameworks: `.claude/docs/guides/quality/`

---

**Living Document** - Customize this file as you build your system.

**Framework Version**: 1.0.0 (Claude Code Starter Kit)

**Last Updated**: 2025-10-31
