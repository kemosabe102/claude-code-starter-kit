# Documentation Index

**Purpose**: Central catalog of all framework documentation in the Claude Code Starter Kit.

**Last Updated**: 2025-10-31

---

## 📚 Quick Navigation

- [Core Framework](#-core-framework) - Orchestration, standards, workflow (3 docs)
- [Agent Guides](#-agent-guides) - Agent design, creation, patterns (11 docs)
- [Execution Patterns](#-execution-patterns) - Decision frameworks, research, parallelization, tools (9 docs)
- [Quality & Validation](#-quality--validation) - Validation, errors, reliability (6 docs)
- [Cross-Cutting Workflows](#-cross-cutting-workflows) - SDD, context, documentation, MCP (9 docs)
- [Claude Code Platform](#-claude-code-platform) - Platform documentation (16 docs)
- [Research Papers](#-research-papers) - Prompt engineering research (9 docs)
- [Schemas](#-schemas) - Agent contracts (15 schemas)
- [Examples](#-examples) - Templates and samples (7 examples)
- [Security](#-security) - Security patterns (1 doc)

**Total Documentation**: 89 files

---

## 📖 Core Framework

**Location**: `.claude/docs/` (root level)

Essential framework documentation auto-loaded at session startup:

1. **orchestrator-workflow.md** - Core orchestration patterns, quick reference, workflow execution (70% optimized)
2. **agent-standards-extended.md** - Comprehensive agent design standards (12 core standards)
3. **agent-standards-runtime.md** - Runtime behavior and contracts for all agents

**When to use**: Understanding orchestration architecture, agent design principles, system workflow.

### Orchestration Specializations

**Location**: `.claude/docs/guides/orchestration/`

Detailed orchestration patterns (progressive disclosure):

1. **agent-capabilities.md** - Full agent matrix, maturity tracking, capability mapping
2. **parallel-execution-patterns.md** - Parallel vs sequential rules, performance optimization
3. **code-reuse-integration.md** - Code reuse workflows, technical debt reduction
4. **research-coordination.md** - researcher-lead patterns, iterative research workflows
5. **synthesis-framework.md** - Multi-agent result consolidation, overlap detection

**When to use**: Deep-dive into agent capabilities, parallel execution strategies, research coordination.

---

## 🤖 Agent Guides

**Location**: `.claude/docs/guides/agents/`

Complete agent lifecycle from design to creation:

### Agent Design & Standards
1. **agent-design-best-practices.md** - Prompt engineering, tool selection, patterns
2. **agent-selection-guide.md** - Domain-first thinking, 7 selection frameworks
3. **agent-categorization.md** - Agent type taxonomy (6 categories)
4. **agent-naming-conventions.md** - Naming standards and patterns
5. **base-agent-pattern.md** - Agent inheritance pattern (1,150-token template)
6. **base-review-agent-pattern.md** - Review agent specialization pattern
7. **golden-agent-standards.md** - Quality standards and benchmarks

### Agent Creation
8. **agent-creation-guide.md** - Complete /create-agent workflow (300+ lines)
9. **create-agent-interactive-mode-addendum.md** - Interactive creation workflow
10. **create-agent-command-insertions.md** - Command integration patterns
11. **agent-descriptions-update.md** - Agent description maintenance

**When to use**: Creating new agents, evaluating agent quality, understanding agent architecture.

---

## ⚡ Execution Patterns

**Location**: `.claude/docs/guides/patterns/`

Runtime patterns for research, parallelization, and execution:

### Decision Frameworks
1. **ooda-loop-framework.md** - Comprehensive OODA decision-making framework (Observe, Orient, Decide, Act)

### Research Patterns
2. **research-patterns.md** - Research delegation strategies, 10:1 compression
3. **synthesis-and-recommendation-framework.md** - Multi-agent result consolidation

### Parallelization & Performance
4. **tool-parallelization-patterns.md** - Read/Grep/Write efficiency patterns
5. **parallel-execution-patterns.md** - General parallel execution strategies
6. **agent-parallelization-strategy.md** - Multi-agent delegation and coordination

### File & Tool Operations
7. **file-operation-protocol.md** - File editing protocol, best practices (simplified)
8. **tool-design-patterns.md** - Tool architecture and design patterns

### Feature Planning
9. **feature-artifact-structure.md** - Spec/plan/task organization patterns

**When to use**: Implementing research workflows, optimizing performance, designing tools.

---

## ✅ Quality & Validation

**Location**: `.claude/docs/guides/quality/`

Validation, error handling, and reliability patterns:

### Validation & Review
1. **validation-rubrics.md** - Quality validation frameworks
2. **quality-scoring-algorithms.md** - Scoring methodologies
3. **review-aggregation-logic.md** - Multi-reviewer synthesis patterns

### Error Handling
4. **error-classification-framework.md** - Error categorization and handling
5. **circuit-breaker-pattern.md** - Service protection patterns
6. **retry-strategies.md** - Exponential backoff, jitter, retry logic

**When to use**: Building validation workflows, implementing error handling, designing reliable systems.

---

## 🔄 Cross-Cutting Workflows

**Location**: `.claude/docs/guides/` (root level)

Cross-cutting concerns and development workflows:

### Development Methodology
1. **spec-driven-development.md** - SDD methodology and workflow
2. **README.md** - Guides overview and navigation

### Context & Documentation
3. **documentation-context-loading.md** - Documentation loading strategies
4. **critical-docs-auto-loading.md** - Auto-load implementation patterns
5. **context-monitoring-guide.md** - Token usage tracking and monitoring
6. **doc-optimization-methodology.md** - Documentation optimization approaches

### System Patterns
7. **orchestrator-timestamp-management.md** - Timestamp patterns and conventions
8. **progressive-disclosure-ai-context-windows.md** - Progressive disclosure for AI context management

### MCP & Tools
9. **mcp-agent-optimization.md** - MCP/Context7 usage patterns, token optimization strategies (located in `.claude/docs/`)

**When to use**: Understanding development workflows, managing context, optimizing documentation, MCP tool usage.

---

## 🛠️ Claude Code Platform

**Location**: `.claude/docs/guides/claude/`

Universal Claude Code platform documentation (applicable to any project):

### Core Platform
1. **sub-agents.md** - Sub-agent system architecture
2. **agent-skills.md** - Agent skills framework
3. **cli-reference.md** - CLI commands and usage
4. **settings.md** - Settings configuration

### Extension Systems
5. **hooks.md** - Hook system overview
6. **hooks-reference.md** - Hook API reference
7. **plugins.md** - Plugin system overview
8. **plugins-reference.md** - Plugin API reference
9. **plugins-marketplace.md** - Plugin marketplace guide
10. **slash-commands.md** - Slash command system

### Integration & Operations
11. **github-actions.md** - GitHub Actions integration
12. **memory.md** - Memory management
13. **monitoring.md** - Monitoring and observability
14. **iam.md** - IAM and permissions
15. **mcp.md** - Model Context Protocol

### Advanced Topics
16. **AI Agent Tool Design and Agent-Tool Interactions.md** - Tool interaction patterns

**When to use**: Understanding Claude Code platform capabilities, integrating with external systems.

---

## 🔬 Research Papers

**Location**: `.claude/docs/research/prompt-engineering/`

Prompt engineering and multi-agent research:

### Foundational Research
1. **Anthropic Multi-Agent Research System.md** - Framework research and patterns
2. **Principles for Subagent Prompt Design.pdf** - 10-page research document (4 core principles)

### Prompt Engineering
3. **Prompt Engineering Standards and Practices_.md** - Standards and best practices
4. **Prompt Engineering Research Analysis.md** - Research patterns analysis
5. **Prompt Engineering Lifecycle Analysis.md** - Lifecycle management patterns

### Context Management
6. **Context Management in AI Agents.md** - Context handling patterns
7. **Context-Management-Best-Practices.md** - Best practices guide
8. **Context-Optimization-Analysis-Report.md** - Optimization strategies

### Advanced Topics
9. **agent2agent_protocol_and_self_optimizing_prompts.md** - A2A protocol, self-optimization
10. **Agents vs. Workflows Research Plan_.md** - Architecture decision framework

**When to use**: Deep-diving into prompt engineering theory, understanding advanced patterns.

---

## 📋 Schemas

**Location**: `.claude/docs/schemas/`

Agent output contracts and system schemas:

### Base Schema
1. **base-agent.schema.json** - Universal agent contract (extended by all agents)

### Framework Agents
2. **agent-architect.schema.json** - Agent creation and lifecycle
3. **prompt-evaluator.schema.json** - Prompt quality evaluation

### Research Agents
4. **researcher-lead.schema.json** - Research orchestration
5. **researcher-codebase.schema.json** - Codebase analysis
6. **researcher-web.schema.json** - Web research
7. **researcher-library.schema.json** - Library documentation

### OODA Agents
8. **intent-analyzer.schema.json** - Request decomposition (OBSERVE)
9. **hypothesis-former.schema.json** - Solution generation (DECIDE)
10. **contingency-planner.schema.json** - Risk planning (DECIDE)

### Context Agents
11. **context-readiness-assessor.schema.json** - Context quality gating
12. **context-optimizer.schema.json** - Token budget management

### System Schemas
13. **claude-code.schema.json** - Claude Code configuration
14. **workflow.schema.json** - Workflow execution patterns
15. **sow.schema.json** - Statement of Work contracts

### Documentation
16. **specify-output-schema.md** - Schema definition guide

**When to use**: Designing agent outputs, understanding agent contracts, validating agent responses.

---

## 📝 Examples

Templates and example implementations:

**Project Structure Examples** (`.claude/examples/`):
1. **SPEC-example.md** - Complete feature specification example (financial research system)
2. **COMPONENT_ALMANAC-example.md** - Component catalog example

**Workflow Examples** (`.claude/docs/examples/`):
3. **claude-code-agent-flows.md** - Agent workflow examples
4. **commit-message-guide.md** - Git commit message patterns
5. **roadmap-item-template.md** - Roadmap planning template
6. **decision-examples.yaml** - Decision framework examples
7. **sow-examples.yaml** - Statement of Work examples

**When to use**: Creating specifications, understanding documentation patterns, learning by example.

---

## 🔒 Security

**Location**: `.claude/docs/security/`

Security patterns and configurations:

1. **allowed-domains.md** - SSRF protection whitelist (156-domain whitelist for researcher-web)
2. **README.md** - Security patterns and best practices

**When to use**: Configuring security policies, understanding security boundaries.

---

## 📊 Statistics

- **Core Framework**: 3 docs
- **Agent Guides**: 11 docs
- **Execution Patterns**: 10 docs
- **Quality & Validation**: 6 docs
- **Cross-Cutting**: 7 docs
- **Platform Docs**: 16 docs
- **Research Papers**: 10 docs
- **Schemas**: 16 files
- **Examples**: 5 files
- **Security**: 2 files

**Total**: 86 files

---

## 🔗 Quick Reference Paths

### For New Users
1. Start: `README.md`
2. Core concepts: `orchestrator-workflow.md`
3. Create first agent: `guides/agents/agent-creation-guide.md`
4. Learn patterns: `guides/patterns/research-patterns.md`

### For Agent Designers
1. Design: `guides/agents/agent-design-best-practices.md`
2. Selection: `guides/agents/agent-selection-guide.md`
3. Standards: `agent-standards-extended.md`
4. Schemas: `schemas/base-agent.schema.json`

### For Advanced Users
1. Research: `research/prompt-engineering/`
2. Patterns: `guides/patterns/`
3. Quality: `guides/quality/`
4. Platform: `guides/claude/`

---

## 📖 Auto-Loaded Documentation

These files are automatically loaded at session startup (available without Read tool):

- `orchestrator-workflow.md` - Agent coordination and OODA loop
- `agent-standards-runtime.md` - Runtime agent behavior
- `guides/agents/agent-selection-guide.md` - Domain-first agent selection
- `guides/patterns/file-operation-protocol.md` - File editing protocol
- `guides/patterns/research-patterns.md` - Research delegation
- `guides/patterns/tool-parallelization-patterns.md` - Tool optimization
- `guides/agents/base-agent-pattern.md` - Agent inheritance

---

**Navigation**: Use this index to quickly locate documentation. All paths are relative to `.claude/docs/`.

**Maintenance**: Update this index when adding/removing documentation files.
