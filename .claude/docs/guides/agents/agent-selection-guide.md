# Agent Selection Guide



## Purpose



This guide provides **framework-based reasoning** for selecting the right agent for any task. Instead of keyword matching or algorithmic rules, these frameworks help you understand the relationship between file location, work type, and agent expertise.



**Core Problem Addressed**: The task-creator agent was overweighting code-implementer because it used keyword-only matching (e.g., "create" → code-implementer) without understanding domain context. A task to "create intent-analyzer agent in `.claude/agents/intent-analyzer.md`" would match "create" and assign code-implementer, when agent-architect is the domain specialist.



**Solution**: Seven conceptual frameworks that guide reasoning about domain, work type, and expertise matching.



---



**Note for researcher-lead Agent**:



This document is your primary reference for agent→domain mappings when creating research plans. Use the frameworks below to select appropriate workers for research coordination.



**Key Capability - Domain Specialists in Read-Only Mode**:



ANY agent can perform read-only research within their domain of expertise. Beyond the researcher-* family (researcher-web, researcher-codebase, researcher-library), consider domain specialists for targeted analysis:



**Analysis Without Implementation Examples**:

- **agent-architect** → Analyze agent definitions, prompt quality in `.claude/agents/**`

- **debugger** → Analyze test failure patterns, bug patterns in `packages/**`, `tests/**`

- **tech-debt-investigator** → Analyze code quality, duplication, technical debt (any domain)

- **feature-analyzer** → Analyze multi-component dependencies, integration points

- **code-reviewer** → Analyze code quality, standards compliance (read-only assessment)

- **technical-pm** → Analyze business alignment in `docs/**` plans (review-only mode)

- **architecture-review** → Analyze technical architecture (read-only review mode)

- **workflow** → Analyze workflow patterns, hooks, commands in `.claude/**`

- **spec-reviewer** → Analyze specification quality in `docs/**`



**Worker Selection Principle**:

- Match domain expertise to research objective

- Prefer domain specialist over generic researcher-* when expertise aligns

