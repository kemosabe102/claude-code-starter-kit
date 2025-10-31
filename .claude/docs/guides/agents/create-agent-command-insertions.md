# /create-agent Command File Insertions

**Purpose**: Specific text blocks to insert into `.claude/commands/create-agent.md` for interactive mode support.

**Implementation**: Copy-paste each section into the specified locations.

---

## 1. Arguments Section Update (Replace Lines 3-7)

**Location**: `.claude/commands/create-agent.md` lines 3-7

**Replace**:
```yaml
arguments:
  - name: agent-definition-file
    description: Path to agent definition file (required)
    required: true
    type: path
```

**With**:
```yaml
arguments:
  - name: agent-definition-file
    description: Path to agent definition file (optional if using --create-definition)
    required: false
    type: path
  - name: --create-definition
    description: Interactive mode to create agent definition from idea (output path required)
    required: false
    type: path
    example: /create-agent --create-definition my-agent-definition.md
```

---

## 2. Command Usage Section Addition (After Line 89)

**Location**: `.claude/commands/create-agent.md` after line 89 (after existing usage examples)

**Insert**:
```markdown

### Interactive Mode (NEW)

**Purpose**: Create agent definition interactively from a simple idea without needing to understand the complete template structure.

**Usage**:
```bash
# Interactive definition creation only
/create-agent --create-definition path/to/my-agent-definition.md

# Interactive with context directory
/create-agent --create-definition my-agent.md --context-dir=docs/security/

# Interactive with dry-run (preview without creating agent)
/create-agent --create-definition my-agent.md --dry-run
```

**Workflow**:
1. User provides 2-3 sentence idea
2. agent-architect analyzes and proposes structure
3. Interactive Q&A refines proposal
4. Definition file generated
5. User chooses: proceed immediately, review first, or regenerate

**Time**: 5-10 minutes (vs. 30-60 minutes manual template filling)

**See**: `.claude/docs/guides/interactive-agent-definition-workflow.md` for complete workflow specification.
```

---

## 3. Input File Template Section Update (After Line 106)

**Location**: `.claude/commands/create-agent.md` after line 106 (after "Input File Template" section)

**Insert**:
```markdown

### Creating Definition Files

**Option 1: Interactive Mode** (Recommended for first-time users)
```bash
/create-agent --create-definition my-agent.md
```
- Guided Q&A from simple idea to complete definition
- No need to study template structure beforehand
- Confidence-scored recommendations
- Automatic proposal generation

**Option 2: Manual Template Filling** (For experienced users)
- Copy `.claude/templates/agent-definition-input.template.md`
- Fill out all sections manually
- Requires understanding of template structure
- More control, but higher time investment
```

---

## 4. New Section: Interactive Workflow (Before Line 109)

**Location**: `.claude/commands/create-agent.md` before line 109 (before "Multi-Phase Workflow")

**Insert**:
```markdown

---

## Interactive Agent Definition Creation (NEW)

**When to Use**: Creating a new agent without prior knowledge of template structure.

**Entry Point**: `/create-agent --create-definition output.md`

**5-Phase Interactive Workflow**:

### Phase 1: Capture User Idea
- **Goal**: Extract core agent concept in 2-3 sentences
- **User Action**: Describe what problem agent solves, what it does, when to call it
- **Time**: 1-2 minutes

### Phase 2: Analyze Idea & Propose Structure
- **Goal**: Transform informal idea into structured proposal
- **Delegation**: agent-architect (analyze_agent_idea operation)
- **Output**: Confidence-scored recommendations for:
  - Agent name options (2-3 choices)
  - Domain scope (directory boundaries)
  - Agent type (Creator/Reviewer/Enhancer/etc.)
  - Purpose statement (orchestrator description)
  - Core capabilities (4-6 items)
  - Expected inputs/outputs
  - Domain knowledge areas
  - Tool recommendations
  - Integration points
- **Time**: 10-15 seconds

### Phase 3: Interactive Refinement
- **Goal**: Walk through proposal with user Q&A
- **Interaction**: User accepts, modifies, or provides custom values for each section
- **Patterns**:
  - Name: Choose from 3 options or provide custom
  - Domain/Type: Accept or specify different
  - Purpose: Accept or provide improved version
  - Lists (capabilities, tools): Accept, add, remove, or edit items
- **Time**: 3-5 minutes

### Phase 4: Generate Definition File
- **Goal**: Create complete agent definition file
- **Delegation**: agent-architect (generate_agent_definition operation)
- **Input**: Refined requirements from Phase 3
- **Output**: Agent definition file at specified path
- **Template**: `.claude/templates/agent-definition-input.template.md`
- **Time**: 5-10 seconds

### Phase 5: Present Completion & Options
- **Goal**: Offer next steps to user
- **Options**:
  1. **Proceed immediately** - Run standard 10-phase workflow now (10-15 min)
  2. **Review first** - Exit, user manually runs `/create-agent definition.md` later
  3. **Regenerate** - Return to Phase 3 with different answers
- **Output**: File preview (first 30 lines) and clear action options
- **Time**: 1 minute

**After Interactive Workflow**:
- If user chooses Option 1: Proceeds to standard 10-phase workflow (below)
- If user chooses Option 2: Command completes, definition file saved
- If user chooses Option 3: Returns to Phase 3 for refinement

**Complete Specification**: `.claude/docs/guides/interactive-agent-definition-workflow.md`

---

## Standard Agent Creation Workflow (Existing)

**When to Use**: Creating agent from existing definition file (manual or interactive output).

**Entry Point**: `/create-agent path/to/agent-definition.md`

**10-Phase Workflow** (Unchanged):
```

---

## 5. Agent Assignment Summary Addition (After Line 1089)

