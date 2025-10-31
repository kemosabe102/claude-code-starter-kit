# Task Template: Individual Work Items

**Based on:** GitHub Spec-Kit Task Template ([source](https://github.com/github/spec-kit/blob/main/templates/tasks-template.md))  
**Integrated with:** Claude Code Starter Kit workflow patterns and Context7 validation

---

## 📋 **Task Format Structure**

### **Task ID Format:**
```
[ID] [P?] Description in path/to/file.ext

Examples:
- [ ] T001 Create PiotroskiItem tests in tests/test_piotroski.py
- [ ] T002 [P] Update Report model in domain/models/report.py
- [ ] T003 [P] Add template in templates/reports/piotroski_breakdown.md.jinja
- [ ] T004 Integrate PiotroskiWorker in workers/piotroski_worker.py
```

**Note**: Task lines should include status checkboxes (`- [ ]`) for orchestrator tracking during implementation.

### **Task Components:**
- **ID:** Sequential identifier (T001, T002, T003, etc.)
- **[P]:** Optional parallel flag (can execute simultaneously with other [P] tasks)
- **Description:** Clear, specific action with exact file path
- **File Path:** Precise location where work will be performed
- **Sub-Agent Assignment:** Specific specialized agent for this task type
- **Preflight Documentation:** Relevant ADRs, feature plans, and context documents to review before implementation

### **Review Groups:**
Tasks are organized into review groups representing coherent, testable units:

**Review Group Format:**
```markdown
## Review Group: [Component Name] [ ]

- [ ] T001 [test-runner] Create [Component] tests in tests/test_[component].py
- [ ] T002 [code-implementer] Implement [Component] in src/[component].py
- [ ] T003 [code-implementer] Integrate [Component] with [System] in src/[integration].py
- [ ] T004 [code-reviewer] Review [Component] implementation (T001-T003)
      Scope: [component].py, [integration].py, test_[component].py
      Focus: security, patterns, error-handling
      Blocks: T005+ (next review group)
      Retry: If fails, code-implementer fixes, re-review (max 3x)
      Success: All checks pass, test coverage >= 80%
```

**Status Markers** (updated by orchestrator during `/implement`):
- `[ ]` Not started (pending)
- `[▶]` In progress (current task/group)
- `[✓]` Completed successfully
- `[⊗]` Blocked (critical issues)

**Review Group Boundaries** (when to insert review checkpoint):
- ✅ After completing a class and its tests (5-8 tasks)
- ✅ After completing an API endpoint and validation (5-8 tasks)
- ✅ After completing a data model and transformations (5-8 tasks)
- ✅ After completing cross-component integration (5-8 tasks)
- ✅ Before starting work on dependent components

**Review Group Anti-Patterns** (when NOT to insert review):
- ❌ After every single task (too granular, breaks flow)
- ❌ Only at the very end (too late to catch issues)
- ❌ At arbitrary task count intervals (ignores logical boundaries)
- ❌ In the middle of implementing a single class (incomplete unit)

---

## 📊 **Phase & Progress Tracking**

### **Phase Header Format:**
```markdown
## Phase 1: Setup & Configuration [ ]
## Phase 2: Core Implementation [ ]
## Phase 3: Integration & Testing [ ]
```

**Phase Status Markers** (updated by orchestrator):
- `[ ]` Not started
- `[▶ in-progress]` Currently executing
- `[✓ completed]` All tasks complete
- `[⊗ blocked]` Critical blockers prevent progress

**Orchestrator Responsibilities**:
1. **At phase start**: Update `[ ]` to `[▶ in-progress]`
2. **At phase completion**: Update `[▶ in-progress]` to `[✓ completed]`
3. **If blocked**: Update to `[⊗ blocked]` with reason

### **Task Status Tracking:**

All individual tasks should be formatted as checkboxlist items for orchestrator tracking:

```markdown
- [ ] T001 [agent] Description
- [ ] T002 [agent] Description
```

**Orchestrator updates during `/implement`**:
- `[▶]` marks current task (only ONE task at a time)
- `[✓]` marks completed tasks
- `[⊗]` marks blocked tasks with reason

**Purpose**: Provides real-time visibility, enables resume capability, creates audit trail.

---

## 🔄 **Task Generation Workflow**

### **Step 1: Derive Tasks from Feature Plan**
**Source Documents:**
- Feature plan technical architecture section
- Constitution Check requirements
- Test-first acceptance criteria
- Implementation phases

**Task Generation Order:**
1. **Setup Tasks** - Configuration, dependencies, infrastructure
2. **Test Tasks** - Unit tests, integration tests, validation tests
3. **Model Tasks** - Pydantic models, domain objects, data structures
4. **Worker Tasks** - Code-first business logic functions
5. **Integration Tasks** - Orchestration, workflow connections
6. **Code Review Tasks** - Structured code review and feedback resolution
7. **Polish Tasks** - Documentation, error handling, optimization

### **Step 2: Apply Context7 Validation**
**Before creating tasks:**
- Research implementation patterns via Context7 for relevant libraries
- Validate architectural compliance with Constitution Check
- Ensure test-first approach aligns with researched testing frameworks
- Document Context7 sources in task descriptions when applicable

### **Step 3: Identify Parallel Opportunities**
**Parallel Task Criteria:**
- ✅ **Different files** - No file overlap between parallel tasks
- ✅ **No direct dependencies** - Can execute independently  
- ✅ **Independent components** - No shared state or integration points
- ✅ **Clear boundaries** - Distinct functional areas

**Parallel Task Examples:**
```
T005 [P] Create QuantWorker tests in tests/test_quant_worker.py
T006 [P] Create ReportStyler tests in tests/test_report_styler.py
T007 [P] Add Jinja2 template in templates/reports/financial_ratios.md.jinja
```

---

## 🤖 **Sub-Agent Task Assignment Guide**

### **Specialized Agent Assignment by Task Type**

**Test Creation Tasks** → **`test-runner-agent`**
- Unit test implementation (`test_*.py` files)
- Integration test setup and validation
- Test fixture creation and mock setup
- Coverage validation and test optimization

**Implementation Tasks** → **`code-implementer-agent`**  
- Core business logic implementation
- Pydantic model creation and validation
- Worker class and connector development
- API endpoint and service implementation

**Debugging Tasks** → **`debugger`**
- Test failure investigation and resolution
- Performance issue diagnosis
- Error handling implementation
- System integration troubleshooting

**Code Review Tasks** → **`code-reviewer`** (Self-Correcting with Retry Logic)
- **Review Group Checkpoints** - After completing coherent units (class+tests+integration)
- **Review Scope Definition** - Explicit task range and file list being reviewed
- **Blocking Behavior** - Subsequent tasks cannot proceed until review passes
- **Focus Areas** - Security, patterns, performance, architecture alignment
- **Automatic Iteration** - If review fails, apply fixes and retry (max 3 attempts)

**Self-Correcting Review Task Format:**
```
T050 [code-reviewer] Review DataConnector implementation (T045-T049)
     Scope: connector.py, protocol.py, tests/test_connector.py
     Focus: security, error-handling, protocol-compliance
     Blocks: T051-T099 (integration tasks depend on validated connector)
     Retry: If fails → code-implementer/debugger fixes → re-review (max 3x)
     Success: All checks pass, no critical issues, coverage >= 80%
     Escalate: After 3 failed attempts, create human intervention task
     Preflight: ADR-005 (connector patterns), ADR-008 (security)
```

**Automatic Iteration Workflow:**
```markdown
ITERATION 1:
  [code-reviewer] → Identifies issues (e.g., "Missing input validation")
  ↓
  IF issues found:
    [code-implementer] → Applies fixes to identified issues
    ↓
    [code-reviewer] → Re-reviews same scope

ITERATION 2 (if still failing):
  [code-reviewer] → Identifies remaining issues (e.g., "Test coverage 65%")
  ↓
  [debugger] → Applies more complex fixes / adds missing tests
  ↓
  [code-reviewer] → Re-reviews same scope

ITERATION 3 (if still failing):
  [code-reviewer] → Final review attempt
  ↓
  IF still failing:
    ESCALATE → Create T050-MANUAL task for human review
    BLOCK → All dependent tasks (T051+) cannot proceed
  ELSE:
    SUCCESS → Unblock dependent tasks
```

**Review Failure Types and Fix Agents:**

| Issue Type | Fix Agent | Example |
|------------|-----------|---------|
| Pattern violations | code-implementer | "Use factory pattern per ADR-005" |
| Security issues | code-implementer | "Add input validation for user data" |
| Test failures | debugger | "Fix failing integration tests" |
| Missing test coverage | debugger | "Add tests for error handling paths" |
| Performance issues | refactorer | "Optimize N+1 query in connector" |
| Architecture violations | code-implementer | "Refactor to match service layer pattern" |

**Refactoring Tasks** → **`refactorer`**
- Code structure improvement and modularization
- Design pattern implementation
- Legacy code modernization
- Performance optimization refactoring

### **Task Format with Sub-Agent Assignment:**
```
T001 [code-implementer-agent] Create DataConnector Protocol interface in packages/core/connectors/protocol.py
T002 [test-runner-agent] Create DataConnector Protocol tests in tests/core/connectors/test_protocol.py  
T003 [debugger] Debug integration test failures in test_company_profile_integration.py
T004 [code-reviewer] Review CompanyProfileConnector implementation for security and best practices
T005 [refactorer] Refactor BaseConnector to improve testability and modularity
```

### **Sub-Agent Usage Rules:**
- **Main Agent Coordination**: Main agent ALWAYS coordinates with sub-agents, never sub-agent-to-sub-agent
- **Explicit Assignment**: Each task MUST specify which sub-agent to use with clear instruction format
- **Single Task Focus**: Each sub-agent handles ONE task completely before returning to main agent
- **Result Integration**: Main agent receives sub-agent results and coordinates next steps

### **Sub-Agent Instruction Format:**
When executing a task, the main agent MUST use this exact format:

```
For Task T001 [test-runner-agent]:
"Use the test-runner-agent to create unit tests for the DataConnector Protocol interface in tests/core/connectors/test_protocol.py. The agent should implement comprehensive test coverage including protocol compliance validation and error handling scenarios."

For Task T002 [code-implementer-agent]:
"Use the code-implementer-agent to create the CompanyProfileConnector class in packages/core/connectors/company_profile.py. The agent should follow ADR-005 specifications and implement all internal transformers with proper error handling."

For Task T003 [code-reviewer]:
"Use the code-reviewer to review the CompanyProfileConnector implementation for security vulnerabilities, best practices compliance, and architectural alignment with ADR-004 and ADR-005."
```

**Critical**: Always specify the exact sub-agent name and provide complete task context in the instruction.

---

## 📚 **Preflight Documentation Requirements**

### **Mandatory Documentation Review (Include in Each Task)**
When creating tasks from this template, specify which documents the code-implementer should review:

**Task-Specific Documentation:**
- **Relevant ADR(s):** `docs/02-architecture/decisions/adr-XXX-[topic].md`
- **Feature Plan:** `docs/01-planning/features/[feature-name].md` (if applicable)
- **Living Sprint Context:** Relevant sections of `docs/00-project/operations/LIVING_SPRINT.md`

**Architectural Context (search by component type):**
- **Workers:** Look for ADRs related to data processing, pipeline patterns, worker architecture
- **Report Generation:** Look for ADRs related to output formatting, template systems, report styling
- **Data Integration:** Look for ADRs related to connectors, data sources, API integration
- **LLM Integration:** Look for ADRs related to agent patterns, model usage, AI orchestration
- **Infrastructure:** Look for ADRs related to deployment, environment setup, observability

**Research Requirements:**
- **Context7 Queries:** Specific library documentation topics to research
- **WebSearch Topics:** Broader implementation concepts requiring current best practices (use 2025-2026 timeframe)

### **Preflight Documentation Template**
```markdown
**Preflight Documentation for Task [ID]:**
- **ADRs to Review:** adr-XXX-[topic].md, adr-YYY-[topic].md
- **Feature Context:** feature-plans/[feature-name].md (sections X, Y)
- **Context7 Research:** library/framework patterns for [specific-topic]
- **WebSearch Research:** [broader-concept] best practices 2025
- **Existing Implementation Search:** Keywords to grep: [keyword1, keyword2, keyword3]
```

## 🧪 **Task Validation Checklist**

### **Before Task Creation:**
- [ ] **Contract Validated** - Requirements from feature plan are clear and testable
- [ ] **Test-First Sequencing** - Test tasks precede implementation tasks
- [ ] **Preflight Documentation Specified** - All relevant ADRs, feature plans, and research topics identified
- [ ] **Context7 Research Topics Listed** - Specific library/framework documentation needs identified
- [ ] **WebSearch Topics Listed** - Broader concepts requiring 2025-2026 best practices research
- [ ] **Existing Implementation Keywords** - Search terms for finding related functionality specified
- [ ] **Constitution Check** - Architectural compliance validated
- [ ] **File Paths Specific** - Exact file locations specified

### **Parallel Task Validation:**
- [ ] **No File Overlap** - Each parallel task works on different files
- [ ] **True Independence** - Tasks can execute without coordination
- [ ] **Clear Dependencies** - Non-parallel tasks properly sequenced
- [ ] **Resource Isolation** - No shared external resources or state

### **Task Quality Standards:**
- [ ] **Specific Action** - Clear, single-purpose work item
- [ ] **Measurable Completion** - Obvious when task is finished
- [ ] **Implementation Ready** - All prerequisites and dependencies identified
- [ ] **Context7 Compliant** - Follows researched library patterns

---

## 📊 **Integration with Existing Workflow**

### **Feature Plan → Task Breakdown Process:**
1. **Extract from Implementation Plan section** - Convert phases into sequential tasks
2. **Apply Constitution Check requirements** - Ensure architectural compliance in tasks
3. **Reference Context7 research** - Include researched patterns in task descriptions
4. **Follow test-first approach** - Create test tasks before implementation tasks
5. **Identify parallel work streams** - Mark independent tasks with [P] flag

### **Task → LIVING_SPRINT.md Integration:**
```markdown
### **Current Sprint Tasks**
- [x] T001 Create PiotroskiItem tests in tests/test_piotroski.py
- [ ] T002 [P] Update Report model in domain/models/report.py
- [ ] T003 [P] Add template in templates/reports/piotroski_breakdown.md.jinja
- [ ] T004 Integrate PiotroskiWorker in workers/piotroski_worker.py

### **Next Sprint Tasks** 
- [ ] T005 [P] Create QuantWorker tests in tests/test_quant_worker.py
- [ ] T006 [P] Create ReportStyler tests in tests/test_report_styler.py
```

### **Code Review Integration:**
**Task completion triggers:**
1. **Implementation** - Complete the specific file work described in task
2. **Context7 Compliance** - Verify implementation follows researched patterns
3. **Code Review Preparation** - Run `uv run python scripts/prepare-code-review.py --stage-changes`
4. **Task Validation** - Confirm task acceptance criteria met
5. **LIVING_SPRINT.md Update** - Mark task complete and advance to next task

---

## 🚀 **Example: Feature Plan → Task Breakdown**

### **Source Feature Plan Section:**
```markdown
## 🚧 Implementation Plan

### Phase 1: Domain Model Enhancement (1 Sprint Point)
1. Update Report model to include piotroski_details field
2. Create Golden Set test for AAPL validation

### Phase 2: Worker Implementation (2 Sprint Points)  
1. Create PiotroskiWorker following ADR-009 pattern
2. Integrate existing PiotroskiCalculator
3. Test PiotroskiWorker with Golden Set
```

### **Generated Task List with Review Groups:**
```markdown
## Review Group 1: Domain Model Enhancement

T001 [test-runner] Create feature test in tests/test_piotroski.py
     Preflight: ADR-009 (worker patterns), feature-plans/piotroski-scoring.md
     Context7: pytest async patterns, pydantic validation
     Existing Search: Worker, PiotroskiCalculator, test patterns

T002 [P] [code-implementer] Update Report model in domain/models/report.py
     Preflight: ADR-003 (domain models), existing Report model
     Context7: pydantic field types, model validation
     Existing Search: Report, BaseModel, piotroski

T003 [P] [test-runner] Create model tests in tests/test_report_model.py
     Preflight: ADR-003, tests/domain/ patterns
     Context7: pydantic testing, field validation testing
     Existing Search: test_report, model_validation

T004 [code-reviewer] Review domain model changes (T001-T003)
     Scope: report.py, test_piotroski.py, test_report_model.py
     Focus: data-validation, model-integrity, test-coverage
     Blocks: T005+ (worker implementation depends on validated model)
     Retry: If fails → code-implementer fixes → re-review (max 3x)
     Success: Model validation correct, tests pass, coverage >= 80%
     Preflight: ADR-003 (domain models)

## Review Group 2: Worker Implementation

T005 [test-runner] Create PiotroskiWorker tests in tests/test_piotroski_worker.py
     Preflight: ADR-009 (workers), existing worker patterns
     Context7: async worker testing, mock data patterns
     Existing Search: Worker, test_worker, async def

T006 [code-implementer] Create PiotroskiWorker in workers/piotroski_worker.py
     Preflight: ADR-009, existing workers (QuantWorker, GrowthWorker)
     Context7: async/await patterns, worker base classes
     Existing Search: Worker, async def, calculator integration

T007 [code-implementer] Integrate PiotroskiCalculator in workers/piotroski_worker.py
     Preflight: packages/core/piotroski.py (existing calculator)
     Context7: component integration, dependency injection
     Existing Search: PiotroskiCalculator, from packages

T008 [test-runner] Create integration test in tests/integration/test_piotroski_flow.py
     Preflight: tests/integration/ patterns, Golden Set data
     Context7: end-to-end testing, test fixtures
     Existing Search: integration, end_to_end, golden_set

T009 [code-reviewer] Review PiotroskiWorker implementation (T005-T008)
     Scope: piotroski_worker.py, test_piotroski_worker.py, test_piotroski_flow.py
     Focus: async-patterns, calculator-integration, error-handling, test-quality
     Blocks: T010+ (template updates depend on working worker)
     Retry: If fails → debugger fixes → re-review (max 3x)
     Success: All tests pass, async patterns correct, integration validated
     Preflight: ADR-009 (worker patterns)
```

### **Task Sequencing Logic:**
- **Review Group 1** - Complete domain model changes before worker
- **T001 first** - Feature test defines acceptance criteria (test-first)
- **T002, T003 parallel** - Different files, no dependencies
- **T004 blocks T005+** - Model must be validated before worker uses it
- **Review Group 2** - Worker implementation after model validated
- **T005-T008 sequential** - Worker implementation flow with dependencies
- **T009 blocks next group** - Worker must be validated before dependent features

### **Main Agent Task Orchestration:**
- **Task T001 [test-runner-agent]**: Main agent launches test-runner-agent → receives test results → proceeds to next task
- **Task T002 [code-implementer-agent]**: Main agent launches code-implementer-agent → receives implementation → proceeds to next task  
- **Task T003 [test-runner-agent]**: Main agent launches test-runner-agent → receives validation results → proceeds to next task
- **Task T004 [code-reviewer]**: Main agent launches code-reviewer → receives review feedback → coordinates resolution
- **Task T005 [debugger]**: Main agent launches debugger (if issues found) → receives fixes → proceeds to next task

---

## 📝 **Task Template Usage**

### **Creating New Tasks:**
1. **Reference approved feature plan** - Extract from implementation phases
2. **Specify preflight documentation** - List relevant ADRs, feature plans, and context documents
3. **Define research requirements**:
   - **Context7 topics:** Specific library/framework documentation needs (e.g., "pydantic validation patterns", "pytest async testing")
   - **WebSearch topics:** Broader implementation concepts (e.g., "Python worker pattern best practices 2025", "async data processing architecture 2026")
   - **Existing search keywords:** Terms to grep for related functionality (e.g., "Worker", "Calculator", "BaseModel")
4. **Follow test-first sequencing** - Test tasks before implementation tasks
5. **Identify parallel opportunities** - Mark independent work with [P]
6. **Validate task quality** - Use validation checklist above
7. **Integrate with LIVING_SPRINT.md** - Add tasks to current/next sprint tracking

### **Research Guidance for Task Creation**

**Use Context7 for:**
- **Specific library documentation:** pydantic field definitions, pytest patterns, fastapi routing
- **Implementation patterns:** async/await best practices, error handling patterns
- **Integration guides:** library-specific integration steps and configuration
- **API usage:** method signatures, parameter options, return types

**Use WebSearch for:**
- **Broad architectural concepts:** worker pattern implementations, data pipeline design
- **Current best practices:** Python async patterns 2025, modern testing approaches 2026
- **Industry standards:** API design patterns, security best practices
- **Complex topics:** multi-service orchestration, performance optimization strategies

**Always specify timeframe:** Include 2025-2026 in WebSearch queries for current best practices

### **Task Execution:**
1. **Backup creation** - If modifying >100 lines, create backup: `cp file .backups/file.$(date +%Y%m%d_%H%M%S)`
2. **Context7 validation** - Verify patterns before implementation
3. **Implementation** - Complete work in specified file path
4. **Code review preparation** - Run `uv run python scripts/prepare-code-review.py --stage-changes` (MANDATORY before sprint update)
5. **Task completion validation** - Confirm acceptance criteria met and all code review artifacts generated
6. **Sprint progress update** - Mark complete in LIVING_SPRINT.md ONLY after code review preparation

### **Rollback Readiness:**
- [ ] Backup created if needed (>100 lines modified)
- [ ] Rollback procedure documented
- [ ] Recovery time estimated: [X minutes]
- [ ] Rollback trigger criteria defined

---

**This template integrates GitHub spec-kit task structure with Claude Code Starter Kit Context7-guided development workflow for systematic, parallel-optimized work breakdown with rollback safety.**