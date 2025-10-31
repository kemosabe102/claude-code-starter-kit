# /create-agent Interactive Mode Addendum

**Purpose**: Summary document for adding interactive agent definition creation (`--create-definition` flag) to the `/create-agent` command.

**Full Specification**: See `.claude/docs/guides/interactive-agent-definition-workflow.md` for complete workflow details.

---

## Command Signature Changes

### Updated Arguments Section

Insert into `.claude/commands/create-agent.md` after line 3:

```yaml
arguments:
  - name: agent-definition-file
    description: Path to agent definition file (optional if using --create-definition)
    required: false  # CHANGED FROM: true
    type: path

  - name: --create-definition
    description: Interactive mode to create agent definition from idea (output path required)
    required: false
    type: path
    example: /create-agent --create-definition my-agent-definition.md

  # ... existing flags remain unchanged ...
```

---

## Usage Examples Update

Insert into `.claude/commands/create-agent.md` Command Usage section (after line 72):

```bash
# NEW: Interactive definition creation
/create-agent --create-definition path/to/my-agent-definition.md

# Existing: Create agent from definition file
/create-agent path/to/agent-definition.md

# Combined: Interactive + context
/create-agent --create-definition security-agent.md --context-dir=docs/security/

# Combined: Interactive + dry-run preview
/create-agent --create-definition security-agent.md --dry-run
```

---

## Workflow Overview

### Interactive Mode (NEW - Phases 1-5)

**When**: User runs `/create-agent --create-definition output.md`

**Phases**:
1. **Capture User Idea** - Collect 2-3 sentence description
2. **Analyze Idea** - Delegate to agent-architect for structured proposal
3. **Interactive Refinement** - Walk through proposal sections with Q&A
4. **Generate Definition File** - Delegate to agent-architect for file creation
5. **Present Completion** - Offer options: proceed immediately, review first, or regenerate

**Output**: Complete agent definition file at specified path, ready for standard workflow

**Time**: 5-10 minutes (vs. 30-60 minutes manual template filling)

---

### Standard Mode (Existing - Phases 1-10)

**When**: User runs `/create-agent path/to/agent-definition.md` (definition already exists)

**Phases**: Existing 10-phase workflow unchanged

**Time**: 10-15 minutes

---

## Integration Logic

### Command Entry Point

```python
def execute_create_agent_command(args):
    """
    Handle both interactive and standard modes.
    """

    # Check for interactive mode flag
    if args.get('--create-definition'):
        output_path = args['--create-definition']

        # Run interactive definition workflow (Phases 1-5)
        result = run_interactive_workflow(output_path)

        # Handle user choice from Phase 5
        if result.user_choice == "proceed_immediately":
            # Option 1: Continue to standard workflow
            definition_file = output_path
            # Fall through to standard workflow below

        elif result.user_choice == "review_first":
            # Option 2: Exit, user will run manually later
            return SUCCESS

        elif result.user_choice == "regenerate":
            # Option 3: Already handled by workflow loop
            return SUCCESS

    else:
        # Standard mode: definition file provided
        definition_file = args['agent-definition-file']

    # Execute standard 10-phase workflow (unchanged)
    return execute_standard_workflow(definition_file, **args)
```

---

## agent-architect Operation Updates

### New Operations (Add to Schema)

**`analyze_agent_idea`** (Phase 2):
- **Input**: `user_idea_text` (2-3 sentences)
- **Output**: Structured proposal with confidence-scored recommendations
- **Sections**: Name options, domain scope, agent type, purpose, capabilities, inputs, outputs, knowledge areas, tools, integration points

**`generate_agent_definition`** (Phase 4):
- **Input**: `refined_requirements` (from user refinement), `output_path`
- **Output**: Complete agent definition file following template structure
- **Template**: `.claude/templates/agent-definition-input.template.md`

### Schema Changes

Add to `.claude/docs/schemas/agent-architect.schema.json`:

```json
{
  "operation_type": {
    "enum": [
      "create_agent",
      "evaluate_agent",
      "implement_feedback",
      "update_agent",
      "create_design_guide",
      "validate_workflow",
      "update_maturity",
      "analyze_agent_idea",        // NEW
      "generate_agent_definition"  // NEW
    ]
  }
}
```

**Full schema structures**: See `.claude/docs/guides/interactive-agent-definition-workflow.md` Section "Schema Updates" for complete input/output schemas.

---

## Phase Breakdown (Quick Reference)

### Phase 1: Capture User Idea
- **Actor**: Orchestrator
- **Action**: Prompt user for 2-3 sentence idea
- **Output**: `user_idea_text`
- **Time**: 1-2 minutes