**Location**: `.claude/commands/create-agent.md` after line 1089 (end of Agent Assignment Summary table)

**Insert**:
```markdown

### Interactive Mode Agent Assignments

| Phase | Task | Agent | Rationale |
|-------|------|-------|-----------|
| 1 | Capture user idea | Orchestrator | Simple text collection, no delegation needed |
| 2 | Analyze idea | agent-architect | Agent expertise, structured analysis, confidence scoring |
| 2 | Propose structure | agent-architect | Agent design patterns, recommendation generation |
| 3 | Interactive refinement | Orchestrator | User interaction, choice collection, Q&A flow |
| 4 | Generate definition file | agent-architect | Template application, file generation, validation |
| 5 | Present completion | Orchestrator | User communication, option handling, transition to standard workflow |

**Note**: After Phase 5 (if user chooses "proceed immediately"), workflow continues with standard 10-phase agent creation.
```

---

## 6. Error Handling Section Addition (After Line 1120)

**Location**: `.claude/commands/create-agent.md` after line 1120 (after existing "Error Handling" section)

**Insert**:
```markdown

### Interactive Mode Error Handling

**Vague User Idea (Phase 1)**:
- Re-prompt with guidance: "What, How, When" framework
- Provide examples of good vs. vague ideas
- Max 3 retry attempts before suggesting manual template

**agent-architect Analysis Failure (Phase 2)**:
- Extract `missing_information` from `failure_details`
- Re-prompt user for specific clarifications
- Offer options: Rephrase idea, Provide more detail, or Cancel

**agent-architect Generation Failure (Phase 4)**:
- Show `failure_details.reasons` to user
- Offer options: Retry generation, Return to refinement (Phase 3), or Cancel

**File System Errors (Phase 4/5)**:
- Output path exists: Offer overwrite, rename, or cancel
- Write permission error: Request new writable path or cancel
- Invalid path format: Validate and suggest corrections

**User Confusion During Refinement (Phase 3)**:
- Provide inline help text for each section
- Offer "skip for now" option for optional sections
- Allow return to previous section
```

---

## 7. agent-architect Operation Documentation (New Section Before Line 1142)

**Location**: `.claude/commands/create-agent.md` before line 1142 (before "Related Documentation")

**Insert**:
```markdown

---

## agent-architect New Operations

### analyze_agent_idea (Phase 2)

**Purpose**: Analyze user's informal agent idea and generate structured proposal with confidence-scored recommendations.

**Input**:
```json
{
  "operation_type": "analyze_agent_idea",
  "task_id": "uuid",
  "description": "Analyze user idea and propose agent structure",
  "agent_idea_analysis": {
    "user_idea_text": "2-3 sentence description from user",
    "analysis_depth": "comprehensive"
  },
  "execution_timestamp": "2025-10-22T10:30:00Z"
}
```

**Output**: Structured proposal with 10 sections (name options, domain scope, agent type, purpose, capabilities, inputs, outputs, knowledge areas, tools, integration points). All recommendations include confidence scores (0.0-1.0) and rationale.

**Time**: 10-15 seconds

---

### generate_agent_definition (Phase 4)

**Purpose**: Generate complete agent definition file from refined requirements using official template.

**Input**:
```json
{
  "operation_type": "generate_agent_definition",
  "task_id": "uuid",
  "description": "Generate agent definition file",
  "definition_generation": {
    "output_path": "path/to/agent-definition.md",
    "refined_requirements": {
      "name": "agent-name",
      "domain": "packages/**",
      "type": "Analyzer",
      "purpose": "Orchestrator description",
      "capabilities": ["capability 1", "capability 2", ...],
      "inputs": [{...}],
      "success_output": "Description",
      "failure_output": "Description",
      "knowledge_areas": [{...}],
      "tools": [{...}],
      "integration_points": {...},
      "original_idea": "User's original 2-3 sentences"
    }
  },
  "execution_timestamp": "2025-10-22T10:35:00Z"
}
```

**Output**: Agent definition file at specified path following `.claude/templates/agent-definition-input.template.md` structure.

**Time**: 5-10 seconds

**Schema Updates**: See `.claude/docs/schemas/agent-architect.schema.json` for complete input/output schemas.

```

---

## 8. Related Documentation Update (Line 1142)

**Location**: `.claude/commands/create-agent.md` line 1142 (Related Documentation section)

**Add to list**:
```markdown
- **Interactive Workflow Spec**: `.claude/docs/guides/interactive-agent-definition-workflow.md`
- **Interactive Mode Addendum**: `.claude/docs/guides/create-agent-interactive-mode-addendum.md`
```

---

## Implementation Order

1. **Update arguments** (Section 1) - Makes flag available
2. **Add usage examples** (Section 2) - Documents new usage
3. **Update template section** (Section 3) - Explains both options
4. **Insert interactive workflow** (Section 4) - Complete Phase 1-5 spec
5. **Add agent assignments** (Section 5) - Documents delegation pattern
6. **Add error handling** (Section 6) - Edge case handling
7. **Add operations docs** (Section 7) - agent-architect new operations
8. **Update related docs** (Section 8) - Cross-references

---

## Validation Checklist

After insertions, verify:
- [ ] Arguments section includes both modes (standard + interactive)
- [ ] Usage examples cover all combinations (interactive, dry-run, context-dir)
- [ ] Interactive workflow (5 phases) clearly separated from standard workflow (10 phases)
- [ ] Agent assignment table includes interactive mode rows
- [ ] Error handling covers interactive-specific failure modes
- [ ] agent-architect operations documented with schemas
- [ ] Related documentation cross-references complete
- [ ] Line numbers updated if sections shifted

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-22
**Status**: Ready for Implementation
