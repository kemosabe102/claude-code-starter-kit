# Progressive Disclosure: Modern Best Practices and Anthropic's Claude Code Skills Implementation

## Executive Summary

**What**: Progressive disclosure is a design pattern that defers advanced or rarely-used features to secondary screens, revealing information only when users need it. This reduces cognitive load and prevents overwhelming users with complexity.

**Why it matters**: Modern applications face exponential complexity growth. Progressive disclosure allows systems to maintain both simplicity for novices and power for experts by strategically revealing functionality based on context and user actions.

**Anthropic's innovation**: Claude Code Skills applies progressive disclosure principles to AI context window management, loading specialized knowledge dynamically rather than all at once. This prevents context overload while maintaining access to extensive capabilities.

---

## Modern Progressive Disclosure Best Practices (2015-2025)

### Core Implementation Principles

**1. User Research Over Designer Assumptions**

The most critical modern insight: designers consistently misjudge what users find important. Implement progressive disclosure based on data, not intuition.

Research methods:

- **Card sorting**: Users categorize features as basic, intermediate, or advanced
- **Task analysis**: Observe users performing actual workflows to identify pain points
- **Analytics**: Identify which features receive 80% of usage (candidates for primary display)
- **A/B testing**: Validate disclosure decisions with real user behavior

**Important caveat**: Analytics alone can mislead. Users might frequently visit a page due to confusion rather than need. Supplement quantitative data with qualitative observation.

**2. Limit Disclosure Depth to Maximum 2 Levels**

Research consistently shows designs exceeding two disclosure levels have low usability. Users get lost navigating between levels and abandon tasks.

If your design requires three or more levels:

- Simplify your information architecture
- Consolidate related features
- Re-evaluate whether "advanced" features belong in the interface at all

**3. Maintain Strong Information Scent**

Users must predict whether hidden content contains what they seek. Implement:

- **Descriptive labels**: "Shipping options" not just "More"
- **Visual affordances**: Clear expand icons, arrows, or "Show more" buttons
- **Preview hints**: Show first line of hidden content or number of hidden items
- **Consistent patterns**: Use same disclosure mechanisms throughout the interface

**4. Ensure Essential Features Remain Visible**

The cardinal sin of progressive disclosure: burying frequently-used functionality. This increases interaction cost unnecessarily and frustrates users.

Guidelines:

