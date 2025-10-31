# CLAUDE.md

**Claude Code Starter Kit** - Multi-Agent Orchestration Framework

**Purpose**: Foundational framework for building sophisticated agent-based systems using Claude Code.

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

### Quick Reference

1. **OBSERVE** - What is being asked?
   - Identify task type, key verbs, entity count, constraints

2. **ORIENT** - What context do I need? (MOST CRITICAL PHASE)
   - Check auto-loaded docs first (orchestrator-workflow.md, agent-selection-guide.md, file-operation-protocol.md, research-patterns.md, tool-parallelization-patterns.md)
   - Assess Context Quality: `(Domain × 0.40) + (Pattern × 0.30) + (Dependency × 0.20) + (Risk × 0.10)`
   - Classify task complexity (single-file, multi-component, cross-domain, architectural)
   - Simple context gathering (≥0.8) OR delegate to researcher-lead (<0.5)

3. **DECIDE** - What's my approach?
   - Apply Agent Selection Framework (`.claude/docs/guides/agents/agent-selection-guide.md`)
   - Calculate confidence: `(Domain Match × 0.60) + (Work Type × 0.30) + (Track Record × 0.10)`
   - Agent exists with confidence ≥ 0.5 → Delegate to agent
   - No agent or confidence < 0.5 → Handle directly OR report + recommend creating agent

4. **ACT** - Execute the plan
   - Delegate to agents (if confidence ≥ 0.5) OR handle directly (if no agent/low confidence)
   - Track progress with TodoWrite
   - Verify outputs
   - Communicate clearly

### Example

**Task**: "Research async validation patterns in Pydantic v2"

- **OBSERVE**: Multi-source research needed
- **ORIENT**: Context_Quality = 0.55 (moderate, Pattern_Clarity low) → Delegate to researcher-lead
- **DECIDE**: Multi-source research → researcher-lead coordinates → Confidence: 0.9
- **ACT**: `Task(researcher-lead, "CREATE A RESEARCH PLAN for async validation in Pydantic v2")`

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

## 🎯 Agent Selection Framework

**Core Principle**: Domain-first thinking → File location reveals domain → Domain determines specialist agent.

**Process**:
1. **Identify Domain**: Where does this work belong? (`.claude/**`, `src/**`, `tests/**`, `docs/**`)
2. **Match Work Type**: What kind of work? (research, implementation, review, planning)
3. **Assess Confidence**: How well does the agent fit?
4. **Execute**: High/Medium confidence → delegate | Low/None → handle directly OR recommend creating agent

**Agent Selection Confidence**:

| Level | Range | Criteria | Action |
|-------|-------|----------|--------|
| **High** | 0.7-1.0 | Domain + work type exact match | Delegate immediately |
| **Medium** | 0.5-0.69 | Domain adjacent OR work type overlap | Delegate with monitoring |
| **Low** | <0.5 | No domain/work type match | Orchestrator handles directly OR report + recommend new agent |
| **None** | 0.0 | No appropriate agent exists | Orchestrator handles directly (starter kit default) |

**Complete Framework**: See `.claude/docs/guides/agents/agent-selection-guide.md` for:
- 7 frameworks (domain-first thinking, work type recognition, expertise mapping)
- 30+ scenario examples with decision rationale
- Complete decision trees and disambiguation principles

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
- Follow agent design best practices (`.claude/docs/guides/agents/agent-design-best-practices.md`)
- Use base-agent-pattern for consistency (`.claude/docs/guides/agents/base-agent-pattern.md`)
- Define clear output schema extending `base-agent.schema.json`
- Include prompt evaluation with prompt-evaluator agent

**Resources**:
- **Complete Guide**: `.claude/docs/guides/agents/agent-creation-guide.md`
- **Command Reference**: `.claude/commands/create-agent.md`
- **Templates**: `.claude/templates/agent*.template.md`
- **Standards**: `.claude/docs/agent-standards-extended.md`

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
- File modifications: MAX 5 agents (approval management, file system constraints)
- Research workers: MAX 5 agents (read-only, parallel safe)
- Review agents: 3-5 optimal (diminishing returns beyond 5)
- **Practical limit**: 15-20 agents total across all categories

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

### Proactive Research Triggers

**Automatic delegation based on keywords**:
- `"best practices"`, `"industry standard"`, `"how to"` → researcher-web
- `"analyze patterns"`, `"find all"`, `"how does X work"` → researcher-codebase
- `"library documentation"`, `"API reference"`, `[framework name]` → researcher-library
- `"research"`, `"investigate"`, `"explore options"` → researcher-lead

**Context-driven triggers**:
- Context_Quality < 0.5 + Implementation task → researcher-codebase → code agent
- Unknown patterns (confidence < 0.7) → researcher-codebase → retry
- Security-critical operation → researcher-web (OWASP) → code-reviewer

### Codebase Exploration

**Rule**:
- **1 file**: Orchestrator reads to understand → If implementation needed, check for appropriate agent
  - Agent exists with confidence ≥ 0.5 → Delegate to agent
  - No agent or confidence < 0.5 → Orchestrator handles directly
- **2+ files**: researcher-codebase agent for compressed synthesis

**Why**: Compressed synthesis, pattern finding, reduced tokens. Agent delegation when specialists are available.

### When Orchestrator Handles Work Directly

**Starter Kit Philosophy**: This framework provides orchestration agents (research, OODA, meta). You build implementation agents as needed.

**Orchestrator Executes Directly When**:
1. **No appropriate agent exists** (Agent_Selection_Confidence = 0.0)
   - Example: No code-implementer agent yet → Orchestrator uses Edit/Write tools
2. **Low agent confidence** (Agent_Selection_Confidence < 0.5)
   - Example: Task requires Python skills but only JavaScript agent exists
3. **Coordination work** (inherently orchestrator's role)
   - Example: Synthesizing results from multiple agents

**Orchestrator Delegates When**:
- **Agent exists with confidence ≥ 0.5** for the task domain and work type
- **Even for simple tasks**: Maintain delegation consistency once agents exist

**Evolution Path**: As you create agents with `/create-agent`, more work shifts from direct execution to delegation. This is expected and healthy growth.

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
