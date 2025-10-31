# Claude Code Starter Kit

A foundational framework for building sophisticated multi-agent orchestration systems using Claude Code.

---

## 🎯 What Is This?

This starter kit provides the **core orchestration framework** and **agent creation tools** for building multi-agent systems with Claude Code. It's designed to help you create domain-specific agents that work together intelligently using the OODA loop (Observe, Orient, Decide, Act) pattern.

**Think of it as:** A foundational framework for agent-based systems that you customize and extend for your domain.

---

## 🚀 What You Get

### Framework Agents (11 included)

**Research & Context:**
- `researcher-lead` - Research orchestration (creates delegation plans)
- `researcher-codebase` - Codebase pattern discovery with 10:1 compression
- `researcher-web` - Web research with SSRF protection
- `researcher-library` - Library/framework documentation via Context7
- `context-readiness-assessor` - Context quality gating
- `context-optimizer` - Token budget optimization
- `intent-analyzer` - Request decomposition (OBSERVE phase)

**Decision & Meta:**
- `hypothesis-former` - Solution hypothesis generation (DECIDE phase)
- `contingency-planner` - Risk mitigation planning (DECIDE phase)
- `agent-architect` - Agent lifecycle management (creation, evaluation, quality)
- `prompt-evaluator` - Prompt engineering quality assessment

### Agent Creation Workflow

- **`/create-agent` command**: Interactive Q&A or template-based agent creation
- **Quality evaluation**: Built-in prompt evaluation and design validation
- **10-15 minute workflow**: Parse → Research → Generate → Validate → Integrate

### Orchestration Patterns

- **OODA Loop**: Core decision-making framework (Observe, Orient, Decide, Act)
- **Agent Selection**: Domain-first thinking with confidence scoring
- **Research Delegation**: Strategic multi-agent research coordination
- **Parallel Execution**: Read-optimized parallelization patterns

### Documentation (86 files)

- **Core framework**: orchestrator-workflow.md, agent-standards-*.md
- **Agent guides**: 11 guides on design, selection, creation, standards
- **Execution patterns**: 10 guides on research, parallelization, file operations
- **Quality frameworks**: 6 guides on validation, error handling, reliability
- **Platform docs**: 16 guides on Claude Code (hooks, plugins, MCP)
- **Research papers**: 10 papers on prompt engineering and multi-agent systems
- **Schemas**: 16 JSON schemas for agent contracts

---

## 💡 What You Build

This starter kit provides the **framework**. You build the **domain-specific implementation**:

- **Your agents**: Code review, testing, deployment, domain expertise
- **Your workflows**: Slash commands for your common processes
- **Your standards**: Code style, testing requirements, quality gates
- **Your structure**: Project organization and conventions
- **Your components**: Reusable functionality catalog

---

## 📖 Quick Start

### 1. Explore the Framework

```bash
# Read the core orchestration guide
cat CLAUDE.md

# Browse the documentation index
cat .claude/docs/DOC-INDEX.md

# Explore available agents
ls .claude/agents/

# Check agent creation guide
cat .claude/docs/guides/agents/agent-creation-guide.md
```

### 2. Understand the OODA Loop

The **Observe-Orient-Decide-Act** loop is the core orchestration pattern:

1. **OBSERVE**: What is being asked? (intent-analyzer)
2. **ORIENT**: What context do I need? (researcher-* agents, context-readiness-assessor)
3. **DECIDE**: What's my approach? (hypothesis-former, contingency-planner)
4. **ACT**: Execute the plan (domain agents you create)

Read `CLAUDE.md` for the complete OODA framework.

### 3. Create Your First Agent

**Interactive Mode** (Recommended):
```bash
/create-agent
```

You'll be guided through a Q&A workflow:
1. **Agent Purpose** - What problem does this agent solve?
2. **Tool Selection** - Which tools does it need? (Read, Write, Grep, etc.)
3. **Domain & Permissions** - Where can it operate? What can it modify?
4. **Quality Standards** - Reasoning approach, output format, validation

