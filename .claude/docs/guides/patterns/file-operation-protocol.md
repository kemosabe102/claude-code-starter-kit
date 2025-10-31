# File Operation Protocol

**Purpose**: Best practices for file operations using Claude Code standard tools.

**Version**: 2.0 (Simplified - Starter Kit Edition)

---

## Quick Reference

| Operation | Tool | When to Use |
|-----------|------|-------------|
| **Modify existing file** | Edit | Replace specific content in existing files |
| **Create new file** | Write | Generate new files from scratch |
| **Create from template** | Read + Write | Read template, modify, write new file |
| **Read file content** | Read | View file contents, verify changes |
| **Find files** | Glob | Search for files by pattern (*.py, **/*.md) |
| **Search content** | Grep | Find text within files |

---

## Core File Operation Tools

### 1. Edit Tool

**Purpose**: Modify existing files by replacing exact text matches.

**When to Use**:
- Updating existing code or documentation
- Making targeted changes to specific sections
- Modifying configuration files

**Prerequisites**:
- **MUST** read the file first to get exact content
- Identify exact `old_string` to replace (must match exactly)
- Prepare `new_string` replacement text

**Example Workflow**:
```python
# Step 1: Read file to see current content
content = Read("packages/models/user.py")

# Step 2: Edit with exact string match
Edit(
    file_path="packages/models/user.py",
    old_string="email: str",
    new_string="email: str\n    email_verified: bool = False"
)

# Step 3: Verify change
verify = Read("packages/models/user.py")
# Confirm field was added correctly
```

**Best Practices**:
- ✅ Always read file before editing
- ✅ Use exact string matching (Edit requires precise match)
- ✅ For large files, target specific sections (not entire file)
- ✅ Verify changes by reading back the file
- ✅ Use meaningful old_string with enough context for uniqueness

**Common Pitfalls**:
- ❌ Not reading file first (causes string mismatch errors)
- ❌ Using approximate matches (Edit requires exact text)
- ❌ Including line numbers in old_string (those are from cat -n output, not actual file content)
- ❌ Trying to edit binary files
- ❌ Editing files you don't have permission to modify

---

### 2. Write Tool

**Purpose**: Create new files or completely overwrite existing files.

**When to Use**:
- Creating new files from scratch
- Generating templates or boilerplate
- Creating documentation or reports

**Prerequisites**:
- **MUST** read existing files before overwriting
- Ensure parent directory exists
- Have necessary write permissions

**Example Workflow**:
```python
# Creating new file
Write(
    file_path=".claude/agents/new-agent.md",
    content="---\nname: new-agent\n...\n"
)

# Overwriting existing file (MUST read first)
current = Read("config.json")
# ... modify content ...
Write(
    file_path="config.json",
    content=modified_content
)
```

**Best Practices**:
- ✅ Always read existing files before overwriting (Write tool requires this)
- ✅ Use Write for new files, Edit for modifications
- ✅ Verify file creation by reading back
- ✅ Check parent directory exists first

**Common Pitfalls**:
- ❌ Using Write to modify existing files (use Edit instead)
- ❌ Not reading file first when overwriting
- ❌ Creating files in non-existent directories
- ❌ Overwriting important files without backup

---

### 3. Read Tool

**Purpose**: View file contents, verify changes, gather context.

**When to Use**:
- Before any Edit operation (to get exact strings)
- After Edit/Write operations (to verify success)
- Gathering context for implementation
- Understanding file structure

**Parameters**:
- `file_path`: Absolute path to file (required)
- `offset`: Line number to start reading (optional)
- `limit`: Number of lines to read (optional)

**Example Workflow**:
```python
# Read entire file
content = Read("packages/models/user.py")

# Read specific section (large files)
content = Read(
    file_path="packages/core/large_file.py",
    offset=100,  # Start at line 100
    limit=50     # Read 50 lines
)
```

**Best Practices**:
- ✅ Use Read before Edit to get exact content
- ✅ Use offset/limit for large files (>500 lines)
- ✅ Verify all Edit/Write operations by reading back
- ✅ Read surrounding context for targeted edits

---

## File Operation Patterns

### Pattern 1: Simple Edit

**Scenario**: Update a single line or small section

```python
# 1. Read file
content = Read("config.yaml")

# 2. Edit with exact match
Edit(
    file_path="config.yaml",
    old_string="debug: false",
    new_string="debug: true"
)

# 3. Verify
verify = Read("config.yaml")
```

### Pattern 2: Multi-Section Edit

**Scenario**: Update multiple sections in same file

```python
# 1. Read file once
content = Read("setup.py")

# 2. First edit (sequential, not parallel)
Edit(
    file_path="setup.py",
    old_string='version="1.0.0"',
    new_string='version="1.1.0"'
)

# 3. Second edit (after first completes)
Edit(
    file_path="setup.py",
    old_string="dependencies = []",
    new_string="dependencies = ['requests', 'pydantic']"
)

# 4. Verify all changes
verify = Read("setup.py")
```

### Pattern 3: Create From Template

**Scenario**: Read template, modify, create new file

```python
# 1. Read template
template = Read(".claude/templates/agent.template.md")

# 2. Create new file with modifications
new_content = template.replace("[agent-name]", "my-agent")
new_content = new_content.replace("[description]", "My agent description")

Write(
    file_path=".claude/agents/my-agent.md",
    content=new_content
)

# 3. Verify
verify = Read(".claude/agents/my-agent.md")
```

### Pattern 4: Targeted Edit in Large File

**Scenario**: Edit specific section without reading entire file

```python
# 1. Find the section (read targeted range)
section = Read(
    file_path="packages/core/large_module.py",
    offset=100,
    limit=20
)

# 2. Edit that section
Edit(
    file_path="packages/core/large_module.py",
    old_string="def old_function():\n    pass",
    new_string="def new_function():\n    return True"
)

# 3. Verify the change (read same range)
verify = Read(
    file_path="packages/core/large_module.py",
    offset=100,
    limit=20
)
```

---

## Best Practices Summary

### Before Editing
1. ✅ **Always Read first** - Get exact content for old_string parameter
2. ✅ **Check file exists** - Verify path and permissions
3. ✅ **Understand context** - Read surrounding code for proper integration
4. ✅ **Plan changes** - Know exactly what to change before editing

### During Editing
1. ✅ **Use exact matches** - Edit requires precise old_string match
2. ✅ **One change at a time** - Sequential edits, not parallel (for same file)
3. ✅ **Targeted edits** - Change specific sections, not entire files
4. ✅ **Preserve formatting** - Match existing indentation and style

### After Editing
1. ✅ **Always verify** - Read back file to confirm changes
2. ✅ **Check syntax** - Ensure valid code/configuration
3. ✅ **Test changes** - Run tests if modifying code
4. ✅ **Document rationale** - Explain why changes were made

---

## File Operation Decision Tree

```
START: Need to modify a file?
│
├─ File doesn't exist?
│  └─ Use Write tool (create new file)
│
├─ Need to modify existing file?
│  ├─ Small, targeted change?
│  │  └─ Use Edit tool
│  │     1. Read file
│  │     2. Edit with exact match
│  │     3. Verify
│  │
│  └─ Complete rewrite?
│     └─ Use Write tool
│        1. Read existing file first (required)
│        2. Write new content
│        3. Verify
│
└─ Need to gather context only?
   └─ Use Read tool
      - Full file: Read(file_path)
      - Section: Read(file_path, offset, limit)
```

---

## Common Scenarios

### Scenario 1: Add Import Statement

```python
# Read file to see imports
content = Read("packages/service.py")

# Add new import (preserve ordering)
Edit(
    file_path="packages/service.py",
    old_string="from typing import Optional",
    new_string="from typing import Optional\nfrom pydantic import BaseModel"
)
```

### Scenario 2: Update Configuration Value

```python
# Read config
content = Read("config.json")

# Update specific value
Edit(
    file_path="config.json",
    old_string='"api_timeout": 30',
    new_string='"api_timeout": 60'
)
```

### Scenario 3: Add Method to Class

```python
# Read class definition
content = Read("packages/models/user.py")

# Add new method at end of class
Edit(
    file_path="packages/models/user.py",
    old_string="    def save(self):\n        pass",
    new_string="    def save(self):\n        pass\n\n    def validate_email(self):\n        return '@' in self.email"
)
```

### Scenario 4: Create New File From Scratch

```python
# No need to read (file doesn't exist)
Write(
    file_path="tests/test_user.py",
    content="""import pytest
from packages.models.user import User

def test_user_creation():
    user = User(email="test@example.com")
    assert user.email == "test@example.com"
"""
)

# Verify creation
verify = Read("tests/test_user.py")
```

---

## Error Handling

### Edit Tool Errors

**Error: "String to replace not found in file"**
- **Cause**: old_string doesn't exactly match file content
- **Fix**: Read file again, copy exact string including whitespace
- **Example**: Missing newline, extra space, wrong indentation

**Error: "File not found"**
- **Cause**: Invalid file path or file doesn't exist
- **Fix**: Check path, use Glob to find file, create with Write if needed

**Error: "Multiple matches found"**
- **Cause**: old_string is not unique in file
- **Fix**: Include more context to make old_string unique

### Write Tool Errors

**Error: "Must read file before writing"**
- **Cause**: Attempting to overwrite existing file without reading first
- **Fix**: Use Read tool first, then Write

**Error: "Directory does not exist"**
- **Cause**: Parent directory for new file doesn't exist
- **Fix**: Create directory first or choose existing location

### General Best Practices for Error Recovery

1. **Read Carefully** - Always read file before editing
2. **Verify Paths** - Use Glob to find files if unsure
3. **Check Permissions** - Ensure you can write to target location
4. **Test Incrementally** - Make small changes, verify each one
5. **Keep Backups** - For critical files, document original state

---

## Validation Checklist

**Before any file operation**:
- [ ] File path is correct and absolute
- [ ] Have read file to understand current content
- [ ] Know exact old_string for Edit operations
- [ ] Prepared new_string with proper formatting
- [ ] Have write permissions for target location

**After file operation**:
- [ ] Read back file to verify changes
- [ ] Check syntax is valid (for code files)
- [ ] Confirm all intended changes were applied
- [ ] No unintended side effects (formatting, other sections)
- [ ] File is still valid and parseable

---

## Integration with Workflows

### Pre-Flight Assessment

Before any file operation, assess:

1. **File Size** - Large files (>500 lines) may need offset/limit
2. **File Type** - Code, config, documentation have different requirements
3. **Change Scope** - Single line, section, or multiple sections?
4. **Dependencies** - Will this change affect other files?
5. **Testing** - How to verify change is correct?

### Verification Protocol

After file operations:

1. **Read Back** - Always read file to confirm changes
2. **Syntax Check** - For code files, verify valid syntax
3. **Diff Review** - Compare old vs. new content mentally
4. **Integration Test** - If modifying code, run relevant tests
5. **Documentation** - Update related docs if needed

---

## Advanced Patterns

### Pattern: Conditional Edit

```python
# Read file
content = Read("config.yaml")

# Only edit if condition is met
if "old_value" in content:
    Edit(
        file_path="config.yaml",
        old_string="setting: old_value",
        new_string="setting: new_value"
    )
else:
    # Handle case where old_value doesn't exist
    print("Old value not found, skipping edit")
```

### Pattern: Multi-File Coordinated Update

```python
# Update related files in sequence
files_to_update = [
    ("models/user.py", "class User:", "class User(BaseModel):"),
    ("models/product.py", "class Product:", "class Product(BaseModel):"),
    ("models/order.py", "class Order:", "class Order(BaseModel):")
]

for file_path, old, new in files_to_update:
    content = Read(file_path)
    Edit(file_path=file_path, old_string=old, new_string=new)
    verify = Read(file_path)
    # Confirm change before proceeding to next file
```

### Pattern: Safe Overwrite

```python
# Read existing file (backup in memory)
original = Read("important_config.yaml")

try:
    # Write new version
    Write(
        file_path="important_config.yaml",
        content=new_configuration
    )

    # Verify new version is valid
    verify = Read("important_config.yaml")

    # If validation fails, could restore original
    # (Note: actual rollback would need error handling)

except Exception as e:
    # Handle error, potentially restore original
    print(f"Error updating config: {e}")
```

---

## Related Documentation

- **tool-parallelization-patterns.md** - When to parallelize file operations
- **validation-rubrics.md** - Quality validation for file changes
- **agent-standards-runtime.md** - Agent file operation contracts
- **ooda-loop-framework.md** - Decision-making framework for file operations

---

**Version**: 2.0 (Simplified for Starter Kit)
**Last Updated**: 2025-10-31
**Target Audience**: All agents performing file operations
**Complexity**: Beginner-friendly, covers 95% of use cases
