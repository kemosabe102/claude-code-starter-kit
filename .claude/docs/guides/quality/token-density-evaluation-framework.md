# Token Density Evaluation Framework

**Purpose**: Systematic methodology for evaluating and optimizing token usage in prompts, agent definitions, and documentation.

**Version**: 1.0.0
**Last Updated**: 2025-10-31

---

## 📋 Quick Assessment (5-Minute Evaluation)

### Step 1: Calculate Base Metrics

```bash
# Get character, line, word counts
wc -c -l -w <file>

# Calculate token estimate
# Conservative: characters / 4
# Optimistic: characters / 3.5
```

**Token Density Score**:
```
Information_Density = Unique_Concepts / Total_Tokens
```

**Target Scores**:
- **High Density**: ≥ 0.15 concepts/token (1 concept per 6-7 tokens)
- **Medium Density**: 0.10-0.14 concepts/token (1 concept per 7-10 tokens)
- **Low Density**: < 0.10 concepts/token (>10 tokens per concept)

---

## 🎯 Six-Dimension Evaluation Matrix

### Dimension 1: **Structural Efficiency** (0-100 score)

**Checklist**:
- [ ] Uses markdown-KV or JSON over tables (47% savings)
- [ ] Hierarchical headers (##, ###) vs inline emphasis
- [ ] Bullet lists for parallel content
- [ ] Code blocks for examples (show vs tell)
- [ ] XML tags for major sections (`<task>`, `<context>`)

**Scoring**:
- 5/5 criteria met: 100 points
- 4/5: 80 points
- 3/5: 60 points
- 2/5: 40 points
- <2: Needs immediate restructuring

**Anti-Patterns** (deduct 10 points each):
- Markdown tables where KV pairs would work
- Box-drawing characters (use ASCII)
- Inline emphasis overuse (***text***)
- Nested lists >3 levels deep

---

### Dimension 2: **Language Efficiency** (0-100 score)

**Checklist**:
- [ ] No filler words ("possibly", "really", "very", "actually")
- [ ] Active voice throughout (not passive)
- [ ] Constraint statements ("Max 100 words") vs explanations ("because...")
- [ ] Abbreviations for established terms (API, HTTP, OODA)
- [ ] Direct commands ("Use X") vs suggestions ("You might consider...")

**Common Filler Words** (flag these):
```
possibly, really, very, actually, basically, essentially, literally,
just, simply, clearly, obviously, of course, in order to, due to the fact that,
at this point in time, as a matter of fact, for the purpose of
```

**Passive Voice Patterns** (flag these):
```
"should be reviewed" → "review"
"can be improved by" → "improve with"
"is handled by" → "handles"
"was created to" → "creates"
```

**Scoring**:
- 0-5 violations: 100 points
- 6-10 violations: 80 points
- 11-20 violations: 60 points
- 21-40 violations: 40 points
- >40: Critical rewrite needed

---

### Dimension 3: **Reference Efficiency** (0-100 score)

**Checklist**:
- [ ] Uses `**Extends**: base-pattern.md` instead of copy-paste
- [ ] Points to comprehensive guides vs embedding details
- [ ] No circular references (A → B → A)
- [ ] Clear information hierarchy (Level 1 → Level 2 → Level 3)
- [ ] Consolidates "See X for Y" statements (not scattered)

**Pattern Detection**:
```python
# Count repeated content blocks
repeated_blocks = find_duplicates(content, min_length=100)

# Each 100-char duplicate across N files:
# Waste = 100 * (N - 1) tokens
```

**Base Pattern Savings Calculation**:
```
Common_Content_Tokens = sum(repeated_sections)
Agents_Using_Content = count(agents_with_duplicates)

Potential_Savings = Common_Content_Tokens * (Agents - 1)
Reference_Overhead = 20 tokens per agent ("**Extends**: base.md")

Net_Savings = Potential_Savings - (Reference_Overhead * Agents)
```

**Scoring**:
- Net_Savings ≥ 5,000 tokens and implemented: 100 points
- Net_Savings 2,000-4,999 and implemented: 80 points
- Net_Savings identified but not implemented: 40 points
- No analysis done: 0 points

---

### Dimension 4: **Example Efficiency** (0-100 score)

**Checklist**:
- [ ] 2-3 examples maximum per concept
- [ ] Examples show format, not describe it
- [ ] No verbose "walk-through" explanations
- [ ] Code examples use minimal viable demonstration
- [ ] Complex examples → separate guide file (reference only)

**Anti-Patterns**:
- "Let me explain step by step what this example does..."
- Example + prose explanation of same content
- >3 examples for same concept
- Inline examples >50 lines (should be external file)

**Scoring**:
```python
example_violations = 0
for section in sections:
    if count_examples(section) > 3:
        example_violations += (count - 3)
    if has_redundant_explanation(section):
        example_violations += 1
    if example_lines(section) > 50:
        example_violations += 1

score = max(0, 100 - (example_violations * 10))
```

---

### Dimension 5: **Progressive Disclosure Compliance** (0-100 score)

**Checklist**:
- [ ] Maximum 2 disclosure levels (quick ref → comprehensive)
- [ ] Essential features visible (80% use cases at top level)
- [ ] Clear navigation ("See X for Y" signposts)
- [ ] Descriptive labels (not "More" or "Advanced")
- [ ] Tier 3 resources executable, not embedded (0 tokens)

**Tier Structure Validation**:
```
Level 1 (Metadata): <500 tokens - Quick reference, formulas, decision trees
Level 2 (Instructions): <3,000 tokens - Comprehensive guide with examples
Level 3+ (Resources): 0 tokens - Templates, schemas, scripts (referenced, not loaded)
```

**Scoring**:
- Proper 2-level structure + all criteria: 100 points
- 2-level but missing criteria: 70 points
- 3-level depth: 40 points
- >3 levels: Critical restructuring needed (0 points)

---

### Dimension 6: **INFUSE Framework Alignment** (0-100 score)

**Checklist**:
- [ ] Identity: Specific behavioral anchors (not "helpful assistant")
- [ ] Navigation: Clear information hierarchy
- [ ] Flow: Domain-matched personality definition
- [ ] User Guidance: Structured workflows (not vague)
- [ ] Signals: Defined adaptation patterns (if user-facing)
- [ ] End Instructions: ALWAYS/NEVER directives (explicit)

**Token Budget per Component**:
```
Identity (I): 50-100 tokens
Navigation (N): 100-150 tokens
Flow (F): 50-100 tokens
User Guidance (U): 300-500 tokens
Signals (S): 200-400 tokens (or reference external file)
End Instructions (E): 100-150 tokens

Total Target: 700-1,200 tokens for agent definition
```

**Scoring**:
- All 6 components present, within budget: 100 points
- 5/6 components: 80 points
- 4/6 components: 60 points
- 3/6 components: 40 points
- <3 components: Incomplete (0 points)

---

## 🧮 Composite Score Calculation

```python
def calculate_token_density_score(file):
    scores = {
        "structural": evaluate_structure(file),      # 0-100
        "language": evaluate_language(file),         # 0-100
        "reference": evaluate_references(file),      # 0-100
        "examples": evaluate_examples(file),         # 0-100
        "disclosure": evaluate_disclosure(file),     # 0-100
        "infuse": evaluate_infuse(file)              # 0-100
    }

    # Weighted average
    weights = {
        "structural": 0.20,    # High impact, easy to fix
        "language": 0.25,      # Highest impact, moderate effort
        "reference": 0.20,     # Very high savings if applicable
        "examples": 0.15,      # Medium impact
        "disclosure": 0.10,    # Architectural principle
        "infuse": 0.10         # Quality framework
    }

    composite = sum(scores[dim] * weights[dim] for dim in scores)
    return composite, scores
```

**Rating Scale**:
- **90-100**: Excellent (token-optimized)
- **75-89**: Good (minor improvements possible)
- **60-74**: Fair (significant optimization opportunity)
- **40-59**: Poor (needs substantial revision)
- **<40**: Critical (complete rewrite recommended)

---

## 📈 Optimization Priority Matrix

### Priority 1: High Impact, Low Effort (Do First)

**Technique**: Remove filler words and passive voice
**Impact**: 10-20% reduction
**Effort**: Find-replace + light editing
**Time**: 30-60 minutes for 1,000-line file

**Technique**: Constraint statements over explanations
**Impact**: 20-40% reduction
**Effort**: Rewrite "why" sections as "what" requirements
**Time**: 1-2 hours for 1,000-line file

### Priority 2: High Impact, Medium Effort (Do Second)

**Technique**: Base pattern extraction
**Impact**: 1,140 tokens saved per agent
**Effort**: Extract common sections, update references
**Time**: 4-6 hours for initial extraction + 15 min per agent migration

**Technique**: Consolidate examples
**Impact**: 20-30% reduction
**Effort**: Move verbose examples to guides, keep 2-3 minimal
**Time**: 2-3 hours for 1,000-line file

### Priority 3: Medium Impact, Low Effort (Quick Wins)

**Technique**: Markdown-KV over tables
**Impact**: 47% reduction on table content
**Effort**: Convert tables to key-value format
**Time**: 15 minutes per table

**Technique**: Active voice conversion
**Impact**: 15-20% reduction
**Effort**: Rewrite passive constructions
**Time**: 1-2 hours for 1,000-line file

### Priority 4: Medium Impact, High Effort (Strategic)

**Technique**: Progressive disclosure restructuring
**Impact**: 3-4x efficiency
**Effort**: Reorganize content into 2-level hierarchy
**Time**: 1-2 days for major documentation suite

**Technique**: Multi-level compression (research agents)
**Impact**: 50:1 compression ratio
**Effort**: Implement compression protocols
**Time**: 1 week for full implementation

---

## 🔧 Automated Analysis Tools

### Quick Token Estimator

```bash
#!/bin/bash
# token-estimate.sh

FILE=$1
CHARS=$(wc -c < "$FILE")
LINES=$(wc -l < "$FILE")
WORDS=$(wc -w < "$FILE")

# Conservative estimate (1 token ≈ 4 characters)
TOKENS_CONSERVATIVE=$((CHARS / 4))

# Optimistic estimate (1 token ≈ 3.5 characters)
TOKENS_OPTIMISTIC=$(echo "scale=0; $CHARS / 3.5" | bc)

echo "File: $FILE"
echo "Characters: $CHARS"
echo "Lines: $LINES"
echo "Words: $WORDS"
echo "Estimated Tokens (conservative): $TOKENS_CONSERVATIVE"
echo "Estimated Tokens (optimistic): $TOKENS_OPTIMISTIC"
```

### Filler Word Detector

```python
# filler-word-detector.py

FILLER_WORDS = [
    "possibly", "really", "very", "actually", "basically",
    "essentially", "literally", "just", "simply", "clearly",
    "obviously", "of course", "in order to", "due to the fact that"
]

def detect_filler_words(text):
    violations = []
    for word in FILLER_WORDS:
        matches = re.finditer(r'\b' + word + r'\b', text, re.IGNORECASE)
        for match in matches:
            line_num = text[:match.start()].count('\n') + 1
            violations.append((line_num, word))
    return violations

def estimate_savings(violations):
    # Average filler word = 1.5 tokens
    return len(violations) * 1.5
```

### Duplicate Content Finder

```python
# duplicate-content-finder.py

from difflib import SequenceMatcher

def find_duplicate_blocks(files, min_length=100):
    """Find repeated content blocks across files."""
    duplicates = []

    for i, file1 in enumerate(files):
        for j, file2 in enumerate(files[i+1:], i+1):
            matcher = SequenceMatcher(None, file1.content, file2.content)
            for match in matcher.get_matching_blocks():
                if match.size >= min_length:
                    duplicates.append({
                        'file1': file1.path,
                        'file2': file2.path,
                        'size': match.size,
                        'content': file1.content[match.a:match.a + match.size]
                    })

    return duplicates

def calculate_reference_savings(duplicates, num_files):
    """Calculate potential savings from base pattern extraction."""
    total_duplicate_chars = sum(d['size'] for d in duplicates)
    reference_overhead = 20  # "**Extends**: base.md" ≈ 20 tokens

    savings = (total_duplicate_chars / 4) * (num_files - 1)
    overhead = reference_overhead * num_files
    net_savings = savings - overhead

    return {
        'total_duplicates': total_duplicate_chars,
        'potential_savings': savings,
        'reference_overhead': overhead,
        'net_savings': net_savings
    }
```

---

## 📊 Example Evaluation Report

```markdown
# Token Density Evaluation: CLAUDE.md

**File**: C:/Users/kemos/Repos/claude-code-starter-kit/CLAUDE.md
**Date**: 2025-10-31

## Base Metrics
- Characters: 23,264
- Lines: 533
- Words: 2,872
- Estimated Tokens: 5,816 (conservative)

## Six-Dimension Scores

| Dimension | Score | Grade | Issues |
|-----------|-------|-------|--------|
| Structural Efficiency | 75 | Good | 3 tables could be KV format |
| Language Efficiency | 65 | Fair | 25 filler words, 12 passive voice constructions |
| Reference Efficiency | 40 | Poor | No base pattern usage, scattered "See" references |
| Example Efficiency | 70 | Good | Some verbose explanations alongside examples |
| Progressive Disclosure | 80 | Good | 2-level structure present, clear navigation |
| INFUSE Alignment | 85 | Good | All components present, slightly over budget |

**Composite Score**: 69.25 / 100 (Fair)

## Optimization Opportunities

### High Priority (Est. 1,500-2,000 token savings)
1. Remove 25 filler words (38 tokens)
2. Convert 12 passive voice constructions (180 tokens)
3. Consolidate "See X for Y" references (300 tokens)
4. Constraint statements over explanations (800 tokens)

### Medium Priority (Est. 500-800 token savings)
5. Convert 3 tables to KV format (400 tokens)
6. Reduce verbose example explanations (300 tokens)

### Projected Impact
- Current: 5,816 tokens
- After optimization: 3,500-4,000 tokens
- **Savings**: 30-40% reduction (1,800-2,300 tokens)

## Recommended Actions
1. Apply Priority 1 optimizations (2-3 hours)
2. Re-evaluate composite score
3. If score ≥ 75, proceed to Priority 2
4. If score < 75, reassess structure
```

---

## 🎯 Target Metrics by Document Type

### Agent Definitions
- **Target**: 700-1,200 tokens
- **Structure**: INFUSE framework (6 components)
- **Inheritance**: Reference base-agent-pattern.md
- **Examples**: 2-3 maximum, minimal demonstration

### Orchestrator Instructions (CLAUDE.md)
- **Target**: 3,000-4,000 tokens
- **Structure**: Identity + OODA loop + quick references
- **Disclosure**: Level 1 (points to comprehensive guides)
- **Style**: Constraint-driven, formula-based, minimal prose

### Comprehensive Guides
- **Target**: 3,000-8,000 tokens
- **Structure**: Deep examples, anti-patterns, scenarios
- **Disclosure**: Level 2 (referenced from Level 1 docs)
- **Style**: Teaching-focused, example-heavy

### Templates/Schemas
- **Target**: 0 tokens (executable resources)
- **Structure**: Code, JSON, YAML (not loaded into context)
- **Disclosure**: Level 3 (executed via tools, not read)
- **Style**: Minimal comments, self-documenting

---

## 🔄 Continuous Improvement Process

### Weekly Review
1. Run token estimation on modified files
2. Flag files >target budget
3. Apply quick wins (filler words, active voice)

### Monthly Audit
1. Run duplicate content finder across agent suite
2. Identify base pattern extraction opportunities
3. Consolidate repeated sections

### Quarterly Optimization
1. Full six-dimension evaluation
2. Progressive disclosure restructuring if needed
3. INFUSE framework alignment review
4. MCP tool usage audit (remove unused tools)

---

**Version History**:
- v1.0.0 (2025-10-31): Initial framework with 6-dimension evaluation matrix

**References**:
- Anthropic Claude Documentation (prompt engineering)
- Context-Management-Best-Practices.md
- progressive-disclosure-ai-context-windows.md
- infuse-framework.md
- base-agent-pattern.md