- Example: "Analyze authentication patterns" → debugger (auth domain expert in packages/**) rather than researcher-codebase (generic code analysis)

- Example: "Analyze agent duplication" → agent-architect (.claude/agents/** expert) rather than researcher-codebase



**Reference**: See Framework 1 (Domain-First Thinking) and Framework 3 (Agent Expertise Mapping) for comprehensive domain → agent mappings.



---



## Framework 1: Domain-First Thinking



**Core Principle**: The location of files in a task reveals the domain of work. Domain determines the specialist agent.



### Understanding Domain Boundaries



**The Claude Code Ecosystem Domain** (`.claude/**`)



Tasks involving `.claude/**` files are about maintaining the Claude Code system itself. Within this ecosystem, there are two specializations:



#### Agent Lifecycle Work (`.claude/agents/**`)

Creating, evaluating, or updating agent definitions requires deep understanding of:

- Prompt engineering patterns

- Agent simulation and evaluation

- Anthropic's best practices for agent design

- The 9-criteria quality matrix

- Workflow integration patterns



**This is agent-architect's specialized domain.** Agent-architect has developed expertise in these specific areas through repeated work on agent definitions.



**Recognition Pattern**: When you see a task description mentioning file paths in `.claude/agents/**`, immediately recognize this as agent lifecycle work. The file extension (.md) and capability to "edit files" is not the qualifier—the domain expertise in agent prompt engineering is.



**Example**: "Create intent-analyzer agent in `.claude/agents/intent-analyzer.md`"

- Keywords present: "create" (could suggest code-implementer)

- Domain signal: `.claude/agents/**` path

- **Decision**: agent-architect (domain ownership trumps keyword)



#### Claude Code Configuration (`.claude/**` excluding agents)

Work on commands, hooks, schemas, or general Claude Code configuration requires understanding of:

- Claude Code system architecture

- Slash command structure and invocation patterns

- Hook lifecycle and event handling

- Schema validation and structure

- Integration between agents, commands, and hooks



**This is claude-code's specialized domain.** Claude-code understands the Claude Code ecosystem holistically.



**Recognition Pattern**: When you see `.claude/**` paths that are NOT in the agents subdirectory, recognize this as Claude Code configuration work.



**Example**: "Update output style in `.claude/output-style.md`"

- Keywords present: "update" (could suggest code-implementer)

- Domain signal: `.claude/**` path (non-agents)

- **Decision**: claude-code (domain ownership)



---



**The Main Codebase Domain** (`packages/**`, `tests/**`, `scripts/**`)



This is where the application's business logic lives. Multiple specialists work in this domain, distinguished by the **type of work** rather than location alone.



Within the main codebase, you need to understand what kind of work is being requested:



**code-implementer** - Creating new functionality

- Implementing features that don't exist yet

- Building new code from specifications

- Adding new capabilities to existing systems

- Writing implementation code for defined requirements



**Recognition Pattern**: Language emphasizing newness, creation, bringing something into existence. The work is constructive.



**test-creator** - Test generation and design

- Creating test suites for features

- Generating test cases

- Designing test strategies

- Analyzing coverage gaps



**Recognition Pattern**: Keywords: "create tests", "generate tests", "design tests", "test coverage analysis"



**test-executor** - Test execution and validation

- Running existing tests and reporting results

- Parsing test output and failure categorization

- Executing test suites with pytest

- Validating test execution results



**Recognition Pattern**: Keywords: "run tests", "execute tests", "validate tests", "test failures"


**test-dataset-creator** - Test data generation
- Mining git history for test scenarios
- Generating diverse validation datasets
- Pydantic-validated JSON fixture creation
- Domain heuristics for ground truth

**Recognition Pattern**: Keywords: "test data", "fixtures", "test scenarios", "validation datasets"




**debugger** - Investigating failures

- Discovering why tests are failing (unknown cause)

- Hypothesis-driven problem solving

- Root cause analysis when behavior is unexpected

- Non-invasive experimentation to understand issues



**Recognition Pattern**: Language about discovery, investigation, "why is this failing", "debug", "troubleshoot". Emphasis on unknown cause.



**code-reviewer** - Quality gates and feedback

- Reviewing code before commit

- Identifying quality issues

- Providing feedback on implementation

- Validating adherence to standards



**Recognition Pattern**: Language about "review", "validate", "assess quality", "audit"



**Why Domain + Work Type**: In the main codebase, the domain alone (packages/**) doesn't tell you which specialist. You need to understand the work type. But in Claude Code ecosystem domains, the domain alone often suffices (`.claude/agents/**` → agent-architect).



---



**The Documentation Domain** (`docs/**`)



Documentation work has its own specialists based on the type of document and the work being done:



**spec-enhancer** - Creating specifications

- Writing new SPEC.md files from scratch or roadmap items

- Comprehensive specification creation (SDD mode)

- Component breakdown and planning metadata

- Regenerative development structure



**Recognition Pattern**: New specification creation, file path includes `**/SPEC.md`, emphasis on requirements and specifications



**spec-reviewer** - Validating specifications

- Reviewing SPEC.md quality

- Checking requirements completeness

- Detecting ambiguity and testability issues

- Ensuring HOW vs WHAT/WHY boundaries



**Recognition Pattern**: Review or validation of existing specifications



**plan-enhancer** - Business context in plans

- Adding business requirements to plans

- Requirements traceability (FR-IDs)

- Code reuse opportunity identification

- Systematic placeholder replacement with business detail



**Recognition Pattern**: Plan files (`**/PLAN.md` or `/plans/`), emphasis on business requirements, pain points, user value



**architecture-enhancer** - Technical architecture in plans

- Populating technical sections of plans

- Context7 architecture pattern research

- Component Almanac integration

- Technology stack decisions with rationale



**Recognition Pattern**: Plan files, emphasis on technical architecture, NFRs, patterns, implementation approach



**task-creator** - Generating tasks

- Creating task lists from PLAN.md files

- Agent assignment for each task

- Dependency identification

- Parallel execution opportunities



**Recognition Pattern**: Task generation work, `/tasks/` directories, converting plans to executable tasks



**technical-pm** - Business alignment review

- Validating business alignment of plans

- ROI validation

- Strategic alignment assessment

- Requirements coverage analysis



**Recognition Pattern**: Review work focused on business value, alignment, strategic fit



**architecture-review** - Technical feasibility review

- Technical feasibility scoring

- NFR validation (performance, security, operational)

- Production readiness evaluation

- Technology choice validation



**Recognition Pattern**: Review work focused on technical approach, architecture, feasibility



**doc-librarian** - Documentation health

- Link validation

- Naming convention enforcement

- Organization compliance

- Cross-reference integrity



**Recognition Pattern**: Maintenance work on documentation structure, not content


**doc-reference-optimizer** - Documentation optimization
- Analyzing agent prompts for verbose content
- Identifying reference replacement opportunities
- Token savings calculation
- Optimization strategy recommendations

**Recognition Pattern**: Agent prompt optimization, documentation refactoring

---



---



**Cross-Domain Work**



Some agents work across all domains based on the **nature of the work**, not the location:



**researcher-*** family - Information gathering

- **researcher-codebase**: Deep code analysis, pattern discovery in the codebase

- **researcher-web**: External research, best practices, industry standards

- **researcher-library**: Official library documentation, API references (Context7)

- **researcher-lead**: Strategic research planning, delegation coordination



**Recognition Pattern**: Work is fundamentally about gathering information, discovering patterns, researching approaches. Location doesn't matter—research work is recognized by intent to learn/discover.



**tech-debt-investigator** - Debt analysis

- Technical debt identification across any codebase location

- Prioritization and remediation planning

- Duplicate functionality detection

- Hotspot analysis



**Recognition Pattern**: Focus on identifying problems, debt, duplication, not on creating or fixing



**git-github** - Git operations

- File grouping for commits

- Git operations execution

- CI monitoring

- Conventional commits



**Recognition Pattern**: Explicit git/GitHub operations regardless of files involved



**sast-scanner** - Security scanning

- Static security analysis across codebase

- Vulnerability detection

- OWASP compliance checking



**Recognition Pattern**: Security scanning, vulnerability detection focus


**intent-analyzer** - Request decomposition
- Breaking down complex multi-intent requests
- Task graph generation with dependencies
- OODA OBSERVE phase coordination

**Recognition Pattern**: Multi-step requests, complex task coordination, dependency analysis

---

**context-readiness-assessor** - Context quality gating
- Assessing context sufficiency before implementation
- Coordinating research agents to fill gaps
- Quality gate enforcement (0.0-1.0 scoring)
- OODA ORIENT phase gating

**Recognition Pattern**: Complex features, unfamiliar domains, quality gates before implementation

---

**hypothesis-former** - Solution hypothesis generation
- Generating 2-5 ranked solution approaches
- DCS scoring and feasibility analysis
- Trade-off matrices for decision-making
- OODA DECIDE phase component

**Recognition Pattern**: Multiple solution paths, architectural decisions, approach selection

---

**contingency-planner** - Failure mode planning
- Identifying 3-5 failure modes per approach
- Risk scoring (probability × impact)
- Fallback strategy generation
- OODA DECIDE phase resilience

**Recognition Pattern**: High-risk features, production deployments, resilience planning

---

**context-optimizer** - Context management
- Token budget optimization
- Context pruning and compression
- Progressive disclosure strategies

**Recognition Pattern**: Large context windows, token optimization needs

---



---



### Domain-First Thinking in Practice



**Step 1**: Look at file paths mentioned in the task

**Step 2**: Identify which domain(s) these paths belong to

**Step 3**: If a single domain and that domain has a clear specialist (`.claude/agents/**`, `.claude/**`, specific docs patterns), you likely have your answer

**Step 4**: If main codebase domain, proceed to work type recognition (Framework 2)

**Step 5**: If cross-domain work, recognize the nature of work (research, debt analysis, git operations)



**Key Insight**: Domain provides the strongest signal for agent selection. Start there, always.



---



## Framework 2: Work Type Recognition



**Core Principle**: Within the same domain (especially main codebase), different types of work require different specialists. Recognize the work type by understanding the task's intent.



### The Two Primary Work Types



#### Creation Work - Bringing Something New Into Existence



**Characteristics**:

- Building a feature that doesn't exist yet

- Writing new code from specifications

- Implementing defined requirements

- Adding new capabilities



**Language Signals**:

- "create", "build", "implement", "add new feature"

- Emphasis on **newness**

- Focus on construction and bringing into existence



**Main Codebase Agent**: code-implementer



**Example**: "Implement payment processing feature in `packages/payments/processor.py`"

- Work type: Creation (new functionality)

- Domain: Main codebase (packages/**)

- Agent: code-implementer



---



#### Investigation Work - Understanding What Exists or Why It Fails



**Characteristics**:

- Discovering root causes of failures

- Understanding why tests aren't passing

- Researching patterns in existing code

- Analyzing why behavior is unexpected



**Language Signals**:

- "debug", "investigate", "find out why", "analyze", "troubleshoot"

- Emphasis on **discovery and understanding**

- Focus on answering "why" questions



**Main Codebase Agent**: debugger (for failures) or researcher-codebase (for patterns)



**Example**: "Debug why login tests are failing in `tests/auth/test_login.py`"

- Work type: Investigation (unknown cause)

- Domain: Main codebase (tests/**)

- Agent: debugger



---



#### Improvement Work - Enhancing What Already Exists



**Characteristics**:

- Restructuring code for better organization

- Optimizing performance

- Improving modularity and separation of concerns

- Refactoring without changing behavior



**Language Signals**:

- "refactor", "restructure", "reorganize", "improve structure", "optimize"

- Emphasis on **making existing things better**

- Focus on transformation of existing code



**Example**: "Refactor auth module to improve separation of concerns in `packages/auth/`"

- Work type: Improvement (structural)

- Domain: Main codebase (packages/**)

---



#### Read-Only Analysis Mode



**Key Distinction**: Many agents can operate in two modes:

- **Implementation Mode**: Create, modify, fix (uses Write/Edit tools)

- **Analysis Mode**: Investigate, assess, report (uses Read/Grep only)



**Language Signals for Analysis Mode**:

- "analyze", "investigate", "assess", "review", "evaluate"

- "understand patterns", "discover issues", "identify gaps"

- Emphasis on discovery and reporting, NOT making changes



**Agent Selection**:

- **Analysis within domain** → Use domain specialist in read-only mode

- **Analysis across domains** → Use researcher-* family or tech-debt-investigator



**Examples**:



**Scenario**: "Analyze authentication code for security vulnerabilities"

- Domain: `packages/**` (auth code)

- Work Type: Analysis (security assessment)

- Mode: Read-only (no fixes, just report)

- **Decision**: code-reviewer (security analysis expertise) OR debugger (pattern analysis) in read-only mode

- **Why not code-implementer**: Work type is analysis, not implementation



**Scenario**: "Analyze agent definitions for duplication"

- Domain: `.claude/agents/**`

- Work Type: Analysis (duplication detection)

- Mode: Read-only (report findings)

- **Decision**: agent-architect (agent domain expert) in read-only mode

- **Why not researcher-codebase**: agent-architect has deeper agent-specific expertise



**Scenario**: "Analyze plan quality and completeness"

- Domain: `docs/**` plans

- Work Type: Analysis (quality assessment)

- Mode: Read-only review

- **Decision**: technical-pm (business alignment) + architecture-review (technical quality)

- **Why not plan-enhancer**: Work type is assessment, not enhancement



---



### Distinguishing Ambiguous Work Types



#### The "Fix" Ambiguity



The word "fix" can mean different types of work depending on context:



**"Fix failing tests" when root cause is unknown**:

- This is investigation work (need to discover why)

- Agent: debugger



**"Fix failing tests" when root cause is known**:

- This is implementation work (apply known solution)

- Agent: code-implementer



**"Fix code structure"**:

- This is improvement work (restructuring)

**Decision Approach**: What kind of "fixing" is needed? Discovery-based, implementation-based, or improvement-based?



---



#### The "Create Tests" vs "Run Tests" vs "Fix Failing Tests"



**"Create tests for new feature"**:

- Writing test code

- Agent: test-creator



**"Run tests and report failures"**:

- Executing test suite and analyzing results

- Agent: test-executor



**"Fix failing tests" (unknown cause)**:

- Debugging test failures

- Agent: debugger



**"Fix failing tests" (known issue in implementation)**:

- Fixing the code being tested

- Agent: code-implementer



**Decision Approach**: Is the work about test creation (test-creator), test execution (test-executor), discovering problems (debugger), or fixing implementation (code-implementer)?



---



## Framework 3: Agent Expertise Mapping



**Core Principle**: Each agent has developed deep expertise in a specific domain or work type. Match the task to the agent whose expertise best fits. Don't just match technical capability—match domain knowledge.



### The Specialist Principle



**Why Specialists Matter**:



A generalist can edit any Markdown file. A specialist has developed:

- **Deep patterns** specific to their domain

- **Templates and structures** that ensure quality

- **Knowledge of pitfalls** in their area

- **Understanding of best practices** for their work type



Using the right specialist means better quality, faster execution, and fewer errors.



### Technical Capability vs Domain Expertise



**Anti-Pattern**: "code-implementer can edit any Python file, so use it for everything in packages/**"



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



### Domain Expertise Examples



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

- Code organization in packages/**

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



### The Domain Alignment Principle



**Agents Are Shaped By Their Domains**:



An agent who has worked repeatedly in `.claude/agents/**` has developed mental models specific to agent lifecycle work. An agent who has worked repeatedly in `packages/**` has developed mental models specific to code implementation.



**Don't force an agent outside their shaped expertise** unless necessary.



**Recognition Pattern**: When selecting an agent, think "has this agent's experience prepared them for this specific type of work?"



---



### Read-Only Research Workers



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



---



## Framework 4: Multi-Agent Decision Framework



**Core Principle**: Some tasks are too complex or too critical for a single agent. Recognize when multiple perspectives or sequential expertise is needed.



### Complexity Signals



**Single-Agent Indicators**:

- Task scope is clear and contained within one domain

- One type of expertise suffices

- Straightforward file paths indicating single domain

- Low risk if something is missed (not security-critical, not high-impact)



**Multi-Agent Indicators**:

- Task spans multiple domains (e.g., "implement + test + document")

- High criticality (security, payments, authentication, data privacy)

- Multiple perspectives valuable (business validation + technical validation)

- Need for validation checkpoints (implement → review → verify)

- Unfamiliar domain requiring research before action



**Recognition Pattern**: When you see "and" connecting different work types ("implement AND test AND document"), think about whether each needs its own specialist.



---



### The Sequential Pipeline Pattern



**When to Use**: Tasks where later steps depend on earlier steps, and each step requires different expertise.



**Structure**: Step 1 (Agent A) → Step 2 (Agent B) → Step 3 (Agent C)



**Example**: Creating a secure payment feature

1. **researcher-web** - Research OWASP payment security patterns (context gathering)

2. **researcher-library** - Research Stripe SDK best practices (library-specific patterns)

3. **code-implementer** - Implement with researched patterns (creation)

4. **test-creator** - Create comprehensive test suite (generation)

5. **test-executor** - Validate test execution (validation)

6. **code-reviewer** - Security-focused code review (quality gate)



**Why Sequential**: Each step builds on the previous. Can't implement securely without research. Can't test before implementation. Can't review before code exists.



**Recognition Pattern**: Dependencies between steps. Output of step N is input to step N+1.



---



### The Parallel Validation Pattern



**When to Use**: Need multiple independent perspectives on the same artifact. All perspectives are equally valuable and can be gathered simultaneously.



**Structure**: All agents review in parallel → Orchestrator synthesizes



**Example**: Reviewing an implementation plan

- **technical-pm** - Business alignment, ROI, strategic fit, requirements coverage

- **architecture-review** - Technical feasibility, NFRs, technology choices, production readiness

- **tech-debt-investigator** - Duplicate detection, cleanup needs, debt implications



**Why Parallel**: Each brings a different lens to the same plan. Reviews are independent—technical-pm doesn't need to wait for architecture-review.



**Recognition Pattern**: Same input artifact, different evaluation criteria, no dependencies between reviews.



---



### The Research-Then-Act Pattern



**When to Use**: Context is missing or confidence would be low without research. Need to gather information before taking action.



**Structure**: researcher-* (context gathering) → specialist agent (action with context)



**Example**: "Add caching to API endpoints" when unfamiliar with existing caching patterns

1. **researcher-codebase** - Discover existing caching patterns in the codebase

2. **code-implementer** - Implement using discovered patterns (higher confidence, consistent with existing approach)



**Why Research First**: Without research, code-implementer might implement caching differently from existing patterns, creating inconsistency or duplicating utilities.



**Recognition Pattern**:

- Unfamiliar domain or pattern

- Risk of duplicating existing functionality

- Need to understand "how we do this here" before acting



---



### Recognizing When Single Agent Suffices



**Don't default to multi-agent for everything**. Multi-agent adds overhead (time, coordination complexity).



**Use single agent when**:

- Domain is clear and matches agent expertise perfectly

- Task is well-defined with no ambiguity

- Risk is low (not security-critical)

- No cross-domain work involved

- Context is sufficient



**Example**: "Create unit tests for login feature in `tests/auth/test_login.py`"

- Clear domain: tests/**

- Clear work type: test creation

- Clear agent: test-creator

- No need for multi-agent (unless feature is security-critical, then add code-reviewer after)



---



## Framework 5: Context-Aware Selection



**Core Principle**: The visible task description may not contain all the context needed to do the work well. Sometimes gathering context IS the first task.



### The "What Don't I Know?" Check



Before assigning an implementation agent, mentally check:



**Questions to Ask**:

- How many related files might this change touch?

- Are there existing patterns in the codebase I should follow?

- What dependencies exist that could be affected?

- Is this potentially duplicating functionality that already exists?

- Do I understand the full scope of this change?



**If Answers Are "I Don't Know"**: Consider starting with **researcher-codebase** to gather context, then delegate to implementation agent with enriched understanding.



---



### The Single-File Assumption Trap



**Anti-Pattern**: Task mentions one file → assume it's a simple one-file change → assign implementation agent directly



**Reality Check**:

- Changing `packages/auth/login.py` might affect:

  - 10 other files that import it

  - Test files that verify its behavior

  - Config files that reference it

  - Other modules that depend on its interface



**The Hidden Complexity**: What looks like a one-file task might have a "context radius" of many related files.



**Decision Framework**:

- **1 file, truly isolated** (utility function, new module):

  - Direct to implementation agent



- **1 file + context of 5-10 related files**:

  - researcher-codebase first (understand dependencies)

  - Then implementation agent with context



- **2-4 files mentioned in task**:

  - researcher-codebase for synthesis (understand relationships)

  - Then implementation agent



- **5+ files mentioned**:

  - researcher-codebase for pattern discovery (find common themes)

  - Possibly multiple implementation agents in parallel



**Why This Matters**: Implementation without context often leads to:

- Breaking existing functionality

- Inconsistent patterns with rest of codebase

- Duplicating utilities that already exist

- Missing edge cases that existing code handles



---



### The Security Context Trigger



**Automatic Research Requirement**: Certain domains require research before implementation, regardless of file count or apparent simplicity.



**High-Risk Domains**:

- Authentication/Authorization

- Payment processing

- External API integration

- Data privacy/PII handling

- Cryptography

- Input validation/sanitization



**Required Pattern**: researcher-web (OWASP/security best practices) → implementation agent → code-reviewer (security lens)



**Why Automatic**: Security mistakes are expensive. Even experienced developers miss security issues. Research establishes the right patterns before writing vulnerable code.



**Example**: "Implement password reset in `packages/auth/reset.py`"

1. **researcher-web** - Research OWASP authentication patterns, password reset best practices

2. **code-implementer** - Implement with security patterns

3. **code-reviewer** - Security-focused review



Even if reset.py is a single new file, the security context requires research-then-implement.



---



### Context Quality Assessment



**High Context Quality** (can proceed directly):

- Task includes detailed requirements

- Patterns are explicitly specified

- Dependencies are listed

- Examples are provided

- Clear acceptance criteria



**Low Context Quality** (gather context first):

- Task is vague ("improve auth")

- No patterns specified

- Unknown dependencies

- No examples

- Ambiguous success criteria



**Recognition Pattern**: If you're uncertain about approach or scope, context gathering is the first task.



---



## Framework 6: Disambiguation Principles



**Core Principle**: When multiple agents seem to fit equally well, use these principles to distinguish the best choice.



### Principle 1: Domain Ownership Trumps All



**When in doubt, domain ownership is the strongest signal.**



Domain boundaries are deliberately designed. Agents have developed expertise in their domains. Respect those boundaries even when technical capability suggests alternatives.



**Example**: "Update agent list in CLAUDE.md"

- Technical capability: Many agents can edit Markdown files

- Domain ownership: CLAUDE.md is Claude Code configuration

- Domain owner: **claude-code**

- **Decision**: claude-code (domain ownership wins)



**Why This Principle**: Domain owners understand:

- The structure and conventions of their domain

- The implications of changes in their domain

- Common pitfalls in their domain

- How their domain integrates with others



**Application**: Always check domain first. If domain has a clear owner, that's usually your answer.



---



### Principle 2: Closest Expertise Match



**When agents overlap in capability, choose the one whose expertise is the closest match to the work type.**



**Example**: "Fix bug in auth.py where login fails with 500 error"



**Agents That Could Technically Do This**:

- debugger (expertise: investigation, root cause analysis)

- code-implementer (expertise: implementation, code writing)




**Analysis**:

- Is root cause known? → No, "login fails with 500 error" doesn't specify why

- Is this investigation work? → Yes, need to discover why

- **Closest expertise**: debugger (investigation is their specialization)

- **Decision**: debugger



**Alternative Scenario**: "Fix known bug in auth.py where missing null check causes 500 error"

- Is root cause known? → Yes, "missing null check" is specific

- Is this investigation work? → No, it's straightforward implementation

- **Closest expertise**: code-implementer (implementation is their specialization)

- **Decision**: code-implementer



**Why This Principle**: The agent whose expertise most closely matches the work type will do the highest quality work in the least time.



---



### Principle 3: Least Assumptions



**When the task is ambiguous or vague, choose the agent that makes the fewest assumptions about what's wanted.**



**Example**: "Improve code quality in payment.py"



**What "improve" could mean**:

- Add comments and documentation

- Restructure for better organization

- Fix bugs

- Optimize performance

- Add error handling

- All of the above?



**Agents That Could Handle This**:

- code-reviewer (assumption: you want feedback on issues)


- code-implementer (assumption: you want new code added)

- debugger (assumption: there are bugs to fix)



**Least Assumptions**:

- **code-reviewer**: Provides feedback on what could be improved, doesn't change code

- **Others**: All assume a specific type of improvement and make changes



**Decision**: code-reviewer (least invasive, provides information that clarifies what "improve" means)



**Why This Principle**: Vague tasks benefit from starting with feedback. code-reviewer's output clarifies what improvements are needed, then you can delegate to the appropriate specialist (code-implementer, debugger) with clear direction.



**Sequential Pattern**: Ambiguous request → code-reviewer (clarify) → specific agent (implement)



---



### Principle 4: Workload Balance



**When two agents are equally qualified, consider recent task distribution to avoid overloading one agent.**







**Why This Principle**:

- No agent should monopolize all work

- Distributed workload suggests healthy use of specializations

- Prevents systematic overuse of one agent (the original problem with code-implementer)

- Better task distribution means agents stay within their expertise zones



**When to Apply**: Only as a tie-breaker. Don't sacrifice expertise match for workload balance. But when expertise is equal, workload balance is a reasonable consideration.



---



### Combining Principles



**The Hierarchy**:

1. **Domain Ownership** (strongest signal)

2. **Closest Expertise** (when domain doesn't fully determine)

3. **Least Assumptions** (when task is ambiguous)

4. **Workload Balance** (when all else is equal)



**Example Application**: "Update schema validation in `.claude/docs/schemas/agent-schema.json`"



**Check Each Principle**:

1. **Domain Ownership**: `.claude/docs/schemas/**` - Could be agent-architect (agent schemas) or claude-code (Claude Code schemas). Let's check further.

2. **Closest Expertise**: "agent-schema.json" specifically → agent schemas → agent-architect has deepest expertise in agent-related artifacts

3. **Decision**: agent-architect (domain + expertise align)



**No Need for Principles 3 & 4**: Clear answer from domain and expertise.



---



## Framework 7: Anti-Patterns to Avoid



**Core Principle**: Learn from common mistakes to develop better selection intuition. Knowing what NOT to do is as valuable as knowing what to do.



### Anti-Pattern 1: Default to Most Familiar Agent



**Mistake**: Always choosing code-implementer because it's used most often or appears most frequently in task histories.



**Why It's Wrong**:

- Familiarity ≠ Best Fit

- Each agent exists because they bring specialized expertise

- Defaulting to one agent ignores the value of specialization

- Creates the original problem (code-implementer overweighting)



**Real Example**: "Review code quality in auth module"

- Familiar choice: code-implementer (it does lots of things)

- Right choice: code-reviewer (specialized in quality review)



**Better Approach**: Let domain and work type guide selection based on expertise match, not habit or frequency of use.



**Self-Check**: "Am I choosing this agent because it's the right expertise, or because it's the one I think of first?"



---



### Anti-Pattern 2: Ignore Domain Boundaries



**Mistake**: Using code-implementer for `.claude/agents/**` work because "it can edit Markdown files" or "it writes code and prompts are kind of like code."



**Why It's Wrong**:

- Technical capability (editing .md files) ≠ Domain expertise (agent prompt engineering)

- code-implementer hasn't developed agent-architect's expertise in:

  - Prompt engineering patterns

  - Agent evaluation criteria

  - Simulation-driven development

  - Anthropic's best practices

- Ignoring boundaries produces lower quality work



**Real Example**: "Create sentiment-analyzer agent in `.claude/agents/sentiment-analyzer.md`"

- Wrong: code-implementer (can edit .md files)

- Right: agent-architect (domain specialist for agent lifecycle)



**Better Approach**: Domain boundaries are hard boundaries. They exist for a reason. Respect specializations regardless of file format.



**Self-Check**: "Am I choosing based on file type capability, or based on domain expertise?"



---



### Anti-Pattern 3: Single Agent for Cross-Domain Tasks



**Mistake**: "Implement user authentication with tests and documentation" → assign to code-implementer for everything.



**Why It's Wrong**:

- Forces one agent to work across multiple domains:

  - `packages/**` (implementation) - code-implementer's domain

  - `tests/**` (testing) - test-creator's and test-executor's domain

  - `docs/**` (documentation) - documentation agents' domain

- Each part gets lower quality than using the specialist

- Documentation specialists know specification structure better than code-implementer

- test-creator knows test design patterns better than code-implementer

- test-executor knows test execution patterns better than code-implementer



**Better Approach**: Decompose cross-domain tasks into specialist sequences.



**Correct Decomposition**:

- T001 [test-creator] Create test suite in `tests/auth/`

- T002 [code-implementer] Implement authentication in `packages/auth/`

- T003 [test-executor] Validate tests pass

- T004 [code-reviewer] Security-focused review

- T005 [spec-enhancer] Document authentication flow in `docs/auth-spec.md`



**Self-Check**: "Does this task span multiple domains? Should I decompose it?"



---



### Anti-Pattern 4: Keyword Matching Without Context



**Mistake**: Task contains "create" → automatically assign code-implementer without considering what's being created or where.



**Why It's Wrong**:

- "Create SPEC.md" and "Create auth.py" both contain "create"

- But they need different specialists:

  - "Create SPEC.md" → spec-enhancer (documentation domain)

  - "Create auth.py" → code-implementer (main codebase domain)

- Keywords are hints, not rules

- Context (domain, work type) matters more than individual words



**Real Example**:

- "Create agent evaluation in `.claude/agents/evaluator.md`"

  - Keyword: "create" (suggests code-implementer)

  - Domain: `.claude/agents/**` (agent lifecycle)

  - Work type: Agent creation

  - **Right choice**: agent-architect (domain + work type override keyword)



**Better Approach**:

1. Don't start with keywords

2. Start with domain (Framework 1)

3. Then work type (Framework 2)

4. Keywords can confirm, but domain/work type determine



**Self-Check**: "Am I pattern matching words, or understanding the task's nature?"



---



### Anti-Pattern 5: Ignore Security Context



**Mistake**: Treating authentication, payment processing, or data privacy tasks like any other implementation.



**Why It's Wrong**:

- Security domains have specific patterns and pitfalls

- General implementation agents might not know OWASP guidelines

- Security mistakes are expensive (data breaches, compliance violations, reputation damage)

- "Move fast and break things" doesn't apply to security



**Real Example**: "Implement OAuth login in `packages/auth/oauth.py`"

- Wrong: code-implementer alone (might implement insecurely)

- Right: researcher-web (OWASP patterns) → code-implementer (secure implementation) → code-reviewer (security validation)



**Security Domains Requiring Research**:

- Authentication/Authorization

- Payment processing

- Cryptography

- Session management

- Input validation

- Data privacy/PII

- External API keys/secrets



**Better Approach**: Recognize security context → automatically trigger research-then-implement-then-review pattern.



**Self-Check**: "Is this security-sensitive? Do I need research and additional validation?"



---



### Anti-Pattern 6: Assume Simple Based on File Count



**Mistake**: "Only touching one file, so it's simple" → assign directly to implementation agent without context gathering.



**Why It's Wrong**:

- One file might have 20 dependents

- Changing a model file affects all services using it

- Modifying a utility affects all callers

- "Simple" based on file count ≠ simple based on impact



**Real Example**: "Update User model in `packages/models/user.py`"

- Looks simple: one file

- Reality: 15 services import User model

- Impact: Need to understand all usages before changing



**Better Approach**: Even for "one file", ask:

- How many files depend on this?

- What's the impact radius?

- Should I gather context first?



If impact is unclear, start with researcher-codebase.



**Self-Check**: "Am I confusing file count with complexity?"



---



### Anti-Pattern 7: No Default Fallback → Default to code-implementer



**Mistake**: "I don't know which agent to use, so I'll default to code-implementer since it's versatile."



**Why It's Wrong**:

- This is exactly how code-implementer became overweighted

- Defaulting to any agent for ambiguous cases hides the ambiguity

- Forces an agent to work outside their expertise

- Produces lower quality work



**Better Approach**: If agent selection is genuinely ambiguous after applying all frameworks, **mark for manual review** rather than defaulting.



**Return**: "Agent selection ambiguous. Considered agents: X, Y, Z. Disambiguation needed: [specific question]"



**Why This Is Better**:

- Makes ambiguity visible

- Forces clarification of requirements

- Prevents systematic misassignment

- Ensures right agent for the actual (clarified) task



**Self-Check**: "Am I defaulting because I'm certain, or because I don't want to say 'I don't know'?"



---



## Quick Reference Summary



### Decision Flow



1. **Apply Domain-First Thinking** (Framework 1)

   - Check file paths

   - Identify domain(s)

   - If single domain with clear specialist → likely have your answer



2. **Recognize Work Type** (Framework 2)

   - If main codebase domain, what kind of work?

   - Creation, investigation, improvement, validation, testing?



3. **Check Agent Expertise** (Framework 3)

   - Does the agent's expertise align with this work?

   - Domain expertise match?



4. **Consider Multi-Agent** (Framework 4)

   - Does complexity or criticality suggest multiple agents?

   - Cross-domain work?

   - Security-critical?



5. **Assess Context Needs** (Framework 5)

   - Is context sufficient?

   - Should I gather context first?



6. **Apply Disambiguation** (Framework 6)

   - Still ambiguous? Use principles:

     - Domain ownership

     - Closest expertise

     - Least assumptions

     - Workload balance



7. **Avoid Anti-Patterns** (Framework 7)

   - Not defaulting to familiar?

   - Respecting domain boundaries?

   - Not keyword matching?

   - Considering security context?



---



## Integration with Other Frameworks



**This guide complements**:

- **Delegation Confidence Scoring (DCS)** (`docs/01-planning/custom/confidence-based-delegation-framework.md`) - Use this guide for common patterns (80%), DCS for novel/complex scenarios (20%)

- **Orchestrator Workflow** (`.claude/docs/orchestrator-workflow.md`) - This guide informs agent selection within orchestrator's coordination patterns

- **Research Patterns** (`.claude/docs/guides/research-patterns.md`) - Research-then-act pattern integrates with researcher-lead delegation



**When to Use This Guide vs DCS**:

- **This guide**: Common patterns, known domains, standard work types

- **DCS calculation**: Novel scenarios, unclear confidence, complex multi-factor decisions



Both enforce domain boundaries and avoid keyword-only matching.



---



## Examples in Practice



### Example 1: "Fix the failing login tests"



**Apply Frameworks**:

1. **Domain**: `tests/**` (testing domain)

2. **Work Type**: "Fix" + "failing" → Investigation or implementation?

   - Is cause known? Not stated.

   - Assume unknown → Investigation work

3. **Agent Expertise**: debugger (investigation specialist)

4. **Multi-Agent?**: Not needed initially (can add if debugging reveals implementation issues)

5. **Context**: Test failure output will provide context

6. **Decision**: debugger



**Alternative Scenario**: "Fix the failing login tests (missing null check in LoginService)"

- Cause is known ("missing null check")

- Work type: Implementation (apply known fix)

- **Decision**: code-implementer



---



### Example 2: "Create payment processing feature"



**Apply Frameworks**:

1. **Domain**: `packages/**` (main codebase)

2. **Work Type**: Creation (new feature)

3. **Agent Expertise**: code-implementer... but wait

4. **Multi-Agent?**: Check criticality

   - Payment processing → HIGH CRITICALITY

   - Security-sensitive domain

   - **Multi-agent required**

5. **Context**: Need security research

6. **Pattern**: Sequential pipeline

   - researcher-web (OWASP payment patterns)

   - researcher-library (payment SDK best practices)

   - code-implementer (secure implementation)

   - test-creator (comprehensive test design)

   - test-executor (test validation)

   - code-reviewer (security-focused review)

7. **Decision**: Multi-agent sequential pipeline



---



### Example 3: "Update CLAUDE.md with new agent list"



**Apply Frameworks**:

1. **Domain**: `CLAUDE.md` (Claude Code configuration)

2. **Domain Specialist**: claude-code

3. **Work Type**: Update (modification)

4. **Disambiguation**: Could others edit Markdown? Yes, technically

   - **But domain ownership principle**: claude-code owns CLAUDE.md

5. **Decision**: claude-code (domain ownership)



---



### Example 4: "Analyze patterns in authentication code"



**Apply Frameworks**:

1. **Domain**: `packages/**` likely (main codebase)

2. **Work Type**: Investigation (analysis, pattern discovery)

3. **Multi-file?**: Probably (authentication code spans files)

4. **Agent Expertise**: researcher-codebase (pattern discovery specialist)

5. **Context**: This IS context gathering

6. **Decision**: researcher-codebase



**Why not code-implementer?**: Work type is investigation, not creation.

**Why not debugger?**: Not fixing failures, discovering patterns.



---



## Conclusion



**Core Takeaway**: Agent selection is about understanding domain, work type, and expertise alignment—not about keyword matching or defaults.



**The Seven Frameworks** provide different lenses for understanding tasks:

1. Where is the work? (Domain)

2. What kind of work is it? (Work Type)

3. Who specializes in this? (Expertise)

4. Is it complex enough for multiple agents? (Multi-Agent)

5. Do I have enough context? (Context-Aware)

6. How do I choose when ambiguous? (Disambiguation)

7. What mistakes should I avoid? (Anti-Patterns)



**Apply these frameworks** and agent selection becomes clear in 80% of cases. For the remaining 20% (novel, complex scenarios), use DCS calculation.



**Remember**: Respecting domain boundaries and matching expertise produces better work than defaulting to the most familiar agent.