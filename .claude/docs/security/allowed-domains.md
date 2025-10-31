# Approved Domains Whitelist

**Last Updated**: 2025-10-10
**Total Domains**: 156

## Purpose

This document contains the approved domain whitelist for WebFetch and WebSearch operations in the `researcher-web` agent. Only domains listed here are permitted to prevent Server-Side Request Forgery (SSRF) attacks.

## Security Hook Reference

**Hook**: `.claude/hooks/security/validate_url.py`
**Function**: `validate_url_safety(url, allowed_domains)`
**Layer**: Layer 3 (Content Moderation)

## Domain Categories

### AI & Development Platforms (17 domains)
- platform.openai.com
- ai.google
- developers.google.com
- www.anthropic.com
- www.microsoft.com
- openai.com
- docs.llamaindex.ai
- developers.llamaindex.ai
- docs.langgraph.com
- modelcontextprotocol.github.io
- spec.modelcontextprotocol.io
- blog.langchain.dev
- blog.langchain.com
- www.deeplearning.ai
- www.promptingguide.ai
- console.anthropic.com
- claude.com

### Documentation & Standards (15 domains)
- developer.mozilla.org
- json-schema.org
- docs.oracle.com
- learn.microsoft.com
- schema.org
- www.w3.org
- python-jsonschema.readthedocs.io
- swagger.io
- github.com
- raw.githubusercontent.com
- cli.github.com
- docs.github.com
- github.blog
- www.atlassian.com
- www.npmjs.com

### Research & Academic (14 domains)
- arxiv.org
- nature.com
- science.org
- pnas.org
- academic.oup.com
- journals.plos.org
- sciencedirect.com
- news.mit.edu
- news.stanford.edu
- news.yale.edu
- yaledailynews.com
- imf.org
- worldbank.org
- nber.org

### Engineering Blogs & Best Practices (12 domains)
- ai.googleblog.com
- google.github.io
- engineering.fb.com
- netflixtechblog.com
- blog.research.google
- research.google
- microsoft.github.io
- engineering.atspotify.com
- blog.google
- martinfowler.com
- refactoring.guru
- www.patterns.dev

### Cloud & Infrastructure (8 domains)
- aws.amazon.com
- kubernetes.io
- docs.docker.com
- developer.hashicorp.com
- docs.ansible.com
- docs.gitlab.com
- jenkins.io
- backstage.io

### Python & Data Science (10 domains)
- pypi.org
- docs.python.org
- docs.pytest.org
- docs.pydantic.dev
- ai.pydantic.dev
- python.langchain.com
- langchain-ai.github.io
- docs.temporal.io
- airflow.apache.org
- context7.com

### Web Frameworks & Languages (20 domains)
- go.dev
- typescriptlang.org
- doc.rust-lang.org
- php.net
- ruby-lang.org
- swift.org
- kotlinlang.org
- react.dev
- nextjs.org
- vuejs.org
- nuxt.com
- svelte.dev
- angular.dev
- docs.solidjs.com
- djangoproject.com
- fastapi.tiangolo.com
- flask.palletsprojects.com
- expressjs.com
- nestjs.com
- spring.io
- rubyonrails.org

### Databases (10 domains)
- postgresql.org
- dev.mysql.com
- mysql.com
- mariadb.com
- sqlite.org
- mongodb.com
- redis.io
- elastic.co
- cassandra.apache.org
- neo4j.com

### Testing & Monitoring (11 domains)
- jestjs.io
- vitest.dev
- mochajs.org
- cypress.io
- playwright.dev
- junit.org
- testng.org
- rspec.info
- selenium.dev
- prometheus.io
- grafana.com

### Financial Data & News (39 domains)
#### News
- wsj.com
- reuters.com
- ft.com
- bloomberg.com
- economist.com
- apnews.com
- barrons.com
- marketwatch.com
- cnbc.com
- finance.yahoo.com
- forbes.com
- fortune.com
- businessinsider.com
- thestreet.com
- seekingalpha.com
- investors.com

#### Regulatory
- sec.gov
- finra.org
- fdic.gov
- federalreserve.gov
- cftc.gov
- occ.gov
- fred.stlouisfed.org
- bea.gov
- bls.gov
- ecb.europa.eu
- bankofengland.co.uk
- newyorkfed.org
- bis.org

