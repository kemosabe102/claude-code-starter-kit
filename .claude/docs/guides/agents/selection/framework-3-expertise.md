# Framework 3: Agent Expertise Mapping

**Core Principle**: Each agent has developed deep expertise in a specific domain or work type. Match task to agent whose expertise best fits. Don't just match technical capability—match domain knowledge.

## The Specialist Principle

### Why Specialists Matter

A generalist can edit any Markdown file. A specialist has developed:
- **Deep patterns** specific to their domain
- **Templates and structures** that ensure quality
- **Knowledge of pitfalls** in their area
- **Understanding of best practices** for their work type

Using the right specialist means better quality, faster execution, and fewer errors.

### Technical Capability vs Domain Expertise

**Anti-Pattern**: "code-implementer can edit any Python file, so use it for everything in `packages/**`"

**Why It's Wrong**:
- code-implementer specializes in **creating new code** (implementation work)
- debugger specializes in **investigating failures** (discovery work)

Both can technically edit Python files, but their **expertise differs**. code-implementer knows implementation patterns but doesn't have debugger's hypothesis-driven investigation framework.

**Better Approach**: Match work type to expertise specialization.

---

**Anti-Pattern**: "Anyone can edit Markdown files in `.claude/agents/`, so use code-implementer"

**Why It's Wrong**:
- Technical capability: Yes, code-implementer can edit .md files
- Domain expertise: No, code-implementer doesn't have agent-architect's understanding of:
  - Prompt engineering patterns
  - Agent simulation and evaluation
  - The 9-criteria quality matrix
  - Workflow integration patterns
  - Anthropic's agent design best practices

**Better Approach**: Don't ask "who can edit this file type?" Ask "who has expertise in this file's domain?"

---

## Domain Expertise Examples

**agent-architect** has expertise in:
- Prompt engineering (how to structure agent prompts)
- Agent evaluation (the 9-criteria matrix)
- Simulation-driven development
- Agent lifecycle (create → evaluate → update)
- Context7 integration for agent knowledge

This expertise doesn't transfer to Python implementation or specification writing.

---

**code-implementer** has expertise in:
- Python implementation patterns
- Code organization in `packages/**`
- Testing strategies for features
- Integration with existing code
- Pre-flight standards compliance

This expertise doesn't transfer to agent prompt design or specification structure.

---

**spec-enhancer** has expertise in:
- Specification structure (SPEC.md format)
- Requirements clarity and testability
- Component breakdown
- Planning metadata (regenerative development)
- Separating HOW from WHAT/WHY

This expertise doesn't transfer to code implementation or agent design.

---

## The Domain Alignment Principle

**Agents Are Shaped By Their Domains**:

An agent who has worked repeatedly in `.claude/agents/**` has developed mental models specific to agent lifecycle work. An agent who has worked repeatedly in `packages/**` has developed mental models specific to code implementation.

**Don't force an agent outside their shaped expertise** unless necessary.

**Recognition Pattern**: When selecting agent, think "has this agent's experience prepared them for this specific type of work?"

---

## Read-Only Research Workers

**Concept**: Domain specialists can serve as research workers when goal is investigation rather than implementation.

**How to Identify**:
1. Task includes "analyze", "investigate", "assess", "review"
2. Domain matches specialist's expertise area
3. Output should be findings/report, not file modifications

**Available Read-Only Specialists** (by domain):

**`.claude/agents/**` Domain**:
- agent-architect: Agent design analysis, prompt evaluation
- prompt-evaluator: Multi-dimensional prompt quality analysis

**`packages/**`, `tests/**`, `scripts/**` Domain**:
- debugger: Failure pattern analysis, test investigation
- code-implementer: Implementation pattern analysis (without implementing)
- code-reviewer: Code quality assessment, standards compliance
- test-creator: Test coverage/pattern analysis, test design patterns (read-only)
- test-executor: Test execution pattern analysis (read-only, no execution)
- test-dataset-creator: Test data pattern analysis (read-only)

**`docs/**` Domain**:
- spec-reviewer: Specification quality assessment
- technical-pm: Business alignment review (read-only mode)
- architecture-review: Technical architecture validation (read-only mode)
- plan-enhancer: Plan completeness analysis (read-only mode)

**`.claude/**` Ecosystem**:
- workflow: Workflow pattern analysis, hook/command investigation
- claude-code: Configuration analysis, ecosystem pattern discovery
- doc-librarian: Documentation health assessment

**Any Domain**:
- tech-debt-investigator: Technical debt analysis, duplication detection
- feature-analyzer: Multi-component dependency analysis
- intent-analyzer: Request complexity analysis
- context-readiness-assessor: Context quality assessment
- context-optimizer: Context usage analysis

**When to Use Domain Specialist vs. researcher-***:
- **Domain specialist**: Targeted analysis within single domain, deeper expertise needed
- **researcher-codebase**: Cross-domain pattern discovery, initial broad investigation
- **researcher-web**: External best practices, community knowledge
- **researcher-library**: Official library documentation, API references

**Example Delegation** (for researcher-lead):
```json
{
  "worker_type": "debugger",
  "worker_id": "debugger_auth_analysis",
  "specific_objective": "Analyze authentication failure patterns in test suite (READ-ONLY - no fixes)",
  "output_format": "Report: common failure types, frequency, affected test files",
  "tool_guidance": {
    "mode": "read-only",
    "tools": ["Read", "Grep"],
    "exclusions": ["Write", "Edit", "implementation"]
  }
}
```
