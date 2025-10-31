# Claude Code Starter Kit - .claude Directory

This directory contains the core orchestration framework for building multi-agent systems with Claude Code.

---

## 📁 Directory Structure

```
.claude/
├── agents/                    # Framework agent definitions (11 agents)
│   ├── researcher-*.md        # Research & context agents (4)
│   ├── context-*.md           # Context quality agents (2)
│   ├── intent-analyzer.md     # OODA: OBSERVE phase
│   ├── hypothesis-former.md   # OODA: DECIDE phase
│   ├── contingency-planner.md # OODA: DECIDE phase
│   ├── agent-architect.md     # Meta: Agent creation
│   └── prompt-evaluator.md    # Meta: Prompt quality
│
├── commands/                  # Slash commands
│   └── create-agent.md        # /create-agent workflow
│
├── templates/                 # Project templates
│   ├── agent-*.template.md    # Agent creation templates
│   ├── spec-template.md       # Feature specification
│   ├── plan-template.md       # Implementation planning
│   ├── task-template.md       # Task breakdown
│   └── component-almanac-template.md  # Component catalog
│
├── hooks/                     # Session lifecycle hooks
│   └── startup-eval.py        # Startup configuration
│
├── docs/                      # Framework documentation (83 files)
│   ├── orchestrator-workflow.md        # Core orchestration guide
│   ├── agent-standards-runtime.md      # Runtime behavior
│   ├── agent-standards-extended.md     # Design standards
│   ├── DOC-INDEX.md                    # Complete documentation catalog
│   │
│   ├── guides/
│   │   ├── agents/            # 11 agent design guides
│   │   ├── patterns/          # 10 execution patterns
│   │   ├── quality/           # 6 quality frameworks
│   │   └── claude/            # 16 platform docs
│   │
│   ├── research/
│   │   └── prompt-engineering/    # 10 research papers
│   │
│   ├── schemas/               # 16 agent JSON schemas
│   ├── examples/              # 5 example implementations
│   └── security/              # Security patterns
│
└── README.md                  # This file
```

---

## 🤖 Framework Agents

The starter kit includes **11 production-ready agents** for orchestration:

### Research & Context (7 agents)

**researcher-lead** - Research orchestration
- Creates delegation plans for multi-source research
- Coordinates researcher-* worker agents
- Synthesizes findings with confidence scoring
- Keyword triggers: "research", "investigate", "explore options"

**researcher-codebase** - Codebase pattern discovery
- Three-phase search strategy (Discovery → Mapping → Validation)
- 10:1 compression ratio for findings
- Progressive narrowing with 'good enough' termination
- Use for: Pattern analysis, architecture understanding, dependency mapping

**researcher-web** - Web research with SSRF protection
- 156-domain whitelist for security
- Progressive search refinement (3 rounds max)
- Source quality scoring (authoritative/supporting/rejected)
- Use for: Best practices, industry standards, external research

**researcher-library** - Library/framework documentation
- Context7 MCP integration for authoritative sources
- Version-specific API signatures and patterns
- 15:1 compression ratio
- Use for: Library APIs, migration guides, official documentation

**context-readiness-assessor** - Context quality gating
- Calculates Context_Quality score (0.0-1.0)
- Coordinates up to 10 research agents for missing context
- Enforces quality gates before implementation
- Manages iterative refinement (max 3 iterations)

**context-optimizer** - Token budget optimization
- Analyzes context usage patterns
- Identifies redundancy and optimization opportunities
- ROI analysis for context investments
- Three optimization modes: targeted, group, ecosystem

**intent-analyzer** - Request decomposition (OBSERVE phase)
- Decomposes complex requests into structured task graphs
- Dependency analysis for task ordering
- Multi-intent detection and disambiguation
- Feeds into OODA loop orchestration

### Decision & Meta (4 agents)

**hypothesis-former** - Solution hypothesis generation (DECIDE phase)
- Generates 2-5 ranked solution hypotheses
- DCS scoring: (Task_Complexity × 0.4) + (Agent_Fit × 0.3) + (Context_Quality × 0.2) + (Cost_Benefit × 0.1)
- Multi-criteria feasibility analysis
- Trade-off matrices for confident decisions

**contingency-planner** - Risk mitigation planning (DECIDE phase)
- Identifies 3-5 failure modes per hypothesis
- Probability × impact risk scoring (0.0-1.0)
- Generates 2-3 fallback strategies per failure mode
- Adaptive retry plans with exponential backoff

**agent-architect** - Agent lifecycle management
- Interactive agent creation workflow
- 9-criterion quality matrix evaluation
- Simulation-driven development
- Automatic CLAUDE.md integration
- Direct file modification capability