#### Data APIs
- alphaadvantage.co
- polygon.io
- tradingview.com
- investing.com

#### Financial Services
- plaid.com
- developer.visa.com
- developer.mastercard.com
- stripe.com
- docs.stripe.com
- twilio.com
- www.twilio.com

#### FinTech Media
- americanbanker.com
- pymnts.com
- finovate.com
- bankingdive.com

### Security & OWASP (4 domains)
- owasp.org
- cheatsheetseries.owasp.org
- genai.owasp.org

### General Knowledge & Support (7 domains)
- en.wikipedia.org
- support.anthropic.com
- support.claude.com
- www.aosabook.org
- hbr.org
- health.harvard.edu
- medium.com

### Product & Strategy (10 domains)
- leanstartup.co
- www.svpg.com
- www.datadog.com
- www.datadoghq.com
- www.notion.com
- www.notion.so
- www.figma.com
- www.sequoiacap.com
- www.ycombinator.com
- openviewpartners.com
- www.profitwell.com
- www.morningstar.com
- www.bloomberg.com

### Miscellaneous (9 domains)
- www.msys2.org
- cygwin.com
- www.dofactory.com
- www.oodesign.com
- developers.notion.com
- www.fipa.org
- docs.crewai.com
- a2a-protocol.org
- cookbook.openai.com

## Adding New Domains

To add a new approved domain:

1. **Evaluate Domain Trustworthiness**:
   - Is it an official documentation site?
   - Is it a reputable organization (academic, government, major company)?
   - Does it have HTTPS?
   - Is the content authoritative for the domain?

2. **Add to Whitelist**:
   - Update this file under the appropriate category
   - Update `.claude/hooks/security/validate_url.py` (`APPROVED_DOMAINS` list)
   - Update total count in header

3. **Test**:
   - Run `uv run python .claude/hooks/security/validate_url.py`
   - Verify new domain passes validation

4. **Document Reason**:
   - Add comment in this file explaining why domain was added
   - Include use case if applicable

## Removing Domains

To remove a domain (e.g., if compromised or no longer needed):

1. Remove from this file
2. Remove from `.claude/hooks/security/validate_url.py`
3. Update total count
4. Document reason for removal in git commit message

## Security Notes

- **Wildcards**: Wildcards (*) are NOT supported for security reasons
- **Subdomains**: Subdomains of approved domains are automatically allowed
  - Example: `developer.mozilla.org` allows `developer.mozilla.org/en-US/docs`
- **IP Addresses**: Direct IP addresses are NEVER allowed (potential SSRF)
- **Localhost**: Localhost (127.0.0.1, ::1) is NEVER allowed
- **Private IPs**: Private IP ranges are NEVER allowed (RFC 1918)
- **Link-Local**: Link-local addresses (169.254.x.x) are NEVER allowed

## Validation Process

When a researcher-web agent attempts to fetch a URL:

```python
from .claude.hooks.security import validate_url_safety

result = validate_url_safety("https://platform.openai.com/docs")

# Result structure:
{
    "safe": True,
    "reason": "URL passed all SSRF checks",
    "domain": "platform.openai.com",
    "ip": "104.18.xx.xx",  # Resolved IP
    "scheme": "https"
}
```

Validation checks (in order):
1. ✅ URL scheme is http/https
2. ✅ Domain is in approved whitelist
3. ✅ Domain resolves to public IP (not private/loopback/link-local)
4. ✅ No redirect to unapproved domain

## Emergency Bypass

**DO NOT CREATE BYPASS MECHANISMS**. If a legitimate use case requires a non-whitelisted domain:

1. Evaluate if truly necessary
2. Research domain thoroughly
3. Add to whitelist properly
4. Document justification

Temporary bypasses create security vulnerabilities.

## Related Documentation

- **Security Framework**: `.claude/docs/security/README.md`
- **Layer 3 (Content Moderation)**: `.claude/docs/security/layers/layer-3-content-moderation.md`
- **OWASP LLM03**: `.claude/docs/security/owasp-llm-top-10.md#llm03-supply-chain-vulnerabilities`

---

**Maintenance**: Review this whitelist quarterly to remove unused domains and add new authoritative sources.
