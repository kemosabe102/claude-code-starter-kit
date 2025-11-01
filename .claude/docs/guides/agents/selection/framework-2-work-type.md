# Framework 2: Work Type Recognition

**Core Principle**: Within same domain (especially main codebase), different work types require different specialists. Recognize work type by understanding task intent.

## Primary Work Types

### Creation Work - Bringing Something New Into Existence

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
- Domain: Main codebase (`packages/**`)
- Agent: code-implementer

---

### Investigation Work - Understanding What Exists or Why It Fails

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
- Domain: Main codebase (`tests/**`)
- Agent: debugger

---

### Improvement Work - Enhancing What Already Exists

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
- Domain: Main codebase (`packages/**`)

---

### Read-Only Analysis Mode

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

## Distinguishing Ambiguous Work Types

### The "Fix" Ambiguity

The word "fix" can mean different work types depending on context:

**"Fix failing tests" when root cause is unknown**:
- Investigation work (need to discover why)
- Agent: debugger

**"Fix failing tests" when root cause is known**:
- Implementation work (apply known solution)
- Agent: code-implementer

**"Fix code structure"**:
- Improvement work (restructuring)

**Decision Approach**: What kind of "fixing" is needed? Discovery-based, implementation-based, or improvement-based?

---

### The "Create Tests" vs "Run Tests" vs "Fix Failing Tests"

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

**Decision Approach**: Is work about test creation (test-creator), test execution (test-executor), discovering problems (debugger), or fixing implementation (code-implementer)?
