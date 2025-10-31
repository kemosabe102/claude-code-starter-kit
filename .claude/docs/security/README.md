# Security Patterns and Best Practices

**Purpose**: Security guidelines and patterns for building secure multi-agent systems with Claude Code.

**Version**: 1.0.0
**Last Updated**: 2025-10-31

---

## Overview

This directory contains security patterns, threat models, and best practices for the Claude Code Starter Kit framework. Security is critical when building agent-based systems that can read files, make web requests, and modify code.

---

## 📁 Security Documentation

### Available Documents

1. **allowed-domains.md** - SSRF protection whitelist (156 approved domains)
   - Domain whitelist for researcher-web agent
   - Prevents arbitrary web requests
   - Regular security audits required

### Planned Documentation

The following security guides are planned for future releases:

- **threat-model.md** - Threat analysis for multi-agent systems
- **secrets-detection.md** - Preventing credential leaks
- **path-traversal-prevention.md** - File operation security
- **agent-sandboxing.md** - Agent isolation strategies

---

## 🔒 Core Security Principles

### 1. Defense in Depth

**Layers of Protection**:
- **Input Validation**: Validate all user inputs and agent parameters
- **Access Control**: Restrict agent capabilities via permissions
- **Domain Filtering**: Whitelist external resources (web, APIs)
- **Path Validation**: Prevent directory traversal attacks
- **Secrets Scanning**: Detect credentials before commits

### 2. Principle of Least Privilege

**Agent Permissions**:
- Agents only have tools they explicitly need
- Read vs. write permissions clearly defined
- No agent spawns sub-agents without orchestrator approval
- Restricted directories enforced (`.env`, `credentials.json`, etc.)

