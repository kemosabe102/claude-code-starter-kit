# MCP Agent Optimization

**Purpose**: Operational guidance for efficient MCP (Model Context Protocol) usage, with focus on Context7 library documentation access.

**Target Audience**: Agents that use MCP tools for research (researcher-library, context-optimizer, prompt-evaluator)

**Version**: 1.0

---

## Quick Reference

**Token Allocation Strategy**:
- **2K tokens**: Quick validation, pattern existence checks
- **5K tokens**: Standard research (DEFAULT for most queries)
- **8K tokens**: Deep analysis, comprehensive architectural research

**Quality Gates**:
- Trust score ≥ 7 (required)
- Code snippets ≥ 100 characters (required)
- Progressive refinement: 3 rounds maximum

**Core Principle**: Start small, expand progressively based on results.

---

## Context7 MCP Overview

**What is Context7**: AI-powered library documentation search optimized for developer queries.

**Key Capabilities**:
- Version-specific API documentation
- Code examples and patterns
- Migration guides and changelogs
- Official library/framework documentation (authoritative primary source)

**When to Use**:
- Library/framework API research
- Version-specific feature lookups
- Migration guidance between versions
- Official documentation queries

**When NOT to Use**:
- General programming concepts → Use researcher-web
- Codebase-specific patterns → Use researcher-codebase
- Community best practices → Use researcher-web

---

## Token Allocation Strategy

### Progressive Research Pattern

**Principle**: Start with minimal token allocation, expand only if needed.

**Three-Tier Approach**:

```markdown
Round 1: tokens=2000, topic="[specific concept]"
  ↓
Evaluate: Sufficient? → STOP
  ↓
Round 2: tokens=5000, topic="[refined focus]"
  ↓
Evaluate: Sufficient? → STOP
  ↓
Round 3: tokens=8000, topic="[comprehensive analysis]"
```

### Token Allocation Guidelines

#### 2K Tokens (Quick Validation)

**Use Cases**:
- Confirm feature exists in library
- Get method signature only
- Check version compatibility
- Validate import path

**Example Topics**:
- "async validator syntax"
- "field types list"
- "basic configuration"

**Expected Results**: 1-3 focused snippets, basic confirmation

---

#### 5K Tokens (Standard Research - DEFAULT)

**Use Cases**:
- Standard implementation patterns
- Common use cases with examples
- Configuration options overview
- Typical integration scenarios

**Example Topics**:
- "async field validation examples"
- "custom validator patterns"
- "model configuration options"

**Expected Results**: 5-10 code examples, comprehensive explanation

---

#### 8K Tokens (Deep Analysis)

**Use Cases**:
- Architectural decision support
- Complex integration patterns
- Migration planning
- Comprehensive feature analysis

**Example Topics**:
- "validation architecture best practices"
- "performance optimization strategies"
- "migration from v1 to v2 guide"

**Expected Results**: 15+ examples, detailed explanations, architectural context

---

## Topic Focusing Strategy

### Good Topics (Specific, 2-4 words)

**Characteristics**:
- Concrete concept or feature name
- Specific enough to filter documentation
- Broad enough to return context

**Examples**:
- ✅ "async field validation"
- ✅ "custom error messages"
- ✅ "model inheritance patterns"
- ✅ "migration guide v2"

**Results**: ~2-8K tokens returned, relevant and focused

---

### Bad Topics (Too Broad or Too Narrow)

**Too Broad**:
- ❌ "documentation" → Returns 20-30K tokens, everything
- ❌ "tutorial" → Unfocused, too much content
- ❌ "getting started" → Returns entire intro section

**Too Narrow**:
- ❌ "validate_email_field_with_regex" → Too specific, may miss related patterns
- ❌ "line 47 implementation" → Context7 doesn't search by line numbers

**Results**: Either overwhelming or insufficient information

---

### Topic Refinement Workflow

**Initial Query**: Broad topic, 2K tokens
```markdown
Round 1: tokens=2000, topic="validation"
Result: Too broad, 10K tokens returned
```

**Refined Query**: Narrowed focus, 5K tokens
```markdown
Round 2: tokens=5000, topic="async validators"
Result: Good focus, 4K tokens returned with examples
```

**Deep Dive** (if needed): Specific aspect, 8K tokens
```markdown
Round 3: tokens=8000, topic="async validator error handling"
Result: Comprehensive coverage with edge cases
```

---

## Quality Validation Gates

### Trust Score (≥ 7 Required)

**What it measures**: Context7's confidence in result relevance and accuracy

