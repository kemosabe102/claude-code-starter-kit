# Agent Categorization Guide

**Purpose**: Organize agents by capability and use case for easy discovery
**Last Updated**: 2025-10-03

## Agent Categories Overview

```
All Agents
├── Planning & Design (6 agents)
├── Implementation & Code (4 agents)
├── Testing & Quality (2 agents)
├── Review & Validation (4 agents)
└── Meta & Management (3 agents)
```

## Category 1: Planning & Design

**Purpose**: Create specifications, plans, and architectural designs

| Agent | Type | Modifies Files | Primary Use |
|-------|------|---------------|-------------|
| **spec-enhancer** | Creator/Enhancer | ✅ Yes | Create comprehensive specifications |
| **plan-enhancer** | Enhancer | ✅ Yes | Add business context to plans |
| **architecture-enhancer** | Enhancer | ✅ Yes | Add technical details to plans |
| **spec-reviewer** | Reviewer | ❌ No | Validate specification quality |
| **technical-pm** | Reviewer | ❌ No | Review business alignment |
| **architecture-review** | Reviewer | ❌ No | Review technical architecture |

### When to Use
- Starting new feature → spec-enhancer
- Creating plans → plan-enhancer + architecture-enhancer
- Validating quality → spec-reviewer, technical-pm, architecture-review

## Category 2: Implementation & Code

**Purpose**: Write, modify, and improve code

| Agent | Type | Primary Use | Key Strength |
|-------|------|-------------|--------------|
| **code-implementer** | Creator | Write new features | Production code |
| **debugger** | Fixer | Diagnose and fix bugs | Problem solving |
| **refactorer** | Improver | Clean up code | Structure improvement |
| **handle-code-review** | Handler | Apply review feedback | Fix implementation |

### When to Use
- New feature → code-implementer
- Bug fixing → debugger
- Code cleanup → refactorer
- Address review → handle-code-review

## Category 3: Testing & Quality

**Purpose**: Ensure code quality through testing

| Agent | Type | Primary Use | Coverage Focus |
|-------|------|-------------|----------------|
| **test-runner** | Creator/Runner | Write and execute tests | Unit, integration |
| **test-reviewer** | Reviewer | Review test quality | Test coverage |

### When to Use
- Need tests → test-runner
- Validate test quality → test-reviewer

## Category 4: Review & Validation

**Purpose**: Review without modification, provide feedback

| Agent | Type | Reviews What | Output |
|-------|------|-------------|--------|
| **code-reviewer** | Reviewer | Code quality, security | Feedback report |
| **spec-reviewer** | Reviewer | Specification quality | Quality assessment |
| **technical-pm** | Reviewer | Business alignment | Business report |
| **architecture-review** | Reviewer | Technical architecture | Technical report |

### Key Characteristic
**ALL reviewers are READ-ONLY** - they cannot modify files

### When to Use
- PR review → code-reviewer
- Spec validation → spec-reviewer
- Business check → technical-pm
- Technical validation → architecture-review

## Category 5: Meta & Management

**Purpose**: Manage agents, workflows, and system configuration

| Agent | Type | Manages | Special Purpose |
|-------|------|---------|-----------------|
| **agent-architect** | Manager | Agent lifecycle | Create/update agents |
| **workflow** | Coordinator | Workflow ecosystem | Slash commands, automation |
| **claude-code** | Manager | Claude configuration | .claude directory management |

### When to Use
- Create new agent → agent-architect
- Workflow automation → workflow
- Claude config → claude-code

## Performance Categories

### 🟢 Fast Agents (<30s startup)
Best for initial analysis and quick tasks:
- spec-reviewer
- technical-pm (after optimization)
- code-reviewer

### 🟡 Medium Agents (1-2min startup)
Good for focused modifications:
- plan-enhancer
- architecture-enhancer
- code-implementer

### 🔴 Heavy Agents (3+min startup)
Use sparingly, batch operations:
- (None currently after optimizations)

## Selection Decision Tree

```
What do you need?
├── Planning/Design
│   ├── Create spec → spec-enhancer
│   ├── Enhance plan → plan-enhancer OR architecture-enhancer
│   └── Review → spec-reviewer OR technical-pm OR architecture-review
├── Implementation
│   ├── New code → code-implementer
│   ├── Fix bugs → debugger
│   ├── Clean code → refactorer
│   └── Apply feedback → handle-code-review
├── Testing
│   ├── Write tests → test-runner
│   └── Review tests → test-reviewer
└── Review Only
    ├── Code → code-reviewer
    ├── Specs → spec-reviewer
    ├── Business → technical-pm
    └── Technical → architecture-review
```

## Capability Matrix

### By Tool Access

| Capability | Agents with Access |
|-----------|-------------------|
| **Write/Edit Files** | spec-enhancer, code-implementer, plan-enhancer, architecture-enhancer, handle-code-review |
| **Read Only** | All reviewers (spec-reviewer, code-reviewer, technical-pm, architecture-review) |
| **Run Commands** | test-runner, code-implementer, debugger |
| **Web Research** | spec-enhancer, technical-pm, architecture-review |

### By Workflow Phase

| Phase | Primary Agents | Support Agents |
|-------|---------------|----------------|
| **Planning** | spec-enhancer | spec-reviewer |
| **Design** | plan-enhancer, architecture-enhancer | technical-pm, architecture-review |
| **Implementation** | code-implementer | debugger, refactorer |
| **Testing** | test-runner | test-reviewer |
| **Review** | code-reviewer | handle-code-review |

## Agent Interaction Patterns

### Sequential Pattern
```
spec-enhancer → spec-reviewer → plan-enhancer → architecture-enhancer → code-implementer → test-runner → code-reviewer
```

### Review-Fix Pattern
```
code-reviewer → handle-code-review → code-reviewer (verify)
```

### Enhancement Pattern
```
plan-enhancer (business) → architecture-enhancer (technical) → technical-pm (validate)
```

## Common Workflows

### Feature Development
1. spec-enhancer - Create specification
2. plan-enhancer - Add business context
3. architecture-enhancer - Add technical details
4. code-implementer - Write code
5. test-runner - Create tests
6. code-reviewer - Review quality

### Bug Fix
1. debugger - Diagnose issue
2. code-implementer - Fix bug
3. test-runner - Add regression test
4. code-reviewer - Review fix

### Code Improvement
1. code-reviewer - Identify issues
2. refactorer - Clean up code
3. test-runner - Ensure no regression
4. code-reviewer - Verify improvements

## Best Practices

### DO ✅
- Use reviewers for validation
- Use enhancers for modifications
- Check performance tier before delegation
- Batch operations for heavy agents
- Follow sequential workflows

### DON'T ❌
- Use reviewers to modify files
- Skip review phases
- Use heavy agents for simple tasks
- Mix review and modification in one agent
- Create duplicate agents

## Quick Reference Card

### Most Used Agents
1. **code-implementer** - Main coding agent
2. **spec-enhancer** - Specification creation
3. **test-runner** - Test automation
4. **code-reviewer** - Quality gates
5. **debugger** - Problem solving

### By Frequency
- Daily: code-implementer, test-runner, code-reviewer
- Weekly: spec-enhancer, plan-enhancer
- As needed: debugger, refactorer
- Rarely: agent-architect, workflow

---

**Remember**: Choose agents based on whether you need to READ (reviewer) or MODIFY (enhancer/code-implementer).