- Features used by >30% of users should be immediately visible
- Critical safety or security features must never hide
- One-click access to common actions (don't require menu navigation)

### Modern Design System Implementations

**Material Design (Google)**

- **Expansion panels**: Vertically stacked content with expand/collapse
- **Bottom sheets**: Contextual actions sliding from screen bottom
- **Navigation drawers**: Hidden primary navigation (use sparingly)
- **Steppers**: Multi-step workflows with clear progression

**Apple Human Interface Guidelines**

- **Disclosure controls**: Expand/collapse with clear chevron indicators
- **Action sheets**: Context-specific options appearing on demand
- **Popovers (iPad)**: Contextual information without full navigation
- **Modal presentations**: Focused tasks requiring user attention

**GitHub Primer Design System**
Distinguishes three progressive disclosure types:

- **Chevron icons**: For collapsed/expandable content sections
- **Ellipsis icons**: For truncated inline text with "show more"
- **Kebab menus**: For dropdown actions (three vertical dots)

Warning from Primer: "Be mindful of interactions that drastically change the user's focus or the surrounding context."

### Common Anti-Patterns to Avoid

**1. Burying Essential Functionality**

- Example: Hiding "Save" in a sub-menu when users need it constantly
- Result: Increased interaction cost, user frustration, task abandonment

**2. Multiple Access Paths to Same Information**

- Example: Settings accessible from three different menu locations
- Result: User confusion about "correct" navigation, inconsistent mental models

**3. Poor Discoverability Indicators**

- Example: No visual cue that additional options exist
- Result: Advanced features effectively non-existent, frustrated power users

**4. Oversimplification**

- Example: Hiding all advanced features with no access path
- Result: Software appears shallow, lacks perceived depth

**5. Vague Labeling**

- Example: Generic "Advanced" or "More" buttons without context
- Result: Exploratory clicking, uncertain navigation, wasted time

### Mobile-First Progressive Disclosure Patterns

**Bottom Navigation vs. Hamburger Menus**

The 2010s taught a hard lesson: hamburger menus save space but severely damage discoverability. Modern consensus:

- **Primary navigation (3-5 items)**: Bottom tabs (always visible)
- **Secondary features**: Hamburger or profile menu
- **Context-specific actions**: Bottom sheets or action sheets

**Gesture-Based Disclosure**

Mobile interfaces leverage interaction patterns:

- **Swipe to reveal**: Hidden actions in email (delete, archive, flag)
- **Pull-to-refresh**: Disclosure through motion rather than visible controls
- **Long-press**: Additional keyboard characters, contextual menus
- **Pinch/zoom**: Progressive detail levels for maps, photos, documents

**Progressive Enhancement by Screen Size**

Responsive design inherently implements progressive disclosure:

- **Mobile**: Essential content only, aggressive hiding of secondary features
- **Tablet**: Contextual information in sidebars, popovers
- **Desktop**: Full feature set visible, multiple simultaneous panels

### Contemporary Application Examples

**Instagram**

- **Primary**: Content feed, camera, direct messages (always visible)
- **Secondary**: Profile, settings, activity (hamburger menu)
- **Tertiary**: Advanced settings, data management (nested menus)

**Amazon Product Pages**

- **Immediate**: Price, main image, primary specifications, Add to Cart
- **Tabbed**: Detailed descriptions, reviews, Q&A
- **Accordion**: Shipping details, warranty information, product specifications
- **Scrolling**: Related products, recommendations, browsing history

**Slack**

- **Primary**: Channel list, current conversation, compose (always visible)
- **Secondary**: Workflows, apps, custom settings (sidebar)
- **Tertiary**: Advanced preferences, integrations (settings panels)

**Dropbox File Sharing**

- **Primary**: Email field, Share button (main interface)
- **Secondary**: Permissions, expiration, password (Settings button)
- **Recognition**: Most users need simple sharing; power users access full control

---

## Anthropic's Claude Code Skills: Progressive Disclosure for AI

### The Context Window Challenge

Large language models face a fundamental constraint: **limited context windows**. Claude's 200,000 token window seems vast but fills quickly with:

- System prompts and instructions
- Conversation history
- Tool definitions and documentation
- Reference materials and examples
- Working memory for current tasks

Traditional approaches like Model Context Protocol (MCP) load all capabilities at initialization. A GitHub MCP server alone consumes tens of thousands of tokens, limiting users to 2-3 MCP servers before context exhaustion degrades accuracy.

### Skills Architecture: Three-Tier Progressive Disclosure

**Level 1: Metadata Scanning (Minimal Load)**

At session startup, Claude scans all available skills but loads only YAML frontmatter:

```yaml
---
name: docx
description: Comprehensive document creation, editing, and analysis with support for tracked changes, comments, formatting preservation, and text extraction.
---
```

Resource consumption: **~100 tokens per skill** regardless of total size

With 200,000 token context window:

- Support for **2,000 skills** using only 10% of context
- Enough information for relevance determination
- Zero detailed instruction loading until needed

**Level 2: Full Skill Loading (On-Demand)**

When a task matches a skill's description, Claude loads the complete SKILL.md file containing:

- Detailed instructions and workflows
- Step-by-step procedures
- Usage examples and edge cases
- References to additional resources
- Integration guidelines

Best practice: Keep SKILL.md under **500 lines** for optimal performance

**Level 3+: Dynamic Resource Access (As-Needed)**

SKILL.md references additional files that Claude loads only when specifically required:

- Reference documentation
- Domain-specific guides
- Validation rules and schemas
- Executable scripts and tools

**Critical optimization**: Executable scripts run via bash without loading contents into context. A 500-line script consumes **zero tokens** during execution; only output enters context window.

Anthropic's statement: "The amount of context that can be bundled into a skill is effectively unbounded" because agents with filesystem and code execution tools don't need to read entire skills into context.

### Implementation Details

**Skill Structure**

```
/skill-name/
├── SKILL.md              # Main instructions (Level 2)
├── examples/             # Reference materials (Level 3+)
│   ├── example1.docx
│   └── example2.docx
├── scripts/              # Executable tools (Level 3+)
│   ├── convert.py
│   └── validate.sh
└── references/           # Domain documentation (Level 3+)
    └── specification.md
```

**SKILL.md Format**

```markdown
---
name: skill-name
description: Brief description for relevance matching
---

# Skill Name

## When to Use This Skill

[Clear triggers for skill activation]

## Core Capabilities

[What this skill enables]

## Implementation Guidelines

[Step-by-step instructions]

## Examples

[Concrete usage patterns]

## Additional Resources

[References to files in skill directory]
```

**Autonomous Loading Logic**

Claude determines skill relevance through:

1. **Semantic matching**: User request keywords vs. skill descriptions
2. **Task context**: Current conversation and goals
3. **Capability requirements**: Needed tools and knowledge
4. **Dependency resolution**: Loading related skills automatically

Users never manually select skills. Claude's internal reasoning process determines appropriate loads based on task requirements.

### Performance Impact: Skills vs. Traditional Approaches

**Context Consumption Comparison**

Traditional MCP approach:

- GitHub server: ~15,000 tokens
- Filesystem server: ~8,000 tokens
- Database server: ~12,000 tokens
- **Total: 35,000 tokens** (17.5% of context window)
- **Maximum: 2-3 servers** before accuracy degradation

Skills approach:

- 50 skills metadata: ~5,000 tokens
- 1 active skill loaded: ~3,000 tokens
- **Total: 8,000 tokens** (4% of context window)
- **Reduction: 3-4x lower consumption**

**Accuracy Benefits**

Less context competition means:

- Higher tool-use accuracy (fewer options to confuse)
- Better task focus (only relevant capabilities present)
- Reduced hallucination (less information to misinterpret)
- Faster response times (less content to process)

### Production Validation

**Anthropic's Internal Usage**

- **90% of Claude Code itself** was written using Claude Code with Skills
- Document creation features (Excel, PowerPoint, Word, PDF) entirely implemented via Skills
- Internal teams report **67% productivity gains**

**Key Advantages Observed**

1. **Dynamic Specialization**
   - Start with general-purpose model
   - Add domain expertise via Skills
   - Become specialist for specific tasks
   - Revert to generalist for other tasks
   - No fine-tuning or RAG infrastructure required

2. **Composability Without Interference**
   - Multiple skills can be available simultaneously
   - Each loads independently based on need
   - Claude coordinates usage automatically
   - No context window conflicts

3. **Radical Simplicity**
   - Markdown files in directory structures
   - No special protocols required
   - Human-readable and debuggable
   - Easy to create, share, and modify

### Comparison: UI/UX Progressive Disclosure vs. AI Skills

**Similarities**

| Aspect                    | Traditional UI                     | Claude Skills                         |
| ------------------------- | ---------------------------------- | ------------------------------------- |
| **Information hierarchy** | Essential → Advanced → Rarely used | Metadata → Instructions → References  |
| **Novice benefits**       | Reduced overwhelming options       | Simplified initial capability set     |
| **Expert benefits**       | Quick access to power features     | Full capability without context bloat |
| **Resource management**   | Screen space, human attention      | Token budget, context window          |

**Critical Difference: Agency**

- **Traditional UI**: Human users explicitly request information through clicks, expansions, and navigation
- **Claude Skills**: AI agent autonomously determines what to load based on semantic task understanding

This autonomous loading represents a fundamental innovation—the system itself decides optimal information revelation without user intervention.

### Best Practices for Creating Skills

**1. Write Clear, Specific Descriptions**

The description determines when Claude loads your skill. Make it:

- Semantically rich with relevant keywords
- Specific about capabilities and use cases
- Concise (under 200 characters ideal)

Poor: "Helps with documents"
Good: "Create, edit, and analyze Word documents with tracked changes, comments, and formatting preservation"

**2. Structure Instructions Hierarchically**

Mirror progressive disclosure in your SKILL.md:

- Start with "When to Use This Skill" (helps Claude's relevance matching)
- Core capabilities (what user gets)
- Step-by-step instructions (how to execute)
- Edge cases and advanced usage (on-demand reading)
- References to external files (Level 3+ resources)

**3. Keep SKILL.md Focused**

Target **500 lines or less** for optimal performance:

- Essential instructions in SKILL.md
- Examples in separate files (loaded on demand)
- Large reference materials as external resources
- Scripts as executable files (never loaded, only run)

**4. Use Executable Scripts Strategically**

Scripts provide unlimited capability without context cost:

- Data transformation and validation
- External API calls
- Complex computations
- File format conversions

Remember: Script contents never enter context window, only outputs.

**5. Test Skill Discoverability**

Ask Claude to perform tasks **without mentioning the skill name**:

- Does Claude correctly identify when to use the skill?
- Are triggering keywords in the description effective?
- Does task phrasing naturally map to skill description?

If Claude misses obvious use cases, improve your description's semantic matching.

---

## Key Takeaways

**Progressive Disclosure Fundamentals**

1. **Base decisions on user research**, not designer intuition
2. **Limit disclosure to maximum 2 levels** to prevent navigation confusion
3. **Maintain strong information scent** so users predict hidden content
4. **Never bury essential functionality** used by >30% of users

**Modern Implementation**

- Mobile-first design inherently requires progressive disclosure
- Gesture-based patterns (swipe, long-press) enable space-efficient disclosure
- Design systems (Material, HIG, Primer) provide tested, accessible components
- Context-specific disclosure (bottom sheets, action sheets) outperforms global hiding

**Anthropic's Innovation**

- Progressive disclosure applies to **any system with limited resources**—human attention or AI context windows
- Three-tier architecture (metadata → instructions → resources) scales to unlimited knowledge
- Autonomous loading by AI agent represents fundamental advancement over user-directed disclosure
- Production results validate approach: 3-4x context efficiency, 67% productivity gains

**Universal Principle**

Whether managing human cognitive load or AI token budgets, the core insight remains: **reveal information strategically based on context and need**. Progressive disclosure transforms overwhelming complexity into manageable progression, maintaining both simplicity for newcomers and power for experts.
