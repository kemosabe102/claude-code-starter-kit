# Agent Creation Guide

**Purpose**: Complete guide to creating production-ready AI agents using the `/create-agent` command and agent definition template.

**Quick Navigation**:
- [Quick Start](#quick-start) - Get started in 5 minutes
- [Agent Definition Template](#agent-definition-template) - Complete template with instructions
- [Step-by-Step Instructions](#step-by-step-instructions) - Detailed guidance
- [Examples](#examples) - Real-world agent examples
- [Command Reference](#command-reference) - All command options
- [Tips & Best Practices](#tips--best-practices) - Expert guidance

---

## Quick Start

**5-Minute Path to Your First Agent**:

1. **Copy the template**:
   ```bash
   # Template location: .claude/templates/agent-definition-input.template.md
   cp .claude/templates/agent-definition-input.template.md my-agent-definition.md
   ```

2. **Fill required sections** (takes ~3 minutes):
   - Agent name: `[domain]-[action]` (e.g., `security-scanner`)
   - Domain scope: Choose one (`.claude/**`, `packages/**`, `docs/**`, `tests/**`, `cross-domain`)
   - Agent type: Choose one (Creator, Reviewer, Enhancer, Runner, Analyzer, Planner)
   - Purpose: 1-3 sentences describing when orchestrator should call this agent
   - Core capabilities: 3-7 specific actions this agent performs

3. **Run creation command**:
   ```bash
   /create-agent my-agent-definition.md
   ```

4. **Review and refine**:
   - Command researches domain knowledge automatically
   - Interactive refinement at 2 decision points
   - Receives clear next steps after completion

5. **Restart Claude Code session** (required for new agents)

**That's it!** The command handles research, documentation generation, schema creation, and integration.

---

## Overview

### What is Agent Creation?

Agent creation is a **10-phase automated workflow** that transforms a high-level agent description into production-ready code:

```
User Input (agent-definition.md)
  ↓
Phase 1-2: Parse & Assess Requirements (orchestrator + agents)
  ↓
Phase 3-4: Research Domain Knowledge (researcher-* agents)
  ↓
Phase 5-6: Generate Documentation & Schema (doc-librarian, agent-architect)
  ↓
Phase 7-8: Build & Validate Agent (agent-architect, quality gates)
  ↓
Phase 9-10: Review & Finalize (technical-pm, integration updates)
  ↓
Production-Ready Agent + Schema + Documentation
```

**Time Efficiency**: 10-15 minutes end-to-end (8-12x faster than manual 2-3 hours)

**Quality Consistency**:
- Template compliance: 100%
- Schema validation: 100%
- Documentation coverage: ≥80% confidence
- Quality matrix score: ≥70%

---

## Interactive Mode (Recommended)

**Coming Soon**: `--create-definition` flag for interactive agent definition creation.

The interactive mode will guide you through filling out the template with prompts and examples.

For now, use **Manual Mode** below by filling out the template directly.

---

## Manual Mode

### Step-by-Step Instructions

#### Step 1: Basic Information

**Agent Name** (`[domain]-[action]` format):
- **Domain examples**: security, spec, code, test, doc, research, git, config, deployment, monitoring, data
- **Action examples**: scanner, reviewer, implementer, enhancer, analyzer, runner, creator, validator, optimizer, monitor
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise

**Good Examples**:
- ✅ `security-scanner` - Clear domain (security) + action (scanner)
- ✅ `test-dataset-creator` - Clear domain (test) + action (creator)
- ✅ `spec-enhancer` - Clear domain (spec) + action (enhancer)

**Bad Examples**:
- ❌ `scanner` - Missing domain (what kind of scanner?)
- ❌ `security_scanner` - Wrong format (use hyphens, not underscores)
- ❌ `SecurityScanner` - Wrong case (use lowercase)

**Domain Scope Selection**:

Choose ONE that best fits your agent's work:

| Scope | Description | Example Files |
|-------|-------------|---------------|
| `.claude/**` | Claude Code ecosystem | Agents, commands, hooks, schemas |
| `packages/**` | Main codebase | Python implementation, scripts |
| `tests/**` | Test suite | Unit tests, integration tests, test data |
| `docs/**` | Documentation | Specifications, plans, guides |
| `cross-domain` | Multiple directories | Research, analysis, cross-cutting concerns |

**Agent Type Selection**:

Choose ONE that best describes the primary work pattern:

| Type | Work Pattern | Example Agents |
|------|--------------|----------------|
| **Creator** | Generates new artifacts (code, docs, specs, tests) | code-implementer, test-dataset-creator, spec-enhancer |
| **Reviewer** | Validates existing artifacts for quality, standards, correctness | code-reviewer, spec-reviewer, architecture-review |
| **Enhancer** | Improves existing artifacts (refactoring, optimization, enrichment) | plan-enhancer, architecture-enhancer, refactorer |
| **Runner** | Executes operations (tests, builds, deployments, commands) | test-runner, git-github (for commit execution) |
| **Analyzer** | Investigates and reports findings (patterns, issues, metrics) | tech-debt-investigator, sast-scanner, feature-analyzer |
| **Planner** | Creates plans, strategies, research delegation | researcher-lead, contingency-planner |

#### Step 2: Purpose & Description

**Orchestrator Description** (1-3 sentences):

Focus on **WHEN** the orchestrator should call this agent. Include:
- Trigger conditions (what events/contexts activate this agent)
- Context signals (what information indicates this agent is needed)
- Integration points (how it fits with other agents)

**Good Example**:
> "Performs static application security testing (SAST) on modified code using Semgrep to detect OWASP Top 10 vulnerabilities before commit. Integrates with git workflow as a parallel quality gate alongside code-reviewer and tech-debt-investigator. Triggers automatically when files in packages/** are modified."

**Why Good?**:
- Clear trigger: "when files in packages/** are modified"
- Clear context: "before commit", "parallel quality gate"
- Clear integration: "alongside code-reviewer and tech-debt-investigator"
- Clear tool/approach: "using Semgrep to detect OWASP Top 10"

**Bad Example**:
> "Handles security scanning."

**Why Bad?**:
- Too vague - what kind of security scanning?
- No trigger conditions - when does it run?
- No integration context - how does it fit with other agents?
- No tool/approach specifics

**Value Proposition**:

Explain **WHY** this agent is needed:
- What problem does it solve?
- What gap does it fill?
- What unique value does it provide?

**Good Example**:
> "Existing code-reviewer focuses on style and best practices but doesn't catch security vulnerabilities. This agent adds OWASP-focused security scanning to prevent CVEs from reaching production, reducing security incidents by catching issues at commit time."

#### Step 3: Core Capabilities

List **3-7 specific, actionable capabilities**:

**Format Requirements**:
- Use action verbs (analyzes, generates, validates, executes, detects, etc.)
- Be specific about WHAT and HOW
- Include clear scope and boundaries

**Good Examples**:
- ✅ "Scans Python code for SQL injection vulnerabilities using Semgrep OWASP ruleset"
  - Action: Scans
  - What: Python code for SQL injection
  - How: Using Semgrep OWASP ruleset

- ✅ "Generates 20 diverse test scenarios from git history with stratified sampling by change type and file count"
  - Action: Generates
  - What: 20 diverse test scenarios
  - How: From git history with stratified sampling

**Bad Examples**:
- ❌ "Handles security" - Too vague (what security tasks?)
- ❌ "Creates tests" - Too vague (what kind of tests? how?)
- ❌ "Improves code quality" - Too vague (which quality aspects? how?)

#### Step 4: Input/Output Contract

**Expected Inputs**:

Define what information the agent needs to do its work:

**Format**:
```markdown
- **[input_field_name]**: [Description, data type, validation rules]
```

**Good Examples**:
```markdown
- **files_to_scan**: List of absolute file paths (string[]) - must exist and be readable
- **scan_mode**: Enum ["fast", "comprehensive"] - determines ruleset selection
- **severity_threshold**: Enum ["critical", "high", "medium", "low"] - minimum severity to report
- **baseline_commit**: Git commit hash (string, 7-40 chars) - for diff-aware scanning
```

**Expected Outputs - SUCCESS State**:

Describe what the agent delivers when the operation completes successfully:

**Good Example**:
```markdown
Security report (JSON) with:
- **findings**: Array of vulnerability objects (severity, confidence, location, remediation)
- **summary**: Aggregate counts by severity level
- **scan_metadata**: Files scanned, rules used, execution time
- **recommendations**: Prioritized action items for developer
- **group_results**: Per-group security status (APPROVED, APPROVED_WITH_WARNINGS, CHANGES_REQUIRED)
```

**Expected Outputs - FAILURE State**:

Describe what information is provided when the operation fails:

**Good Example**:
```markdown
Failure report (JSON) with:
- **failure_category**: Enum ["tool_error", "invalid_input", "file_access_error"]
- **error_details**: Specific error message and stack trace (if applicable)
- **recovery_suggestions**: Actionable steps to resolve the issue
- **partial_results**: Any findings collected before failure (optional)
```

#### Step 5: Domain Knowledge & Expertise

**Optional but Recommended** - Leave blank if unsure, the command will research automatically.

**Required Frameworks/Standards**:

List specific frameworks, methodologies, standards, or best practices this agent needs to understand:

**Good Examples**:
```markdown
- OWASP Top 10 2021 (security vulnerabilities)
- Semgrep rule syntax and customization
- Python PEP 8 style guide (for code context understanding)
- Git pre-commit hook integration patterns
```

**Key Concepts & Terminology**:

List domain-specific terms, jargon, or concepts the agent must understand:

**Good Examples**:
```markdown
- Static Application Security Testing (SAST)
- Dynamic taint analysis
- False positive rate vs. false negative rate
- CVE (Common Vulnerabilities and Exposures)
- Baseline diff scanning (only scan changed lines)
```

#### Step 6: Tool Requirements

**Optional** - Leave blank if unsure, the command will recommend automatically.

**Format**:
```markdown
- **[Tool Name]** (confidence: [0.0-1.0], rationale: [why needed])
```

**Available Tools**:
- **Read** - Reading files, checking existence, gathering context
- **Write** - Creating new files, generating reports, writing artifacts
- **Edit** - Modifying existing files (prefer over Write for updates)
- **Glob** - Finding files by pattern (*.py, **/*.json, etc.)
- **Grep** - Searching file contents with regex patterns
- **Bash** - Executing shell commands (use sparingly, security risk)
- **WebFetch** - Fetching external documentation or resources
- **Task** - Delegating to other agents (for orchestrators/planners only)

**Good Examples**:
```markdown
- **Bash** (confidence: 1.0, rationale: Required to execute Semgrep CLI commands and parse JSON output)
- **Read** (confidence: 1.0, rationale: Must read code files to provide context in security reports)
- **Grep** (confidence: 0.8, rationale: Search for related vulnerability patterns across codebase for context)
- **Write** (confidence: 0.9, rationale: Generate security report artifacts in docs/ for review)
```

#### Step 7: Integration & Workflow

**Integration Points** (optional):

Describe how this agent fits into existing workflows:

**Good Example**:
```markdown
- Runs in parallel with code-reviewer during pre-commit validation
- Triggered by git-github agent when files in packages/** are modified
- Failure blocks commit (validation gate) - escalates to debugger if issues found
- Success allows commit to proceed - reports sent to monitoring dashboard
```

**Trigger Conditions**:

Define when the orchestrator should invoke this agent:

**Good Example**:
```markdown
- ANY file in packages/** modified (auto-trigger)
- User runs /security command (manual trigger)
- Pre-commit hook validation phase (workflow trigger)
- Severity threshold: Run for all commits touching auth/security code
```

**Performance Requirements** (optional):

Specify any time, token, or resource constraints:

**Good Example**:
```markdown
- Execution time: <60 seconds for typical changeset (5-10 files)
- Token budget: <50K tokens for scan + report generation
- Parallelization: Can run in parallel with other quality gates
- Failure tolerance: Must complete even if some files unreadable
```

#### Step 8: Quality & Validation

**Success Criteria**:

Define what "success" looks like for this agent:

**Good Example**:
```markdown
- All requested files scanned successfully
- Report contains actionable findings with remediation steps
- Confidence scores provided for each finding (0.0-1.0)
- False positive rate <10% based on manual review
- No critical vulnerabilities missed (measured against known CVE database)
```

**Validation Checks**:

List specific checks the agent should perform before reporting SUCCESS:

**Good Example**:
```markdown
- [ ] All input files exist and are readable
- [ ] Semgrep execution completed without errors
- [ ] Report validates against security-scanner.schema.json
- [ ] All findings include severity, confidence, and remediation
- [ ] No secrets or credentials exposed in report outputs
```

#### Step 9: Edge Cases & Error Handling

**Known Edge Cases** (optional):

List scenarios where the agent might struggle or fail:

**Good Example**:
```markdown
- Binary files in scan path (should skip gracefully)
- Files too large for Semgrep (>10MB - warn and skip)
- Network-dependent rules (may fail in offline mode)
- Mixed Python 2/3 codebases (different syntax rules)
```

**Error Recovery Strategy** (optional):

Describe how the agent should handle failures:

**Good Example**:
```markdown
- File access error → Skip file, log warning, continue scanning others
- Semgrep crash → Retry once, then fail with diagnostic info
- Rule parsing error → Fall back to default OWASP ruleset
- Timeout → Return partial results with timeout warning
```

#### Step 10: Additional Context

**Security Considerations** (optional):

Any security-specific requirements or constraints:

**Good Example**:
```markdown
- Never expose file contents in reports (paths and line numbers only)
- Sanitize all user-provided inputs (file paths, regex patterns)
- Do not execute untrusted code during analysis
- Report storage must be readable only by authorized users
```

**Future Extensibility** (optional):

How might this agent evolve?

**Good Example**:
```markdown
- Support for additional languages (JavaScript, Go, Rust)
- Custom rule authoring interface for project-specific patterns
- Integration with external vulnerability databases (CVE, NVD)
- Automated fix generation for common vulnerabilities
```

**Related Agents** (optional):

List existing agents this new agent is similar to, complements, or replaces:

**Good Example**:
```markdown
- Similar to: code-reviewer (both validate code quality)
- Complements: test-runner (security + correctness gates)
- Replaces: N/A (new capability)
```

#### Step 11: Model & Configuration

**Recommended Model**:

Choose the Claude model based on task complexity:

- ☑ **sonnet** - Fast, efficient worker agent (simple, well-defined tasks)
- ☐ **sonnet** - Hybrid reasoning agent (complex decisions, multi-step workflows)

**Selection Guidance**:
- Use **sonnet** (worker) for: Scanning, parsing, formatting, validation, simple analysis
- Use **sonnet** (hybrid) for: Planning, research, complex debugging, multi-agent coordination

**Color Identifier**:

Choose a visual color for this agent (helps distinguish in logs/UI):

**Color Conventions**:
- **purple** - Research/analysis agents
- **blue** - Implementation/creation agents
- **green** - Validation/quality agents
- **yellow** - Warning/monitoring agents
- **red** - Critical/security agents

---

## Agent Definition Template

**Complete template with all sections and instructions:**

See `.claude/templates/agent-definition-input.template.md` for the full template.

**Template location**: `.claude/templates/agent-definition-input.template.md`

**Quick copy command**:
```bash
cp .claude/templates/agent-definition-input.template.md my-agent-definition.md
```

**Key sections to fill out**:
1. Basic Information (name, domain, type)
2. Purpose & Description (when to call, why needed)
3. Core Capabilities (3-7 specific actions)
4. Input/Output Contract (structure, types, validation)
5. Domain Knowledge (frameworks, concepts) - optional
6. Tool Requirements (with confidence and rationale) - optional
7. Integration & Workflow (triggers, coordination) - optional
8. Quality & Validation (success criteria, checks)
9. Edge Cases & Error Handling (scenarios, recovery) - optional
10. Additional Context (security, future plans) - optional
11. Model & Configuration (model selection, color)

---

## Examples

### Example 1: Security Scanner Agent (Analyzer)

**Use Case**: SAST scanning for security vulnerabilities before commit

**Key Highlights**:
- **Domain**: `packages/**` (main codebase)
- **Type**: Analyzer (investigates and reports security findings)
- **Tools**: Bash (Semgrep CLI), Read, Grep
- **Integration**: Parallel quality gate with code-reviewer

**Template Excerpt**:
```markdown
## 1. Basic Information
Name: security-scanner
Domain Scope: packages/** (main codebase)
Agent Type: Analyzer

## 2. Purpose & Description
Orchestrator Description:
"Performs static application security testing (SAST) on modified code using Semgrep to detect OWASP Top 10 vulnerabilities before commit. Integrates with git workflow as a parallel quality gate alongside code-reviewer. Triggers automatically when files in packages/** are modified."

Value Proposition:
"Existing code-reviewer focuses on style and best practices but doesn't catch security vulnerabilities. This agent adds OWASP-focused security scanning to prevent CVEs from reaching production."

## 3. Core Capabilities
1. Scans Python code for SQL injection vulnerabilities using Semgrep OWASP ruleset
2. Detects insecure deserialization patterns and command injection risks
3. Validates authentication/authorization implementation against OWASP guidelines
4. Generates security reports with severity scoring and remediation steps
5. Integrates with pre-commit workflow as validation gate

## 4. Input/Output Contract
Expected Inputs:
- **files_to_scan**: List of absolute file paths (string[]) - must exist and be readable
- **scan_mode**: Enum ["fast", "comprehensive"] - determines ruleset selection
- **severity_threshold**: Enum ["critical", "high", "medium", "low"] - minimum severity to report

Expected Outputs (Success):
Security report (JSON) with:
- **findings**: Array of vulnerability objects (severity, confidence, location, remediation)
- **summary**: Aggregate counts by severity level
- **scan_metadata**: Files scanned, rules used, execution time

Expected Outputs (Failure):
- **failure_category**: Enum ["tool_error", "invalid_input", "file_access_error"]
- **error_details**: Specific error message and stack trace
- **recovery_suggestions**: Actionable steps to resolve issue

## 5. Domain Knowledge & Expertise
Required Frameworks/Standards:
- OWASP Top 10 2021 (security vulnerabilities)
- Semgrep rule syntax and customization
- CWE (Common Weakness Enumeration)
- Python security patterns (Django, Flask, FastAPI)

Key Concepts & Terminology:
- Static Application Security Testing (SAST)
- Baseline diff scanning (only scan changed lines)
- False positive vs false negative rates
- CVE (Common Vulnerabilities and Exposures)
```

**See Full Agent**: `.claude/agents/sast-scanner.md`

---

### Example 2: Test Dataset Creator Agent (Creator)

**Use Case**: Generate algorithm validation test datasets from git history

**Key Highlights**:
- **Domain**: `tests/**` (test suite)
- **Type**: Creator (generates new test data artifacts)
- **Tools**: Bash (git log), Write, Grep, Glob, TodoWrite
- **Integration**: Upstream to test-runner for validation

**Template Excerpt**:
```markdown
## 1. Basic Information
Name: test-dataset-creator
Domain Scope: tests/** (test suite)
Agent Type: Creator

## 2. Purpose & Description
Orchestrator Description:
"Generates comprehensive test datasets for algorithm validation based on specification requirements. Parses SPEC.md files to extract input/output examples, edge cases, and validation criteria, then creates structured JSON test data files in tests/fixtures/. Automates 4-6 hours of manual test data creation."

Value Proposition:
"Manual test data creation is time-consuming and error-prone. This agent automates dataset generation from specifications and git history, ensuring comprehensive coverage of edge cases and validation requirements with simulated expert ground truth."

## 3. Core Capabilities
1. Mines git history for diverse commit scenarios with stratified sampling
2. Generates synthetic test data covering happy path, edge cases, and error scenarios
3. Creates structured JSON fixtures with expected outputs for validation
4. Applies domain heuristics to simulate expert ground truth decisions
5. Validates generated datasets against diversity metrics (≥0.80 score)

## 4. Input/Output Contract
Expected Inputs:
- **spec_file_path**: Absolute path to SPEC.md file (string)
- **dataset_size**: Number of test cases to generate (integer, 10-1000)
- **coverage_mode**: Enum ["edge_cases", "comprehensive", "performance"]
- **diversity_targets**: Distribution targets for change types and file counts

Expected Outputs (Success):
- **dataset_file_path**: Path to generated JSON fixture file
- **test_case_count**: Number of cases generated (integer)
- **coverage_report**: Categories covered (dict with counts)
- **diversity_metrics**: Actual distribution vs targets
- **quality_validation**: Diversity score, edge case coverage, quality grade

Expected Outputs (Failure):
- **failure_category**: Enum ["spec_parsing_error", "generation_error", "validation_error", "insufficient_diversity"]
- **error_details**: Specific error with line numbers
- **partial_results**: Any test cases generated before failure
- **recovery_suggestions**: Expand git log, create synthetic scenarios, lower requirements
```

**See Full Agent**: `.claude/agents/test-dataset-creator.md`

---

## Command Reference

### Basic Usage

```bash
# Required argument: agent definition file
/create-agent path/to/agent-definition.md
```

### Optional Flags

#### `--context-dir=<path>`

Provides additional documentation for research.

**Use when**:
- You have domain-specific context (security policies, coding standards, etc.)
- You want to bias research toward specific sources
- You have existing documentation to incorporate

**Example**:
```bash
/create-agent my-agent-definition.md --context-dir=docs/04-guides/security/
```

**What it does**:
- Analyzes files in provided directory for frameworks and processes
- Maps findings to agent requirements from definition
- Reduces external research needs if context is comprehensive

---

#### `--dry-run`

Previews agent definition without creating files.

**Use when**:
- Experimenting with agent design
- Validating definition quality before committing
- Testing different configurations

**Example**:
```bash
/create-agent my-agent-definition.md --dry-run
```

**What it does**:
- Executes all phases through Phase 9 (interactive review)
- Does NOT write any files in Phase 10
- Presents complete summary of what WOULD be created
- User can review before running without --dry-run

---

#### `--skip-validation`

Bypasses quality checks for rapid prototyping.

**Use when**:
- Iterating quickly on agent design
- Trust your input completely
- Need faster turnaround for experimentation

**Example**:
```bash
/create-agent my-agent-definition.md --skip-validation
```

**⚠️ Not recommended for production** - may produce lower quality agents.

---

#### `--template=<minimal|standard|comprehensive>`

Controls agent definition verbosity.

**Options**:
- **minimal**: ~8K tokens (core functionality only)
- **standard**: ~12K tokens (balanced, recommended)
- **comprehensive**: ~15K tokens (full documentation and examples)

**Use when**:
- Minimal: Simple, well-defined agents with clear scope
- Standard: Most agents (default, good balance)
- Comprehensive: Complex agents with many integration points

**Example**:
```bash
/create-agent my-agent-definition.md --template=minimal
```

---

### Multi-Phase Workflow

The command executes **10 phases automatically**:

| Phase | Description | Time | Agents Used |
|-------|-------------|------|-------------|
| 1 | Parse & Validate | 30s | researcher-codebase, claude-code, tech-debt-investigator |
| 2 | Assess Requirements | 1 min | context-readiness-assessor |
| 3 | Review Context | 30s | researcher-codebase (if --context-dir provided) |
| 4 | Research Gaps | 2-3 min | researcher-lead (planning), researcher-* (execution) |
| 5 | Organize Documentation | 2 min | doc-librarian (parallel, max 5) |
| 6 | Design Schema | 1 min | agent-architect |
| 7 | Build Agent | 2 min | agent-architect |
| 8 | Validate Quality | 1 min | agent-architect, claude-code, tech-debt-investigator |
| 9 | Interactive Review | Variable | technical-pm, user interaction |
| 10 | Finalize & Integrate | 1 min | agent-architect, technical-pm |

**Total**: 10-15 minutes end-to-end

---

## Tips & Best Practices

### Naming Conventions

**✅ DO**:
- Use `[domain]-[action]` format
- Use kebab-case (lowercase with hyphens)
- Be specific and descriptive
- Group related agents with common prefix (e.g., `researcher-*`)

**❌ DON'T**:
- Use underscores or camelCase
- Use generic names without domain context
- Use abbreviations or acronyms without clarity
- Mix separators (hyphens and underscores)

**Good Examples**:
- `security-scanner`, `test-dataset-creator`, `spec-enhancer`
- `researcher-codebase`, `researcher-web`, `researcher-lead` (grouped)

---

### Domain Scope Selection

**Rule of Thumb**: Match domain to file location

| If agent primarily works with... | Choose domain... |
|----------------------------------|------------------|
| `.claude/agents/**` | `.claude/**` |
| `packages/**/*.py` | `packages/**` |
| `tests/**` | `tests/**` |
| `docs/**` | `docs/**` |
| Multiple directories | `cross-domain` |

**Why it matters**:
- Affects permission boundaries
- Determines integration patterns
- Influences tool selection
- Sets coordination expectations

---

### Agent Type Selection

**Decision Tree**:

```
Does agent CREATE new artifacts?
├─ YES → Creator
└─ NO → Does agent VALIDATE existing artifacts?
    ├─ YES → Reviewer
    └─ NO → Does agent IMPROVE existing artifacts?
        ├─ YES → Enhancer
        └─ NO → Does agent EXECUTE operations?
            ├─ YES → Runner
            └─ NO → Does agent ANALYZE and REPORT?
                ├─ YES → Analyzer
                └─ NO → Does agent CREATE PLANS?
                    ├─ YES → Planner
                    └─ UNSURE → Ask for guidance
```

**Type Characteristics**:

| Type | Typical Tools | Typical Outputs | Example Operations |
|------|---------------|-----------------|-------------------|
| Creator | Write, Edit, Task | New files, generated code | Implement feature, generate spec |
| Reviewer | Read, Grep | Quality reports, recommendations | Code review, spec validation |
| Enhancer | Read, Edit | Improved artifacts | Refactor code, enrich plans |
| Runner | Bash, Read | Execution results | Run tests, execute commands |
| Analyzer | Read, Grep, Bash | Analysis reports, metrics | Security scan, tech debt analysis |
| Planner | Read, Task | Plans, strategies | Research coordination, contingency plans |

---

### Core Capabilities Writing

**Formula**: `[Action Verb] + [What] + [How/Context]`

**Good Examples**:
- "Scans Python code for SQL injection vulnerabilities using Semgrep OWASP ruleset"
  - Action: Scans
  - What: Python code for SQL injection vulnerabilities
  - How: Using Semgrep OWASP ruleset

- "Generates 20 diverse test scenarios from git history with stratified sampling"
  - Action: Generates
  - What: 20 diverse test scenarios
  - How: From git history with stratified sampling

**Avoid**:
- Generic verbs without specifics ("handles", "manages", "processes")
- Vague scope ("all files", "any code", "everything")
- Missing implementation details (no "how")

---

### Tool Selection Guidelines

**Start with Read** - Almost all agents need to read files.

**Add Write/Edit**:
- Write: Creating NEW files (reports, artifacts, generated code)
- Edit: Modifying EXISTING files (updates, fixes, enhancements)

**Consider Bash**:
- ⚠️ Security risk - use sparingly
- Required for CLI tools (git, semgrep, pytest, etc.)
- Necessary for system operations (file stats, environment checks)

**Add Grep/Glob**:
- Grep: Content search with regex (find patterns in files)
- Glob: File discovery with patterns (find files by name)

**Use Task** (orchestrators/planners only):
- Delegates to other agents
- Coordinates multi-agent workflows
- Only for agents that spawn sub-agents

**Use WebFetch** (research agents):
- Fetches external documentation
- Queries web resources
- Requires justification for security

---

### Input/Output Contract Design

**Input Best Practices**:
- Be specific about data types (string, integer, array, enum)
- Include validation rules (min/max, patterns, required/optional)
- Document edge cases (empty arrays, null values, special characters)

**Output Best Practices**:
- Define SUCCESS structure (what deliverables?)
- Define FAILURE structure (what error categories?)
- Include confidence scores (0.0-1.0 range)
- Add recommendations (actionable next steps)

**Example Template**:
```json
{
  "status": "SUCCESS | FAILURE",
  "agent": "agent-name",
  "confidence": 0.92,
  "execution_timestamp": "ISO-8601",
  "summary": "Brief overview",
  "agent_specific_output": {
    // SUCCESS: Agent's deliverables
  },
  "failure_details": {
    // FAILURE: Error categorization and recovery
  }
}
```

---

### Research Requirements

**When to provide domain knowledge**:
- ✅ Provide if you have specific frameworks/standards in mind
- ✅ Provide if domain is niche or specialized
- ✅ Provide if external docs are hard to find
- ❌ Skip if domain is common (command will research)
- ❌ Skip if unsure (better to let command research)

**Research happens automatically**:
- Phase 4 executes targeted research for gaps
- researcher-lead creates delegation plan
- researcher-* workers execute in parallel
- Confidence threshold: ≥0.7 per topic

---

### Quality Validation

**Target Scores**:
- Template compliance: 100% (mandatory)
- Schema validation: 100% (mandatory)
- Quality matrix: ≥70% (passing grade)
- Documentation coverage: ≥80% confidence

**If quality score <70%**:
- Command offers auto-fix or manual refinement
- Re-validation after fixes
- User decides to proceed or cancel

**Quality Matrix Dimensions** (9 criteria, 0-5 scale):
1. Role clarity and boundary definition
2. Schema integration quality
3. Reasoning approach sophistication
4. Tool usage appropriateness
5. Error recovery completeness
6. Output optimization
7. Integration point clarity
8. Documentation references
9. Validation coverage

---

### Integration Considerations

**Think about**:
- Which agents will this work WITH? (parallel execution)
- Which agents will this work AFTER? (sequential dependencies)
- What triggers should activate this agent? (auto, manual, workflow)
- What performance constraints exist? (time, tokens, resources)

**Common Integration Patterns**:
- **Parallel Quality Gates**: code-reviewer + tech-debt-investigator + sast-scanner
- **Sequential Workflow**: spec-enhancer → task-creator → code-implementer
- **Research Coordination**: researcher-lead → researcher-* workers → synthesis
- **Fix-Review Loop**: code-implementer → code-reviewer → (if fail) → code-implementer

---

### Common Pitfalls

**❌ AVOID**:

1. **Too Broad Scope**
   - Problem: "Handles all security" (what security tasks specifically?)
   - Fix: "Scans Python code for OWASP Top 10 vulnerabilities using Semgrep"

2. **Missing Trigger Conditions**
   - Problem: No clear when/how orchestrator should call this agent
   - Fix: "Triggers automatically when files in packages/** are modified"

3. **Vague Capabilities**
   - Problem: "Manages code quality" (how? what aspects?)
   - Fix: "Validates PEP 8 compliance and detects code smells using Ruff"

4. **Wrong Agent Type**
   - Problem: Calling a Creator agent a Reviewer (creates confusion)
   - Fix: Match type to PRIMARY work pattern

5. **Tool Overload**
   - Problem: Requesting 8+ tools "just in case"
   - Fix: Select 3-5 essential tools with clear rationale

6. **No Error Handling**
   - Problem: Only defining SUCCESS path
   - Fix: Define FAILURE structure with recovery suggestions

---

## What Happens Next?

After running `/create-agent my-agent-definition.md`, you'll see:

### Phase 1-2: Requirements (1.5 minutes)
```
✅ Agent definition parsed (security-scanner)
✅ Domain scope validated (packages/**)
✅ No duplicate agents found
✅ Information requirements identified (12 topics)

Options:
1. ✅ Proceed with all high + medium confidence topics (9 topics)
2. 🔧 Modify list (add/remove topics)
3. 📊 Research all topics including low-confidence (12 topics)
```

### Phase 3-4: Research (3-4 minutes)
```
Research Results:

Topic: OWASP Top 10 2021
Confidence: 0.95
Sources: 3 (OWASP official docs, Semgrep rules, GitHub examples)
Key Findings:
- A03:2021 - Injection covers SQL injection, command injection, XSS
- Python-specific patterns available in Semgrep p/security-audit ruleset
- CWE mapping provided for common weakness enumeration

... (8 more topics)
```

### Phase 5-6: Documentation & Schema (3 minutes)
```
Documentation Generated:
.claude/docs/guides/security-scanner/
├── security-patterns.md (OWASP Top 10, CWE mapping)
├── development-workflows.md (Semgrep integration, pre-commit hooks)
└── domain-knowledge.md (SAST concepts, tool usage)

Schema Created:
.claude/docs/schemas/security-scanner.schema.json
- Extends base-agent.schema.json
- Defines agent_specific_output structure (findings, scan_summary, group_results)
- Defines failure_details structure (failure_type, recovery_suggestions)
```

### Phase 7-8: Build & Validate (3 minutes)
```
Agent Created:
.claude/agents/security-scanner.md

Quality Validation:
✅ Template Compliance: PASS
✅ Naming Conventions: PASS
✅ Duplication Check: PASS (no overlap detected)

Quality Matrix Score: 82/100
- Role Clarity: 5/5
- Schema Integration: 4/5
- Reasoning Approach: 4/5
- Tool Usage: 5/5
- Error Recovery: 4/5
- Output Optimization: 3/5
- Integration Points: 5/5
- Documentation: 5/5
- Validation: 4/5
```

### Phase 9: Interactive Review
```
# Security Scanner - Ready for Review

**Type**: Analyzer
**Domain**: packages/** (main codebase)

**Orchestrator Description**:
"Performs static application security testing (SAST) on modified code using Semgrep to detect OWASP Top 10 vulnerabilities before commit..."

**Core Capabilities**:
- Scans Python code for SQL injection vulnerabilities (confidence: 0.95)
- Detects insecure deserialization patterns (confidence: 0.92)
...

**Tools**: Bash, Read, Grep
**Rationale**: Bash for Semgrep CLI execution, Read for code context, Grep for pattern analysis

**Documentation**:
- 3 framework guides created (OWASP, Semgrep, Git workflow)
- Security patterns integrated

**Quality Score**: 82/100
- ✅ Template compliant
- ✅ No duplicates found
- ⚠️  Recommendation: Consider adding output compression techniques

---

Options:
1. ✅ Approve and finalize
2. 🔧 Refine specific sections
3. 📝 Add additional documentation
4. 🔄 Re-evaluate after manual changes
5. ❌ Cancel creation
```

### Phase 10: Finalization
```
# Agent Creation Complete: security-scanner

## Files Created
- ✅ Agent: .claude/agents/security-scanner.md
- ✅ Schema: .claude/docs/schemas/security-scanner.schema.json
- ✅ Documentation: .claude/docs/guides/security-scanner/ (3 files)

## Integrations Updated
- ✅ CLAUDE.md (delegation table)
- ✅ orchestrator-workflow.md (agent legend)
- ✅ agent-categorization.md
- ✅ DOC-INDEX.md

## Quality Metrics
- Quality Score: 82/100
- Template Compliance: ✅
- Naming Convention: ✅
- Duplication Check: ✅
- Schema Validation: ✅

## Next Steps
1. ⚠️  RESTART Claude Code session (new agent requires restart)
2. Test agent with sample task:
   ```
   Task(subagent_type="security-scanner", prompt="""
   Scan packages/core/auth/validators.py for security vulnerabilities.
   Report findings with OWASP classification and remediation steps.
   """)
   ```
3. Monitor performance and iterate if needed

---

Agent is ready for use after session restart!
```

---

## Support & Questions

### Need Help?

**Documentation References**:
- **Agent Template**: `.claude/templates/agent.template.md` (structure reference)
- **Input Template**: `.claude/templates/agent-definition-input.template.md` (this template)
- **Command Definition**: `.claude/commands/create-agent.md` (10-phase workflow)
- **Agent Standards**: `.claude/docs/agent-standards-runtime.md` (quality requirements)
- **Existing Agents**: `.claude/agents/` (30+ examples for inspiration)

**Ask the Orchestrator**:
- "How do I create an agent for [use case]?"
- "Show me examples of [agent type] agents"
- "What tools does [similar agent] use?"
- "Help me fill out the agent definition template"

### Template Issues?

**Report Problems**:
- Delegate to agent-architect: "Report template issue: [description]"
- Suggest improvements via pull request
- Check `.claude/docs/changelog.md` for recent updates

### Common Questions

**Q: How long does agent creation take?**
A: 10-15 minutes end-to-end (8-12x faster than manual 2-3 hours)

**Q: What if I don't know the domain knowledge?**
A: Leave that section blank - Phase 4 research will fill it automatically

**Q: Can I modify the agent after creation?**
A: Yes! Use `/create-agent [name] --operation=update` or edit manually

**Q: What if my agent fails quality validation?**
A: Command offers auto-fix or manual refinement options. You can iterate until passing.

**Q: Do I need to restart Claude Code after creation?**
A: Yes - new agent files require session restart to be recognized

**Q: Can I preview before creating?**
A: Yes - use `--dry-run` flag to see what would be created without writing files

---

## Related Documentation

**Essential Reading**:
- **CLAUDE.md** - Agent selection framework and delegation patterns
- **.claude/docs/orchestrator-workflow.md** - How agents coordinate
- **.claude/docs/agent-standards-runtime.md** - Quality requirements
- **.claude/docs/guides/agent-selection-guide.md** - 30+ scenario mappings

**Advanced Topics**:
- **.claude/docs/guides/tool-design-patterns.md** - Tool description best practices
- **.claude/docs/guides/documentation-context-loading.md** - Context hierarchy patterns
- **.claude/docs/guides/agent-categorization.md** - Agent taxonomy
- **docs/01-planning/custom/confidence-based-delegation-framework.md** - DCS scoring

---

**Template Version**: 1.0.0
**Last Updated**: 2025-10-22
**Compatible With**: Claude Code v1.0.111+, Template v5.0