**Scoring**:
- **9-10**: Highly relevant, official docs, exact match
- **7-8**: Relevant, good quality, may need minor refinement
- **4-6**: Potentially relevant but uncertain quality
- **0-3**: Low relevance, likely not useful

**Gates**:
- ✅ **Trust ≥ 7**: Accept results, proceed with analysis
- ⚠️ **Trust 4-6**: Review carefully, consider refining query
- ❌ **Trust < 4**: Reject, refine topic or switch to different source

### Code Snippet Size (≥ 100 Characters Required)

**What it measures**: Substantive code examples vs. trivial snippets

**Rationale**:
- Snippets < 100 chars: Usually just imports or method signatures (insufficient)
- Snippets ≥ 100 chars: Real implementation examples with context

**Example**:

**Insufficient (< 100 chars)**:
```python
from pydantic import validator
```

**Sufficient (≥ 100 chars)**:
```python
from pydantic import BaseModel, validator

class UserModel(BaseModel):
    email: str

    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email')
        return v
```

**Gates**:
- ✅ **Snippets ≥ 100 chars**: Actionable code examples
- ⚠️ **Snippets 50-99 chars**: May be sufficient for simple queries
- ❌ **Snippets < 50 chars**: Likely insufficient, request more detail

---

## Response Size Management

### Compression Ratio Target: 10:1

**Principle**: Return 10% of input as synthesized findings

**Example**:
- Input: 5,000 tokens of Context7 documentation
- Output: 500 tokens of compressed findings
- Compression: 10:1 ratio

### Compression Techniques

**1. Pattern Extraction**
- Identify 3-5 key patterns from 15+ examples
- Extract common structure, ignore variations
- Focus on "what" and "when", not exhaustive "how"

**2. Deduplication**
- Remove repetitive examples
- Consolidate similar patterns
- Reference "5 similar examples" vs. showing all

**3. Hierarchical Summarization**
- High-level summary (2-3 sentences)
- Key patterns (3-5 bullets)
- Code example (1-2 representative snippets)
- Edge cases (only if critical)

**4. Progressive Disclosure**
- Provide summary findings immediately
- Offer "more detail available on X" for edge cases
- Let orchestrator request deeper analysis if needed

---

## Multi-Round Research Strategy

### When to Use Multiple Rounds

**Scenarios**:
1. Initial query too broad (>10K tokens returned)
2. Results lack specific detail needed
3. Multiple related concepts to explore
4. Validation of hypotheses from initial research

**Maximum Rounds**: 3 (diminishing returns beyond this)

### Round Structure

**Round 1: Reconnaissance (2K tokens)**
- Goal: Confirm capability exists
- Topic: Broad concept name
- Outcome: Yes/No + general approach

**Round 2: Implementation (5K tokens)**
- Goal: Get working examples
- Topic: Refined based on Round 1
- Outcome: Code patterns + configuration

**Round 3: Edge Cases (8K tokens)**
- Goal: Handle complex scenarios
- Topic: Specific advanced use case
- Outcome: Comprehensive coverage

### Example: Async Validation Research

```markdown
Round 1 (2K tokens):
- Topic: "async validation"
- Result: Confirmed Pydantic v2 supports async validators
- Trust: 8, Snippets: 150 chars average
- Decision: Need implementation details → Round 2

Round 2 (5K tokens):
- Topic: "async field validators pydantic"
- Result: 6 code examples, decorator patterns, await syntax
- Trust: 9, Snippets: 200 chars average
- Decision: Sufficient for standard use case → STOP

Round 3 (Not needed): Standard case covered
```

---

## Context7 Tool Usage

### resolve-library-id

**Purpose**: Find library ID for documentation access

**Usage**:
```markdown
resolve-library-id(library_name="pydantic")
→ Returns: library_id="pydantic-v2"
```

