# Research Coordination Patterns

**Purpose**: Orchestrator-to-researcher-lead delegation patterns and iterative research workflows.

---

## Orchestrator-to-researcher-lead Invocation Pattern

**Purpose**: Clear invocation pattern to ensure researcher-lead returns plans, not executes research

### Phase 1: Initial Research Planning

**Orchestrator invokes**:
```
Task(
  agent="researcher-lead",
  prompt="CREATE A RESEARCH PLAN for [objective]"  ← KEY PHRASE
)
```

**researcher-lead returns**:
```json
{
  "delegation_plans": [
    {"worker_type": "researcher-web", "specific_objective": "...", ...},
    {"worker_type": "researcher-codebase", "specific_objective": "...", ...}
  ]
}
```

**Orchestrator then spawns workers IN PARALLEL**:
```
Single message with multiple Task calls:
- Task(agent="researcher-web", prompt="...")
- Task(agent="researcher-codebase", prompt="...")
```

### Phase 2: Follow-Up Planning (if needed)

**Orchestrator detects gaps**:
- Worker confidence < 0.85
- Unanswered open_questions

**Orchestrator invokes researcher-lead AGAIN**:
```
Task(
  agent="researcher-lead",
  prompt="CREATE FOLLOW-UP RESEARCH PLAN to address [gaps_summary]"
)
```

**researcher-lead returns**:
```json
{"delegation_plans": [...]}  ← Targeted, 1-3 workers
```

**Orchestrator spawns targeted workers**

### Anti-Pattern (Don't Do This)

```
❌ WRONG: "Investigate feature 005 readiness"
→ researcher-lead will execute research instead of planning (99.4k tokens, 3m 53s)

✅ CORRECT: "CREATE A RESEARCH PLAN for investigating feature 005 readiness"
→ researcher-lead returns delegation plan (5-10k tokens, <30s)
→ Orchestrator spawns workers from plan
→ Workers execute research in parallel (2-3 minutes total)
```

**Key Insights**:
- Phrase matters: "CREATE A RESEARCH PLAN" triggers planning mode, "Investigate" triggers execution mode
- researcher-lead returns PLANS, orchestrator SPAWNS workers
- Orchestrator SYNTHESIZES results after workers complete
- Iteration: Call researcher-lead again with gaps if needed

---

## Iterative Research Workflow

**Purpose**: Enable multi-round research when initial findings are incomplete

### Worker Capabilities (v2.0 - all researchers support iteration)

- **researcher-web**: Returns `open_questions` and `confidence_breakdown` with low_confidence_rationale
- **researcher-codebase**: Returns `open_questions` and `confidence_breakdown` with code-specific factors
- **researcher-library**: Returns `open_questions` and `confidence_breakdown` for documentation gaps

**Iteration Trigger Threshold**: Individual worker confidence < 0.85 OR unanswered open_questions

### Orchestrator Iteration Logic

**1. Initial Research Phase**:
- Orchestrator calls researcher-lead for initial plan
- researcher-lead returns delegation plan (Phase 1-5)
- Orchestrator spawns workers based on plan

**2. Worker Result Analysis (NEW)**:
```
FOR each completed worker:
  - Check individual confidence score
  - IF confidence < 0.85:
      → Record gap: worker_id + low_confidence_rationale
  - Check open_questions
  - FOR each question:
      → Cross-check: Did any other worker answer this?
      → IF unanswered: Record gap: question + suggested_approach
```

**3. Iteration Decision**:
```
IF gaps_summary is not empty:
  - Orchestrator calls researcher-lead AGAIN (Phase 6: Follow-Up Planning)
  - Pass gaps_summary (NOT full worker results - token efficient)
  - researcher-lead returns targeted follow-up plan (1-3 workers)
  - Orchestrator spawns follow-up workers
  - REPEAT steps 2-3 until:
      * All workers confidence >= 0.85 AND
      * All open_questions answered OR
      * Max iterations reached (default: 3)
ELSE:
  - Research complete, synthesize all findings
```

**4. Final Synthesis**:
- Combine findings from all rounds
- Return comprehensive answer to user

### Key Design Principles

- **Orchestrator-driven**: Orchestrator checks individual results and decides iteration
- **Stateless planning**: researcher-lead called multiple times, doesn't retain state
- **Token-efficient**: Only gap summaries sent to researcher-lead, not full worker results
- **Individual thresholds**: Each worker evaluated independently (not aggregated confidence)
- **Targeted follow-up**: Follow-up plans address specific gaps with 1-3 workers

### Example Flow

**Round 1**:
```
User: "Research async validation patterns in Pydantic v2"
→ researcher-lead creates plan (3 workers: web, codebase, library)
→ Orchestrator spawns workers
→ researcher-web returns confidence 0.72 + open_question: "async nested models?"
→ researcher-codebase returns confidence 0.88 (no iteration needed)
→ researcher-library returns confidence 0.90 (no iteration needed)
```

**Orchestrator Detects**:
```
researcher-web: confidence < 0.85 AND unanswered question
→ gaps_summary: ["Low confidence: async patterns (0.72)", "Unanswered: async nested models"]
```

**Round 2**:
```
→ Orchestrator calls researcher-lead with gaps_summary
→ researcher-lead creates targeted follow-up (1 worker: researcher-library for official docs)
→ Orchestrator spawns researcher-library (targeted)
→ researcher-library returns confidence 0.92 + answers nested models question
```

**Orchestrator Checks**:
```
All workers confidence >= 0.85: ✓
All open_questions answered: ✓
→ Research complete, synthesize Round 1 + Round 2 findings
```

### Performance Impact

- Initial research: Same as before (10-15 minutes typical)
- Follow-up research: 2-5 minutes per round (targeted, not full re-research)
- Total: 15-25 minutes for 2-round research (vs 10-15 minutes accept-incomplete)
