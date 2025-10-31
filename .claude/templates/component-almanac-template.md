# Component Almanac Template

**Purpose:** A comprehensive reference guide for AI agents to understand and leverage existing functionality in your codebase, preventing duplication and promoting code reuse.

**Last Updated:** [Date]

---

## 📖 How to Use This Template

**For Project Teams:**
1. Copy this template to your project root as `COMPONENT_ALMANAC.md`
2. Organize components by logical categories (infrastructure, domain logic, integrations, etc.)
3. Document each reusable component with: location, purpose, key features, usage example
4. Update whenever new reusable components are added
5. Reference in CLAUDE.md: "Check COMPONENT_ALMANAC.md before creating new components"

**For AI Agents:**
- **ALWAYS check this file** before implementing new functionality
- Search for keywords related to your task (e.g., "authentication", "caching", "API client")
- Reuse existing components when possible
- If building similar functionality, consider extending existing components instead

---

## Table of Contents

<!-- Customize these categories for your domain -->

1. [System Architecture Overview](#system-architecture-overview)
2. [Core Infrastructure](#core-infrastructure)
3. [Data Access & Storage](#data-access--storage)
4. [External Integrations](#external-integrations)
5. [Business Logic & Domain Models](#business-logic--domain-models)
6. [Utilities & Helpers](#utilities--helpers)
7. [Testing Infrastructure](#testing-infrastructure)
8. [Component Integration Patterns](#component-integration-patterns)

---

## System Architecture Overview

<!-- Describe your high-level architecture -->

**Architecture Pattern:** [e.g., Microservices, Monolith, Serverless, etc.]

**Key Design Principles:**
- [Principle 1: e.g., Separation of concerns]
- [Principle 2: e.g., Dependency injection]
- [Principle 3: e.g., Test-driven development]

**Technology Stack:**
- **Language:** [e.g., Python 3.11+, TypeScript, Go]
- **Framework:** [e.g., FastAPI, React, Express]
- **Database:** [e.g., PostgreSQL, MongoDB, Redis]
- **Infrastructure:** [e.g., Docker, Kubernetes, AWS Lambda]

---

## Core Infrastructure

### Configuration Management

**Location:** `[path/to/config/]`

**Purpose:** Centralized configuration management for environment variables, feature flags, and runtime settings.

**Key Components:**
- **`settings.py`** - Environment configuration with validation
- **`feature_flags.py`** - Feature toggle management
- **`secrets.py`** - Secure credential loading

**Usage Example:**
```python
from myproject.config import get_settings

settings = get_settings()  # Singleton with validation
database_url = settings.DATABASE_URL
```

**Related Components:**
- Secret Management → See [External Integrations](#external-integrations)
- Environment Validation → See startup checks below

---

### Logging & Observability

**Location:** `[path/to/logging/]`

**Purpose:** Structured logging with correlation IDs and metrics tracking.

**Key Features:**
- JSON-formatted logs
- Automatic correlation ID propagation
- Performance metrics injection
- PII scrubbing capabilities

**Usage Example:**
```python
from myproject.logging import get_logger

logger = get_logger(__name__)
logger.info("Operation completed", extra={"user_id": 123, "duration_ms": 45})
```

---

## Data Access & Storage

<!-- Document your data layer components -->

### Database Client

**Location:** `[path/to/db/]`

**Purpose:** [Describe your database abstraction layer]

**Key Features:**
- [Feature 1]
- [Feature 2]

**Usage Example:**
```python
# Add your database usage example here
```

---

## External Integrations

<!-- Document third-party integrations and API clients -->

### [Service Name] Client

**Location:** `[path/to/clients/service.py]`

**Purpose:** [What this integration does]

**Key Features:**
- Automatic retries with exponential backoff
- Circuit breaker pattern
- Rate limiting
- Response caching

**Usage Example:**
```python
# Add usage example
```

---

## Business Logic & Domain Models

<!-- Document your core business logic and domain models -->

### [Domain Model Name]

**Location:** `[path/to/models/model.py]`

**Purpose:** [What this model represents]

**Key Attributes:**
- `attribute1`: [Description]
- `attribute2`: [Description]

**Key Methods:**
- `method1()`: [Description]
- `method2()`: [Description]

**Usage Example:**
```python
# Add usage example
```

---

## Utilities & Helpers

<!-- Document reusable utility functions and helpers -->

### [Utility Category]

**Location:** `[path/to/utils/]`

**Available Utilities:**
- **`file_utils.py`** - File operations (read, write, validate)
- **`date_utils.py`** - Date/time formatting and parsing
- **`string_utils.py`** - String manipulation and validation

**Usage Example:**
```python
from myproject.utils.file_utils import safe_read_json

data = safe_read_json("config.json")  # Returns None on error instead of throwing
```

---

## Testing Infrastructure

<!-- Document test utilities and fixtures -->

### Test Fixtures

**Location:** `[tests/fixtures/]`

**Available Fixtures:**
- **`database_fixtures.py`** - Database setup/teardown
- **`mock_clients.py`** - Mock external API clients
- **`sample_data.py`** - Test data generators

**Usage Example:**
```python
import pytest
from tests.fixtures import create_test_user

def test_user_creation(test_db):
    user = create_test_user(test_db, email="test@example.com")
    assert user.email == "test@example.com"
```

---

## Component Integration Patterns

### How Components Work Together

**Pattern 1: [Name]**
- **When to use:** [Scenario]
- **Components involved:** [List]
- **Flow:** [Step-by-step]

**Example:**
```
Client Request → API Handler → Business Logic → Data Access → Response
```

---

## Quick Reference

### Most Commonly Used Components

| Component | Location | Purpose |
|-----------|----------|---------|
| Settings | `config/settings.py` | Configuration management |
| Logger | `logging/logger.py` | Structured logging |
| DB Client | `db/client.py` | Database access |
| Cache | `cache/redis.py` | Caching layer |

### Before You Build Something New

1. **Search this almanac** for similar functionality
2. **Check the codebase** for existing implementations
3. **Consider extending** existing components instead of building new ones
4. **Document your new component** in this almanac when done

---

## Maintenance Notes

**How to Update:**
1. Add new components as they're created
2. Keep usage examples up-to-date
3. Remove deprecated components with migration notes
4. Review quarterly for accuracy

**Ownership:** [Team/Person responsible for maintaining this doc]

**Questions?** [How to get help - Slack channel, email, etc.]

---

**This is a living document** - Keep it updated as your codebase evolves.
