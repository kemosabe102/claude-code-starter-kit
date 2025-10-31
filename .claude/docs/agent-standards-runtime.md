# Agent Runtime Standards

**Auto-Load:** This minimal document is automatically loaded by all agents.

## Core Requirements

### Working Directory & Bash Behavior
- **Initial directory**: Repository root (agents always start here)
- **CRITICAL**: Claude Code resets `cwd` between bash calls - `cd` commands DO NOT PERSIST
- **NEVER use `cd` commands** - They don't work across separate bash invocations

**Path Usage Rules**:
- **Bash commands**: MUST use absolute paths
  * ✅ CORRECT: `uv run pytest C:/Users/username/Repos/your-project/tests/unit/`
  * ❌ WRONG: `cd tests && uv run pytest unit/` (cwd resets, pytest runs from root)
- **Tool calls** (Read/Write/Edit/Grep/Glob): Use relative paths from root
  * ✅ CORRECT: `Read("docs/guides/file.md")`
  * ✅ ALSO CORRECT: `Read("C:/Users/username/Repos/your-project/docs/guides/file.md")`
- **Use forward slashes**: `docs/guides/file.md` not `docs\guides\file.md`

### Status Types
- **SUCCESS**: Task completed successfully
- **NEEDS_CLARIFICATION**: Missing information, provide concrete gaps + next steps
- **ERROR**: Task failed, include reason and recovery options

### Timestamp Authority (CRITICAL)
- **Orchestrator provides execution_timestamp** in ISO 8601 UTC format
- **Sub-agents MUST use orchestrator timestamp only** - never generate locally
- **All timestamps must be consistent** across orchestration session

### Output Requirements
Always include: `status`, `agent`, `task_id`, `summary`, `execution_timestamp`

### Scope Enforcement
- Work within allowed directories only
- No secrets in outputs
- Sanitize all paths and inputs

### File Operations (For Agents That Modify Files)
**Required Reading**: `.claude/docs/guides/file-operation-protocol.md`

**Tool Hierarchy:**
1. **Edit Tool (PRIMARY)** - Standard exact string replacement
   - Read file first to get exact content
   - Use exact match for old_string parameter
   - If fails: Re-read file and retry with corrected match (up to 2 attempts)
2. **Bash with sed (FALLBACK)** - Only after 2 Edit failures
   - Use when Edit tool consistently fails on exact matches
   - Ensures compatibility across all environments (sed is bash standard)
   - Example: `sed -i 's/old_text/new_text/g' file.txt`
3. **Write Tool** - For new files or complete rewrites
   - Must Read existing files before overwriting
   - Use for files >22.5K tokens (estimate: lines × 4.5)

**Critical Rules:**
- MUST Read file before Edit/Write/sed operations
- Always use exact strings from Read output for old_string
- Try Edit tool twice before falling back to sed
- Document why fallback was needed in agent output

---

**Extended Documentation**: See `.claude/docs/agent-standards-extended.md` for detailed procedures, examples, and advanced patterns.