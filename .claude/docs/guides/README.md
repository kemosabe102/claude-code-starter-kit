# Knowledge Base Guide Index

**Last Updated**: 2025-09-26
**Integration Status**: Framework Complete - All Critical Agents Enhanced
**Guide Count**: 22 Active Guides

## Quick Start

### For Agents
- **Planning Frameworks**: Use 4 core frameworks for all planning activities
- **Validation Algorithms**: Apply concrete scoring for objective quality assessment
- **Architecture Standards**: Follow established patterns for technical review
- **Business Framework**: Integrate cost and risk analysis in all specifications

### For Users
- **Browse by Category**: Find guides organized by functional area
- **Integration Status**: See which agents use which frameworks
- **Usage Examples**: Review practical implementation patterns
- **Quality Metrics**: Understand objective assessment criteria

## Core Planning Frameworks [ACTIVE INTEGRATION]

### Cost Analysis Framework
**File**: `.claude/docs/guides/planning/cost-analysis-framework.md`
**Purpose**: $100/month budget constraint framework with systematic cost analysis
**Integration**: spec-enhancer, technical-pm, architecture-review
**Key Features**:
- Tier 1-4 cost decision framework (Free → $80+ enterprise)
- Standard cost assessment table template
- Budget compliance validation checklist
- P×I×E cost risk scoring integration
- Free tier maximization strategies

**When to Use**: All feature specifications requiring external services, infrastructure, or paid tools

### Risk Assessment Matrix
**File**: `.claude/docs/guides/planning/risk-assessment-matrix.md`
**Purpose**: P×I×E scoring framework (Probability × Impact × Exposure) for systematic risk evaluation
**Integration**: spec-enhancer, architecture-review, technical-pm
**Key Features**:
- Risk Score = P × I × E (1-125 scale)
- Risk categories: Technical, Resource, Business, Operational
- Standard risk assessment table template
- Risk mitigation strategies by score level
- Risk lifecycle management process

**When to Use**: Every specification and technical plan for comprehensive risk assessment

### Development Sequencing Guide
**File**: `.claude/docs/guides/planning/development-sequencing-guide.md`
**Purpose**: Parallel vs sequential component development decision matrix
**Integration**: spec-enhancer, architecture-review
**Key Features**:
- Dependency analysis framework
- Interface contract analysis methods
- Decision tree for parallel vs sequential development
- Integration readiness checklists
- Common anti-patterns to avoid

**When to Use**: Multi-component features requiring coordination and integration planning

### Quality Scoring Algorithms
**File**: `.claude/docs/guides/validation/quality-scoring-algorithms.md`
**Purpose**: Mathematical formulas for objective quality assessment
**Integration**: spec-enhancer, architecture-review, technical-pm
**Key Features**:
- Pain Point Alignment Score (≥0.4 target)
- MVP Complexity Score (≤0.3 target)
- Requirements Completeness Score (≥0.7 target)
- Quality gate algorithms (SPEC, PLAN, Sprint readiness)
- Continuous quality metrics and trend analysis

**When to Use**: All specifications and plans for objective quality validation

## Architecture Review Guides [SPECIALIZED INTEGRATION]

### Architecture Review Framework
**Primary Files**:
- `.claude/docs/guides/architecture-review-scoring-rubric.md` - 5-point scoring system
- `.claude/docs/guides/architecture-review-success-criteria.md` - Production readiness criteria
- `.claude/docs/guides/architecture-review-stage-policies.md` - MVP/Alpha/Beta/GA policies
- `.claude/docs/guides/architecture-review-traceability-guide.md` - Requirements traceability
- `.claude/docs/guides/architecture-review-slo-sli-framework.md` - Performance framework
- `.claude/docs/guides/architecture-review-integration-guide.md` - Integration patterns
- `.claude/docs/guides/architecture-review-integration-enhancement.md` - Enhancement protocols