### Phase 2: Analyze Idea & Propose Structure
- **Actor**: agent-architect (analyze_agent_idea)
- **Action**: Generate structured proposal with confidence scores
- **Output**: `agent_proposal` (10 sections)
- **Time**: 10-15 seconds

### Phase 3: Interactive Refinement
- **Actor**: Orchestrator
- **Action**: Walk through each proposal section with user Q&A
- **Output**: `refined_requirements`
- **Time**: 3-5 minutes

### Phase 4: Generate Definition File
- **Actor**: agent-architect (generate_agent_definition)
- **Action**: Create definition file from refined requirements
- **Output**: Agent definition file at `output_path`
- **Time**: 5-10 seconds

### Phase 5: Present Completion & Options
- **Actor**: Orchestrator
- **Action**: Show preview, offer 3 options (proceed/review/regenerate)
- **Output**: User choice (proceed immediately, review first, or regenerate)
- **Time**: 1 minute

---

## Example Session (Abbreviated)

```
User: /create-agent --create-definition security-scanner.md

Orchestrator: Let's create your agent definition!

Describe your agent idea in 2-3 sentences:

User: I want an agent that scans Python code for security vulnerabilities
using Semgrep. It should run before commits and catch SQL injection and XSS.

Orchestrator: [Delegates to agent-architect for analysis...]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AGENT NAME OPTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. security-scanner (confidence: 0.95)
   Rationale: Clear domain + action pattern
2. sast-analyzer (confidence: 0.80)
3. vulnerability-detector (confidence: 0.70)

Which name? (1/2/3 or custom)

User: 1

[... continues through domain, type, purpose, capabilities, etc. ...]

Orchestrator: Definition file created!

What would you like to do?
1. Proceed with agent creation NOW (10-15 min)
2. Review/edit definition first
3. Regenerate with different answers

User: 1

Orchestrator: Starting agent creation workflow...
[Proceeds to standard 10-phase workflow]
```

---

## Error Handling

### Vague User Idea
```
If idea lacks specifics:
- Re-prompt with guidance on what, how, when
- Provide examples of good ideas
- Max 3 retry attempts before suggesting manual template
```

### agent-architect Analysis Failure
```
If analyze_agent_idea returns FAILURE:
- Extract missing_information from failure_details
- Re-prompt user for specific clarifications
- Option to rephrase idea or cancel
```

### agent-architect Generation Failure
```
If generate_agent_definition returns FAILURE:
- Show failure_details.reasons
- Offer: Retry, Return to refinement (Phase 3), or Cancel
```

### File System Errors
```
Output path exists: Offer overwrite, rename, or cancel
Write permission error: Request new path or cancel
```

---

## Success Metrics

| Metric | Target | Comparison |
|--------|--------|------------|
| Time to Definition | 5-10 min | vs. 30-60 min manual |
| User Input Required | 2-3 sentences + Q&A choices | vs. Complete template knowledge |
| Template Compliance | 100% (generated) | vs. ~70% manual (common errors) |
| Confidence Scoring | All recommendations | vs. None (manual guesswork) |
| Barrier to Entry | Minimal (idea only) | vs. High (template mastery) |

---

## Documentation Cross-References

- **Full Workflow Spec**: `.claude/docs/guides/interactive-agent-definition-workflow.md`
- **Standard Workflow**: `.claude/commands/create-agent.md` (existing Phases 1-10)
- **Input Template**: `.claude/templates/agent-definition-input.template.md`
- **Agent Template**: `.claude/templates/agent.template.md`
- **Schema Updates**: `.claude/docs/schemas/agent-architect.schema.json`

---

## Implementation Checklist

**Command File Updates**:
- [ ] Update arguments section (make agent-definition-file optional)
- [ ] Add --create-definition flag documentation
- [ ] Add usage examples for interactive mode
- [ ] Update command entry logic to handle both modes

**agent-architect Updates**:
- [ ] Add analyze_agent_idea operation implementation
- [ ] Add generate_agent_definition operation implementation
- [ ] Update schema with new operation types
- [ ] Add confidence scoring for all recommendations

**Testing**:
- [ ] Test interactive workflow with various idea complexities
- [ ] Test error handling (vague ideas, failures, file errors)
- [ ] Test all 3 completion options (proceed/review/regenerate)
- [ ] Test integration with standard workflow (Option 1)
- [ ] Validate generated definition files match template structure

---

**Document Version**: 1.0.0
**Last Updated**: 2025-10-22
**Status**: Ready for Implementation