**Best Practices**:
- Always resolve ID before get-library-docs
- Cache library_id for session (don't re-resolve)
- If resolution fails: Library not in Context7, fall back to researcher-web

---

### get-library-docs

**Purpose**: Retrieve version-specific documentation with topic focusing

**Parameters**:
- `library_id`: From resolve-library-id
- `topic`: Specific concept (2-4 words)
- `tokens`: Allocation (2000/5000/8000)

**Usage Pattern**:
```markdown
get-library-docs(
  library_id="pydantic-v2",
  topic="async field validation",
  tokens=5000
)
```

**Best Practices**:
- Start with 5K tokens (default)
- Use specific topics (not "documentation")
- Validate trust ≥ 7 before proceeding
- Check snippet size ≥ 100 chars
- Compress findings to 10:1 ratio

---

## Failure Handling

### Context7 Insufficient → Delegate to researcher-web

**Triggers**:
1. Trust score < 7 after 2 refinement attempts
2. Library not found in Context7
3. Topic too community-specific (not official docs)
4. Need cross-library comparison

**Delegation Pattern**:
```markdown
Context7 Result: Trust=5, snippets insufficient
→ FAILURE mode with delegation recommendation
→ Return: "DELEGATE to researcher-web for community patterns"
```

**Rationale**: Context7 = official docs, researcher-web = community knowledge

### Progressive Refinement Exhausted

**Max Refinement Rounds**: 3

**If still insufficient after 3 rounds**:
1. Return partial findings with confidence score
2. Recommend alternative research approach
3. Document what was attempted (prevent retry loops)
4. Suggest manual research or different agent

---

## Token Optimization Best Practices

### 1. Cache Library IDs
- Resolve once per session
- Reuse across multiple queries
- Saves ~200 tokens per query

### 2. Batch Related Queries
- Single 8K token query > Two 5K queries
- Reduces overhead, better context
- Use when researching related concepts

### 3. Explicit Token Limits
- Always specify tokens parameter
- Don't rely on defaults (may change)
- Budget token usage across multi-query research

### 4. Topic Precision
- Invest time crafting specific topics
- Saves tokens through better targeting
- 2-4 words optimal for most queries

### 5. Early Termination
- Stop when sufficient information found
- Don't always use full token allocation
- "Good enough" termination rule (0.7 confidence)

---

## Integration with Research Patterns

**This guide complements**: `.claude/docs/guides/patterns/research-patterns.md`

**Division of Responsibility**:
- **research-patterns.md**: High-level research coordination, delegation, 4-component structure
- **mcp-agent-optimization.md** (this doc): Tactical MCP/Context7 tool usage

**When to Reference**:
- **researcher-library agent**: Primary user, operational guidance
- **context-optimizer agent**: Token budget planning, compression validation
- **prompt-evaluator agent**: Evaluating research agent prompts for MCP usage

---

## Examples

### Example 1: Simple Feature Validation (2K tokens)

**Task**: Confirm Pydantic v2 supports async validators

**Query**:
```markdown
library_id = resolve-library-id("pydantic")
result = get-library-docs(
  library_id=library_id,
  topic="async validators",
  tokens=2000
)
```

**Expected Result**:
- Trust: 8-9
- Snippets: 1-2 examples (~150 chars each)
- Outcome: Confirmed, basic syntax shown
- Tokens used: ~1,500
- Compression: Summary in 150 tokens (10:1)

---

### Example 2: Implementation Pattern (5K tokens)

**Task**: Get working async field validation examples

**Query**:
```markdown
library_id = resolve-library-id("pydantic")
result = get-library-docs(
  library_id=library_id,
  topic="async field validation examples",
  tokens=5000
)
```

**Expected Result**:
- Trust: 9
- Snippets: 5-7 examples (~200 chars each)
- Outcome: Working patterns with configuration
- Tokens used: ~4,200
- Compression: 3 key patterns + 2 examples in 450 tokens (10:1)

---

### Example 3: Progressive Refinement (2K → 5K → 8K)

**Task**: Research comprehensive async validation architecture

**Round 1 (2K)**:
```markdown
topic="async validation"
Result: Basic confirmation, trust=7, insufficient detail
Decision: Need more → Round 2
```

**Round 2 (5K)**:
```markdown
topic="async field validators pydantic"
Result: Good examples, trust=9, but missing error handling
Decision: Need edge cases → Round 3
```

**Round 3 (8K)**:
```markdown
topic="async validator error handling patterns"
Result: Comprehensive, trust=9, includes edge cases
Decision: SUFFICIENT → Stop
```

**Total Tokens**: 2K + 5K + 8K = 15K
**Compressed Output**: 1,500 tokens (10:1 across all rounds)

---

## Related Documentation

- **`.claude/docs/guides/patterns/research-patterns.md`**: High-level research delegation framework
- **`.claude/docs/guides/progressive-disclosure-ai-context-windows.md`**: Progressive disclosure principles for token management
- **`.claude/docs/research/prompt-engineering/Context-Optimization-Analysis-Report.md`**: Theoretical foundation for token optimization
- **`.claude/agents/researcher-library.md`**: Primary consumer of this guidance

---

**Version**: 1.0
**Last Updated**: 2025-10-31
**Ownership**: Framework documentation (shared across agents)
