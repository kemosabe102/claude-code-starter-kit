# Claude Code Starter Kit

A foundational framework for building sophisticated multi-agent orchestration systems using Claude Code.

---

## 📖 Quick Start (5 Minutes)

Get value immediately with these copy-paste prompts:

### 1. Explore the Framework

```
I want to understand the Claude Code Starter Kit framework. Please help me explore:

1. The core orchestration guide in CLAUDE.md - explain the key concepts
2. The documentation index at .claude/docs/DOC-INDEX.md - show me how it's organized
3. The available framework agents in .claude/agents/ - what each one does
4. The agent creation guide - how the /create-agent workflow works

Give me a high-level overview of each, highlighting what I need to know to get started.
```

### 2. Understand the OODA Loop

```
I want to understand the OODA Loop framework used in this starter kit. Please explain:

1. What OODA stands for (Observe, Orient, Decide, Act)
2. How each phase works in the context of multi-agent orchestration
3. Which framework agents support each phase:
   - OBSERVE: intent-analyzer
   - ORIENT: researcher-* agents, context-readiness-assessor
   - DECIDE: hypothesis-former, contingency-planner
   - ACT: domain agents (that I create)
4. A concrete example of OODA in action for a typical coding request

Reference CLAUDE.md and .claude/docs/guides/patterns/ooda-loop-framework.md to explain this.
```

### 3. Create Your First Agent

```
I want to create my first custom agent using /create-agent. Please walk me through:

1. What the interactive workflow will ask me (agent purpose, tools, domain, permissions)
2. What happens behind the scenes during the 10-15 minute creation process:
   - Parse phase (2 min)
   - Research phase (3-5 min)
   - Generate phase (2-3 min)
   - Validate phase (2-3 min)
   - Integrate phase (1 min)
3. How to use /create-agent in interactive mode vs manual template mode
4. What I need to know about the INFUSE framework for agent design
5. Why I need to restart Claude Code after creating the agent

Then help me start the /create-agent command.
```

---

## 🎯 What Is This?

**Claude Code Starter Kit** provides the **core orchestration framework** for building multi-agent systems with Claude Code.

**Think of it as:** A foundational framework that you customize and extend for your domain. It gives you the orchestration tools, patterns, and agent creation workflow—you build the domain-specific implementation.

**Philosophy:** This is a **framework**, not a complete system. Start with 11 framework agents, then create your own agents for code, testing, deployment, and domain expertise.

---

## 🚀 What You Get vs. What You Build

### What You Get (Framework)

**11 Framework Agents:**
- **Research:** researcher-lead, researcher-codebase, researcher-web, researcher-library
- **Context:** context-readiness-assessor, context-optimizer, intent-analyzer
- **Decision:** hypothesis-former, contingency-planner
- **Meta:** agent-architect, prompt-evaluator

**Agent Creation Tools:**
- `/create-agent` command with interactive Q&A workflow
- Quality evaluation and design validation
- 10-15 minute creation process (parse → research → generate → validate → integrate)

**Orchestration Patterns:**
- OODA Loop decision-making framework
- Agent selection with confidence scoring
- Research delegation strategies
- Parallel execution patterns

**86 Documentation Files:**
- Core framework guides (orchestrator-workflow.md, agent-standards)
- 11 agent design guides
- 10 execution pattern guides
- 6 quality frameworks (including token density optimization)
- 16 platform docs (Claude Code hooks, plugins, MCP)
- 10 prompt engineering research papers
- 16 JSON schemas for agent contracts

### What You Build (Implementation)

- **Your agents:** Code review, testing, deployment, domain expertise
- **Your workflows:** Slash commands for your common processes
- **Your standards:** Code style, testing requirements, quality gates
- **Your structure:** Project organization and conventions
- **Your components:** Reusable functionality catalog

---

## 🔑 Key Concepts

### OODA Loop

The core decision-making framework for orchestration:
- **Observe:** Understand the request (what, why, constraints)
- **Orient:** Gather context (self-assessment, research delegation)
- **Decide:** Choose approach (agent selection, confidence scoring)
- **Act:** Execute plan (delegate to agents, synthesize results)

### Domain-First Thinking

Agent selection based on file location and domain expertise:
- `.claude/**` → meta agents (agent-architect)
- `src/**` → implementation agents (you create these)
- `tests/**` → testing agents (you create these)
- Cross-domain → research agents (researcher-*)

### Agent Selection Confidence

