# Agent Definition Input Template

**Purpose**: Use this template to define a new agent for the `/create-agent` command. Fill out all required sections completely to enable automatic agent generation with proper research, tool selection, and integration.

**📚 Need Help?** See **`docs/04-guides/agent-creation-guide.md`** for:
- Step-by-step instructions for filling out this template
- Complete examples (security-scanner, test-dataset-creator)
- Tips & best practices for agent design
- Command reference and workflow details

---

## 1. Basic Information

### Agent Name
**Format**: `[domain]-[action]` (e.g., `security-scanner`, `spec-reviewer`, `code-implementer`)

**Name**: _______________

**Naming Guidance**:
- **Domain Options**: security, spec, code, test, doc, research, git, config, deployment, monitoring, data, etc.
- **Action Options**: scanner, reviewer, implementer, enhancer, analyzer, runner, creator, validator, optimizer, monitor, etc.
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise

### Domain Scope
**Choose ONE that best fits** (determines which files/directories this agent operates on):

- [ ] `.claude/**` - Claude Code ecosystem (agents, commands, hooks, schemas)
- [ ] `packages/**` - Main codebase implementation (Python, scripts)
- [ ] `tests/**` - Test suite (unit tests, integration tests, test data)
- [ ] `docs/**` - Documentation and specifications
- [ ] `cross-domain` - Works across multiple directories (e.g., research, analysis)

**Selected**: _______________

**Directory Boundaries** (if not cross-domain, specify exact paths this agent can access):
- Read access: _______________
- Write access: _______________
- Forbidden paths: _______________

### Agent Type
**Choose ONE that best describes the primary work pattern**:

- [ ] **Creator** - Generates new artifacts (code, docs, specs, tests)
- [ ] **Reviewer** - Validates existing artifacts for quality, standards, correctness
- [ ] **Enhancer** - Improves existing artifacts (refactoring, optimization, enrichment)
- [ ] **Runner** - Executes operations (tests, builds, deployments, commands)
- [ ] **Analyzer** - Investigates and reports findings (patterns, issues, metrics)
- [ ] **Planner** - Creates plans, strategies, research delegation

**Selected**: _______________

---

## 2. Purpose & Description

### Orchestrator Description
**Instructions**: Write 1-3 sentences describing WHEN the orchestrator should call this agent. Focus on trigger conditions and context signals.

**Example**: "Performs static application security testing (SAST) on modified code using Semgrep to detect vulnerabilities before commit. Integrates with git workflow as a parallel quality gate alongside code-reviewer. Triggers automatically when files in packages/** are modified."

**Your Description**:
```
[Write your description here - be specific about triggers, context, and integration points]
```

### Value Proposition
**Instructions**: Explain WHY this agent is needed (what problem does it solve? what gap does it fill?).

**Example**: "Existing code-reviewer focuses on style and best practices but doesn't catch security vulnerabilities. This agent adds OWASP-focused security scanning to prevent CVEs from reaching production."

**Your Value Proposition**:
```
[What unique value does this agent provide?]
```

---

## 3. OODA Loop Integration

**Instructions**: Define how this agent will use the OODA loop framework for decision-making. See `.claude/docs/guides/patterns/ooda-loop-framework.md` for complete framework.

### Observe Phase
**What information does this agent gather before acting?**

**Examples**:
```
- File paths and modification timestamps
- Existing test coverage metrics
- Specification requirements from SPEC.md
- Available tools and their capabilities
```

**Your Agent's Observe Phase**:
```
[What signals, inputs, or context does your agent need to gather?]
```

### Orient Phase
**How does this agent assess context quality and complexity?**

**Examples**:
```
- Check if test fixtures exist for this algorithm
- Assess specification completeness (required sections present?)
- Classify task complexity (simple dataset vs. comprehensive coverage)
- Determine if external research needed (edge case patterns)
```

**Your Agent's Orient Phase**:
```
[How does your agent evaluate context and make sense of the situation?]
```

### Decide Phase
**What decision framework does this agent use?**

**Examples**:
```
- Select dataset generation strategy (random vs. specification-based)
- Choose validation approach (schema vs. algorithm execution)
- Determine confidence thresholds for synthetic data
- Plan fallback if specification parsing fails
```

