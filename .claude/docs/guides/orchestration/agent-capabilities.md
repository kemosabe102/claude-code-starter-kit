# Agent Capabilities Reference

**Purpose**: Comprehensive agent capability matrix and maturity tracking for orchestrator delegation decisions.

**Last Updated**: 2025-10-26

---

## Agent Legend & Current Capabilities

**Overall Workflow Maturity**: Alpha (1.67) - Production Testing Ready with Test Architecture Enhancement

### Critical Agents (Primary Workflow - 80% Weight)

**spec-enhancer** (v1.0, B+)
- Capabilities: Specification creation, planning metadata generation, research
- Strengths: Context7 research, spec creation with embedded planning data, roadmap development
- Limits: Large-scale implementation coordination

**technical-pm** (v1.2, A)
- Capabilities: Business alignment review and structured reporting
- Strengths: Business context review, NFR assessment, requirements traceability analysis, structured report generation
- Performance: OPTIMIZED - 7 tools (Read+Grep+Research only), zero file mutations

**architecture-review** (v1.3, B+)
- Capabilities: Technical architecture analysis and structured reporting
- Strengths: Technical analysis, production readiness assessment, Technical Review Reports + Edit Plans
- Performance: OPTIMIZED - 6 tools (Read+Grep+Research only), zero file mutations

**code-implementer** (v0.8, C+)
- Capabilities: Code implementation, technical execution
- Strengths: Feature development, API integration
- Limits: Complex architectural decisions

**test-runner** (v0.9, B-)
- Capabilities: Test creation, validation, quality assurance
- Strengths: Unit testing, validation frameworks
- Limits: Integration test complexity

**code-reviewer** (v1.1, B+)
- Capabilities: Quality gates, security validation, standards compliance
- Strengths: Code standards, security review
- Limits: Performance optimization

### Support Agents (Secondary Impact - 20% Weight)

**architecture-enhancer** (v1.0, B+)
- Capabilities: Technical architecture enhancement, Context7 research, placeholder replacement
- Strengths: Technical content population, research-backed decisions, file modification
- Limits: Large-scale integration analysis

**spec-reviewer** (v1.0, B+)
- Capabilities: Specification quality assessment, peer validation review
- Strengths: Quality scoring, ambiguity detection, improvement recommendations
- Limits: Complex multi-spec validation, cross-specification consistency

**debugger** (v0.7, C)
- Capabilities: Problem diagnosis, troubleshooting
- Strengths: Error analysis, systematic debugging
- Limits: Complex integration issues

**test-creator** (v1.0, A-)
- Capabilities: Test generation, coverage analysis, AAA pattern enforcement
- Strengths: Unit test creation, pytest fixtures, Context7 research for testing patterns
- Limits: Test execution (use test-executor), application bug fixing (use debugger)

**test-executor** (v1.0, B+)
- Capabilities: Test execution, failure categorization, delegation routing
- Strengths: Multi-framework test running (pytest/jest/go test), 12-heuristic failure classification, delegation to debugger/test-creator/code-reviewer
- Limits: Test creation (use test-creator), application bug fixing (use debugger)

**refactorer** (v0.6, C-)
- Capabilities: Code organization, cleanup, optimization
- Strengths: Structure improvement, cleanup
- Limits: Large-scale architectural changes

**agent-architect** (v1.0, B)
- Capabilities: Agent lifecycle management, evaluation
- Strengths: Agent creation, quality assessment
- Limits: Complex workflow coordination

**context-optimizer** (v1.0, B)
- Capabilities: Context analysis, optimization planning
- Strengths: Targeted/group/ecosystem token analysis, redundancy detection, flexible scope optimization
- Limits: Analysis only, no modifications

**k8s-deployment** (v1.0, B+)
- Capabilities: Kubernetes deployment orchestration, pod troubleshooting, manifest management
- Strengths: Script-driven Kustomize workflows, event-driven troubleshooting, rollback strategies
- Limits: Multi-cluster environments, cloud provider integrations

---

## Workflow Maturity Calculation

```
Critical Agent Average: (1.0 + 1.2 + 1.3 + 0.8 + 0.9 + 1.1) / 6 = 1.05
Support Agent Average: (1.0 + 1.0 + 0.7 + 1.0 + 1.0 + 0.6 + 1.0 + 1.0 + 1.0) / 9 = 0.92
Overall Maturity = (1.05 + 0.92) × 0.85 = 1.97 × 0.85 = 1.67 (Alpha)
```

