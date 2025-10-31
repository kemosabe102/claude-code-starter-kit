---
description: Create a new AI agent with systematic research, documentation, and validation
arguments:
  - name: agent-definition-file
    description: Path to agent definition file (optional if using --create-definition)
    required: false
    type: path
  - name: --create-definition
    description: Interactive mode to create agent definition from idea (output path required)
    required: false
    type: path
    example: /create-agent --create-definition my-agent-definition.md
  - name: --context-dir
    description: Directory containing additional context files
    required: false
    type: path
  - name: --dry-run
    description: Preview agent without writing files
    required: false
    type: flag
  - name: --skip-validation
    description: Skip quality matrix validation (rapid prototyping)
    required: false
    type: flag
  - name: --template
    description: Token budget control (minimal|standard|comprehensive)
    required: false
    type: enum
    default: standard
allowed_tools: Read, Write, Edit, Glob, Grep, Task, TodoWrite, WebSearch, WebFetch, mcp__context7__resolve-library-id, mcp__context7__get-library-docs
model: sonnet
color: purple
---

# /create-agent - Systematic AI Agent Creation

**Purpose**: Create production-ready AI agents with automated research, documentation generation, schema creation, and quality validation.

**Design Philosophy**:
- Delegation-first architecture (orchestrator coordinates, agents execute)
- Research-driven (auto-discover domain knowledge requirements)
- Quality-enforced (template compliance, naming conventions, duplication checks)
- User-friendly (interactive refinement, clear next steps)

---

## CRITICAL: ORCHESTRATOR DELEGATION PRINCIPLE

The orchestrator (Claude Code) **ORCHESTRATES, NEVER EXECUTES**.