**Your Agent's Decide Phase**:
```
[What decisions does your agent make and how?]
```

### Act Phase
**How does this agent execute and verify?**

**Examples**:
```
- Generate test datasets using selected strategy
- Validate outputs against schema
- Write fixtures to tests/fixtures/ directory
- Verify file creation and format compliance
```

**Your Agent's Act Phase**:
```
[What actions does your agent take and how does it verify success?]
```

---

## 4. Core Capabilities

**Instructions**: List 3-7 specific, actionable capabilities. Each should be a concrete task the agent performs.

**Format**: Use action verbs (analyzes, generates, validates, executes, detects, etc.)

**Examples**:
- ✅ GOOD: "Scans Python code for SQL injection vulnerabilities using Semgrep OWASP ruleset"
- ❌ BAD: "Handles security" (too vague)

**Your Capabilities**:
1. [Capability 1 - specific action with clear scope]
2. [Capability 2 - specific action with clear scope]
3. [Capability 3 - specific action with clear scope]
4. [Capability 4 - optional]
5. [Capability 5 - optional]
6. [Capability 6 - optional]
7. [Capability 7 - optional]

---

## 5. Input/Output Contract

### Expected Inputs
**Instructions**: Define what information the agent needs to do its work. Be specific about data types and validation requirements.

**Format**:
```
- **[input_field_name]**: [Description, data type, validation rules]
```

**Examples**:
```
- **files_to_scan**: List of absolute file paths (string[]) - must exist and be readable
- **scan_mode**: Enum ["fast", "comprehensive"] - determines ruleset selection
- **severity_threshold**: Enum ["critical", "high", "medium", "low"] - minimum severity to report
```

**Your Inputs**:
```
- **[input_1]**: [description, type, validation]
- **[input_2]**: [description, type, validation]
- **[input_3]**: [description, type, validation]
```

### Expected Outputs

#### On Success (Status: SUCCESS)
**Instructions**: Describe what the agent delivers when the operation completes successfully. Include structure, format, and key fields.

**Example**:
```
Security report (JSON) with:
- **findings**: Array of vulnerability objects (severity, confidence, location, remediation)
- **summary**: Aggregate counts by severity level
- **scan_metadata**: Files scanned, rules used, execution time
- **recommendations**: Prioritized action items for developer
```

**Your Success Output**:
```
[Describe structure, format, and key fields for successful execution]
```

#### On Failure (Status: FAILURE)
**Instructions**: Describe what information is provided when the operation fails. Include error categorization and recovery guidance.

**Example**:
```
Failure report (JSON) with:
- **failure_category**: Enum ["tool_error", "invalid_input", "file_access_error"]
- **error_details**: Specific error message and stack trace (if applicable)
- **recovery_suggestions**: Actionable steps to resolve the issue
- **partial_results**: Any findings collected before failure (optional)
```

**Your Failure Output**:
```
[Describe error structure, categorization, and recovery information]
```

---

## 6. Domain Knowledge & Expertise

### Required Frameworks/Standards
**Instructions**: List specific frameworks, methodologies, standards, or best practices this agent needs to understand. Be as specific as possible. If unknown, the command will research automatically.

**Examples**:
```
- OWASP Top 10 2021 (security vulnerabilities)
- Semgrep rule syntax and customization
- Python PEP 8 style guide (for code context understanding)
- Git pre-commit hook integration patterns
```

**Your Domain Knowledge** (optional - leave blank if unsure):
```
- [Framework/standard 1]
- [Framework/standard 2]
- [Framework/standard 3]
- [Framework/standard 4]
```

### Key Concepts & Terminology
**Instructions**: List domain-specific terms, jargon, or concepts the agent must understand.

**Examples**:
```
- Static Application Security Testing (SAST)
- Dynamic taint analysis
- False positive rate vs. false negative rate
- CVE (Common Vulnerabilities and Exposures)
```

**Your Key Concepts** (optional):
```
- [Concept 1]
- [Concept 2]
- [Concept 3]
```

---

## 7. Tool Requirements

**Instructions**: If you know which Claude Code tools this agent needs, list them with confidence scores (0.0-1.0) and rationale. Otherwise, leave blank and the command will recommend automatically.

