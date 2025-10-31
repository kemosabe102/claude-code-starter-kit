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

## 🎨 INFUSE Framework

The **INFUSE Framework** is a structured prompt methodology for creating clear, effective agent definitions and behaviors.

### What is INFUSE?

INFUSE is an acronym representing six core components of well-structured prompts:

- **I**dentity - Who is this agent? What role does it play?
- **N**avigation - What documentation should it reference? What context does it need?
- **F**low - How should it think? What's the decision-making process?
- **U**ser guidance - What outputs does it produce? How does it communicate?
- **S**ignals - What triggers specific behaviors? What warnings or errors should it handle?
- **E**nd instructions - What are the final reminders? What should never be forgotten?

### When to Use INFUSE

- **Creating new agents**: Structure your agent definitions with clear identity, navigation paths, and decision flows
- **Enhancing behavior**: Add signals for edge cases, improve user guidance sections
- **Debugging agents**: Check if all INFUSE components are present and well-defined

### Framework Benefits

- **Consistency**: All agents follow the same structural pattern
- **Completeness**: Ensures no critical components are missing
- **Maintainability**: Easy to locate and update specific behavioral aspects
- **Onboarding**: New team members understand agent design quickly

**Learn More**: See `.claude/docs/guides/patterns/infuse-framework.md` for complete methodology and examples.

---

## 🔀 Skills, Workflows & Slash Commands

The starter kit supports three different patterns for extending functionality. Choose based on complexity and invocation method:

### Skills

**What**: Complex, multi-step capabilities invoked automatically by Claude Code when semantically matched to user intent.

**Structure**: Directory-based with `SKILL.md` + supporting resources
```
.claude/skills/my-skill/
├── SKILL.md           # Skill definition with INFUSE structure
├── templates/         # Optional: templates, examples
└── utils/             # Optional: helper scripts
```

**When to Use**:
- Complex multi-agent workflows requiring coordination
- Domain-specific capabilities needing multiple tools
- Reusable patterns invoked by semantic intent (not explicit commands)
- Example: Code review skill, deployment workflow, test generation

**How Claude Code Chooses**: Automatic semantic matching based on skill description and user request.

### Slash Commands

**What**: Simple, user-invoked prompts for quick operations and guidance.

**Structure**: Single `.md` file in `.claude/commands/`
```
.claude/commands/my-command.md
```

**When to Use**:
- Simple prompt expansion (single instruction set)
- User needs explicit control over invocation
- Quick reference or guidance workflows
- Example: `/create-agent`, `/review-pr`, `/explain-architecture`

**How Invoked**: User types `/command-name` explicitly.

### Workflows (Architectural Pattern)

**What**: Coded logic paths for automated sequences (DAG architecture).

**Note**: Workflows are an architectural pattern, not a built-in framework feature. You implement workflow logic within skills or agents.

**When to Use**:
- Multi-step automation with conditional branching
- State management across multiple operations
- Example: CI/CD pipeline, release process, migration workflow

**Implementation**: Code workflow logic inside a skill's supporting scripts or agent behavior.

### Decision Tree

```
Need multi-step automation with state?
├─ Yes → Build a Skill (with workflow logic if needed)
└─ No → Is it simple prompt expansion?
    ├─ Yes → Create Slash Command
    └─ No → Is it model-invoked by intent?
        ├─ Yes → Create Skill
        └─ No → Create Slash Command
```

**Learn More**:
- Skills: `.claude/docs/guides/claude/agent-skills.md`
- Slash Commands: `.claude/docs/guides/claude/slash-commands.md`
- INFUSE: `.claude/docs/guides/patterns/infuse-framework.md`

---

## 📖 Quick Start

### 1. Explore the Framework

**Copy and paste this prompt to get a guided tour:**

```
I want to understand the Claude Code Starter Kit framework. Please help me explore:

1. The core orchestration guide in CLAUDE.md - explain the key concepts
2. The documentation index at .claude/docs/DOC-INDEX.md - show me how it's organized
3. The available framework agents in .claude/agents/ - what each one does
4. The agent creation guide - how the /create-agent workflow works

Give me a high-level overview of each, highlighting what I need to know to get started.
```

### 2. Understand the OODA Loop

**Copy and paste this prompt to learn the core orchestration pattern:**

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

**Copy and paste this prompt to start the interactive agent creation workflow:**

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

**Alternative - Manual Template Approach:**

```
I want to create a custom agent using the manual template approach. Please:

1. Show me the agent-definition-input.template.md structure
2. Explain each section I need to fill out (using INFUSE framework)
3. Point me to examples of well-designed agents for reference
4. Guide me through using /create-agent --create-definition after I've filled in the template

Reference .claude/docs/guides/agents/agent-creation-guide.md and the INFUSE framework.
```

### 4. Get More Information

**Copy and paste this prompt to understand specific framework features:**

```
I need help understanding more about the Claude Code Starter Kit. Please help me with:

[Choose ONE or more topics below]

- The 11 framework agents: what each does, when to use them, and how they work together
- Progressive Disclosure: the 3-tier architecture and how it optimizes token usage
- Research delegation patterns: when to use researcher-lead vs researcher-codebase vs researcher-web
- Agent selection confidence scoring: the formula and decision thresholds
- File operation protocols: Edit tool hierarchy and when to use fallbacks
- INFUSE framework: creating well-structured agent prompts
- Skills vs Slash Commands: when to build each type of extension

Reference the relevant documentation in .claude/docs/ and explain with examples.
```

### 5. Customize for Your Domain

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
│       │   ├── quality/          # 7 quality frameworks (includes token density evaluation)
│       │   └── claude/           # 16 platform docs
│       ├── research/
│       │   └── prompt-engineering/    # 10 research papers
│       ├── schemas/              # 16 agent JSON schemas
│       ├── examples/             # 5 example implementations
│       └── security/             # Security patterns
├── CLAUDE.md                     # Core orchestration instructions (~505 lines, token-optimized)
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
- **Token density optimization**: `.claude/docs/guides/quality/token-density-evaluation-framework.md`

### Token Density Optimization

The framework includes a comprehensive evaluation methodology for optimizing token usage in prompts and documentation:

**Six-Dimension Evaluation Matrix**:
1. **Structural Efficiency** - Markdown format, hierarchy, data structures
2. **Language Efficiency** - Filler words, active voice, constraint statements
3. **Reference Efficiency** - Base patterns, inheritance, consolidation
4. **Example Efficiency** - 2-3 max rule, show vs tell
5. **Progressive Disclosure** - 2-level max depth
6. **INFUSE Alignment** - 6-component framework compliance

**Automated Tools Included**:
- Token estimator (character count / 4 for conservative estimate)
- Filler word detector
- Duplicate content finder
- Reference savings calculator

**Target Metrics**:
- Agent definitions: 700-1,200 tokens
- Orchestrator instructions: 3,000-4,000 tokens
- Comprehensive guides: 3,000-8,000 tokens
- Templates/schemas: 0 tokens (executable resources)

**Typical Optimizations**:
- Remove filler words: 10-67% reduction per instance
- Constraint statements over explanations: 20-40% reduction
- Base pattern extraction: 93% reduction on common content
- Markdown-KV over tables: 47% reduction

**See**: `.claude/docs/guides/quality/token-density-evaluation-framework.md` for complete methodology with scoring rubrics and automated analysis scripts.

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
