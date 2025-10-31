# Example Project Component Almanac

**Purpose:** A comprehensive reference guide for AI coding agents to understand and leverage existing functionality in your codebase, preventing duplication and promoting code reuse.

**Note**: This is an example file showing how to structure your Component Almanac. Replace with your actual project components.

**Last Updated:** 2025-09-15

---

## Table of Contents

1. [System Architecture Overview](#system-architecture-overview)
2. [Core Infrastructure](#core-infrastructure)
3. [Data Connectors & Protocols](#data-connectors--protocols)
4. [Resilience & Reliability](#resilience--reliability)
5. [Observability & Monitoring](#observability--monitoring)
6. [Caching Infrastructure](#caching-infrastructure)
7. [Workers & Orchestration](#workers--orchestration)
8. [Domain Models & Business Logic](#domain-models--business-logic)
9. [LLM Integration](#llm-integration)
10. [Development & Testing Tools](#development--testing-tools)
11. [API & Service Layer](#api--service-layer)
12. [Component Integration Patterns](#component-integration-patterns)

---

## System Architecture Overview

This example system implements a **three-layer architecture** for financial research automation:

1. **Workflow Orchestration (LangGraph)** - Multi-step workflow coordination and state persistence
2. **Inter-Agent Communication (A2A Protocol)** - Standardized, vendor-neutral agent communication
3. **Individual Agent Implementation (Pydantic AI)** - Type-safe, modern agent implementations

### Key Design Principles
- **Thin LLM Layer:** Code-first workers handle data processing; LLMs only generate narratives
- **Parallel Execution:** Asynchronous orchestration with timeout management
- **Facts-First Architecture:** All data converted to traceable `Fact` objects
- **Conservative Analysis:** Confidence scoring on all outputs with human review flags

---

## Core Infrastructure

### Configuration Management

#### Environment Configuration
**Location:** `packages/core/config/`

- **`environment.py`** - Centralized environment variable management with pydantic-settings
- **`model_config.py`** - LLM model configuration (OpenAI, Gemini, Ollama)
- **`startup_validation.py`** - Application startup validation and health checks
- **`k8s_config.py`** - Kubernetes-specific configuration management
- **`ticker_mappings.py`** - Stock ticker symbol resolution and mapping

**Usage Example:**
```python
from packages.core.config.environment import get_settings
settings = get_settings()  # Singleton pattern with validation
```

### Secret Management
**Location:** `packages/core/secrets/`

- **`azure_vault.py`** - Azure Key Vault integration for secure credential storage
  - Automatic token refresh
  - Caching to reduce API calls
  - Fallback to environment variables

**Usage Example:**
```python
from packages.core.secrets import AzureVaultClient
vault = AzureVaultClient()
api_key = await vault.get_secret("openai-api-key")
```

### Logging & Structured Output
**Location:** `packages/core/logging/`

- **`structured.py`** - JSON-formatted structured logging with contextual metadata
  - Automatic correlation IDs
  - Performance metrics injection
  - PII scrubbing capabilities

**Usage Example:**
```python
from packages.core.logging import get_structured_logger
logger = get_structured_logger(__name__)
logger.info("Operation completed", extra={"ticker": "AAPL", "execution_time_ms": 250})
```

---

## Data Connectors & Protocols

### DataConnector Protocol (ADR-004)
**Location:** `packages/core/connectors/protocol.py`

The **DataConnector Protocol** provides a unified interface for ALL external data ingestion:

**Key Features:**
- Standardized `ConnectorInput` and `ConnectorResult` models
- Comprehensive observability metrics (execution time, API calls, cache hits)
- Never raises exceptions for predictable failures (returns status codes)
- Support for partial success scenarios

**Core Components:**
- `DataConnector` - Protocol interface all connectors must implement
- `ConnectorStatus` - Enum for standardized status codes (SUCCESS, PARTIAL_SUCCESS, API_ERROR, etc.)
- `ConnectorResult` - Unified output with facts, metrics, and error details
- `ConnectorInput` - Standardized input (ticker + optional params)

### HTTP Integration Framework
**Location:** `packages/core/connectors/http_integration.py`

Provides resilient HTTP client patterns for API integrations:
- Automatic retry with exponential backoff
- Rate limiting and throttling
- Connection pooling with httpx
- Comprehensive error handling

### Multi-API Orchestrator
**Location:** `packages/core/connectors/orchestrator.py`

Implements fallback orchestration across multiple data providers:
- Circuit breaker patterns for API resilience
- Intelligent routing between providers
- Global timeout management
- Priority-based fallback chains

**Usage Example:**
```python
from packages.core.connectors.orchestrator import MultiAPIOrchestrator
orchestrator = MultiAPIOrchestrator([primary_api, fallback_api])
result = await orchestrator.fetch_with_fallback(input, timeout_seconds=30)
```

### Qualitative Data Connectors
**Location:** `packages/core/qual/`

Framework for collecting qualitative financial data:

**Base Infrastructure:**
- `base.py` - BaseConnector class with metrics tracking and error handling
- `facts.py` - Fact model with confidence scoring and source traceability
- `factory.py` - Dynamic connector discovery and instantiation
- `config.py` - Connector-specific configuration management

**Implemented Connectors:**
- `connectors/ceo_tenure.py` - CEO tenure and leadership stability analysis
- `connectors/news_sentiment.py` - News sentiment analysis with confidence scoring
- `connectors/current_ceo.py` - Current CEO information retrieval
- `connectors/quantitative_analysis.py` - Quantitative metrics integration

---

## Resilience & Reliability

### Circuit Breaker Pattern
**Location:** `packages/core/resilience/async_circuit_breaker.py`

AsyncIO-compatible circuit breaker wrapper around pybreaker:
- Configurable failure thresholds and recovery timeout
- Automatic state transitions (CLOSED → OPEN → HALF_OPEN)
- Prevents cascade failures in distributed systems

**Usage Example:**
```python
from packages.core.resilience import AsyncCircuitBreaker, CircuitBreakerConfig

config = CircuitBreakerConfig(
    failure_threshold=5,
    recovery_timeout=60,
    expected_exception=httpx.HTTPError
)
breaker = AsyncCircuitBreaker(config)
result = await breaker.call(api_function, *args)
```

### Retry Logic
**Location:** `packages/core/resilience/retry.py`

Sophisticated retry patterns with exponential backoff and jitter:
- Full jitter to prevent thundering herd
- Configurable max attempts and delays
- Smart exception filtering

**Usage Example:**
```python
from packages.core.resilience import RetryConfig, exponential_backoff_with_jitter

config = RetryConfig(max_attempts=3, base_delay=1.0, max_delay=30.0)
delay = exponential_backoff_with_jitter(attempt, config)
```

---

## Observability & Monitoring

### OpenTelemetry Integration
**Location:** `packages/core/observability/telemetry.py`

Comprehensive telemetry with automatic instrumentation:
- OpenLLMetry for LLM cost tracking
- Auto-instrumentation for FastAPI, httpx, Redis
- OTLP export to collectors (Grafana, Datadog, etc.)
- Configuration-driven for cloud migration

**Features:**
- Distributed tracing across services
- Metrics collection (latency, throughput, error rates)
- Resource attributes for service identification
- Automatic span creation for critical operations

### Structured Logging
**Location:** `packages/core/observability/structured_logger.py`

Enhanced logging with OpenTelemetry integration:
- JSON-formatted output for log aggregation
- Automatic trace and span ID injection
- Contextual metadata propagation
- Log level configuration per component

---

## Caching Infrastructure

### Redis Cache Manager
**Location:** `packages/core/cache/redis_cache.py`

Production-grade Redis caching with Context7 best practices:
- RESP3 protocol with client-side caching
- Built-in connection pooling and retries
- Native TTL support with configurable expiration
- Health checks and automatic reconnection

**Features:**
- Namespace-based key management
- Batch operations for efficiency
- Graceful degradation on cache failure
- Metrics tracking for cache hit rates

**Usage Example:**
```python
from packages.core.cache import QualConnectorCache
cache = QualConnectorCache()
await cache.set_with_ttl("key", data, ttl_seconds=3600)
cached_data = await cache.get("key")
```

### Cache Decorators
**Location:** `packages/core/cache/cache_decorator.py`

Decorator-based caching for functions and methods:
- Automatic key generation from function arguments
- TTL configuration per function
- Skip cache on specific conditions
- Metrics integration

---

## Workers & Orchestration

### Simple Orchestrator
**Location:** `services/orchestrator/simple_orchestrator.py`

Coordinates parallel execution of workers:
- Async/await pattern for concurrent execution
- Timeout management per worker
- Clean cancellation on failure
- Result aggregation and error handling

**Key Functions:**
- `evaluate_company()` - Main orchestration entry point
- Parallel execution of QuantWorker and QualWorker
- Mandatory quant analysis with best-effort qual analysis

### Quantitative Worker
**Location:** `workers/quant.py`

Deterministic financial calculations:
- Piotroski F-Score computation (9-point fundamental analysis)
- Integration with yfinance for market data
- Confidence scoring on data quality
- Fact generation with source traceability

### Qualitative Worker
**Location:** `workers/qual.py`

Orchestrates multiple qualitative data connectors:
- Parallel connector execution with timeout management
- Result aggregation from multiple sources
- Confidence-weighted fact synthesis
- Fallback handling for failed connectors

---

## Domain Models & Business Logic

### Core Business Models
**Location:** `domain/models/`

**Financial Metrics:**
- `financial_metrics.py` - Core financial calculations and ratios
- `piotroski.py` - Piotroski F-Score implementation
- `metric_spec.py` - Metric definitions and specifications

**Analysis Results:**
- `analysis_results.py` - Unified analysis result models
- `results.py` - Worker result containers (QuantResult, QualResult)
- `report.py` - Report generation models

**Fact Management:**
- `facts.py` - Core Fact model with confidence and traceability
  - Unique fact IDs for deduplication
  - Confidence levels (HIGH, MEDIUM, LOW, VERY_LOW)
  - Source attribution and timestamps
  - Support for both quantitative and qualitative facts

**Agent States:**
- `agent_states.py` - State management for multi-agent workflows
- `request_models.py` - Input validation models for API requests

---

## LLM Integration

### LLM Factory Pattern
**Location:** `packages/core/llm/`

Unified LLM abstraction supporting multiple providers:

**Core Components:**
- `llm_factory.py` - Factory for creating LLM instances
- `llm_strategy.py` - Strategy pattern for provider abstraction
- `config.py` - LLM-specific configuration management
- `prompt_manager.py` - Centralized prompt template management

**Provider Support:**
- OpenAI (GPT-4, GPT-3.5)
- Google Gemini (Pro, Flash)
- Ollama (local models)

**Usage Example:**
```python
from packages.core.llm import create_llm_client
llm = create_llm_client(provider="openai", model="gpt-4")
response = await llm.generate(prompt, temperature=0.7)
```

---

## Development & Testing Tools

### Code Review Pipeline
**Location:** `scripts/prepare-code-review.py`

Comprehensive code review preparation:
- Three-tier validation (lint-only, fast, full)
- Automatic file staging
- Diff report generation
- AI review prompt creation
- Integration with CI/CD

### Test Runners
**Location:** `scripts/testing/`

- `run_tests.py` - Targeted test execution with markers
- `run_golden_set.py` - Golden set validation for regression testing
- `k8s_manifests_smoke_test.py` - Kubernetes manifest validation
- `redis_test_commands.py` - Redis connectivity testing

### Validation Scripts
**Location:** `scripts/validation/`

- `validate_intake.py` - Intake agent validation
- `validate_json.py` - JSON schema validation
- `validate_ollama_integration.py` - Local LLM integration testing
- `redis_performance_validation.py` - Cache performance benchmarking

### Deployment Tools
**Location:** `scripts/deployment/`

- `validate_deployment.py` - Kubernetes deployment validation
- `verify_observability.py` - Telemetry and monitoring verification

---

## API & Service Layer

### FastAPI Application
**Location:** `services/api/main.py`

RESTful API with automatic documentation:
- Async request handling
- Dependency injection with Pydantic AI
- OpenAPI/Swagger documentation
- Health check endpoints
- CORS configuration

### Service Components
**Location:** `services/`

- `api/orchestrator.py` - API orchestration logic
- `api/example_agent.py` - Example agent implementation
- `reporting/view_models.py` - Report presentation models

---

## Component Integration Patterns

### Common Integration Patterns

#### 1. Worker + Connector Pattern
```python
# Worker orchestrates multiple connectors
from workers.qual import collect_qual_signals
from packages.core.qual.factory import QualConnectorFactory

# Factory discovers and instantiates all enabled connectors
factory = QualConnectorFactory()
connectors = factory.create_all_connectors()

# Worker manages parallel execution with timeout
results = await collect_qual_signals("AAPL", connectors=connectors)
```

#### 2. Circuit Breaker + HTTP Client Pattern
```python
from packages.core.resilience import AsyncCircuitBreaker
from packages.core.connectors.http_integration import create_resilient_client

# Wrap HTTP client with circuit breaker
breaker = AsyncCircuitBreaker(config)
client = create_resilient_client()

async def fetch_data(ticker):
    return await breaker.call(client.get, f"/api/data/{ticker}")
```

#### 3. Cache + Connector Pattern
```python
from packages.core.cache import cache_decorator
from packages.core.connectors.protocol import DataConnector

class CachedConnector(DataConnector):
    @cache_decorator(ttl_seconds=3600)
    async def fetch(self, input):
        # Expensive API call cached for 1 hour
        return await self._fetch_from_api(input)
```

#### 4. Observability + Worker Pattern
```python
from packages.core.observability import get_tracer
from packages.core.logging import get_structured_logger

tracer = get_tracer(__name__)
logger = get_structured_logger(__name__)

@tracer.start_as_current_span("process_ticker")
async def process_ticker(ticker: str):
    logger.info("Processing ticker", extra={"ticker": ticker})
    # Processing logic with automatic tracing
    return results
```

### Best Practices for Component Usage

1. **Always use existing infrastructure** - Don't reinvent logging, caching, or retry logic
2. **Follow the DataConnector Protocol** - All external data sources must implement this interface
3. **Use structured logging** - Include contextual metadata in all log statements
4. **Implement confidence scoring** - Every fact and analysis must have confidence levels
5. **Handle partial failures gracefully** - Use ConnectorStatus.PARTIAL_SUCCESS when appropriate
6. **Leverage circuit breakers** - Protect against cascade failures in external dependencies
7. **Cache expensive operations** - Use Redis cache with appropriate TTLs
8. **Emit metrics** - Use OpenTelemetry for observability
9. **Validate with Pydantic** - All data structures should be Pydantic models
10. **Test with existing utilities** - Use scripts/testing/ tools for validation

---

## Quick Reference: Key Components by Use Case

### "I need to fetch external data"
→ Implement `DataConnector` protocol from `packages/core/connectors/protocol.py`
→ Use `http_integration.py` for HTTP APIs
→ Add circuit breaker from `packages/core/resilience/`

### "I need to add caching"
→ Use `QualConnectorCache` from `packages/core/cache/redis_cache.py`
→ Or use `@cache_decorator` from `cache_decorator.py`

### "I need to handle retries"
→ Use `RetryConfig` and retry utilities from `packages/core/resilience/retry.py`

### "I need to log with structure"
→ Use `get_structured_logger()` from `packages/core/logging/`

### "I need to track metrics"
→ Use OpenTelemetry from `packages/core/observability/telemetry.py`

### "I need to manage configuration"
→ Use pydantic-settings from `packages/core/config/environment.py`

### "I need to store secrets"
→ Use Azure Key Vault from `packages/core/secrets/azure_vault.py`

### "I need to validate data"
→ Create Pydantic models extending types in `domain/models/`

### "I need to run tests"
→ Use test runners from `scripts/testing/`

### "I need to prepare for code review"
→ Run `scripts/prepare-code-review.py --stage-changes`

---

## Appendix: File Structure Reference

```
example-project/
├── packages/core/           # Shared infrastructure
│   ├── cache/              # Redis caching
│   ├── config/             # Configuration management
│   ├── connectors/         # DataConnector protocol & implementations
│   ├── llm/                # LLM abstractions
│   ├── logging/            # Structured logging
│   ├── observability/      # Telemetry & monitoring
│   ├── qual/               # Qualitative data framework
│   ├── resilience/         # Circuit breakers & retry
│   └── secrets/            # Secret management
├── domain/models/          # Business logic & models
├── workers/                # Data processing workers
├── services/               # API & orchestration
├── scripts/                # Development & ops tools
│   ├── code-review/        # Code review utilities
│   ├── deployment/         # Deployment validation
│   ├── testing/            # Test runners
│   └── validation/         # Various validators
└── tests/                  # Test suites
```

---

**Note:** This almanac is a living document. As new components are added or existing ones are modified, this reference should be updated to maintain accuracy. Always check the actual implementation for the most current details.