**Integration**: architecture-review agent (primary), technical-pm (validation)
**Purpose**: Comprehensive technical architecture review with structured scoring
**Key Features**:
- 5-point rubric scoring across multiple dimensions
- Stage-specific policies for maturity levels
- SLO/SLI framework for performance requirements
- Integration coherence validation
- Technical debt assessment

### Technical PM Business Framework
**Primary Files**:
- `.claude/docs/guides/technical-pm-usage-guide.md` - Agent usage patterns
- `.claude/docs/guides/technical-pm-research-guides.md` - Research methodologies
- `.claude/docs/guides/technical-pm-procedures.md` - Review procedures

**Integration**: technical-pm agent (primary), spec-enhancer (business context)
**Purpose**: Business alignment review and structured reporting
**Key Features**:
- Business Review Report + Business Edit Plan generation
- Cost framework integration with business justification
- Risk assessment validation from business perspective
- NFR framework assessment and validation

## Development Process Guides [WORKFLOW INTEGRATION]

### Agent Coordination Guides
- **Strategic Planning Relationships** (`.claude/docs/guides/strategic-planning-relationships.md`)
- **Agent Design Best Practices** (`.claude/docs/guides/agent-design-best-practices.md`)
- **code-implementer Assist I/O** (`.claude/docs/guides/code-implementer-assist-io.md`)

**Integration**: All agents reference for coordination patterns
**Purpose**: Agent interaction patterns, handoff protocols, and best practices

### Documentation & Validation Guides
- **Feature Artifact Structure** (`.claude/docs/guides/feature-artifact-structure.md`)
- **Validation Rubrics** (`.claude/docs/guides/validation-rubrics.md`)
- **Doc Update Strategy** (`.claude/docs/guides/doc-update-strategy.md`)
- **MCP Agent Optimization** (`.claude/docs/mcp-agent-optimization.md`)

**Integration**: All agents for consistent output structure and quality validation

### Orchestrator Workflow Guides
- **Orchestrator Timestamp Management** (`.claude/docs/guides/orchestrator-timestamp-management.md`)
- **Timestamp System Implementation Plan** (`.claude/docs/guides/timestamp-system-implementation-plan.md`)

**Integration**: Main orchestrator for workflow coordination and state management

## Agent Integration Status

### spec-enhancer (Primary Framework Integration)
**Integration Level**: ⭐⭐⭐⭐⭐ Complete
**Active Frameworks**: All 4 core frameworks
**Capabilities Enhanced**:
- Automatic cost analysis table generation
- P×I×E risk scoring for all specifications
- Development sequencing recommendations
- Quality scoring with mathematical validation
- Planning Recommendations with embedded framework results

**Usage Pattern**: Framework consultation required for all specifications

### architecture-review (Technical Framework Integration)
**Integration Level**: ⭐⭐⭐⭐⭐ Complete
**Active Frameworks**: All validation frameworks + specialized architecture guides
**Capabilities Enhanced**:
- Framework compliance validation in Technical Review Reports
- Cost and risk assessment verification
- Quality gate validation with concrete thresholds
- Technical Edit Plan generation with framework integration

**Usage Pattern**: Validates framework application in all technical plans

### technical-pm (Business Framework Integration)
**Integration Level**: ⭐⭐⭐⭐ Strong
**Active Frameworks**: Cost analysis, risk assessment, quality scoring
**Capabilities Enhanced**:
- Business alignment validation with cost/risk integration
- Business Review Reports with framework compliance
- Cross-framework validation and consistency checking
- Business Edit Plan generation

**Usage Pattern**: Business context review with framework validation

### plan-enhancer (Limited Framework Integration)
**Integration Level**: ⭐⭐⭐ Moderate
**Active Frameworks**: Framework-aware business context enhancement
**Capabilities Enhanced**:
- Framework-aware business context population
- Cost consideration in business goal alignment
- Risk awareness in requirement development

**Usage Pattern**: Framework consideration during business enhancement

## Usage Examples

### Complete Framework Integration Workflow