**Example** from agent definitions:
```markdown
## Permissions

**Allowed Operations**:
- ✅ Read files in `docs/**` and `src/**`
- ✅ Write to `docs/reports/**` only

**Restricted Operations**:
- ❌ NO edits to `.claude/agents/**`
- ❌ NO edits to `.env` or secrets files
- ❌ NO Task tool (no sub-agent spawning)
```

### 3. Fail Securely

**Error Handling**:
- Errors don't expose sensitive paths or credentials
- Failed authentication returns generic messages
- Timeouts don't leak system information
- Logs are sanitized before storage

---

## 🛡️ Security Patterns

### SSRF (Server-Side Request Forgery) Protection

**Problem**: Agents making web requests could be exploited to scan internal networks or fetch malicious content.

**Solution**: Domain whitelist pattern (see `allowed-domains.md`)

**Implementation**:
```python
# researcher-web agent uses approved domain list
ALLOWED_DOMAINS = load_allowed_domains()

def fetch_url(url):
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc not in ALLOWED_DOMAINS:
        raise SecurityError(f"Domain {parsed.netloc} not in whitelist")
    # Proceed with fetch
```

**Whitelist Criteria**:
- Official documentation sites (docs.python.org, etc.)
- Reputable news sources
- Technical communities (Stack Overflow, GitHub, etc.)
- No URL shorteners or redirect services
- Regular security audits (quarterly recommended)

**Current Whitelist**: 156 approved domains (see `allowed-domains.md`)

---

### Path Traversal Prevention

**Problem**: File operations could access files outside intended directories.

**Solution**: Path validation before all file operations

**Implementation Pattern**:
```python
import os
from pathlib import Path

ALLOWED_ROOTS = [
    Path("/workspace/src"),
    Path("/workspace/docs"),
    Path("/workspace/tests")
]

def validate_path(file_path: str) -> Path:
    """Validate path is within allowed directories."""
    resolved = Path(file_path).resolve()

    # Check if within allowed roots
    if not any(resolved.is_relative_to(root) for root in ALLOWED_ROOTS):
        raise SecurityError(f"Path {file_path} outside allowed directories")

    # Prevent accessing sensitive files
    FORBIDDEN_NAMES = {".env", "credentials.json", "secrets.yaml", "id_rsa"}
    if resolved.name in FORBIDDEN_NAMES:
        raise SecurityError(f"Access to {resolved.name} is forbidden")

    return resolved
```

**Agent Contract** (from `file-operation-protocol.md`):
- All file paths validated before operations
- Symbolic links resolved and checked
- Hidden files require explicit approval
- `.env` and credential files always blocked

---

### Secrets Detection

**Problem**: Agents might accidentally commit API keys, passwords, or tokens.

**Solution**: Multi-layer secrets detection

**Pre-Commit Hook** (`.git/hooks/pre-commit`):
```bash
#!/bin/bash
# Scan for common secret patterns

PATTERNS=(
    "AKIA[0-9A-Z]{16}"                    # AWS Access Key
    "ghp_[a-zA-Z0-9]{36}"                 # GitHub Personal Access Token
    "sk-[a-zA-Z0-9]{48}"                  # OpenAI API Key
    "password\s*=\s*['\"][^'\"]+['\"]"    # Hardcoded passwords
)

for pattern in "${PATTERNS[@]}"; do
    if git diff --cached | grep -E "$pattern"; then
        echo "ERROR: Potential secret detected: $pattern"
        exit 1
    fi
done
```

**Agent Guidelines**:
- Never log secrets or credentials
- Use environment variables for all keys
- Template files use `<YOUR_KEY_HERE>` placeholders
- Encourage `.env.example` with fake values

**Files Always Excluded**:
- `.env`, `.env.local`, `.env.production`
- `credentials.json`, `secrets.yaml`, `config/secrets/**`
- Private keys: `*.pem`, `*.key`, `id_rsa`, `id_ed25519`

---

### Agent Isolation

**Problem**: Malicious or buggy agents could interfere with each other or the system.

**Solution**: Capability-based isolation

**Orchestrator Enforcement**:
```python
class AgentExecutor:
    def execute(self, agent_name: str, task: Task) -> Result:
        agent_def = load_agent(agent_name)

        # Enforce tool restrictions
        allowed_tools = agent_def.tools
        for tool in task.tools_requested:
            if tool not in allowed_tools:
                raise SecurityError(f"{agent_name} not authorized for {tool}")

        # Enforce write restrictions
        if "Write" in allowed_tools or "Edit" in allowed_tools:
            for path in task.target_files:
                if not self.check_write_permission(agent_def, path):
                    raise SecurityError(f"{agent_name} cannot write to {path}")

        # Execute with timeout
        return self.run_with_timeout(agent_def, task, timeout=600)
```

**Agent Boundaries**:
- Agents cannot modify their own definitions
- Agents cannot spawn sub-agents (only orchestrator)
- Agents cannot escalate their own permissions
- Agents operate within defined tool sets

---

## 🔍 OWASP LLM Top 10 Alignment

The framework addresses [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) security risks:

| Risk | Mitigation Strategy |
|------|---------------------|
| **LLM01: Prompt Injection** | Input validation, agent role boundaries, no direct user input to system prompts |
| **LLM02: Insecure Output Handling** | Output sanitization, no eval() on agent outputs, schema validation |
| **LLM03: Training Data Poisoning** | N/A (using Claude API, not training models) |
| **LLM04: Model Denial of Service** | Request rate limiting, timeout enforcement, token budgets |
| **LLM05: Supply Chain** | Vetted dependencies, MCP server whitelisting, regular audits |
| **LLM06: Sensitive Information Disclosure** | Secrets scanning, log sanitization, no credentials in prompts |
| **LLM07: Insecure Plugin Design** | MCP server review, capability restrictions, sandboxing |
| **LLM08: Excessive Agency** | Agent permission model, orchestrator approval gates, no self-modification |
| **LLM09: Overreliance** | Confidence scoring, human-in-the-loop for critical operations |
| **LLM10: Model Theft** | N/A (using Claude API, not self-hosting models) |

---

## 📋 Security Checklist for New Agents

When creating new agents with `/create-agent`, verify:

- [ ] **Permissions Defined**: Explicit allowed/restricted operations listed
- [ ] **Tool Justification**: Each tool has clear purpose in agent description
- [ ] **Write Boundaries**: If Write/Edit tools used, paths clearly restricted
- [ ] **No Secrets Access**: Agent cannot read `.env`, `credentials.json`, etc.
- [ ] **No Task Tool** (unless orchestration agent): Prevents unauthorized sub-agent spawning
- [ ] **Error Messages**: Failures don't expose sensitive information
- [ ] **Input Validation**: Agent validates inputs before operations
- [ ] **Timeout Enforcement**: Long-running operations have timeouts
- [ ] **Audit Trail**: Agent logs operations for security review

---

## 🚨 Security Incident Response

### Suspected Security Issue

1. **Stop Execution**: Use `/cancel` or kill agent process
2. **Isolate**: Disable affected agent (comment out in `.claude/agents/`)
3. **Assess**: Review agent logs, file modifications, network requests
4. **Remediate**: Fix vulnerability, update agent definition
5. **Test**: Verify fix with security-focused test cases
6. **Document**: Record incident, root cause, and mitigation

### Reporting Security Vulnerabilities

**Internal Project**: Add to project issue tracker with `[SECURITY]` prefix

**Framework Issues**: Report to framework maintainers via:
- GitHub Security Advisories (recommended)
- Private email to security contact
- DO NOT post publicly until patched

---

## 🔧 Security Tools and Resources

### Static Analysis

- **Semgrep**: `semgrep --config=auto .` for vulnerability scanning
- **Bandit** (Python): `bandit -r src/` for Python security issues
- **ESLint Security Plugin** (JavaScript/TypeScript)

### Dynamic Analysis

- **Agent Execution Logging**: Enable debug logs to track agent behavior
- **Network Monitoring**: Monitor outbound requests for unexpected destinations
- **File Change Tracking**: Git diff after agent operations

### Security Research

- **OWASP LLM Top 10**: https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **Anthropic Safety Best Practices**: https://docs.anthropic.com/en/docs/build-with-claude/guardrails
- **NIST AI Risk Management**: https://www.nist.gov/itl/ai-risk-management-framework

---

## 📖 Additional Resources

### Framework Documentation

- **orchestrator-workflow.md** - Agent coordination security
- **agent-standards-runtime.md** - Runtime safety contracts
- **file-operation-protocol.md** - Safe file handling patterns

### External References

- [OWASP LLM Security](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Anthropic Claude Safety](https://www.anthropic.com/safety)
- [Microsoft AI Security](https://www.microsoft.com/en-us/security/business/ai-machine-learning/ai-security)

---

## 📞 Security Contact

**For security-related questions or concerns**:

- **Framework Issues**: [Add security contact for framework]
- **Project-Specific**: [Add your security contact]

---

**Remember**: Security is everyone's responsibility. When in doubt, choose the more restrictive option and document the decision.

---

**Last Review**: 2025-10-31
**Next Review**: 2026-01-31 (Quarterly)
