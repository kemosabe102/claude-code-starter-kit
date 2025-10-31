## Deep Dive: Google’s Agent2Agent (A2A) Protocol

### 1. Introduction

Google’s Agent2Agent (A2A) protocol is an open specification designed to standardize communication between autonomous AI agents. It provides a common framework—built on HTTP and JSON-RPC—for describing tasks, capabilities, and results, enabling heterogeneous agents (from different vendors or frameworks) to interoperate seamlessly. This document explores the A2A standard in detail and demonstrates how to implement and leverage it in multi-agent workflows. It also covers techniques for **self-optimizing prompts**, where agents dynamically refine their own instructions and tool descriptions to improve performance over time.

---

### 2. A2A Protocol Architecture

#### 2.1 Core Components

- **Agent Registry**: A service where agents register their metadata (capabilities, supported message versions, authentication) via a standardized `RegisterAgent` call.
- **Task Dispatcher**: An HTTP endpoint that routes incoming tasks (JSON-RPC) to the appropriate agent(s) based on their declared capabilities.
- **Message Schema**: A shared JSON schema defining fields like `task_id`, `agent_id`, `capabilities`, `params`, `timeout`, and optional `callback_url`.
- **Result Collector**: A callback or polling endpoint where agents post their completed task messages, including status, outputs, and metrics.

#### 2.2 Communication Flow

1. **Registration**: Agent A calls `POST /a2a/register` with its `agent_id`, `capabilities`, and public key.
2. **Task Submission**: The orchestrator (or another agent) sends a JSON-RPC `executeTask` request to `/a2a/dispatch`, specifying `task_id`, target `agent_id` (or capability filter), and `params`.
3. **Execution**: The receiving agent unpacks the JSON message, performs the task, and optionally calls subagents via the same dispatcher.
4. **Result Reporting**: Agent posts a JSON-RPC `taskCompleted` request to `/a2a/callback` with `task_id`, `status` (`success`/`error`), and `result` object.

---

### 3. A2A Message Definition Examples

#### 3.1 Task Registration Payload

```json
{
  "jsonrpc": "2.0",
  "method": "RegisterAgent",
  "params": {
    "agent_id": "fact_extractor_v1",
    "capabilities": ["web_search", "text_analysis"],
    "public_key": "<PEM-encoded-key>",
    "version": "1.0"
  }
}
```

#### 3.2 Task Dispatch Payload

```json
{
  "jsonrpc": "2.0",
  "method": "ExecuteTask",
  "params": {
    "task_id": "task_20250809_001",
    "target": { "capability": "web_search" },
    "params": {
      "query": "latest semiconductor industry mergers",
      "max_results": 5
    },
    "timeout_ms": 30000,
    "callback_url": "https://orchestrator.local/a2a/callback"
  }
}
```

#### 3.3 Task Completion Payload

```json
{
  "jsonrpc": "2.0",
  "method": "TaskCompleted",
  "params": {
    "task_id": "task_20250809_001",
    "agent_id": "web_search_agent_v2",
    "status": "success",
    "result": {
      "items": [
        { "title": "...", "url": "...", "snippet": "..." },
        ...
      ]
    },
    "metrics": {
      "latency_ms": 1234,
      "tokens_used": 45
    }
  }
}
```

---

### 4. Implementing A2A in Your Environment

1. **Choose or Build an A2A-Compatible Runtime**: Use Google’s open-source A2A SDK or any JSON-RPC library. Ensure HTTP endpoints (`/a2a/register`, `/a2a/dispatch`, `/a2a/callback`) are secured (TLS + auth headers).
2. **Agent Configuration**:
   - Implement a startup routine to register with the Agent Registry.
   - Expose capabilities and version metadata.
3. **Dispatcher Setup**:
   - Map capabilities to agent endpoints.
   - Implement routing logic, including fan-out to multiple agents for parallel tasks.
4. **Error Handling & Retries**:
   - Use `status: error` with an `error.code` and `error.message` in the `TaskCompleted` payload.
   - Define retry policies (e.g., retry on network error up to 3 times with backoff).