**Maturity Stages**:
- **MVP (0-1.5)**: Development environment testing ready, manual oversight required
- **Alpha (1.5-2.5)**: Production testing ready, monitoring required
- **Beta (2.5-3.5)**: Production candidate, standard development workflow
- **GA (3.5+)**: Production ready, critical business workflows

---

## Agent Capability Matrix

### Research & Analysis Capabilities
- **Primary**: researcher-lead (complex multi-source research coordination), spec-enhancer (Context7 integration, strategic analysis), technical-pm (business alignment review, structured reporting)
- **Secondary**: researcher-codebase (code analysis), researcher-web (web/doc research), researcher-library (library/API documentation), architecture-review (technical research), debugger (problem analysis), agent-architect (prompt research)
- **Delegation Strategy**: Simple queries handled directly; complex multi-source research delegated to researcher-lead for coordinated worker execution

### Strategic Planning Capabilities
- **Primary**: plan-enhancer (business context enhancement, requirements mapping) - FAST STARTUP
- **Secondary**: spec-enhancer (technical planning), technical-pm (business alignment review), architecture-review (technical strategy)

### Business Analysis Capabilities
- **Primary**: plan-enhancer (business goals, user value, requirements traceability) - PERFORMANCE OPTIMIZED
- **Secondary**: technical-pm (business alignment review, NFR assessment), spec-enhancer (strategic context)

### Implementation Capabilities
- **Primary**: code-implementer (feature development, API integration)
- **Secondary**: refactorer (code structure), debugger (issue resolution)

### Architecture & Technical Design Capabilities
- **Primary**: architecture-enhancer (technical content population, single-file focused), architecture-review (technical validation, integration analysis, production readiness)
- **Secondary**: spec-enhancer (architectural planning), technical-pm (NFR framework assessment)

### Validation & Testing Capabilities
- **Primary**: test-runner (automated testing, validation)
- **Secondary**: code-reviewer (manual review), debugger (failure analysis)

### Quality & Standards Capabilities
- **Primary**: code-reviewer (security, compliance, standards)
- **Secondary**: refactorer (code quality), agent-architect (agent standards)

### Architectural & Strategic Capabilities
- **Primary**: spec-enhancer (specification design, strategic planning)
- **Secondary**: agent-architect (agent architecture), code-reviewer (architectural review)

### Deployment & Operations Capabilities
- **Primary**: k8s-deployment (Kubernetes orchestration, pod troubleshooting, manifest management)
- **Secondary**: code-implementer (manifest modifications), debugger (application-level diagnosis), git-github (configuration PRs)

---

## Sub-Agent Coordination Patterns

**Sub-Agents as Specialized Tools**:
- **Planner**: Strong at research, architecture, strategic thinking
- **Technical-PM**: Strong at business alignment review, NFR assessment, requirements traceability analysis, structured reporting
- **Architecture-Review**: Strong at technical validation, integration analysis, production readiness, quality gates
- **code-implementer**: Strong at code implementation, technical execution
- **Test-Runner**: Strong at validation, quality assurance, automation
- **Code-Reviewer**: Strong at quality gates, security, standards compliance
- **Debugger**: Strong at problem diagnosis, troubleshooting
- **Refactorer**: Strong at code organization, refactoring, cleanup
- **Agent-Architect**: Strong at agent lifecycle, prompt engineering
- **Researcher-Lead**: Strong at research orchestration, multi-source coordination, complex information synthesis
- **Researcher-Codebase**: Strong at code analysis, pattern discovery, architecture investigation
- **Researcher-Web**: Strong at web/documentation research, best practices discovery, source quality assessment
- **Researcher-Library**: Strong at Context7-based library documentation research, official API references, version-specific patterns, framework docs (15:1 compression ratio, <15s performance, Alpha maturity - Production Ready)
- **k8s-deployment**: Strong at Kubernetes deployment orchestration, pod troubleshooting, manifest management, script-driven Kustomize workflows, event-driven troubleshooting, rollback strategies

**Coordination Rules**:
- Only orchestrator can delegate to sub-agents
- Sub-agents cannot call other sub-agents directly
- All sub-agent communication flows through orchestrator
- Orchestrator maintains context and state across sub-agent interactions
- Orchestrator can launch multiple sub-agents in parallel when no file conflicts exist
- Parallel execution recommended for independent file processing (plan enhancement, task generation)
