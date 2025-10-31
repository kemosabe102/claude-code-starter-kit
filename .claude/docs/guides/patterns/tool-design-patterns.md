# Tool Design Patterns Guide

**Purpose**: Anthropic best practices for designing agent-tool interfaces and tool descriptions

**Referenced by**: agent-architect, all agents (via template)

## Core Principle

**Agent-Tool Interfaces as Critical as Human-Computer Interfaces**

Tools represent contracts between deterministic systems and non-deterministic agents. Unlike traditional functions, agents may:
- Call tools correctly
- Answer from general knowledge
- Ask clarifying questions
- Occasionally hallucinate

This fundamental difference demands rethinking tool design.

## Tool Description Quality Standards

### Write for New Team Member
- Explain as if onboarding someone unfamiliar with system
- Don't assume implicit knowledge
- Provide context and examples

### Make Implicit Context Explicit
- **Query formats**: Specify expected input structure
- **Niche terminology**: Define specialized terms
- **Resource relationships**: Explain dependencies

### Unambiguous Parameter Naming
- ❌ `user` (ambiguous - ID? name? object?)
- ✅ `user_id` (clear - expects identifier)
- ✅ `user_email` (clear - expects email address)

### Disclose Important Behaviors
- Destructive changes (deletes, overwrites)
- Open-world access (web, external APIs)
- Side effects (notifications, logs)
- Rate limits or costs

### Include Examples
```markdown
search_codebase(pattern: str, file_type: str = "py")

Searches project codebase for pattern.

Parameters:
- pattern: Regex pattern to match (e.g., "class.*Auth", "def process_.*")
- file_type: File extension filter (e.g., "py", "js", "md")

Returns: List of {file, line, match} objects

Example: search_codebase("async def", "py") finds all async functions
```

## Tool Response Optimization

### High-Signal Information Only
- Prioritize contextual relevance over flexibility
- Return what agents need, not everything possible
- Eschew low-level IDs in favor of semantic fields

### Token Efficiency
**Bad** (206 tokens):
```json
{
  "uuid": "a1b2c3d4",
  "mime_type": "application/pdf",
  "created_ts": 1234567890,
  "modified_ts": 1234567899,
  "size_bytes": 102400,
  "internal_id": 42,
  "file_name": "report.pdf"
}
```

**Good** (72 tokens - 3x reduction):
```json
{
  "name": "report.pdf",
  "type": "PDF",
  "modified": "2024-01-15"
}
```

### Response Format Options
Implement `response_format` enum parameter:
- `concise`: Essential fields only
- `detailed`: Full information

Enables agents to request appropriate detail level.

### Pagination & Limits
- Default limits (e.g., 25 results)
- Page/offset parameters
- Total count in response
- Truncation with helpful guidance

```python
def search_documents(query: str, limit: int = 25, offset: int = 0):
    """
    If results truncated, suggests:
    - Refine query for specificity
    - Use pagination for systematic review
    - Filter by date/type to narrow scope
    """
```

## Tool Consolidation Patterns

### Atomic High-Level Operations
❌ **Low-Level Exposure**:
- `list_users()`
- `list_events()`
- `create_event(user_id, time)`

✅ **Consolidated**:
- `schedule_event(attendees, duration, preferences)`
  - Finds availability automatically
  - Creates event atomically
  - Returns confirmation

### Context-Aware Responses
❌ **Separate Calls**:
```
customer = get_customer_by_id(123)
transactions = list_transactions(customer_id=123)
notes = list_notes(customer_id=123)
```

✅ **Consolidated**:
```
get_customer_context(customer_id=123)
# Returns: profile + recent transactions + notes in one call
```

### Smart Defaults & Filters
❌ **Raw Data Dump**:
```
read_logs() # Returns 100MB of logs
```

✅ **Filtered & Relevant**:
```
search_logs(
    pattern="error",
    since="1h",
    context_lines=3  # Shows surrounding context
)
```

## Tool Selection Heuristics for Agents

### Guidance to Include in Tool Descriptions

**When to Use This Tool**:
- Specific scenarios where tool applies
- Versus alternatives (why choose this one)

**Tool Selection Priority**:
1. Examine all available tools first
2. Match tool to user intent
3. Prefer specialized over generic
4. Use right tool for context (critical for correctness)

### Critical Scenarios
"An agent searching web for context that only exists in Slack is doomed from start."

Tool descriptions must clarify:
- **Data sources** tool accesses
- **Scope** of information available
- **Limitations** of tool capabilities

## MCP Integration Patterns

### Namespacing Related Tools
Group tools under common prefixes:
- `asana_search`, `asana_create`, `asana_update`
- `github_list_prs`, `github_create_pr`, `github_comment`

Benefits:
- Easier discovery
- Clearer relationships
- Better organization with many tools

### Quality Across Developers
With MCP exposing hundreds of tools from different developers:
- Maintain consistent description quality
- Follow standardized parameter naming
- Use common response structures
- Document clearly per these patterns

## Error Response Patterns

### Actionable Error Messages
❌ **Vague**: "Operation failed"

✅ **Actionable**:
```
Search failed: Pattern 'class.*(' has unclosed parenthesis.
Try: 'class.*\\(' to match literal parenthesis
```

### Adaptive Recovery
"Letting agent know when tool failing and letting it adapt works surprisingly well."

Combine:
- AI agent adaptability (try alternatives)
- Deterministic safeguards (retry logic, checkpoints)

### Error Response Format
```json
{
  "success": false,
  "error": {
    "message": "Clear explanation",
    "suggestion": "How to fix or try alternative",
    "context": "Why this failed"
  }
}
```

## Tool Testing & Improvement

### Tool-Testing Agent Pattern
Anthropic's approach:
1. Create agent that attempts using tools dozens of times
2. Identify failure patterns systematically
3. Rewrite tool descriptions based on failures
4. **Result**: 40% reduction in task completion time

### Continuous Improvement
- Monitor agent tool usage patterns
- Identify common failure modes
- Iterate on descriptions
- Measure improvement (completion time, success rate)

## Validation Checklist

**Tool Description**:
- [ ] Written for new team member understanding
- [ ] Implicit context made explicit
- [ ] Unambiguous parameter names
- [ ] Destructive changes disclosed
- [ ] Examples included

**Tool Response**:
- [ ] High-signal information prioritized
- [ ] Token-optimized (concise by default)
- [ ] Response format options available
- [ ] Pagination/limits implemented
- [ ] Helpful truncation guidance

**Tool Design**:
- [ ] Consolidated vs low-level operations
- [ ] Context-aware where beneficial
- [ ] Smart defaults and filters
- [ ] Clear selection heuristics
- [ ] Actionable error messages

---

**40% Improvement Potential**: Tool description quality directly impacts agent performance. Invest as much effort in tool design as prompt engineering.
