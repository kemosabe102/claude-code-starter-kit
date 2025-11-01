# Framework 1: Domain-First Thinking

**Core Principle**: File location reveals domain. Domain determines specialist agent.

## Understanding Domain Boundaries

### Claude Code Ecosystem (`.claude/**`)

Tasks involving `.claude/**` files are about maintaining the Claude Code system itself.

#### Agent Lifecycle Work (`.claude/agents/**`)

**Domain Owner**: agent-architect

**Expertise**:
- Prompt engineering patterns
- Agent simulation and evaluation
- 9-criteria quality matrix
- Workflow integration patterns
- Anthropic's agent design best practices

**Recognition**: File paths in `.claude/agents/**`

**Example**: "Create intent-analyzer agent in `.claude/agents/intent-analyzer.md`"
- Keywords: "create" (could suggest code-implementer)
- Domain signal: `.claude/agents/**` path
- **Decision**: agent-architect (domain ownership trumps keyword)

#### Claude Code Configuration (`.claude/**` excluding agents)

**Domain Owner**: claude-code

**Expertise**:
- Claude Code system architecture
- Slash command structure and invocation patterns
- Hook lifecycle and event handling
- Schema validation and structure
- Integration between agents, commands, and hooks

**Recognition**: `.claude/**` paths NOT in agents subdirectory

**Example**: "Update output style in `.claude/output-style.md`"
- Keywords: "update" (could suggest code-implementer)
- Domain signal: `.claude/**` path (non-agents)
- **Decision**: claude-code (domain ownership)

---

### Main Codebase Domain (`packages/**`, `tests/**`, `scripts/**`)

Application business logic lives here. Multiple specialists work in this domain, distinguished by **work type** rather than location alone.

**code-implementer** - Creating new functionality
- Implementing features that don't exist yet
- Building new code from specifications
- Adding new capabilities to existing systems
- Writing implementation code for defined requirements

**Recognition**: Language emphasizing newness, creation, bringing something into existence

**test-creator** - Test generation and design
- Creating test suites for features
- Generating test cases
- Designing test strategies
- Analyzing coverage gaps

**Recognition**: Keywords: "create tests", "generate tests", "design tests", "test coverage analysis"

**test-executor** - Test execution and validation
- Running existing tests and reporting results
- Parsing test output and failure categorization
- Executing test suites with pytest
- Validating test execution results

**Recognition**: Keywords: "run tests", "execute tests", "validate tests", "test failures"

**test-dataset-creator** - Test data generation
- Mining git history for test scenarios
- Generating diverse validation datasets
- Pydantic-validated JSON fixture creation
- Domain heuristics for ground truth

**Recognition**: Keywords: "test data", "fixtures", "test scenarios", "validation datasets"

**debugger** - Investigating failures
- Discovering why tests are failing (unknown cause)
- Hypothesis-driven problem solving
- Root cause analysis when behavior is unexpected
- Non-invasive experimentation to understand issues

**Recognition**: Language about discovery, investigation, "why is this failing", "debug", "troubleshoot". Emphasis on unknown cause.

**code-reviewer** - Quality gates and feedback
- Reviewing code before commit
- Identifying quality issues
- Providing feedback on implementation
- Validating adherence to standards

**Recognition**: Keywords: "review", "validate", "assess quality", "audit"

**Key Insight**: In main codebase, domain alone (`packages/**`) doesn't determine specialist. You need work type. But in Claude Code ecosystem domains, domain alone often suffices (`.claude/agents/**` → agent-architect).

---

### Documentation Domain (`docs/**`)

Documentation work has its own specialists based on document type and work being done.

**spec-enhancer** - Creating specifications
- Writing new SPEC.md files from scratch or roadmap items
- Comprehensive specification creation (SDD mode)
- Component breakdown and planning metadata
- Regenerative development structure

**Recognition**: New specification creation, `**/SPEC.md`, emphasis on requirements and specifications

**spec-reviewer** - Validating specifications
- Reviewing SPEC.md quality
- Checking requirements completeness
- Detecting ambiguity and testability issues
- Ensuring HOW vs WHAT/WHY boundaries

**Recognition**: Review or validation of existing specifications

**plan-enhancer** - Business context in plans
- Adding business requirements to plans
- Requirements traceability (FR-IDs)
- Code reuse opportunity identification
- Systematic placeholder replacement with business detail