**What Happens Behind the Scenes**:
1. **Parse** (2 min) - Analyzes your inputs and validates requirements
2. **Research** (3-5 min) - Reviews existing agents, best practices, and patterns
3. **Generate** (2-3 min) - Creates agent definition with proper structure
4. **Validate** (2-3 min) - Runs prompt-evaluator for quality assessment
5. **Integrate** (1 min) - Saves to `.claude/agents/` and updates documentation

**Total Time**: 10-15 minutes

**Manual Mode** (Advanced):
```bash
# 1. Copy template
cp .claude/templates/agent-definition-input.template.md my-agent-input.md

# 2. Edit with your specifications
# (Fill in agent name, purpose, tools, permissions, etc.)

# 3. Generate agent from your template
/create-agent --create-definition my-agent-input.md
```

**⚠️ Restart Required**: After creating new agents, restart Claude Code for recognition.

### 4. Customize for Your Domain

1. **Add project structure** to `CLAUDE.md`
2. **Create 3-5 core agents** for your domain (code, testing, deployment, etc.)
3. **Build workflows** as slash commands in `.claude/commands/`
4. **Document patterns** in `.claude/docs/guides/`
5. **Create component catalog** using `.claude/templates/component-almanac-template.md`

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
├── CLAUDE.md                     # Core orchestration instructions (347 lines)
└── README.md                     # This file
```

---

## 🎓 Learning Path

### For New Users

1. **Read**: `CLAUDE.md` - Core orchestration framework
2. **Explore**: `.claude/docs/DOC-INDEX.md` - Organized documentation
3. **Study**: `.claude/docs/orchestrator-workflow.md` - Orchestration patterns
4. **Review**: `.claude/docs/guides/agents/agent-selection-guide.md` - Decision frameworks
5. **Create**: Your first agent with `/create-agent`

### For Builders

1. Define your project structure and standards (customize `CLAUDE.md`)
2. Create 3-5 core domain agents using `/create-agent`
3. Build workflows as slash commands (`.claude/commands/`)
4. Document patterns as they emerge (`.claude/docs/guides/`)
5. Iterate and refine based on usage

### Advanced Topics

- **Prompt engineering**: `.claude/docs/research/prompt-engineering/`
- **Architecture patterns**: `.claude/docs/guides/patterns/`
- **Quality frameworks**: `.claude/docs/guides/quality/`
- **Multi-agent coordination**: `.claude/docs/orchestrator-workflow.md`

---

## 🔑 Key Concepts

### OODA Loop

The core decision-making framework for orchestration:
- **Observe**: Understand the request (what, why, constraints)
- **Orient**: Gather context (self-assessment, research delegation)
- **Decide**: Choose approach (agent selection, confidence scoring)
- **Act**: Execute plan (delegate to agents, synthesize results)

### Domain-First Thinking

Agent selection based on file location and domain expertise:
- `.claude/**` → meta agents (agent-architect)
- `src/**` → implementation agents (you create these)
- `tests/**` → testing agents (you create these)
- Cross-domain → research agents (researcher-*)

### Agent Selection Confidence

Quantified confidence scoring for delegation decisions:
- **Formula**: (Domain Match × 0.60) + (Work Type × 0.30) + (Track Record × 0.10)
- **High** (0.7-1.0): Delegate immediately
- **Medium** (0.5-0.69): Delegate with monitoring
- **Low** (<0.5): Orchestrator handles directly OR recommend new agent
- **None** (0.0): No appropriate agent exists - orchestrator handles directly

**Starter Kit Default**: Until you create domain-specific agents, the orchestrator handles implementation work directly. As you build agents with `/create-agent`, more work shifts to delegation.

### Orchestrator Direct Execution

The orchestrator handles work directly when delegation isn't optimal:
- **No appropriate agent exists** (Agent_Selection_Confidence = 0.0)
- **Low agent confidence** (<0.5) for the specific task
- **Coordination work** (synthesizing results, orchestrating multiple agents)

**Evolution Pattern**: As you create agents with `/create-agent`, more work naturally shifts from direct execution to delegation. This is expected and healthy growth for your system.

### Research Delegation

Strategic coordination pattern for complex research:
- Use `researcher-lead` as coordinator (creates delegation plans)
- Spawn worker agents in parallel (researcher-codebase, researcher-web, researcher-library)
- Synthesize findings with confidence scoring
- Iterate up to 3 rounds with 0.85 confidence threshold

---

## 📚 Essential Documentation

**Must-Read** (auto-loaded at session startup):
- `orchestrator-workflow.md` - Core orchestration patterns
- `agent-selection-guide.md` - Domain-first agent selection
- `file-operation-protocol.md` - File editing rules
- `research-patterns.md` - Research delegation
- `tool-parallelization-patterns.md` - Optimization patterns

**Agent Creation**:
- `guides/agents/agent-creation-guide.md` - Complete creation workflow
- `guides/agents/agent-design-best-practices.md` - Design patterns
- `agent-standards-extended.md` - Comprehensive standards

**Complete Catalog**:
- `DOC-INDEX.md` - Organized navigation of all 86 framework files

---

## 🤝 Contributing

This is a **starter kit template**. Customize it for your needs!

**To share improvements back**:
1. Focus on **framework** improvements (not domain-specific features)
2. Ensure changes are **universally applicable**
3. Update documentation for any framework changes
4. Follow existing patterns and standards

---

## ⚙️ Configuration & Formatting

### Prettier Configuration (AI-Optimized)

The included `.prettierrc.json` uses settings optimized for AI/LLM consumption based on research into tokenization efficiency and semantic comprehension.

**Key Settings & Rationale:**

**`printWidth: 100`** - Optimal line width for AI tokenization
- Modern tokenizers (GPT-4, Claude) efficiently merge whitespace into single tokens
- Claude has a 1024-space single token - whitespace is extremely cheap
- Research shows 95-100 characters per line has peak reading speed
- Avoids fragmenting semantic units mid-thought (problem with 80-column limit)
- **Benefit**: ~5-8% fewer newline tokens vs 80cpl, maintains readability

**`proseWrap: "preserve"`** - Semantic line breaks (Prettier default since v1.9)
- Maintains semantic line breaks that help LLMs parse logical structure
- GitHub/BitBucket renderers are linebreak-sensitive - preservation ensures correct display
- Breaking at "substantial units of thought" creates cleaner boundaries for AI
- **Benefit**: Semantic meaning preserved, better AI comprehension of documentation flow

**`tabWidth: 2, useTabs: false`** - Consistent tokenization
- Spaces tokenize consistently across all LLM implementations (tabs vary by tokenizer)
- Modern tokenizers efficiently merge consecutive spaces into single tokens
- 2-space indentation balances clarity with narrower total width
- AI text editor tools require exact whitespace matching (spaces = deterministic)
- **Benefit**: Predictable token boundaries for AI code parsing and editing

**`trailingComma: "all"`** - Clean diffs for AI code understanding
- Single-line changes create cleaner git diffs that AI code tools parse more effectively
- Structure-aware AI systems better understand comma-delimited structures
- Enables safe automated code generation without syntax errors
- **Benefit**: Better git history for LLMs processing commits, consistent patterns for AI tools

**Combined Effect**: ~10-15% token reduction vs non-optimized settings, clearer semantic boundaries for AI systems, better version control integration for AI-assisted development.

**Sources**: Based on Anthropic documentation, Prettier maintainer rationale, tokenization research (Karpathy/fast.ai), semantic line break specification, and readability research showing 95-100cpl optimal for both humans and AI.

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙋 Getting Help

**Documentation**: Start with `.claude/docs/DOC-INDEX.md` for organized navigation.

**Troubleshooting**:
- New agents not recognized? Restart Claude Code session
- Agent quality issues? Use `prompt-evaluator` agent for assessment
- Unclear decision? Check `agent-selection-guide.md` for frameworks

**Community**: [Add your community links - Discord, GitHub Discussions, etc.]

---

**Built with Claude Code** - Multi-agent orchestration for sophisticated systems.

**Framework Version**: 1.0.0

**Last Updated**: 2025-10-31