For **EVERY task in EVERY phase**:
1. ✅ Identify the work to be done
2. ✅ Select appropriate sub-agent using [Agent Selection Framework](../../../CLAUDE.md#-agent-selection-framework)
3. ✅ Delegate using `Task(subagent_type="[agent]", prompt="...")`
4. ✅ Synthesize results from agents
5. ✅ Make phase transition decisions

**Orchestrator's ONLY responsibilities**:
- Read command parameters
- Coordinate agent delegation
- Synthesize agent outputs
- Present choices to user
- Track progress with TodoWrite
- Make phase transition decisions

❌ **Orchestrator should NEVER**:
- Read files directly (use researcher-codebase or appropriate agent)
- Parse content itself (delegate to appropriate agent)
- Validate structure itself (delegate to validator agent)
- Generate documentation itself (delegate to doc-librarian)
- Create files itself (delegate to agent-architect or appropriate agent)

**Every phase below specifies which agent to use for each task.**

---

## Command Usage

```bash
# Basic usage (required)
/create-agent path/to/agent-definition.md

# With optional context
/create-agent path/to/agent-definition.md --context-dir=docs/security/

# Preview without creating
/create-agent path/to/agent-definition.md --dry-run

# Rapid prototyping
/create-agent path/to/agent-definition.md --skip-validation

# Control token budget
/create-agent path/to/agent-definition.md --template=minimal
```

### Interactive Mode (NEW)

**Purpose**: Create agent definition interactively from a simple idea without needing to understand the complete template structure.

**Usage**:
```bash
# Interactive definition creation only
/create-agent --create-definition path/to/my-agent-definition.md

# Interactive with context directory
/create-agent --create-definition my-agent.md --context-dir=docs/security/

# Interactive with dry-run (preview without creating agent)
/create-agent --create-definition my-agent.md --dry-run
```

**Workflow**:
1. User provides 2-3 sentence idea
2. agent-architect analyzes and proposes structure
3. Interactive Q&A refines proposal
4. Definition file generated
5. User chooses: proceed immediately, review first, or regenerate

**Time**: 5-10 minutes (vs. 30-60 minutes manual template filling)

**See**: `.claude/docs/guides/interactive-agent-definition-workflow.md` for complete workflow specification.

---

## Input File Template

Users must create an agent definition file using the template at:
`.claude/templates/agent-definition-input.template.md`

**Template includes**:
- Agent metadata (name, domain, type)
- Purpose and orchestrator description
- Core capabilities
- Expected inputs/outputs
- Domain knowledge requirements (optional)
- Tool requirements (optional)
- Integration points (optional)

### Creating Definition Files

**Option 1: Interactive Mode** (Recommended for first-time users)
```bash
/create-agent --create-definition my-agent.md
```
- Guided Q&A from simple idea to complete definition
- No need to study template structure beforehand
- Confidence-scored recommendations
- Automatic proposal generation

**Option 2: Manual Template Filling** (For experienced users)
- Copy `.claude/templates/agent-definition-input.template.md`
- Fill out all sections manually
- Requires understanding of template structure
- More control, but higher time investment

---

## Interactive Agent Definition Creation (NEW)

**When to Use**: Creating a new agent without prior knowledge of template structure.

**Entry Point**: `/create-agent --create-definition output.md`

**5-Phase Interactive Workflow**:

### Phase 1: Capture User Idea
- **Goal**: Extract core agent concept in 2-3 sentences
- **User Action**: Describe what problem agent solves, what it does, when to call it
- **Time**: 1-2 minutes

### Phase 2: Analyze Idea & Propose Structure
- **Goal**: Transform informal idea into structured proposal
- **Delegation**: agent-architect (analyze_agent_idea operation)
- **Output**: Confidence-scored recommendations for:
  - Agent name options (2-3 choices)
  - Domain scope (directory boundaries)
  - Agent type (Creator/Reviewer/Enhancer/etc.)
  - Purpose statement (orchestrator description)
  - Core capabilities (4-6 items)
  - Expected inputs/outputs
  - Domain knowledge areas
  - Tool recommendations
  - Integration points
- **Time**: 10-15 seconds

### Phase 3: Interactive Refinement
- **Goal**: Walk through proposal with user Q&A
- **Interaction**: User accepts, modifies, or provides custom values for each section
- **Patterns**:
  - Name: Choose from 3 options or provide custom
  - Domain/Type: Accept or specify different
  - Purpose: Accept or provide improved version
  - Lists (capabilities, tools): Accept, add, remove, or edit items
- **Time**: 3-5 minutes

### Phase 4: Generate Definition File
- **Goal**: Create complete agent definition file
- **Delegation**: agent-architect (generate_agent_definition operation)
- **Input**: Refined requirements from Phase 3
- **Output**: Agent definition file at specified path
- **Template**: `.claude/templates/agent-definition-input.template.md`
- **Time**: 5-10 seconds

### Phase 5: Present Completion & Options
- **Goal**: Offer next steps to user
- **Options**:
  1. **Proceed immediately** - Run standard 10-phase workflow now (10-15 min)
  2. **Review first** - Exit, user manually runs `/create-agent definition.md` later
  3. **Regenerate** - Return to Phase 3 with different answers
- **Output**: File preview (first 30 lines) and clear action options
- **Time**: 1 minute

**After Interactive Workflow**:
- If user chooses Option 1: Proceeds to standard 10-phase workflow (below)
- If user chooses Option 2: Command completes, definition file saved
- If user chooses Option 3: Returns to Phase 3 for refinement

**Complete Specification**: `.claude/docs/guides/interactive-agent-definition-workflow.md`

---

## Standard Agent Creation Workflow (Existing)

**When to Use**: Creating agent from existing definition file (manual or interactive output).

**Entry Point**: `/create-agent path/to/agent-definition.md`

## Multi-Phase Workflow (10 Phases)

### **Phase 0: Setup & Progress Tracking**

**Orchestrator Actions**:
1. Use TodoWrite to create task list for all 10 phases:
   ```
   - Phase 1: Parse agent definition & validate preconditions
   - Phase 2: Determine information requirements
   - Phase 3: Review user-provided context
   - Phase 4: Research information gaps
   - Phase 5: Organize documentation
   - Phase 6: Determine input/output schema
   - Phase 7: Build agent definition
   - Phase 8: Validate agent quality
   - Phase 9: Interactive review & refinement
   - Phase 10: Finalization & integration
   ```

2. Mark Phase 1 as in_progress
3. Proceed to Phase 1

---

### **Phase 1: Parse Agent Definition & Validate Preconditions**

**Goal**: Extract structured information from user's agent definition file and validate readiness for agent creation.

**Orchestrator Actions**:
1. Launch 3 tasks in parallel

**Task 1: Parse Agent Definition**
```
Agent: researcher-codebase
Rationale: File analysis and structured information extraction

Task(subagent_type="researcher-codebase", prompt="""
PARSE AGENT DEFINITION FILE and extract structured information.

File: [agent-definition-file-path]

Extract and validate:
1. Agent name (check format: [domain]-[action])
2. Domain scope (.claude/**, packages/**, docs/**, cross-domain)
3. Purpose (1-2 sentence orchestrator description)
4. Core capabilities (list)
5. Expected inputs (schema hints)
6. Expected outputs (schema hints)
7. Domain knowledge references (if any)
8. Tool requirements (if any)
9. Additional context (if any)

Return structured JSON with all extracted fields and validation notes.
""")
```

**Task 2: Validate Preconditions** (Parallel)
```
Agent: claude-code
Rationale: .claude/ directory structure validation

Task(subagent_type="claude-code", prompt="""
VALIDATE AGENT CREATION PRECONDITIONS.

Check:
1. .claude/agents/ directory exists and is writable
2. .claude/templates/agent.template.md exists
3. .claude/docs/schemas/ directory exists
4. Base schema exists: .claude/docs/schemas/base-agent.schema.json

Return JSON with pass/fail status for each check and any error details.
""")
```

**Task 3: Check for Duplicate Agents** (Parallel)
```
Agent: tech-debt-investigator
Rationale: Duplicate functionality detection

Task(subagent_type="tech-debt-investigator", prompt="""
CHECK FOR DUPLICATE AGENTS with overlapping capabilities.

Proposed Agent Name: [name from definition file]
Proposed Capabilities: [list from definition file]

Search existing agents in .claude/agents/ for:
1. Exact name match
2. Similar name patterns
3. Overlapping capabilities
4. Domain overlap

Return JSON with:
- is_duplicate: boolean
- similar_agents: [list with similarity scores]
- overlap_analysis: string
- recommendation: "proceed" | "rename" | "merge_with_existing"
""")
```

**Synthesis**:
1. Collect results from all 3 agents
2. If any validation fails:
   - Present errors to user with correction guidance
   - Exit or offer retry
3. If all validations pass:
   - Store parsed agent definition for later phases
   - Update TodoWrite: Mark Phase 1 complete, Phase 2 in_progress
   - Proceed to Phase 2

**Success Criteria**:
- ✅ Agent definition parsed and validated
- ✅ No duplicates found
- ✅ Preconditions met
- ✅ Naming conventions followed

---

### **Phase 2: Determine Information Requirements (Confidence-Based)**

**Goal**: Identify what domain knowledge, frameworks, and processes the agent needs to know.

**Orchestrator Actions**:
1. Delegate to context-readiness-assessor

**Task 1: Analyze Information Requirements**
```
Agent: context-readiness-assessor
Rationale: Specializes in determining what context is needed before implementation

Task(subagent_type="context-readiness-assessor", prompt="""
ASSESS INFORMATION REQUIREMENTS for new agent creation.

Agent Definition:
- Name: [name]
- Domain: [domain]
- Purpose: [purpose]
- Capabilities: [list]

Determine what information this agent needs to know to accomplish its goals:
1. Domain expertise required (frameworks, methodologies, standards)
2. Technical concepts needed (patterns, algorithms, architectures)
3. Processes/workflows agent will execute
4. Tool usage patterns and best practices
5. Integration points with other agents/systems

For each information requirement, provide:
- Topic name
- Confidence score (0.0-1.0) indicating importance
- Rationale for why this information is needed
- Specificity level (broad topic vs. specific subtopic)

Return structured JSON with categorized requirements and confidence scores.
""")
```

**Synthesis**:
1. Receive information requirements report
2. Categorize by confidence:
   - High (≥0.8): Essential
   - Medium (0.5-0.79): Important
   - Low (<0.5): Optional
3. Present to user:
   ```
   I've identified N information requirements:

   🔴 High-Confidence (Essential):
   - Topic 1 (confidence: 0.9) - Rationale
   - Topic 2 (confidence: 0.85) - Rationale

   🟡 Medium-Confidence (Important):
   - Topic 3 (confidence: 0.7) - Rationale

   🟢 Low-Confidence (Optional):
   - Topic 4 (confidence: 0.4) - Rationale

   Options:
   1. ✅ Proceed with all high + medium confidence topics
   2. 🔧 Modify list (add/remove topics)
   3. 📊 Research all topics including low-confidence
   ```
4. Await user decision
5. Update TodoWrite: Mark Phase 2 complete, Phase 3 in_progress
6. Proceed to Phase 3 with approved requirements

**Success Criteria**:
- ✅ Information requirements identified and scored
- ✅ User approval obtained
- ✅ Requirements list ready for research phase

---

### **Phase 3: Review User-Provided Context**

**Goal**: Extract frameworks and domain knowledge from user-provided context files (if any).

**Orchestrator Actions**:

**If `--context-dir` provided**:

**Task 1: Analyze User Context**
```
Agent: researcher-codebase
Rationale: File analysis and structured information extraction

Task(subagent_type="researcher-codebase", prompt="""
ANALYZE USER-PROVIDED CONTEXT for agent creation.

Context Directory: [context-dir-path]
Information Requirements: [list from Phase 2]

Extract from user-provided files:
1. Frameworks mentioned (with descriptions)
2. Processes/workflows described
3. Tool requirements and usage patterns
4. Domain-specific knowledge and terminology
5. Best practices and standards
6. Examples and code patterns

Map each finding to information requirements from Phase 2:
- Which requirements are fully covered?
- Which are partially covered?
- Which have no coverage?

Return structured JSON with:
- covered_requirements: [list with coverage scores]
- extracted_frameworks: [list]
- extracted_processes: [list]
- gap_analysis: {requirement: coverage_score}
""")
```

**Synthesis**:
1. If context provided:
   - Receive coverage analysis from researcher-codebase
   - Generate gap analysis
2. If no context:
   - All requirements are gaps
3. Present gap analysis:
   ```
   ✅ Covered by user context:
   - Requirement 1 (coverage: 95%)
   - Requirement 2 (coverage: 80%)

   ⚠️ Partially covered:
   - Requirement 3 (coverage: 40%) - Need more detail on X

   ❌ Gaps requiring research:
   - Requirement 4 (coverage: 0%)
   - Requirement 5 (coverage: 0%)
   ```
4. Update TodoWrite: Mark Phase 3 complete, Phase 4 in_progress
5. Proceed to Phase 4 with identified gaps

**Success Criteria**:
- ✅ User context analyzed (if provided)
- ✅ Coverage mapped to requirements
- ✅ Gap list ready for research

---

### **Phase 4: Research Information Gaps (Targeted & Specific)**

**Goal**: Execute targeted research for all information gaps using parallel research workers.

**Orchestrator Actions**:

**Task 1: Create Research Plan**
```
Agent: researcher-lead
Rationale: Strategic research planning and delegation

Task(subagent_type="researcher-lead", prompt="""
CREATE A RESEARCH PLAN for agent creation information gaps.

Agent Being Created: [name]
Domain: [domain]

Information Gaps (from Phase 3):
[List of gaps with context]

For each gap:
1. Convert broad topic to 2-3 specific research queries
2. Determine research strategy (breadth-first vs depth-first)
3. Assign research source type (web, library docs, codebase patterns)
4. Estimate worker count and parallel execution plan

Focus on:
- Frameworks and methodologies (structured approaches)
- Processes and workflows (step-by-step procedures)
- Best practices and standards (industry guidance)
- Integration patterns (how this fits with existing systems)

Return delegation_plans with worker assignments and specific prompts.
DO NOT EXECUTE RESEARCH - ONLY CREATE THE PLAN.
""")
```

**Task 2: Execute Research Workers** (After plan received)
```
Agents: researcher-web, researcher-library, researcher-codebase (as assigned)
Rationale: Parallel research execution for speed

# Orchestrator spawns workers from plan (max 5 simultaneously)
# Example workers:

Task(subagent_type="researcher-web", prompt="""
[Specific research query from plan]
Focus on: [frameworks/processes/patterns]
Sources: [recommended sources from plan]
""")

Task(subagent_type="researcher-library", prompt="""
[Specific library documentation query]
Library: [library name]
Topics: [specific API/patterns needed]
""")

Task(subagent_type="researcher-codebase", prompt="""
[Specific codebase pattern search]
Pattern: [what to look for]
Files: [scope]
""")
```

**Synthesis**:
1. Receive delegation_plans from researcher-lead
2. Parse plans and spawn workers in parallel (max 5)
3. Collect research results as workers complete
4. Synthesize findings:
   ```
   Research Results:

   Topic: [Topic 1]
   Confidence: 0.92
   Sources: 3 (GitHub Actions docs, existing git-github agent, Spotify blog)
   Key Findings:
   - Framework 1: [Summary]
   - Process 1: [Summary]
   - Integration pattern: [Summary]
   ```
5. If any topic has confidence <0.7:
   - Refine query and re-research (max 2 iterations)
6. Update TodoWrite: Mark Phase 4 complete, Phase 5 in_progress
7. Proceed to Phase 5 with research findings

**Success Criteria**:
- ✅ All gaps researched with ≥0.7 confidence
- ✅ Frameworks, processes, and patterns documented
- ✅ Sources tracked for provenance

---

### **Phase 5: Organize Documentation (Categorized & AI-Readable)**

**Goal**: Generate structured, AI-readable documentation from research findings using template.

**Orchestrator Actions**:

**Step 1: Categorize Research Findings**

Categorize findings by domain:
- Planning (specifications, roadmaps)
- Development (implementation patterns, workflows)
- Testing (test strategies, validation)
- Review (quality standards, checklists)
- Security (OWASP patterns, threat models)
- Domain-Specific (agent's unique knowledge)

**Step 2: Generate Documentation Files** (Parallel, max 5)

For each category with findings:

```
Agent: doc-librarian
Rationale: Documentation organization and health maintenance

Task(subagent_type="doc-librarian", prompt="""
GENERATE AI-READABLE DOCUMENTATION from research findings.

Category: [planning|development|testing|review|security|domain-specific]
Agent Name: [agent-name]
Template: .claude/templates/agent-documentation.template.md

Research Findings:
[Relevant findings for this category]

Use the AI-readable documentation template to create:
1. Overview (1-2 sentence summary)
2. Core Frameworks (structured with Purpose/When to Use/How to Apply/Example)
3. Processes & Workflows (step-by-step with rationale)
4. Decision Trees (condition → action mappings)
5. Anti-Patterns (what to avoid with alternatives)
6. Integration Points (how this connects to other components)

Output file path: .claude/docs/guides/[agent-name]/[category]-[topic].md

Follow template structure exactly for AI readability.
Include sources with URLs for provenance.
""")
```

**Step 3: Update Documentation Indices** (After files generated)

```
Agent: doc-librarian
Rationale: Maintaining documentation health and indices

Task(subagent_type="doc-librarian", prompt="""
UPDATE DOCUMENTATION INDICES for new agent documentation.

New Documentation Files:
[List of generated files]

Update:
1. .claude/docs/DOC-INDEX.md (add entries under appropriate category)
2. .claude/docs/guides/agent-categorization.md (add agent to category)

Maintain alphabetical ordering and consistent formatting.
""")
```

**Synthesis**:
1. Launch doc-librarian tasks in parallel (one per category, max 5)
2. Collect generated documentation files
3. Launch doc-librarian to update indices
4. Verify documentation structure:
   ```
   .claude/docs/guides/[agent-name]/
   ├── planning-frameworks.md       (if applicable)
   ├── development-workflows.md     (if applicable)
   ├── security-patterns.md         (if applicable)
   └── domain-knowledge.md          (agent-specific)
   ```
5. Update TodoWrite: Mark Phase 5 complete, Phase 6 in_progress
6. Proceed to Phase 6

**Success Criteria**:
- ✅ Documentation generated using AI-readable template
- ✅ Files organized in categorized directories
- ✅ Indices updated
- ✅ All documentation includes sources and examples

---

### **Phase 6: Determine Input/Output Schema**

**Goal**: Design and generate JSON Schema file extending base-agent.schema.json.

**Orchestrator Actions**:

**Task 1: Design Schema Structure**
```
Agent: agent-architect
Rationale: Agent lifecycle management includes schema design

Task(subagent_type="agent-architect", prompt="""
DESIGN INPUT/OUTPUT SCHEMA for new agent.

Agent Definition:
- Name: [name]
- Capabilities: [list]
- Expected Inputs: [from Phase 1 parsed definition]
- Expected Outputs: [from Phase 1 parsed definition]

Analyze capabilities to determine:
1. Input structure:
   - Required fields (context, operation_type, etc.)
   - Optional parameters (flags, configuration)
   - Multiple operation types? (like agent-architect: create, evaluate, update)

2. Output structure:
   - SUCCESS state: What deliverables, changes, artifacts?
   - FAILURE state: What error types, recovery steps?
   - Metadata: confidence, sources, recommendations?

Generate JSON Schema file that:
- Extends base-agent.schema.json
- Defines agent_specific_output structure
- Defines failure_details structure
- Includes descriptions for all fields
- Validates against JSON Schema Draft 07

Output file: .claude/docs/schemas/[agent-name].schema.json
""")
```

**Synthesis**:
1. Receive generated schema file from agent-architect
2. Validate schema:
   - Extends base-agent.schema.json correctly
   - Has SUCCESS and FAILURE states
   - All fields have descriptions
   - Follows two-state model
3. If validation fails:
   - Request corrections from agent-architect
4. Store schema file path for Phase 7
5. Update TodoWrite: Mark Phase 6 complete, Phase 7 in_progress
6. Proceed to Phase 7

**Success Criteria**:
- ✅ Schema file created
- ✅ Extends base-agent.schema.json
- ✅ Two-state model (SUCCESS/FAILURE)
- ✅ JSON Schema Draft 07 compliant
- ✅ All fields documented

---

### **Phase 7: Build Agent Definition (Template-Driven)**

**Goal**: Generate complete agent definition file using template, documentation, and schema.

**Orchestrator Actions**:

**Step 1: Prepare Tool Recommendations**

Analyze capabilities to suggest tools with confidence:
- Read (1.0 - all agents need to read)
- Write (0.9 - agent creates files)
- Edit (0.8 - agent modifies files)
- Bash (0.6 - agent executes commands)
- Task (0.5 - agent delegates to other agents)
- Etc.

**Step 2: Generate Agent Definition**

```
Agent: agent-architect
Operation: create_agent
Rationale: Agent lifecycle management, template application

Task(subagent_type="agent-architect", prompt="""
CREATE NEW AGENT DEFINITION using template and simulation-driven development.

Agent Requirements:
- Name: [name]
- Domain: [domain]
- Purpose: [purpose]
- Capabilities: [list from Phase 1]

Documentation References (generated in Phase 5):
[List all .claude/docs/guides/[agent-name]/*.md files]

Schema File: .claude/docs/schemas/[agent-name].schema.json

Tool Recommendations (with confidence and rationale):
[Orchestrator-provided recommendations]
- Read (confidence: 1.0, rationale: All agents need to read files)
- Write (confidence: 0.9, rationale: Agent creates X files)
- Bash (confidence: 0.6, rationale: May need to execute Y commands)

Instructions:
1. Use simulation-driven development (think from agent's perspective)
2. Apply .claude/templates/agent.template.md structure
3. Apply base pattern inheritance (reference base-agent-pattern.md)
4. Reference frameworks from documentation in appropriate sections
5. Include tool usage patterns with rationale
6. Create clear orchestrator description (1-2 sentences, when to call)
7. Follow all template requirements (YAML frontmatter, section ordering, etc.)

Output: .claude/agents/[agent-name].md
""")
```

**Synthesis**:
1. Receive agent definition file and quality report
2. Store agent file path for next phase
3. Update TodoWrite: Mark Phase 7 complete, Phase 8 in_progress
4. Proceed to Phase 8

**Success Criteria**:
- ✅ Agent definition created
- ✅ Template structure followed (19 sections)
- ✅ Base pattern inheritance applied
- ✅ Documentation frameworks referenced
- ✅ Tools justified with confidence scores
- ✅ Orchestrator description clear and concise

---

### **Phase 8: Validate Agent Quality**

**Goal**: Run comprehensive quality validation across template, documentation, prompt engineering, and context optimization dimensions.

**Orchestrator Actions**:

**Step 1: Parallel Validation** (Launch 5 tasks simultaneously)

**Validator 1: Template Compliance**
```
Agent: agent-architect
Operation: validate_workflow
Rationale: Template validation expertise

Task(subagent_type="agent-architect", prompt="""
VALIDATE TEMPLATE COMPLIANCE for new agent.

Agent File: .claude/agents/[agent-name].md
Template: .claude/templates/agent.template.md

Check:
1. YAML frontmatter on line 1 (not lines 1-22 warnings)
2. Tools field is comma-separated string (not YAML list)
3. All 19 sections present in correct order
4. Base pattern references included
5. Schema reference included
6. File operation protocol referenced

Return validation report with pass/fail per check.
""")
```

**Validator 2: Documentation Health Validation**
```
Agent: doc-librarian
Rationale: Documentation integrity and organization validation

Task(subagent_type="doc-librarian", prompt="""
VALIDATE DOCUMENTATION HEALTH for new agent.

Agent File: .claude/agents/[agent-name].md
Generated Docs: .claude/docs/guides/[agent-name]/*.md (from Phase 5)
Schema File: .claude/docs/schemas/[agent-name].schema.json

Check:
1. Documentation structure (all Phase 5 files exist)
2. Internal link integrity (all markdown links resolve)
3. Cross-reference validity (references to guides are correct)
4. Naming conventions (kebab-case.md standard)
5. Organization compliance (DOCS-MANAGEMENT.md rules)

Return health report with:
- health_score (0-100)
- broken_links: [list]
- missing_files: [list]
- naming_violations: [list]
- organization_issues: [list]
- recommendations: [list]
""")
```

**Validator 3: Prompt Quality Evaluation**
```
Agent: prompt-evaluator
Rationale: Prompt engineering best practices and anti-pattern detection

Task(subagent_type="prompt-evaluator", prompt="""
EVALUATE PROMPT QUALITY for new agent.

Agent File: .claude/agents/[agent-name].md
Schema File: .claude/docs/schemas/[agent-name].schema.json

Evaluate across 4 frameworks:
1. Structural Quality: Clarity, modularity, reasonable length
2. Prompt Engineering: Best practices, implicit context handling
3. Token Optimization: Redundancy, compression opportunities
4. Testing Strategy: Validation approach, quality gates

Return evaluation report with:
- framework_scores: {structural, engineering, tokens, testing}
- anti_patterns: [list with severity: high/medium/low]
- optimization_opportunities: [list with quantified impact]
- improvement_roadmap: [prioritized recommendations]
- confidence_scores: [0.0-1.0 per recommendation]
""")
```

**Validator 4: Context Optimization Analysis**
```
Agent: context-optimizer
Rationale: Token budget analysis and efficiency validation

Task(subagent_type="context-optimizer", prompt="""
ANALYZE CONTEXT USAGE for new agent.

Agent File: .claude/agents/[agent-name].md
Generated Docs: .claude/docs/guides/[agent-name]/*.md
Template: .claude/templates/agent.template.md
Base Pattern: .claude/docs/guides/base-agent-pattern.md

Analyze:
1. Current token count for agent definition
2. Redundancy with base-agent-pattern.md
3. Redundancy with generated documentation
4. Documentation reference opportunities
5. Optimization potential with ROI

Return optimization report with:
- current_tokens: number
- optimized_tokens: number (if recommendations applied)
- potential_savings: number
- redundancy_analysis: [list with overlap percentages]
- reference_opportunities: [list with token savings]
- optimization_roadmap: [prioritized by ROI]
""")
```

**Validator 5: Quality Matrix Evaluation**
```
Agent: agent-architect
Operation: evaluate_agent
Rationale: 9-dimensional quality evaluation

Task(subagent_type="agent-architect", prompt="""
EVALUATE AGENT QUALITY using 9-dimensional matrix.

Agent File: .claude/agents/[agent-name].md

Score each dimension (0-5 scale):
1. Role clarity and boundary definition
2. Schema integration quality
3. Reasoning approach sophistication
4. Tool usage appropriateness
5. Error recovery completeness
6. Output optimization
7. Integration point clarity
8. Documentation references
9. Validation coverage

Calculate weighted score: (sum × weights) / 45 × 100

Return quality report with scores and recommendations.
""")
```

**Synthesis**:
1. Launch all 5 validators in parallel
2. Collect all validation results
3. Synthesize comprehensive quality report:
   ```
   Quality Validation Report:

   ✅ Template Compliance: PASS
   ✅ Documentation Health: 85/100
      - All Phase 5 files exist
      - 2 broken links found (fixable)
      - Organization compliant
   ✅ Prompt Quality: GOOD
      - No high-severity anti-patterns
      - 2 medium-priority optimization opportunities
      - Testing strategy well-defined
   ✅ Context Optimization: 4,200 tokens
      - 800 token savings identified
      - 3 documentation reference opportunities
      - Within 5,000 token target

   Quality Matrix Score: 82/100
   - Role Clarity: 5/5
   - Schema Integration: 4/5
   - Reasoning Approach: 4/5
   - Tool Usage: 4/5
   - Error Recovery: 4/5
   - Output Optimization: 3/5
   - Integration Points: 5/5
   - Documentation: 5/5
   - Validation: 4/5

   ⚠️ Recommendations:
   - Fix 2 broken documentation links (doc-librarian)
   - Apply documentation references to save 800 tokens (context-optimizer)
   - Consider improving output compression techniques (quality matrix)
   ```

## Comprehensive Validation Checklist

### 1. Template Compliance
- [ ] YAML frontmatter on line 1 (not lines 1-22 warnings)
- [ ] Tools field is comma-separated string (NOT YAML list)
- [ ] All 19 sections present in correct order
- [ ] Base pattern references included
- [ ] Schema reference included
- [ ] File operation protocol referenced

### 2. Documentation Health (Phase 5 artifacts)
- [ ] All generated documentation files exist
- [ ] Internal links resolve correctly
- [ ] Cross-references to guides are valid
- [ ] Naming conventions followed (kebab-case.md)
- [ ] Organization compliant with DOCS-MANAGEMENT.md
- [ ] Health score ≥80/100

### 3. Prompt Quality
- [ ] Structural clarity (clear sections, no ambiguity)
- [ ] Prompt engineering best practices applied
- [ ] No high-severity anti-patterns detected
- [ ] Testing strategy defined
- [ ] Tool descriptions meet quality standards
- [ ] Examples provided where helpful

### 4. Context Optimization
- [ ] Agent definition ≤5,000 tokens (target)
- [ ] No unnecessary duplication with base-agent-pattern.md
- [ ] Documentation references used where appropriate
- [ ] Generated docs properly referenced (not duplicated in agent)
- [ ] Optimization opportunities documented

### 5. Quality Matrix Score
- [ ] Overall score ≥70/100 (minimum acceptable)
- [ ] No dimension scored <2/5 (critical failure)
- [ ] Role clarity: ≥4/5
- [ ] Schema integration: ≥4/5
- [ ] Tool usage: ≥4/5

### 6. Schema Validation
- [ ] Schema file exists (.claude/docs/schemas/[name].schema.json)
- [ ] Extends base-agent.schema.json correctly
- [ ] Defines agent_specific_output for SUCCESS state
- [ ] Defines failure_details for FAILURE state
- [ ] All fields have descriptions
- [ ] JSON Schema Draft 07 compliant

### 7. Integration & Workflow
- [ ] Orchestrator workflow integration planned
- [ ] CLAUDE.md delegation table update ready
- [ ] Maturity version declared (v0.x, v1.x, etc.)
- [ ] Capability description clear for orchestrator
- [ ] Integration points documented

## Quality Gates

**PASS Criteria** (proceed to Phase 9):
- ✅ Template compliance: 100%
- ✅ Documentation health: ≥80/100
- ✅ Prompt quality: No high-severity anti-patterns
- ✅ Context optimization: ≤5,000 tokens OR documented exception
- ✅ Quality matrix: ≥70/100

**CONDITIONAL PASS** (proceed with recommendations):
- ⚠️ Documentation health: 60-79/100 (apply fixes before finalization)
- ⚠️ Context optimization: 5,000-7,000 tokens (schedule optimization task)
- ⚠️ Medium-severity anti-patterns detected (address in Phase 9 refinement)

**FAIL** (require fixes before Phase 9):
- ❌ Template compliance: Any failure
- ❌ Documentation health: <60/100
- ❌ High-severity anti-patterns detected
- ❌ Quality matrix: <60/100
- ❌ Schema validation: Any failure

4. If validation failures or quality gates not met:
   - Present issues to user with detailed breakdown
   - Offer auto-fix for documentation links (doc-librarian)
   - Offer optimization implementation (context-optimizer)
   - Re-validate after fixes
5. If all quality gates pass:
   - Update TodoWrite: Mark Phase 8 complete, Phase 9 in_progress
   - Proceed to Phase 9

**Success Criteria**:
- ✅ Template compliance validated
- ✅ Documentation health ≥80/100
- ✅ Prompt quality validated (no high-severity anti-patterns)
- ✅ Context optimization analyzed (≤5,000 tokens target)
- ✅ Quality matrix score ≥70%
- ✅ All quality gates pass

---

### **Phase 9: Interactive Review & Refinement**

**Goal**: Present agent to user for review and apply refinements if requested.

**Orchestrator Actions**:

**Step 1: Generate Agent Summary**

```
Agent: technical-pm
Rationale: Executive summary creation for user review

Task(subagent_type="technical-pm", prompt="""
GENERATE EXECUTIVE SUMMARY for agent review.

Agent File: .claude/agents/[agent-name].md
Quality Report: [from Phase 8]
Documentation: [list of doc files]
Schema: .claude/docs/schemas/[agent-name].schema.json

Create user-friendly summary:
1. Agent name and type (Creator/Reviewer/Enhancer/etc.)
2. Orchestrator description (when to call this agent)
3. Core capabilities with confidence scores
4. Tools assigned with rationale
5. Documentation created (count of frameworks/processes)
6. Quality score and key strengths
7. Recommendations for improvement (if any)

Format for clarity with emojis and sections.
""")
```

**Step 2: Present to User**

Present summary with options:
```
# [Agent Name] - Ready for Review

**Type**: [Creator/Reviewer/Enhancer/Runner/Analyzer]
**Domain**: [domain]

**Orchestrator Description**:
[1-2 sentence clear description of when to call this agent]

**Core Capabilities**:
- Capability 1 (confidence: 0.95)
- Capability 2 (confidence: 0.88)
- ...

**Tools**: Read, Write, Grep, Bash
**Rationale**: [Explain why each tool is needed]

**Documentation**:
- 3 framework guides created
- 2 workflow processes documented
- Security patterns integrated

**Quality Score**: 82/100
- ✅ Template compliant
- ✅ No duplicates found
- ⚠️  Recommendation: Consider adding error recovery pattern for X

---

Options:
1. ✅ Approve and finalize
2. 🔧 Refine specific sections (capabilities, tools, description)
3. 📝 Add additional documentation
4. 🔄 Re-evaluate after manual changes
5. ❌ Cancel creation
```

**Step 3: Handle User Decision**

If user chooses refinement:

```
Agent: agent-architect
Operation: implement_feedback
Rationale: Feedback application and updates

Task(subagent_type="agent-architect", prompt="""
APPLY USER REFINEMENTS to agent definition.

Agent File: .claude/agents/[agent-name].md

User Feedback:
[Specific refinements requested]

Apply changes while maintaining:
- Template compliance
- Base pattern inheritance
- Documentation references
- Quality standards

Return updated agent file.
""")
```

Then return to Phase 8 for re-validation.

If user approves:
- Update TodoWrite: Mark Phase 9 complete, Phase 10 in_progress
- Proceed to Phase 10

**Success Criteria**:
- ✅ User explicitly approves agent
- ✅ All refinements applied and validated
- ✅ Quality standards maintained

---

### **Phase 10: Finalization & Integration**

**Goal**: Write all files, update integration points, and provide user with next steps.

**Orchestrator Actions**:

**Step 1: Verify Files Ready**

Ensure all files are ready for final write:
- `.claude/agents/[agent-name].md`
- `.claude/docs/schemas/[agent-name].schema.json`
- `.claude/docs/guides/[agent-name]/*.md`

**Step 2: Update Integration Points**

```
Agent: agent-architect
Operation: update_maturity
Rationale: Integration updates across documentation

Task(subagent_type="agent-architect", prompt="""
UPDATE INTEGRATION POINTS for new agent.

Agent Name: [name]
Agent File: .claude/agents/[agent-name].md
Agent Type: [Creator/Reviewer/etc.]
Domain: [domain]

Update:
1. CLAUDE.md delegation table (lines 639-666)
   - Add row with agent, domain scope, use case, type
2. .claude/docs/orchestrator-workflow.md agent legend
   - Add entry with description
3. .claude/docs/guides/agent-categorization.md
   - Add to appropriate category
4. .claude/docs/DOC-INDEX.md (if not already updated)

Maintain alphabetical ordering and consistent formatting.
Return list of files updated.
""")
```

**Step 3: Generate Handoff Summary**

```
Agent: technical-pm
Rationale: User-facing documentation and next steps

Task(subagent_type="technical-pm", prompt="""
GENERATE HANDOFF SUMMARY for agent creation completion.

Agent Name: [name]
Files Created: [list]
Files Updated: [list]
Quality Score: [score]

Create summary with:
1. Files Created section (with paths)
2. Integrations Updated section (with files)
3. Quality Metrics section (scores, validations)
4. Next Steps section (restart session, test agent, monitor)
5. Usage Example (how orchestrator calls this agent)

Format with emojis, clear sections, actionable next steps.
""")
```

**Step 4: Present Handoff to User**

```markdown
# Agent Creation Complete: [agent-name]

## Files Created
- ✅ Agent: .claude/agents/[agent-name].md
- ✅ Schema: .claude/docs/schemas/[agent-name].schema.json
- ✅ Documentation: .claude/docs/guides/[agent-name]/ (3 files)

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
   Task(subagent_type="[agent-name]", prompt="""
   [Example usage based on capabilities]
   """)
   ```
3. Monitor performance and iterate if needed
4. Consider adding to project roadmap

---

Agent is ready for use after session restart!
```

**Step 5: Mark Complete**

Update TodoWrite: Mark Phase 10 complete
Command execution complete!

**Success Criteria**:
- ✅ All files written successfully
- ✅ Integrations updated (CLAUDE.md, orchestrator-workflow.md, etc.)
- ✅ User has clear next steps
- ✅ Handoff summary provided

---

## Agent Assignment Summary

| Phase | Task | Agent | Rationale |
|-------|------|-------|-----------|
| 1 | Parse definition | researcher-codebase | File analysis |
| 1 | Validate preconditions | claude-code | .claude/ directory ops |
| 1 | Check duplicates | tech-debt-investigator | Duplicate detection |
| 2 | Assess requirements | context-readiness-assessor | Context needs |
| 3 | Analyze context | researcher-codebase | File analysis |
| 4 | Create plan | researcher-lead | Research planning |
| 4 | Execute research | researcher-*/multiple | Parallel research |
| 5 | Generate docs | doc-librarian | Documentation org |
| 5 | Update indices | doc-librarian | Index maintenance |
| 6 | Design schema | agent-architect | Schema creation |
| 7 | Create agent | agent-architect | Agent generation |
| 8 | Validate template | agent-architect | Template validation |
| 8 | Validate documentation | doc-librarian | Documentation health |
| 8 | Evaluate prompt quality | prompt-evaluator | Prompt engineering analysis |
| 8 | Analyze context usage | context-optimizer | Token budget analysis |
| 8 | Quality evaluation | agent-architect | Quality matrix |
| 9 | Generate summary | technical-pm | Executive summary |
| 9 | Apply refinements | agent-architect | Feedback application |
| 10 | Update integrations | agent-architect | Integration updates |
| 10 | Generate handoff | technical-pm | User documentation |

### Interactive Mode Agent Assignments

| Phase | Task | Agent | Rationale |
|-------|------|-------|-----------|
| 1 | Capture user idea | Orchestrator | Simple text collection, no delegation needed |
| 2 | Analyze idea | agent-architect | Agent expertise, structured analysis, confidence scoring |
| 2 | Propose structure | agent-architect | Agent design patterns, recommendation generation |
| 3 | Interactive refinement | Orchestrator | User interaction, choice collection, Q&A flow |
| 4 | Generate definition file | agent-architect | Template application, file generation, validation |
| 5 | Present completion | Orchestrator | User communication, option handling, transition to standard workflow |

**Note**: After Phase 5 (if user chooses "proceed immediately"), workflow continues with standard 10-phase agent creation.

---

## Dry-Run Mode

If `--dry-run` flag provided:
- Execute all phases through Phase 9
- Do NOT write any files in Phase 10
- Present complete summary of what WOULD be created
- Include all file paths and content previews
- User can review before running without --dry-run

---

## Error Handling

**Phase Failures**:
- If any phase fails validation, present error with context
- Offer retry with corrections
- Offer manual intervention option
- Offer cancel option

**Iteration Limits**:
- Phase 4 research: Max 2 iterations if confidence <0.7
- Phase 8 validation: Max 3 fix attempts before escalating to user
- Phase 9 refinement: No limit (user-driven)

**Recovery**:
- All intermediate results stored for resume capability
- User can cancel at any phase
- Partial artifacts cleaned up on cancel

### Interactive Mode Error Handling

**Vague User Idea (Phase 1)**:
- Re-prompt with guidance: "What, How, When" framework
- Provide examples of good vs. vague ideas
- Max 3 retry attempts before suggesting manual template

**agent-architect Analysis Failure (Phase 2)**:
- Extract `missing_information` from `failure_details`
- Re-prompt user for specific clarifications
- Offer options: Rephrase idea, Provide more detail, or Cancel

**agent-architect Generation Failure (Phase 4)**:
- Show `failure_details.reasons` to user
- Offer options: Retry generation, Return to refinement (Phase 3), or Cancel

**File System Errors (Phase 4/5)**:
- Output path exists: Offer overwrite, rename, or cancel
- Write permission error: Request new writable path or cancel
- Invalid path format: Validate and suggest corrections

**User Confusion During Refinement (Phase 3)**:
- Provide inline help text for each section
- Offer "skip for now" option for optional sections
- Allow return to previous section

---

## Success Metrics

**Time Efficiency**:
- Target: 10-15 minutes end-to-end
- Improvement: 8-12x faster than manual (2-3 hours)

**Quality Consistency**:
- Template Compliance: 100%
- Schema Validation: 100%
- Documentation Coverage: ≥80% confidence
- Quality Matrix Score: ≥70%

**User Experience**:
- Required Input: 1 file (agent definition)
- Interactive Refinement: 2 decision points (Phase 2, Phase 9)
- Clear Next Steps: Provided in handoff summary

---

## agent-architect New Operations

### analyze_agent_idea (Phase 2)

**Purpose**: Analyze user's informal agent idea and generate structured proposal with confidence-scored recommendations.

**Input**:
```json
{
  "operation_type": "analyze_agent_idea",
  "task_id": "uuid",
  "description": "Analyze user idea and propose agent structure",
  "agent_idea_analysis": {
    "user_idea_text": "2-3 sentence description from user",
    "analysis_depth": "comprehensive"
  },
  "execution_timestamp": "2025-10-22T10:30:00Z"
}
```

**Output**: Structured proposal with 10 sections (name options, domain scope, agent type, purpose, capabilities, inputs, outputs, knowledge areas, tools, integration points). All recommendations include confidence scores (0.0-1.0) and rationale.

**Time**: 10-15 seconds

---

### generate_agent_definition (Phase 4)

**Purpose**: Generate complete agent definition file from refined requirements using official template.

**Input**:
```json
{
  "operation_type": "generate_agent_definition",
  "task_id": "uuid",
  "description": "Generate agent definition file",
  "definition_generation": {
    "output_path": "path/to/agent-definition.md",
    "refined_requirements": {
      "name": "agent-name",
      "domain": "packages/**",
      "type": "Analyzer",
      "purpose": "Orchestrator description",
      "capabilities": ["capability 1", "capability 2"],
      "inputs": [],
      "success_output": "Description",
      "failure_output": "Description",
      "knowledge_areas": [],
      "tools": [],
      "integration_points": {},
      "original_idea": "User's original 2-3 sentences"
    }
  },
  "execution_timestamp": "2025-10-22T10:35:00Z"
}
```

**Output**: Agent definition file at specified path following `.claude/templates/agent-definition-input.template.md` structure.

**Time**: 5-10 seconds

**Schema Updates**: See `.claude/docs/schemas/agent-architect.schema.json` for complete input/output schemas.

---

## Related Documentation

- **Agent Template**: `.claude/templates/agent.template.md`
- **Input Template**: `.claude/templates/agent-definition-input.template.md`
- **Documentation Template**: `.claude/templates/agent-documentation.template.md`
- **Base Schema**: `.claude/docs/schemas/base-agent.schema.json`
- **Agent Selection Framework**: `CLAUDE.md#-agent-selection-framework`
- **Orchestrator Workflow**: `.claude/docs/orchestrator-workflow.md`
- **Interactive Workflow Spec**: `.claude/docs/guides/interactive-agent-definition-workflow.md`
- **Interactive Mode Addendum**: `.claude/docs/guides/create-agent-interactive-mode-addendum.md`