**prompt-evaluator** - Prompt quality evaluation
- 4 evaluation frameworks (structural/engineering/tokens/testing)
- Evidence-based recommendations
- Anti-pattern detection
- Quantified optimization opportunities

---

## 📚 Documentation Navigator

### Getting Started
1. **Read**: `../CLAUDE.md` - Core orchestration framework
2. **Explore**: `docs/DOC-INDEX.md` - Complete documentation catalog
3. **Learn**: `docs/orchestrator-workflow.md` - Orchestration patterns
4. **Practice**: `docs/guides/agents/agent-creation-guide.md` - Create agents

### Essential Guides (Auto-Loaded)
- `docs/orchestrator-workflow.md` - Agent coordination, OODA loop
- `docs/guides/agents/agent-selection-guide.md` - Domain-first thinking
- `docs/guides/patterns/file-operation-protocol.md` - File editing rules
- `docs/guides/patterns/research-patterns.md` - Research delegation
- `docs/guides/patterns/tool-parallelization-patterns.md` - Optimization

### Agent Design
- `docs/guides/agents/agent-design-best-practices.md` - Design patterns
- `docs/guides/agents/base-agent-pattern.md` - Standard structure
- `docs/agent-standards-extended.md` - Comprehensive standards
- `docs/schemas/base-agent.schema.json` - Output schema contract

### Execution Patterns
- `docs/guides/patterns/ooda-loop-framework.md` - OODA decision-making
- `docs/guides/patterns/research-patterns.md` - Research coordination
- `docs/guides/patterns/infuse-framework.md` - Prompt engineering
- `docs/guides/quality/validation-patterns.md` - Quality gates

---

## 🚀 Quick Start

### Create Your First Agent

```bash
# Interactive mode (recommended)
/create-agent

# Manual mode
cp templates/agent-definition-input.template.md my-agent-input.md
# Edit my-agent-input.md with your agent details
/create-agent --create-definition my-agent-input.md
```

**⚠️ Restart Required**: After creating agents, restart Claude Code for recognition.

### Customize the Framework

1. **Add domain agents**: Create code-implementer, test-runner, deployment-manager
2. **Build workflows**: Add slash commands to `commands/`
3. **Document patterns**: Add guides to `docs/guides/`
4. **Track components**: Create COMPONENT_ALMANAC.md using template

---

## 🎯 Agent Selection Logic

The orchestrator uses **domain-first thinking** to select agents:

### Selection Formula
```
Agent_Selection_Confidence = (Domain_Match × 0.60) + (Work_Type × 0.30) + (Track_Record × 0.10)
```

### Confidence Thresholds
- **0.7-1.0 (High)**: Delegate immediately
- **0.5-0.69 (Medium)**: Delegate with monitoring
- **<0.5 (Low)**: Orchestrator handles directly OR recommend new agent
- **0.0 (None)**: No appropriate agent - orchestrator executes

### Delegation Decision Tree

```
User Request
    ↓
Check for matching agent (domain + work type)
    ↓
Agent exists?
    ├─ Yes → Calculate confidence
    │           ↓
    │       Confidence ≥ 0.5?
    │           ├─ Yes → DELEGATE to agent
    │           └─ No → HANDLE DIRECTLY (log for future agent)
    │
    └─ No → HANDLE DIRECTLY (recommend creating agent)
```

---

## 🔀 Orchestration Patterns

### OODA Loop (Observe-Orient-Decide-Act)

**OBSERVE** - What is being asked?
- intent-analyzer decomposes request
- Identifies task type, entities, constraints

**ORIENT** - What context do I need?
- context-readiness-assessor calculates Context_Quality
- Delegates to researcher-* agents if needed (<0.5 quality)
- Loads relevant documentation

**DECIDE** - What's my approach?
- hypothesis-former generates solution options
- contingency-planner identifies risks
- Agent selection framework chooses executor

**ACT** - Execute the plan
- Delegate to agents (if confidence ≥ 0.5)
- OR handle directly (if no agent/low confidence)
- Track progress, verify outputs, communicate

### Research Delegation

**Pattern**: researcher-lead coordinates workers

```python
# Correct pattern (coordinator mode)
Task(agent="researcher-lead", prompt="CREATE A RESEARCH PLAN for async validation in Pydantic v2")

# Incorrect pattern (triggers execution instead of planning)
# Task(agent="researcher-lead", prompt="Investigate async validation")
```

**Research Flow**:
1. researcher-lead creates delegation plan
2. Orchestrator spawns worker agents in parallel (max 5)
3. Workers (researcher-codebase, researcher-web, researcher-library) execute research
4. Workers return compressed findings (10:1 ratio)
5. Orchestrator synthesizes results