Quantified confidence scoring for delegation decisions:
- **Formula:** (Domain Match × 0.60) + (Work Type × 0.30) + (Track Record × 0.10)
- **High (0.7-1.0):** Delegate immediately
- **Medium (0.5-0.69):** Delegate with monitoring
- **Low (<0.5):** Orchestrator handles directly OR recommend new agent

**Evolution Pattern:** As you create agents with `/create-agent`, more work shifts from direct execution to delegation.

### Research Delegation

Strategic coordination for complex research:
- Use `researcher-lead` as coordinator (creates delegation plans)
- Spawn worker agents in parallel (researcher-codebase, researcher-web, researcher-library)
- Synthesize findings with confidence scoring
- Iterate up to 3 rounds with 0.85 confidence threshold

---

## 📖 Next Steps

### For New Users (Start Here)

1. **Understand the Framework:**
   - Read `CLAUDE.md` - Core orchestration instructions
   - Explore `.claude/docs/DOC-INDEX.md` - Organized documentation catalog
   - Review `.claude/docs/orchestrator-workflow.md` - Agent coordination patterns

2. **Learn OODA Loop:**
   - Study `.claude/docs/guides/patterns/ooda-loop-framework.md`
   - Understand Observe → Orient → Decide → Act phases
   - See which framework agents support each phase

3. **Create Your First Agent:**
   - Run `/create-agent` for interactive workflow
   - Or use `.claude/templates/agent-definition-input.template.md` for manual approach
   - Study `.claude/docs/guides/agents/agent-creation-guide.md`

### For Builders (Customize Your System)

1. **Define Your Project:**
   - Add project structure to `CLAUDE.md`
   - Document your conventions and standards

2. **Create Domain Agents:**
   - Build 3-5 core agents using `/create-agent`
   - Examples: code-reviewer, test-runner, deployment-manager

3. **Build Workflows:**
   - Create slash commands in `.claude/commands/`
   - Add skills in `.claude/skills/` for complex workflows

4. **Document Patterns:**
   - Capture emerging patterns in `.claude/docs/guides/`
   - Build component catalog using `.claude/templates/component-almanac-template.md`

5. **Iterate & Refine:**
   - Use `prompt-evaluator` agent for quality checks
   - Apply token density optimization (see quality frameworks)

### For Advanced Topics

- **Prompt Engineering:** `.claude/docs/research/prompt-engineering/` (10 research papers)
- **Architecture Patterns:** `.claude/docs/guides/patterns/` (10 guides)
- **Quality Frameworks:** `.claude/docs/guides/quality/` (6 guides including token density)
- **Multi-Agent Coordination:** `.claude/docs/orchestrator-workflow.md`

---

## 🎨 Framework Components

### INFUSE Framework (Prompt Methodology)

Structured approach for creating clear, effective agent definitions:

- **I**dentity - Agent role and purpose
- **N**avigation - Documentation references and context
- **F**low - Decision-making processes
- **U**ser guidance - Output format and communication
- **S**ignals - Behavioral triggers and error handling
- **E**nd instructions - Critical reminders

**Benefits:** Consistency, completeness, maintainability, easy onboarding

**Learn More:** `.claude/docs/guides/patterns/infuse-framework.md`

### Skills, Workflows & Slash Commands

Three patterns for extending functionality:

**Skills** (Complex, auto-invoked):
- Multi-step capabilities triggered by semantic intent
- Directory structure with `SKILL.md` + resources
- Example: Code review, deployment workflow, test generation

**Slash Commands** (Simple, user-invoked):
- Single `.md` file for quick operations
- Explicit invocation with `/command-name`
- Example: `/create-agent`, `/review-pr`

**Workflows** (Architectural pattern):
- Coded logic for conditional branching
- Implemented within skills or agents
- Example: CI/CD pipelines, release processes

**Decision Tree:**
```
Need multi-step automation with state?
├─ Yes → Build a Skill (with workflow logic if needed)
└─ No → Is it simple prompt expansion?
    ├─ Yes → Create Slash Command
    └─ No → Is it model-invoked by intent?
        ├─ Yes → Create Skill
        └─ No → Create Slash Command
```

**Learn More:**
- Skills: `.claude/docs/guides/claude/agent-skills.md`
- Slash Commands: `.claude/docs/guides/claude/slash-commands.md`

---

## 📚 Documentation Reference

**Auto-Loaded Guides** (available at session start):
- `orchestrator-workflow.md` - Core orchestration patterns
- `agent-selection-guide.md` - Domain-first agent selection
- `file-operation-protocol.md` - File editing rules
- `research-patterns.md` - Research delegation strategies
- `tool-parallelization-patterns.md` - Optimization patterns