**Specification Creation**:
```markdown
## Cost Analysis & Budget Compliance
| Category | Service/Component | Monthly Cost | Justification | Alternatives |
|----------|-------------------|--------------|---------------|--------------|
| Infrastructure | Cloud hosting | $25 | Core application hosting | Free tier options |
| Database | Managed DB | $15 | Data persistence needs | Self-hosted alternative |
**Total Monthly Cost:** $40 / $100 budget ✅

## Risk Assessment Matrix
| Risk ID | Risk Description | P | I | E | Score | Priority | Mitigation Strategy |
|---------|-----------------|---|---|---|-------|----------|-------------------|
| TECH-001 | New framework adoption | 3 | 3 | 3 | 27 | Medium | Training + prototype |

## Quality Self-Assessment
- **Pain Point Alignment:** 0.65 (Target: ≥0.4) ✅ PASS
- **MVP Complexity:** 0.28 (Target: ≤0.3) ✅ PASS
```

**Architecture Review Validation**:
```json
{
  "framework_compliance": {
    "cost_analysis_present": true,
    "risk_assessment_complete": true,
    "quality_scoring_valid": true,
    "development_sequencing_appropriate": true
  },
  "validation_results": {
    "budget_within_limit": true,
    "risk_scores_acceptable": true,
    "quality_gates_passed": true
  }
}
```

### Framework Decision Points

**When Cost Analysis Required**:
- Any external service or infrastructure cost
- Technology selection decisions
- Scaling architecture considerations
- Third-party API integrations

**When Risk Assessment Required**:
- All specifications (mandatory)
- Technical architecture decisions
- Integration complexity evaluation
- Resource and timeline planning

**When Development Sequencing Required**:
- Multi-component features
- Complex integration scenarios
- Parallel development opportunities
- Dependency management needs

**When Quality Scoring Required**:
- All specifications and plans (mandatory)
- Quality gate validation
- Progress measurement
- Stakeholder confidence building

## Success Metrics

### Framework Adoption Metrics
- **100% Integration**: All critical agents enhanced with core frameworks
- **Consistent Application**: Standard tables and scoring across all specifications
- **Quality Improvement**: Objective vs subjective assessment replacement
- **Cost Control**: $100/month budget constraint enforcement

### Quality Improvement Indicators
- **Objective Assessment**: Mathematical scoring replaces subjective evaluation
- **Consistent Standards**: All agents apply same quality criteria
- **Predictable Outcomes**: Framework compliance leads to implementation success
- **Risk Mitigation**: P×I×E scoring enables proactive risk management

### Development Efficiency Gains
- **Reduced Rework**: Framework compliance prevents common issues
- **Faster Reviews**: Objective criteria speed up validation
- **Better Planning**: Risk and cost analysis improve decision quality
- **Clearer Handoffs**: Structured reports enable clean agent coordination

## Maintenance Guidelines

### Adding New Guides
1. **Create Guide**: Follow established template patterns
2. **Define Integration**: Specify which agents should use the guide
3. **Update Agents**: Enhance agent frontmatter with guide consultation requirements
4. **Test Framework**: Validate guide usage in real workflows
5. **Update Index**: Add guide to this index with integration status

### Framework Evolution
1. **Monitor Usage**: Track framework effectiveness in real implementations
2. **Gather Feedback**: Collect agent performance and user experience data
3. **Iterate Algorithms**: Refine scoring formulas based on outcome correlation
4. **Version Control**: Maintain backward compatibility during framework updates
5. **Document Changes**: Update integration guides when frameworks evolve

### Agent Enhancement Process
1. **Identify Opportunity**: Find agents that could benefit from framework integration
2. **Design Integration**: Plan how agent will consume and apply frameworks
3. **Update Agent Definition**: Add framework consultation to agent frontmatter
4. **Test Integration**: Validate framework usage in agent operations
5. **Monitor Performance**: Track agent startup time and output quality

---

**This knowledge base provides systematic, framework-driven development with objective quality assessment and consistent application across all agent operations.**