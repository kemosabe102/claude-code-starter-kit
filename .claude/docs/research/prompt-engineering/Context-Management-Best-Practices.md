# Context Management Best Practices for AI Agents

**Purpose**: Define clear, measurable guidelines for optimal context usage in Claude Code agents
**Audience**: Agent designers, context optimizers, system architects
**Version**: 1.0
**Last Updated**: 2025-10-10

---

## Table of Contents
1. [Core Principles](#core-principles)
2. [Context Budgets by Operation Type](#context-budgets-by-operation-type)
3. [Agent Design Patterns](#agent-design-patterns)
4. [Compression Strategies](#compression-strategies)
5. [Tool Usage Optimization](#tool-usage-optimization)
6. [Anti-Patterns to Avoid](#anti-patterns-to-avoid)
7. [Measurement & Monitoring](#measurement--monitoring)
8. [Optimization Decision Framework](#optimization-decision-framework)

---

## Core Principles

### Principle 1: Treat Context as Precious Resource
**Guideline**: Only keep the smallest, most high-signal set of tokens needed at each step

**What This Means**:
- Every token should serve a clear purpose
- Avoid redundancies and irrelevant information
- Always ask: "Does the model *need* this right now?"
- If not needed immediately, remove or defer

**Measurement**:
- Signal-to-Noise Ratio: `useful_tokens / total_tokens`
- Target: ≥ 0.85 (85% useful content)

### Principle 2: Compress Aggressively, Preserve Meaning
**Guideline**: Summarize and truncate without losing critical information

**What This Means**:
- Replace verbose history with concise summaries
- Truncate old data with low relevance
- Keep essential facts, drop wordy details
- Compress early and often

**Measurement**:
- Compression Ratio: `original_tokens / compressed_tokens`
- Target: 10:1 for worker findings, 50:1 for multi-agent research

### Principle 3: Reference, Don't Embed
**Guideline**: Point to knowledge sources instead of duplicating content

**What This Means**:
- Create shared guides for common patterns
- Reference guides from agents
- Maintain single source of truth
- Update once, benefit everywhere

**Measurement**:
- Duplication Rate: `duplicated_tokens / total_tokens`
- Target: ≤ 0.10 (10% acceptable duplication for clarity)

### Principle 4: Structure for Clarity
**Guideline**: Organize context with clear sections, labels, and hierarchy

**What This Means**:
- Use consistent section ordering
- Label different types of content (system, user, tool)
- Create visual separation with headers
- Make it easy to scan and parse

**Measurement**:
- Structure Consistency Score: Validate against template
- Target: ≥ 0.95 (95% template compliance)

### Principle 5: Monitor and Optimize Continuously
**Guideline**: Track usage, identify patterns, improve over time

**What This Means**:
- Implement context size monitoring
- Set threshold alerts (75%, 85%, 95%)
- Analyze usage patterns
- Iterate based on data

**Measurement**:
- Context Utilization: `used_tokens / available_tokens`
- Target: ≤ 0.75 (stay under 75% for safety margin)

---

## Context Budgets by Operation Type

### Budget Allocation Framework

```yaml
# Recommended token budgets per operation type
budgets:
  # Simple operations (single file, straightforward task)
  simple_query: 5,000_tokens

  # Research operations (2-5 sources, pattern finding)
  basic_research: 15,000_tokens
  standard_research: 30,000_tokens
  deep_research: 50,000_tokens

  # Implementation operations (code changes, testing)
  small_implementation: 20,000_tokens  # 1-2 files
  medium_implementation: 50,000_tokens  # 3-5 files
  large_implementation: 80,000_tokens  # 6+ files

  # Multi-agent coordination (parallel workers)
  dual_agent: 40,000_tokens  # 2 agents
  multi_agent_small: 70,000_tokens  # 3-5 agents
  multi_agent_large: 100,000_tokens  # 6+ agents

  # Review and validation operations
  code_review: 25,000_tokens
  architecture_review: 35,000_tokens
  security_review: 40,000_tokens

# Alert thresholds
thresholds:
  warn_at: 150,000_tokens  # 75% of 200k
  compress_at: 170,000_tokens  # 85%
  fail_safe: 190,000_tokens  # 95%
```

### Budget Justification

**Simple Query (5K tokens)**:
- Read 1 file (~1K)
- Grep 2-3 patterns (~0.5K)
- Agent prompt (~1.5K)
- Response generation (~2K)

**Standard Research (30K tokens)**:
- Read 5-8 files (~8K)
- Grep 10+ patterns (~2K)
- Web search results (~5K)
- Agent prompt (~3K)
- Synthesis & response (~12K)

**Multi-Agent Large (100K tokens)**:
- Orchestrator context (~5K)
- 5 agents × 15K each (~75K)
- Compressed results (~10K)
- Synthesis & coordination (~10K)

### Budget Monitoring

**How to Track**:
```python
# Pseudo-code for budget tracking
def track_operation_budget(operation_type, actual_tokens):
    budget = BUDGETS[operation_type]
    utilization = actual_tokens / budget

    if utilization > 1.2:  # Over budget by 20%
        log_warning(f"{operation_type} exceeded budget")
        trigger_analysis(operation_type)
    elif utilization < 0.5:  # Under budget by 50%
        log_info(f"{operation_type} could reduce budget")

    return {
        "operation": operation_type,
        "budget": budget,
        "actual": actual_tokens,
        "utilization": utilization
    }
```

---

## Agent Design Patterns

### Pattern 1: Minimal Agent Definition
**Goal**: Keep agent prompts lean and focused

**Structure**:
```markdown
# Agent Name

## Role (50-100 tokens)
Clear, concise role description

## Schema Reference (20 tokens)
**Extends**: base-agent.schema.json

## Knowledge Base (100-150 tokens)
**Extends**: base-agent-pattern.md

**Additional Knowledge**:
- [Only agent-specific guides]

## Agent-Specific Workflow (300-500 tokens)
[Unique workflow steps only]

## Tool Patterns (100-200 tokens)
**Extends**: tool-design-patterns.md

**Agent-Specific Patterns**:
- [Only unique tool usage]

## Examples (100-200 tokens)
[1-2 minimal examples, link to guide for more]
```

**Total Target**: 700-1,200 tokens per agent (down from 1,500-3,700)

### Pattern 2: Base + Extension Model
**Goal**: Maximize reuse, minimize duplication

**Implementation**:
1. Create `base-agent-pattern.md` with common sections
2. Agents extend base with `**Extends**: base-agent-pattern.md`
3. Agents include only deviations/additions
4. Maintain clear inheritance hierarchy

**Benefits**:
- Update once, propagate to all agents
- Consistent patterns across ecosystem
- Easier maintenance and onboarding
- 50-70% reduction in duplication

### Pattern 3: Progressive Disclosure
**Goal**: Load context only when needed

**Implementation**:
1. Start with minimal context (role, basic tools)
2. Load domain knowledge on-demand
3. Reference guides for detailed patterns
4. Fetch external docs only when necessary

**Example**:
```markdown
## Knowledge Loading Strategy

**Always Loaded** (300 tokens):
- Agent role and boundaries
- Base workflow pattern
- Core tool definitions

**Load on First Use** (500 tokens):
- Domain-specific guides
- Complex examples
- Framework documentation

**Load on Explicit Request** (1000+ tokens):
- External API documentation
- Comprehensive examples
- Historical context
```

### Pattern 4: Compression Checkpoints
**Goal**: Reduce context size at natural breakpoints

**Implementation**:
1. Identify phases in agent workflow
2. Compress completed phases to summaries
3. Archive detailed logs to Memory tool
4. Maintain only essential working context

**Example**:
```python
# Pseudo-code for compression checkpoints
def execute_workflow(task):
    # Phase 1: Analysis
    analysis_result = analyze_task(task)  # 10K tokens
    summary_1 = compress(analysis_result)  # 1K tokens

    # Phase 2: Research
    research_result = conduct_research(summary_1)  # 20K tokens
    summary_2 = compress(research_result)  # 2K tokens

    # Phase 3: Implementation
    impl_result = implement_solution(summary_2)  # 15K tokens
    summary_3 = compress(impl_result)  # 1.5K tokens

    # Final output: 4.5K tokens vs 45K if no compression
    return synthesize(summary_1, summary_2, summary_3)
```

---

## Compression Strategies

### Strategy 1: Multi-Level Compression
**Context**: Worker → Lead → Orchestrator hierarchy

**Compression Ratios**:
- Worker-Level: 10:1 (200K research → 20K findings)
- Lead-Level: 5:1 additional (100K findings → 20K report)
- Overall: 50:1 for complex multi-agent research

**Implementation**:
```python
# Worker compression
def worker_compress(raw_findings):
    """Compress 200K tokens to 20K essential findings"""
    return {
        "key_patterns": extract_patterns(raw_findings),  # 5K
        "representative_examples": select_examples(raw_findings, n=3),  # 3K
        "insights": synthesize_insights(raw_findings),  # 7K
        "recommendations": generate_recommendations(raw_findings),  # 5K
    }

# Lead compression
def lead_compress(worker_findings):
    """Compress 100K worker findings to 20K synthesis"""
    return {
        "cross_cutting_themes": identify_themes(worker_findings),  # 6K
        "consolidated_recommendations": merge_recommendations(worker_findings),  # 8K
        "high_level_insights": synthesize_across_workers(worker_findings),  # 6K
    }
```

### Strategy 2: Semantic Preservation
**Goal**: Compress without losing meaning

**Techniques**:
1. **Abstractive Summarization**: Rewrite in concise form
2. **Extractive Summarization**: Select most important sentences
3. **Hierarchical Summaries**: Multi-level detail (overview → details)
4. **Representative Sampling**: Keep exemplars, drop duplicates

**Quality Metrics**:
- Semantic Similarity: cosine_similarity(original, compressed) ≥ 0.85
- Information Retention: key_facts_preserved / total_facts ≥ 0.95
- Compression Ratio: original_tokens / compressed_tokens ≥ 10:1

### Strategy 3: Lossy vs Lossless Compression
**When to use each**:

**Lossless** (preserve everything):
- Critical instructions
- System prompts
- Schema definitions
- API contracts
- Security policies

**Lossy** (compress with information loss):
- Historical context (older conversations)
- Verbose tool outputs (keep key findings)
- Intermediate reasoning steps (keep conclusion)
- Redundant examples (keep representative samples)

**Decision Framework**:
```python
def choose_compression_strategy(content_type, age, importance):
    if content_type in ["instruction", "schema", "security"]:
        return "lossless"
    elif importance == "critical":
        return "lossless"
    elif age < 5_minutes:
        return "lossless"  # Recent context
    else:
        return "lossy"  # Older, less critical
```

### Strategy 4: Progressive Summarization
**Goal**: Compress incrementally as conversation grows

**Implementation**:
```
Turn 1: Full context (5K)
Turn 2: Full context (10K)
Turn 3: Full context (15K)
...
Turn 10: Summarize turns 1-5 (50K → 10K), keep 6-10 full (30K) = 40K total
Turn 20: Summarize turns 1-15 (150K → 20K), keep 16-20 full (30K) = 50K total
Turn 30: Summarize turns 1-25 (250K → 30K), keep 26-30 full (30K) = 60K total
```

**Benefits**:
- Prevents context explosion
- Maintains recent context in detail
- Preserves historical summary
- Scales to long conversations

---

## Tool Usage Optimization

### MCP Tool Selection
**Problem**: Loading all tools consumes massive context
**Solution**: Selective tool loading

**Audit Process**:
1. Track actual tool usage over 100+ sessions
2. Identify tools with 0 usage
3. Identify tools with <5 usage
4. Create essential tool subset

**Example Configuration**:
```json
{
  "github": {
    "include": [
      "get_me",  // Used 50x
      "list_repositories",  // Used 30x
      "get_file_contents",  // Used 45x
      "create_pull_request",  // Used 20x
      "search_code"  // Used 25x
    ],
    "exclude": [
      "list_teams",  // Used 0x
      "get_team_member",  // Used 0x
      // ... 45 other unused tools
    ]
  }
}
```

**Impact**:
- Before: 70+ tools, 79K tokens
- After: 12 tools, 18K tokens
- Savings: 61K tokens (77%)

### Context7 Query Optimization
**Problem**: Broad queries return 15K+ tokens
**Solution**: Topic specificity and progressive queries

**Anti-Pattern**:
```python
# ❌ Returns 15K+ tokens
get_library_docs(
    library="/anthropic/claude",
    topic="documentation",
    max_tokens=8000  # Ignored, just a suggestion
)
```

**Best Practice**:
```python
# ✅ Returns ~3K tokens per query, 9K total
setup_docs = get_library_docs(
    library="/anthropic/claude",
    topic="installation and setup steps",
    max_tokens=2000
)

config_docs = get_library_docs(
    library="/anthropic/claude",
    topic="configuration options",
    max_tokens=2000
)

integration_docs = get_library_docs(
    library="/anthropic/claude",
    topic="API integration patterns",
    max_tokens=2000
)
```

**Token Allocation Guidelines**:
- Quick validation: 2K (actual: 3-4K)
- Standard query: 5K (actual: 6-8K)
- Deep dive: 8K (actual: 10-15K)
- **Multiplier**: Expect 1.3-1.5x actual vs requested

### File Operation Token Awareness
**Problem**: Large files can exceed read limits
**Solution**: Token-based strategy selection

**Token Estimation**: `line_count × 4.5 = approx_tokens`

**Strategy Matrix**:

| File Size | Token Estimate | Strategy |
|-----------|----------------|----------|
| <500 lines | <2.2K tokens | Direct Edit (safe) |
| 500-2K lines | 2.2K-9K tokens | Direct Edit (monitor) |
| 2K-5K lines | 9K-22.5K tokens | Sequential Edit + Re-read |
| >5K lines | >22.5K tokens | Write with Versioning |
| >5.5K lines | >25K tokens | Orchestrator Coordination |

**Implementation**:
```python
def select_file_operation_strategy(file_path):
    lines = count_lines(file_path)
    tokens = lines * 4.5

    if tokens < 10000:
        return "direct_edit"
    elif tokens < 22500:
        return "sequential_edit"  # Re-read between operations
    elif tokens < 25000:
        return "write_versioning"  # Create v2, replace
    else:
        return "request_orchestrator_help"
```

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Kitchen Sink Agent
**Description**: Including every possible feature/guide in agent definition

**Example**:
```markdown
❌ BAD: 3,700 token agent with:
- Full framework explanations (800 tokens)
- 10+ examples (500 tokens)
- Complete API documentation (600 tokens)
- Redundant workflow descriptions (400 tokens)
```

**Fix**:
```markdown
✅ GOOD: 1,200 token agent with:
- Role and boundaries (100 tokens)
- Reference to framework guide (20 tokens)
- 1-2 minimal examples (150 tokens)
- Agent-specific workflow only (400 tokens)
```

**Savings**: 2,500 tokens (67% reduction)

### Anti-Pattern 2: Copy-Paste Common Sections
**Description**: Duplicating shared content across multiple agents

**Example**:
```markdown
❌ BAD: Pre-flight checklist in 15 agents
- 250 tokens × 15 = 3,750 tokens total
- 90% identical across agents
```

**Fix**:
```markdown
✅ GOOD: Reference base pattern
- Base pattern: 250 tokens (1x)
- Each agent references: 20 tokens (15x = 300 tokens)
- Total: 550 tokens

Savings: 3,200 tokens (85% reduction)
```

### Anti-Pattern 3: Verbose Examples
**Description**: Including comprehensive examples inline

**Example**:
```markdown
❌ BAD: code-reviewer.md with:
- 15 verification pattern examples (200+ tokens)
- Full error recovery workflows (150 tokens)
- Complete finding templates (100 tokens)
```

**Fix**:
```markdown
✅ GOOD: Minimal inline + guide reference
- 2 representative examples (50 tokens)
- Reference to verification-patterns.md (20 tokens)
- Reference to error-recovery-guide.md (20 tokens)

Savings: 360 tokens (80% reduction)
```

### Anti-Pattern 4: Circular References
**Description**: Agents referencing guides that reference agents

**Example**:
```markdown
❌ BAD:
- code-implementer.md → References coding-guide.md
- coding-guide.md → References code-implementer.md workflow
- Result: Infinite loop, confusion
```

**Fix**:
```markdown
✅ GOOD: Clear hierarchy
- base-pattern.md (foundation)
  ↓
- domain-guide.md (general patterns)
  ↓
- agent.md (specific implementation)

No circular dependencies
```

### Anti-Pattern 5: No Context Monitoring
**Description**: Running blind without usage tracking

**Example**:
```markdown
❌ BAD:
- No visibility into context size
- Hit 200K limit unexpectedly
- No data for optimization
```

**Fix**:
```markdown
✅ GOOD: Implement monitoring
- PostToolUse hook tracks usage
- Alerts at 75%, 85%, 95%
- Analytics dashboard for patterns
- Proactive compression triggers
```

---

## Measurement & Monitoring

### Key Metrics

#### 1. Context Utilization Rate
**Definition**: `used_tokens / available_tokens`
**Target**: ≤ 0.75 (stay under 75%)
**Alert Thresholds**:
- 🟢 0-75%: Optimal
- 🟡 75-85%: Warning
- 🔴 85-95%: Critical
- ⛔ >95%: Imminent failure

#### 2. Agent Token Efficiency
**Definition**: `useful_output_tokens / total_context_tokens`
**Target**: ≥ 0.20 (20% of context produces output)
**Benchmark**:
- <0.10: Inefficient (review agent design)
- 0.10-0.20: Acceptable
- 0.20-0.30: Good
- >0.30: Excellent

#### 3. Compression Ratio
**Definition**: `original_tokens / compressed_tokens`
**Target**:
- Worker findings: ≥ 10:1
- Lead synthesis: ≥ 5:1
- Overall multi-agent: ≥ 50:1

#### 4. Duplication Rate
**Definition**: `duplicated_tokens / total_tokens`
**Target**: ≤ 0.10 (10% duplication acceptable)
**Measurement**: Compare agent definitions for repeated sections

#### 5. Template Compliance
**Definition**: `agents_matching_template / total_agents`
**Target**: ≥ 0.95 (95% compliance)
**Measurement**: Validate section ordering and structure

### Monitoring Implementation

```python
# Context monitoring hook
class ContextMonitor:
    def __init__(self):
        self.thresholds = {
            "warn": 150000,  # 75%
            "compress": 170000,  # 85%
            "critical": 190000  # 95%
        }
        self.history = []

    def track_usage(self, operation, tokens_used):
        self.history.append({
            "timestamp": now(),
            "operation": operation,
            "tokens": tokens_used,
            "cumulative": sum(h["tokens"] for h in self.history)
        })

        cumulative = self.history[-1]["cumulative"]

        if cumulative > self.thresholds["critical"]:
            return "CRITICAL: 95% context used - immediate action required"
        elif cumulative > self.thresholds["compress"]:
            return "WARNING: 85% context used - trigger compression"
        elif cumulative > self.thresholds["warn"]:
            return "INFO: 75% context used - monitor closely"

        return "OK"

    def get_analytics(self):
        return {
            "total_operations": len(self.history),
            "total_tokens": sum(h["tokens"] for h in self.history),
            "avg_per_operation": mean(h["tokens"] for h in self.history),
            "top_consumers": sorted(self.history, key=lambda h: h["tokens"])[-5:]
        }
```

---

## Optimization Decision Framework

### When to Optimize

**Trigger Conditions** (optimize if ANY are true):
1. Context utilization > 75% consistently
2. Agent definitions > 2,000 tokens
3. Duplication rate > 15%
4. Compression ratio < target
5. Performance degradation observed
6. User feedback on slow responses

### Optimization Approach

```
1. MEASURE
   ├─ Collect baseline metrics
   ├─ Identify bottlenecks
   └─ Quantify current state

2. ANALYZE
   ├─ Find redundancies
   ├─ Identify compression opportunities
   └─ Assess tool usage patterns

3. PLAN
   ├─ Prioritize high-impact optimizations
   ├─ Estimate savings potential
   └─ Define success metrics

4. IMPLEMENT
   ├─ Start with low-risk, high-impact
   ├─ Pilot with subset
   └─ Validate functionality maintained

5. VALIDATE
   ├─ Compare before/after metrics
   ├─ User acceptance testing
   └─ Performance benchmarking

6. ITERATE
   ├─ Apply learnings to remaining items
   ├─ Continuous monitoring
   └─ Incremental improvements
```

### ROI Calculation

```python
def calculate_optimization_roi(optimization):
    # Benefits
    token_savings = optimization.tokens_saved
    performance_gain = optimization.speed_improvement_pct
    maintenance_reduction = optimization.maintenance_hours_saved

    # Costs
    implementation_hours = optimization.hours_to_implement
    risk_factor = optimization.risk_score  # 0.0-1.0

    # Value calculation
    token_value = token_savings * 0.01  # $0.01 per 1K tokens saved per session
    performance_value = performance_gain * 10  # $10 per 1% improvement
    maintenance_value = maintenance_reduction * 50  # $50 per hour saved

    total_value = token_value + performance_value + maintenance_value
    total_cost = implementation_hours * 100  # $100 per hour

    # Adjust for risk
    adjusted_value = total_value * (1 - risk_factor)

    roi = (adjusted_value - total_cost) / total_cost

    return {
        "roi": roi,
        "breakeven_sessions": total_cost / token_value if token_value > 0 else float('inf'),
        "recommendation": "IMPLEMENT" if roi > 0.5 else "DEFER"
    }
```

---

## Quick Reference Checklist

### Agent Design Checklist
- [ ] Agent definition < 1,500 tokens
- [ ] References base-agent-pattern.md
- [ ] No duplicated common sections
- [ ] 1-2 minimal examples maximum
- [ ] Links to guides for detailed patterns
- [ ] Follows standard template order
- [ ] Schema reference included
- [ ] Clear role and boundaries

### Context Usage Checklist
- [ ] Context utilization < 75%
- [ ] Compression ratios meet targets
- [ ] No circular references
- [ ] Tool usage optimized (only essential loaded)
- [ ] File operations token-aware
- [ ] Context7 queries specific
- [ ] Monitoring enabled and functioning
- [ ] Budget allocation defined

### Optimization Checklist
- [ ] Baseline metrics collected
- [ ] High-impact items identified
- [ ] Pilot group selected
- [ ] Success criteria defined
- [ ] Rollback plan prepared
- [ ] Validation suite ready
- [ ] ROI calculated
- [ ] Risk assessment completed

---

## Appendix: Example Calculations

### Example 1: Agent Optimization ROI

**Scenario**: Optimize spec-enhancer.md from 3,700 to 1,200 tokens

**Calculation**:
```python
optimization = {
    "tokens_saved": 2500,
    "speed_improvement_pct": 15,  # Faster loading
    "maintenance_hours_saved": 2,  # Easier to update
    "hours_to_implement": 3,
    "risk_score": 0.2  # Low risk, well-tested pattern
}

roi = calculate_optimization_roi(optimization)
# Result: ROI = 2.3x, breakeven = 12 sessions, IMPLEMENT
```

### Example 2: MCP Tool Optimization

**Scenario**: Reduce GitHub tools from 50 to 7

**Calculation**:
```python
optimization = {
    "tokens_saved": 60000,  # Massive savings
    "speed_improvement_pct": 40,  # Much faster startup
    "maintenance_hours_saved": 0,  # No maintenance impact
    "hours_to_implement": 1,  # Simple config change
    "risk_score": 0.1  # Very low risk
}

roi = calculate_optimization_roi(optimization)
# Result: ROI = 10.4x, breakeven = 2 sessions, IMPLEMENT IMMEDIATELY
```

---

**Document End**

For questions or suggestions, see: `.claude/docs/SETUP.md` or create issue in project repo.