**Recognition**: Plan files (`**/PLAN.md` or `/plans/`), emphasis on business requirements, pain points, user value

**architecture-enhancer** - Technical architecture in plans
- Populating technical sections of plans
- Context7 architecture pattern research
- Component Almanac integration
- Technology stack decisions with rationale

**Recognition**: Plan files, emphasis on technical architecture, NFRs, patterns, implementation approach

**task-creator** - Generating tasks
- Creating task lists from PLAN.md files
- Agent assignment for each task
- Dependency identification
- Parallel execution opportunities

**Recognition**: Task generation work, `/tasks/` directories, converting plans to executable tasks

**technical-pm** - Business alignment review
- Validating business alignment of plans
- ROI validation
- Strategic alignment assessment
- Requirements coverage analysis

**Recognition**: Review work focused on business value, alignment, strategic fit

**architecture-review** - Technical feasibility review
- Technical feasibility scoring
- NFR validation (performance, security, operational)
- Production readiness evaluation
- Technology choice validation

**Recognition**: Review work focused on technical approach, architecture, feasibility

**doc-librarian** - Documentation health
- Link validation
- Naming convention enforcement
- Organization compliance
- Cross-reference integrity

**Recognition**: Maintenance work on documentation structure, not content

**doc-reference-optimizer** - Documentation optimization
- Analyzing agent prompts for verbose content
- Identifying reference replacement opportunities
- Token savings calculation
- Optimization strategy recommendations

**Recognition**: Agent prompt optimization, documentation refactoring

---

### Cross-Domain Work

Some agents work across all domains based on **nature of the work**, not location.

**researcher-*** family - Information gathering
- **researcher-codebase**: Deep code analysis, pattern discovery in the codebase
- **researcher-web**: External research, best practices, industry standards
- **researcher-library**: Official library documentation, API references (Context7)
- **researcher-lead**: Strategic research planning, delegation coordination

**Recognition**: Work is fundamentally about gathering information, discovering patterns, researching approaches. Location doesn't matter—research work is recognized by intent to learn/discover.

**tech-debt-investigator** - Debt analysis
- Technical debt identification across any codebase location
- Prioritization and remediation planning
- Duplicate functionality detection
- Hotspot analysis

**Recognition**: Focus on identifying problems, debt, duplication, not on creating or fixing

**git-github** - Git operations
- File grouping for commits
- Git operations execution
- CI monitoring
- Conventional commits

**Recognition**: Explicit git/GitHub operations regardless of files involved

**sast-scanner** - Security scanning
- Static security analysis across codebase
- Vulnerability detection
- OWASP compliance checking

**Recognition**: Security scanning, vulnerability detection focus

**intent-analyzer** - Request decomposition
- Breaking down complex multi-intent requests
- Task graph generation with dependencies
- OODA OBSERVE phase coordination

**Recognition**: Multi-step requests, complex task coordination, dependency analysis

**context-readiness-assessor** - Context quality gating
- Assessing context sufficiency before implementation
- Coordinating research agents to fill gaps
- Quality gate enforcement (0.0-1.0 scoring)
- OODA ORIENT phase gating

**Recognition**: Complex features, unfamiliar domains, quality gates before implementation

**hypothesis-former** - Solution hypothesis generation
- Generating 2-5 ranked solution approaches
- DCS scoring and feasibility analysis
- Trade-off matrices for decision-making
- OODA DECIDE phase component

**Recognition**: Multiple solution paths, architectural decisions, approach selection

**contingency-planner** - Failure mode planning
- Identifying 3-5 failure modes per approach
- Risk scoring (probability × impact)
- Fallback strategy generation
- OODA DECIDE phase resilience

**Recognition**: High-risk features, production deployments, resilience planning

**context-optimizer** - Context management
- Token budget optimization
- Context pruning and compression
- Progressive disclosure strategies

**Recognition**: Large context windows, token optimization needs

---

## Domain-First Thinking in Practice

**Step 1**: Look at file paths mentioned in the task
**Step 2**: Identify which domain(s) these paths belong to
**Step 3**: If single domain and that domain has clear specialist (`.claude/agents/**`, `.claude/**`, specific docs patterns), you likely have your answer
**Step 4**: If main codebase domain, proceed to work type recognition (Framework 2)
**Step 5**: If cross-domain work, recognize nature of work (research, debt analysis, git operations)

**Key Insight**: Domain provides the strongest signal for agent selection. Start there, always.
