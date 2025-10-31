# Multi-Agent Orchestration with Claude Code

A starter repository for building sophisticated multi-agent orchestration systems using Claude Code.

## Purpose

This repository helps developers get started with multi-agent orchestration patterns, providing core principles, reusable components, and tooling for creating new agents.

## Core Principles

- **Orchestrator-Worker Pattern**: Central orchestrator delegates tasks to specialized sub-agents
- **Context Management**: Efficient context passing between agents with minimal redundancy
- **Delegation Confidence**: Score-based decision framework for optimal agent selection
- **Observable Systems**: Built-in monitoring and telemetry for agent interactions

## Getting Started

Use the agent creator workflow to scaffold new agents with best practices:
```bash
# Create a new agent using the agent creator command
./create-agent.sh <agent-name> <agent-purpose>
```

This will generate the necessary components and configuration for your new agent, following established orchestration patterns.

## Components

- Agent templates and scaffolding
- Orchestration framework utilities
- Common delegation patterns
- Example multi-agent workflows