**Agent Creation:**
- `guides/agents/agent-creation-guide.md` - Complete workflow
- `guides/agents/agent-design-best-practices.md` - Design patterns
- `agent-standards-extended.md` - Comprehensive standards

**Complete Catalog:**
- `DOC-INDEX.md` - Organized navigation of all 86 framework files

---

## 📁 Repository Structure

```
claude-code-starter-kit/
├── .claude/
│   ├── agents/                    # 11 framework agents
│   ├── commands/                  # /create-agent command
│   ├── templates/                 # Agent + project templates
│   ├── hooks/                     # Session lifecycle hooks
│   └── docs/
│       ├── orchestrator-workflow.md    # Core orchestration guide
│       ├── agent-standards-*.md        # Agent design standards
│       ├── DOC-INDEX.md                # Complete documentation catalog
│       ├── guides/
│       │   ├── agents/           # 11 agent design guides
│       │   ├── patterns/         # 10 execution patterns
│       │   ├── quality/          # 6 quality frameworks
│       │   └── claude/           # 16 platform docs
│       ├── research/
│       │   └── prompt-engineering/    # 10 research papers
│       ├── schemas/              # 16 agent JSON schemas
│       ├── examples/             # 5 example implementations
│       └── security/             # Security patterns
├── CLAUDE.md                     # Core orchestration instructions (~505 lines)
└── README.md                     # This file
```

---

## 🔬 Advanced Topics

### Token Density Optimization

Comprehensive evaluation methodology for optimizing token usage:

**Six-Dimension Evaluation Matrix:**
1. Structural Efficiency - Markdown format, hierarchy, data structures
2. Language Efficiency - Filler words, active voice, constraint statements
3. Reference Efficiency - Base patterns, inheritance, consolidation
4. Example Efficiency - 2-3 max rule, show vs tell
5. Progressive Disclosure - 2-level max depth
6. INFUSE Alignment - 6-component framework compliance

**Target Metrics:**
- Agent definitions: 700-1,200 tokens
- Orchestrator instructions: 3,000-4,000 tokens
- Comprehensive guides: 3,000-8,000 tokens

**Typical Optimizations:**
- Remove filler words: 10-67% reduction
- Constraint statements: 20-40% reduction
- Base pattern extraction: 93% reduction
- Markdown-KV over tables: 47% reduction

**Learn More:** `.claude/docs/guides/quality/token-density-evaluation-framework.md`

### Multi-Agent Orchestration Patterns

- **Parallel Execution:** Read-optimized parallelization (max 5 agents for writes)
- **Research Coordination:** Strategic delegation with confidence scoring
- **Context Gathering:** Progressive disclosure with quality gating
- **Failure Handling:** Contingency planning with adaptive retry logic

**Learn More:** `.claude/docs/orchestrator-workflow.md`

---

## ⚙️ Configuration

### Prettier Configuration (AI-Optimized)

The included `.prettierrc.json` uses settings optimized for AI/LLM tokenization efficiency:

**Key Settings:**
- **`printWidth: 100`** - Optimal for AI tokenization (5-8% fewer tokens vs 80cpl)
- **`proseWrap: "preserve"`** - Semantic line breaks for better AI comprehension
- **`tabWidth: 2, useTabs: false`** - Consistent tokenization across LLMs
- **`trailingComma: "all"`** - Cleaner git diffs for AI code understanding

**Combined Effect:** ~10-15% token reduction vs non-optimized settings

**Sources:** Anthropic documentation, tokenization research (Karpathy/fast.ai), readability studies

---

## 🤝 Contributing

This is a **starter kit template**. Customize it for your needs!

**To share improvements back:**
1. Focus on **framework** improvements (not domain-specific features)
2. Ensure changes are **universally applicable**
3. Update documentation for any framework changes
4. Follow existing patterns and standards

---

## 🙋 Getting Help

**Documentation:** Start with `.claude/docs/DOC-INDEX.md` for organized navigation

**Troubleshooting:**
- New agents not recognized? Restart Claude Code session
- Agent quality issues? Use `prompt-evaluator` agent for assessment
- Unclear decision? Check `agent-selection-guide.md` for frameworks

**Community:** [Add your community links - Discord, GitHub Discussions, etc.]

---

## 📄 License

MIT License - See LICENSE file for details

---

**Built with Claude Code** - Multi-agent orchestration for sophisticated systems

**Framework Version:** 1.0.0
**Last Updated:** 2025-10-31