5. **Monitoring & Metrics Collection**:
   - Instrument A2A calls to capture latency, throughput, and success rates.
   - Export metrics to Prometheus or your monitoring stack.

---

## Self-Optimizing Prompts: Techniques & Patterns

As MAS scale, maintaining and tuning subagent prompts becomes labor-intensive. Self-optimizing prompts leverage AI-driven evaluation loops to **automatically refine instructions and tool descriptions**. Below are key patterns:

### 1. Prompt Critic Agent

- **Role**: Reviews subagent outputs against expected task outcomes.
- **Workflow**: After a subagent completes its task, the critic agent receives the output and a *golden reference* or quality criteria.
- **Action**: Generates a report with:
  - Deviations from the definition of done
  - Suggestions for prompt changes (e.g., tightening scope, clarifying instructions)
- **Implementation**: Use the A2A protocol to invoke the critic:

```json
{
  "method": "ExecuteTask",
  "params": {
    "task_id": "critique_001",
    "target": { "agent_id": "prompt_critic_v1" },
    "params": {
      "original_prompt": "<system prompt for subagent>",
      "subagent_output": { ... },
      "reference": { ... }
    }
  }
}
```

- **Output**: A structured JSON with `recommendations`: an array of `{ change: "<instruction tweak>", rationale: "<why>" }`.

### 2. Tool Description Refinement Loop

- **Role**: Autonomous testing of tool descriptions within prompts.
- **Workflow**:
  1. Spawn a **Test Agent** to repeatedly run the subagent task using current tool descriptions.
  2. Measure failure modes (wrong tool selection, API misuse).
  3. Use a **Refiner Agent** to adjust the description text for clarity.
  4. Re-test until error rate falls below threshold.
- **Key Pattern**: *Generate → Evaluate → Refine → Re-test* cycle.

### 3. Automated A/B Prompt Testing

- **Role**: Conducts comparative experiments between prompt variants.
- **Workflow**:
  1. **Variant Generator Agent** produces N prompt variants (changing wording, structure).
  2. A **Batch Runner** parallelizes agent invocations with each variant.
  3. A **Metric Aggregator** collects performance metrics (accuracy, latency, token efficiency).
  4. **Selector Agent** chooses the best variant based on defined KPIs.
- **Implementation Note**: Use A2A `capability: parallel_execution` to fan-out tests, then collect all `TaskCompleted` results for analysis.

### 4. On-the-Fly Prompt Adaptation

- **Concept**: Agents adapt their own system prompt mid-session based on performance signals.
- **Mechanism**: Subagent monitors task progress (e.g., count of successful API calls vs. errors). If certain error thresholds are exceeded, it requests an updated prompt from a **Meta-Agent**.
- **Example Sequence**:
  1. Subagent hits repeated 404 errors using a web-scraping tool.
  2. It sends an A2A `ExecuteTask` to `meta_prompt_agent_v1` with its current prompt and error logs.
  3. Meta-agent returns a refined system prompt (e.g., specifying updated user-agent headers or alternate source domains).
  4. Subagent reloads the new prompt and retries.

---

### 5. Best Practices for Self-Optimizing Systems

| Practice                        | Explanation                                                                            |
| ------------------------------- | -------------------------------------------------------------------------------------- |
| **Granular Logging**            | Capture prompt, context, tool calls, and outputs for each step.                        |
| **Metric Instrumentation**      | Define clear KPIs (accuracy, completion, cost) for automated decisions.                |
| **Isolation of Variants**       | Run experiments in sandboxed sub-environments to avoid cross-contamination.            |
| **Version Control for Prompts** | Store prompt definitions in a repo with version tags for traceability.                 |
| **Human-in-the-Loop Oversight** | For high-risk tasks, require human sign-off on prompt changes after critical failures. |

---

## References

1. Surapaneni, R. *et al.* (2025). “Announcing the Agent2Agent (A2A) Protocol.” Google Developers Blog.
2. Anthropic (2025). “How we built our multi-agent research system.”
3. Anthropic Documentation (2023). “Subagents – Create and use specialized AI subagents in Claude Code.”
4. Murad, J. (2024). “How JSON Prompting Supercharges Multi-Agent AI Systems.” AICompetence.org.

---

*End of Document*