### Parallel Execution

**Core Principle**: Parallel for reads, sequential for writes

**Safe for Parallel**:
- Multiple file reads (Read tool)
- Search operations (Grep, Glob)
- Independent analysis by different agents
- Research workers (read-only, max 5)

**Must Be Sequential**:
- File modifications (Edit, Write)
- Git operations (commit, push)
- .claude/ directory edits (max 5 agents)

---

## 🛠️ Customization Guide

### Step 1: Define Your Project
Add to `../CLAUDE.md`:
- Directory structure and conventions
- Code style and standards
- Testing requirements
- Deployment process

### Step 2: Create Domain Agents
Priority order:
1. **code-implementer** - Feature development
2. **test-runner** - Test execution and validation
3. **code-reviewer** - Quality gates and security
4. **deployment-manager** - Deployment orchestration

Use `/create-agent` with interactive mode.

### Step 3: Build Workflows
Create slash commands in `commands/`:
- `/review-pr` - Pull request review workflow
- `/deploy-staging` - Deployment automation
- `/run-tests` - Test suite execution
- Domain-specific workflows

### Step 4: Document Standards
Add to `docs/guides/`:
- Code style guide
- Testing patterns
- Architecture decisions
- Domain-specific patterns

### Step 5: Track Components
Create `../COMPONENT_ALMANAC.md`:
```bash
cp templates/component-almanac-template.md ../COMPONENT_ALMANAC.md
# Document reusable components, services, utilities
```

---

## 📋 Templates

### Agent Templates
- `agent-definition-input.template.md` - Input spec for agent creation
- `agent-documentation.template.md` - Agent documentation structure
- `agent.template.md` - Complete agent definition skeleton

### Project Templates
- `spec-template.md` - Feature specification (SPEC format)
- `plan-template.md` - Implementation planning
- `task-template.md` - Task breakdown and tracking
- `component-almanac-template.md` - Component catalog structure

---

## 🔒 Security

### SSRF Protection
- `docs/security/allowed-domains.md` - 156-domain whitelist
- researcher-web uses domain filtering
- No arbitrary URL fetching

### Path Safety
- File operations validate paths
- No directory traversal
- Restricted write locations

### Secrets Detection
- Git hooks check for API keys
- .env files excluded from commits
- Credential scanning patterns

**Security Documentation**: See `docs/security/` directory

---

## 📊 Schema Contract

All agents extend `docs/schemas/base-agent.schema.json`:

```json
{
  "status": "SUCCESS | FAILURE | PARTIAL",
  "agent": "agent-name",
  "confidence": 0.0-1.0,
  "timestamp": "ISO-8601",
  "agent_specific_output": {
    // Agent defines their unique structure
  },
  "failure_details": {
    // Agent defines failure information
  }
}
```

**Benefits**:
- Consistent orchestrator integration
- Predictable error handling
- Confidence-based retry logic
- Standardized meta-flags

---

## 🔧 Hook System

### startup-eval.py
Runs at session startup:
- Loads developer identity
- Displays current focus
- Shows repository health
- Configurable via `.claude/config/developer.json`

**Configuration**:
```json
{
  "developer_name": "Your Name",
  "focus_area": "Current work description"
}
```

---

## 📈 Maturity Levels

Framework agents have documented maturity:
- **GA (General Availability)**: Production-ready, stable API
- **BETA**: Functional but API may change
- **ALPHA**: Experimental, breaking changes expected
- **MVP**: Minimum viable, limited testing

Check `docs/orchestrator-workflow.md` for agent maturity grades.

---

## 🤝 Contributing to Framework

This is a **starter kit template** - customize for your domain!

**To contribute framework improvements**:
1. Focus on **universally applicable** patterns
2. Ensure **backward compatibility** with existing agents
3. Update documentation for any framework changes
4. Follow existing patterns and standards
5. Submit improvements via pull request

**Domain-specific customizations**: Keep in your fork, not framework.

---

## 📄 Version

**Framework Version**: 1.0.0
**Last Updated**: 2025-10-31
**Compatibility**: Claude Code latest

---

## 🙋 Getting Help

**Documentation**: Start with `docs/DOC-INDEX.md` for organized navigation

**Common Issues**:
- **Agents not recognized**: Restart Claude Code session
- **Low agent confidence**: Review `docs/guides/agents/agent-selection-guide.md`
- **Context overflow**: Use `context-optimizer` agent
- **Quality issues**: Run `prompt-evaluator` agent

**Framework Support**: [Add your support channels]

---

**Built with Claude Code** - Multi-agent orchestration for sophisticated systems.