**Available Tools**: Read, Write, Edit, Glob, Grep, Bash, WebFetch, Task

**Format**:
```
- **[Tool Name]** (confidence: [0.0-1.0], rationale: [why needed])
```

**Examples**:
```
- **Bash** (confidence: 1.0, rationale: Required to execute Semgrep CLI commands and parse JSON output)
- **Read** (confidence: 1.0, rationale: Must read code files to provide context in security reports)
- **Grep** (confidence: 0.8, rationale: Search for related vulnerability patterns across codebase for context)
- **Write** (confidence: 0.9, rationale: Generate security report artifacts in docs/ for review)
```

**Your Tool Requirements** (optional - leave blank if unsure):
```
- **[Tool 1]** (confidence: [0.0-1.0], rationale: [why])
- **[Tool 2]** (confidence: [0.0-1.0], rationale: [why])
- **[Tool 3]** (confidence: [0.0-1.0], rationale: [why])
```

**Tool Selection Guidance**:
- **Read** - Reading files, checking existence, gathering context
- **Write** - Creating new files, generating reports, writing artifacts
- **Edit** - Modifying existing files (prefer over Write for updates)
- **Glob** - Finding files by pattern (*.py, **/*.json, etc.)
- **Grep** - Searching file contents with regex patterns
- **Bash** - Executing shell commands (use sparingly, security risk)
- **WebFetch** - Fetching external documentation or resources
- **Task** - Delegating to other agents (for orchestrators/planners only)

---

## 8. Integration & Workflow

### Integration Points
**Instructions**: Describe how this agent fits into existing workflows, which agents it coordinates with, and any dependencies.

**Examples**:
```
- Runs in parallel with code-reviewer during pre-commit validation
- Triggered by git-github agent when files in packages/** are modified
- Failure blocks commit (validation gate) - escalates to debugger if issues found
- Success allows commit to proceed - reports sent to monitoring dashboard
```

**Your Integration Points** (optional):
```
[Describe workflow integration, agent coordination, and dependencies]
```

### Trigger Conditions
**Instructions**: Define when the orchestrator should invoke this agent.

**Examples**:
```
- ANY file in packages/** modified (auto-trigger)
- User runs /security command (manual trigger)
- Pre-commit hook validation phase (workflow trigger)
- Severity threshold: Run for all commits touching auth/security code
```

**Your Trigger Conditions**:
```
[When should orchestrator call this agent?]
```

### Performance Requirements
**Instructions**: Specify any time, token, or resource constraints.

**Examples**:
```
- Execution time: <60 seconds for typical changeset (5-10 files)
- Token budget: <50K tokens for scan + report generation
- Parallelization: Can run in parallel with other quality gates
- Failure tolerance: Must complete even if some files unreadable
```

**Your Performance Requirements** (optional):
```
[Time, token, or resource constraints]
```

---

## 9. Quality & Validation

### Success Criteria
**Instructions**: Define what "success" looks like for this agent. How do you measure quality of outputs?

**Examples**:
```
- All requested files scanned successfully
- Report contains actionable findings with remediation steps
- Confidence scores provided for each finding (0.0-1.0)
- False positive rate <10% based on manual review
- No critical vulnerabilities missed (measured against known CVE database)
```

**Your Success Criteria**:
```
[How do you measure quality and success?]
```

### Validation Checks
**Instructions**: List specific checks the agent should perform before reporting SUCCESS.

**Examples**:
```
- [ ] All input files exist and are readable
- [ ] Semgrep execution completed without errors
- [ ] Report validates against security-scanner.schema.json
- [ ] All findings include severity, confidence, and remediation
- [ ] No secrets or credentials exposed in report outputs
```

**Your Validation Checks**:
```
- [ ] [Validation check 1]
- [ ] [Validation check 2]
- [ ] [Validation check 3]
```

---

## 10. Edge Cases & Error Handling

### Known Edge Cases
**Instructions**: List scenarios where the agent might struggle or fail. This helps the command design better error handling.

**Examples**:
```
- Binary files in scan path (should skip gracefully)
- Files too large for Semgrep (>10MB - warn and skip)
- Network-dependent rules (may fail in offline mode)
- Mixed Python 2/3 codebases (different syntax rules)
```

**Your Edge Cases** (optional):
```
[Scenarios where agent might fail or behave unexpectedly]
```

### Error Recovery Strategy
**Instructions**: Describe how the agent should handle failures.

**Examples**:
```
- File access error → Skip file, log warning, continue scanning others
- Semgrep crash → Retry once, then fail with diagnostic info
- Rule parsing error → Fall back to default OWASP ruleset
- Timeout → Return partial results with timeout warning
```

**Your Error Recovery** (optional):
```
[How should agent handle failures and recover?]
```

---

## 11. Additional Context

### Security Considerations
**Instructions**: Any security-specific requirements or constraints?

**Examples**:
```
- Never expose file contents in reports (paths and line numbers only)
- Sanitize all user-provided inputs (file paths, regex patterns)
- Do not execute untrusted code during analysis
- Report storage must be readable only by authorized users
```

**Your Security Considerations** (optional):
```
[Security requirements, constraints, or concerns]
```

### Future Extensibility
**Instructions**: How might this agent evolve? What features might be added later?

**Examples**:
```
- Support for additional languages (JavaScript, Go, Rust)
- Custom rule authoring interface for project-specific patterns
- Integration with external vulnerability databases (CVE, NVD)
- Automated fix generation for common vulnerabilities
```

**Your Future Plans** (optional):
```
[Potential enhancements or extensions]
```

### Related Agents
**Instructions**: List existing agents this new agent is similar to, complements, or replaces.

**Examples**:
```
- Similar to: code-reviewer (both validate code quality)
- Complements: test-runner (security + correctness gates)
- Replaces: N/A (new capability)
```

**Your Related Agents** (optional):
```
[Similar, complementary, or superseded agents]
```

---

## 12. Model & Configuration

### Recommended Model
**Instructions**: Choose the Claude model based on task complexity.

- [ ] **sonnet** - Fast, efficient worker agent (simple, well-defined tasks)
- [ ] **sonnet** - Hybrid reasoning agent (complex decisions, multi-step workflows)

**Selected**: _______________

**Selection Guidance**:
- Use **sonnet** (worker) for: Scanning, parsing, formatting, validation, simple analysis
- Use **sonnet** (hybrid) for: Planning, research, complex debugging, multi-agent coordination

### Color Identifier
**Instructions**: Choose a visual color for this agent (helps distinguish in logs/UI).

**Options**: `purple`, `blue`, `green`, `yellow`, `red`

**Selected**: _______________

**Color Conventions**:
- **purple** - Research/analysis agents
- **blue** - Implementation/creation agents
- **green** - Validation/quality agents
- **yellow** - Warning/monitoring agents
- **red** - Critical/security agents

---

## 13. Completion Checklist

**Before submitting this template, verify**:

- [ ] Agent name follows `[domain]-[action]` format (kebab-case)
- [ ] Domain scope selected (`.claude/**`, `packages/**`, `docs/**`, `tests/**`, or `cross-domain`)
- [ ] Agent type selected (Creator, Reviewer, Enhancer, Runner, Analyzer, Planner)
- [ ] Orchestrator description written (1-3 sentences with trigger conditions)
- [ ] OODA loop integration defined (Observe, Orient, Decide, Act phases)
- [ ] Core capabilities listed (3-7 specific, actionable items)
- [ ] Input/output contract defined (structure, types, validation)
- [ ] Success criteria and validation checks specified
- [ ] Model selected (sonnet or sonnet based on complexity)
- [ ] Color identifier chosen (purple, blue, green, yellow, red)

**Optional but recommended**:
- [ ] Domain knowledge specified (frameworks, standards, concepts)
- [ ] Tool requirements listed (with confidence and rationale)
- [ ] Integration points described (workflow, triggers, dependencies)
- [ ] Edge cases and error recovery documented
- [ ] Security considerations noted
- [ ] Future extensibility plans outlined

---

## 14. Usage Instructions

### How to Use This Template

1. **Fill Out Template**:
   - Save this template to a new file: `my-agent-definition.md`
   - Complete all required sections (marked with "_______________")
   - Fill optional sections where you have knowledge

2. **Run Create Command**:
   ```bash
   /create-agent path/to/my-agent-definition.md
   ```

3. **Optional Flags**:
   ```bash
   # Provide additional context/documentation
   /create-agent my-agent-definition.md --context-dir=docs/security/

   # Preview without creating files (dry-run mode)
   /create-agent my-agent-definition.md --dry-run

   # Skip quality checks for rapid prototyping
   /create-agent my-agent-definition.md --skip-validation

   # Control template size (minimal, standard, comprehensive)
   /create-agent my-agent-definition.md --template=minimal
   ```

4. **What Happens Next**:
   - Command validates your input for completeness
   - Researches domain knowledge (if not provided)
   - Recommends tools based on capabilities
   - Generates agent definition (`.claude/agents/[name].md`)
   - Creates JSON schema (`.claude/docs/schemas/[name].schema.json`)
   - Updates integration documentation
   - Provides usage examples and testing guidance

5. **Review & Refine**:
   - Review generated agent definition
   - Test with sample inputs
   - Iterate and refine based on results

### Template Flags Explained

**`--context-dir=path/`**:
- Provides additional documentation for research
- Useful for domain-specific context (security policies, coding standards, etc.)
- Example: `--context-dir=docs/04-guides/security/`

**`--dry-run`**:
- Preview agent definition without creating files
- Validates input and shows research plan
- Safe for experimentation

**`--skip-validation`**:
- Bypasses quality checks (not recommended for production)
- Faster iteration during prototyping
- Use when you trust your input completely

**`--template=minimal|standard|comprehensive`**:
- **minimal**: ~8K tokens (core functionality only)
- **standard**: ~12K tokens (balanced, recommended)
- **comprehensive**: ~15K tokens (full documentation and examples)
- Controls agent definition verbosity

---

## 15. Examples

### Example 1: Security Scanner Agent

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
```

### Example 2: Test Dataset Creator Agent

```markdown
## 1. Basic Information
Name: test-dataset-creator
Domain Scope: tests/** (test suite)
Agent Type: Creator

## 2. Purpose & Description
Orchestrator Description:
"Generates comprehensive test datasets for algorithm validation based on specification requirements. Parses SPEC.md files to extract input/output examples, edge cases, and validation criteria, then creates structured JSON test data files in tests/fixtures/."

Value Proposition:
"Manual test data creation is time-consuming and error-prone. This agent automates dataset generation from specifications, ensuring comprehensive coverage of edge cases and validation requirements."

## 3. Core Capabilities
1. Parses SPEC.md files to extract algorithm requirements and validation criteria
2. Generates synthetic test data covering happy path, edge cases, and error scenarios
3. Creates structured JSON fixtures with expected outputs for validation
4. Validates generated datasets against schema definitions
5. Documents test data provenance and generation methodology

## 4. Input/Output Contract
Expected Inputs:
- **spec_file_path**: Absolute path to SPEC.md file (string)
- **dataset_size**: Number of test cases to generate (integer, 10-1000)
- **coverage_mode**: Enum ["edge_cases", "comprehensive", "performance"]

Expected Outputs (Success):
- **dataset_file_path**: Path to generated JSON fixture file
- **test_case_count**: Number of cases generated (integer)
- **coverage_report**: Categories covered (dict with counts)

Expected Outputs (Failure):
- **failure_category**: Enum ["spec_parsing_error", "generation_error", "validation_error"]
- **error_details**: Specific error with line numbers
- **partial_results**: Any test cases generated before failure
```

---

## Support & Questions

**Need Help?**
- **📚 COMPREHENSIVE GUIDE**: `docs/04-guides/agent-creation-guide.md` (step-by-step instructions, examples, tips)
- Check `.claude/templates/agent.template.md` for full agent structure reference
- See existing agents in `.claude/agents/` for inspiration (30+ examples)
- Ask orchestrator: "How do I create an agent for [use case]?"

**Template Issues?**
- Report template problems to agent-architect
- Suggest improvements via pull request
- Check `.claude/docs/changelog.md` for recent updates

---

**Template Version**: 1.0.0
**Last Updated**: 2025-10-22
**Compatible With**: Claude Code v1.0.111+, Template v5.0
