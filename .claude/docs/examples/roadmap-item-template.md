# Roadmap Item Template Example

**Purpose:** Roadmap Planning strategic roadmap template optimized for quick scanning and executive reporting. Critical information appears first, detailed content follows for deep-dive analysis.

---

## ✅ Ready Status Example (Score: 9/10)

```markdown
### 🎯 ENGINE-001: Automated Quantitative Analysis Engine

| **Roadmap Item Overview** |  |
|---------------------------|---|
| **Owner** | CodenameDev |
| **Status** | Ready |
| **Goal** | Transform manual financial screening into automated, reliable quantitative analysis |
| **Description** | Implement automated Piotroski F-Score calculation with multi-API fallback for consistent 5-minute company analysis |
| **Priority** | P0 |
| **Points** | 20 |

**Quick Value**: 95% time savings (2-4 hours → 5 minutes), $5-per-analysis cost target

---

**Business Value**:
- Reduce analyst screening time from 2-4 hours to under 5 minutes (95% time savings)
- Enable systematic application of Piotroski F-Score and key financial ratios
- Create foundation for $5-per-analysis cost target through automation
- Eliminate human error in quantitative calculations

**Details** (Timeline: Phase 2, Q4 2025 | Dependencies: Development Foundation Complete)

**Strategic Outcomes**:
- [ ] Piotroski F-Score calculated within 2 minutes for any ticker
- [ ] Consistent criteria applied across batch company screening
- [ ] Analysis continues via backup sources with <10% performance degradation during outages
- [ ] 50+ companies processed daily within SLO targets
- [ ] <$2 per company cost target achieved

**Constraints**: <30min analysis SLO | <$5 total cost | FMP/Alpha Vantage integration | Reliable fallback strategies

**Key Risks**: Data provider rate limits (→ multi-provider fallback) | Cost escalation (→ caching + monitoring)

**Success Metrics**: <5min analysis time | <$2 cost | 99.5% reliability | 100% accuracy vs manual calculation

**Related**: Strategic Plan (002-report-maturation.md) | Architecture (ADR-009) | Future Spec (XXX-quantitative-engine/)
```

## 🟡 Planning Status Example (Score: 6/10)

```markdown
### 🎯 REPORT-001: Professional Investment Report Generation

| **Roadmap Item Overview** |  |
|---------------------------|---|
| **Owner** | [NEEDS VERIFICATION - assign codename] |
| **Status** | Planning |
| **Goal** | Create analyst-grade investment reports matching professional standards |
| **Description** | Generate PDF reports with charts, tables, and professional formatting suitable for investment committee presentations |
| **Priority** | P1 |
| **Points** | TBD |

**Quick Value**: Eliminate manual formatting, enable stakeholder-ready reports, differentiate from DIY tools

---

**Business Value**:
- Enable analysts to deliver professional reports without manual formatting
- Differentiate from DIY tools through institutional-quality presentation
- Support stakeholder communication and investment committee presentations
- [NEEDS VERIFICATION] Potential enterprise customer value through professional output

**Details** (Timeline: Phase 2, Q4 2025 | Dependencies: ENGINE-001)

**Strategic Outcomes**:
- [ ] Professional formatting matches industry standards for completed analyses
- [ ] Output suitable for investment committee review and presentations
- [ ] [NEEDS VERIFICATION] Flexible formatting options for report customization
- [ ] [NEEDS VERIFICATION] Branded output support for enterprise customers

**Constraints**: ENGINE-001 integration | [NEEDS VERIFICATION] Performance requirements | [NEEDS VERIFICATION] Export formats

**Key Risks**: [NEEDS VERIFICATION] Formatting complexity vs timeline (→ phased approach)

**Success Metrics**: [NEEDS VERIFICATION] Generation time | Customer satisfaction | Analyst adoption rate

**Related**: Strategic Plan (002-report-maturation.md) | Architecture (ADR-008) | Future Spec (XXX-professional-reporting/)
```

---

## Template Structure

Copy this structure for new roadmap items:

```markdown
### 🎯 [ID]: [Strategic Capability Name]

| **Roadmap Item Overview** |  |
|---------------------------|---|
| **Owner** | [Codename] |
| **Status** | Ready \| Planning \| Proposed |
| **Goal** | [One-line strategic capability description] |
| **Description** | [120-character detailed description of implementation approach and key components] |
| **Priority** | P0 \| P1 \| P2 |
| **Points** | [1-30] |

**Quick Value**: [One-line business impact summary - savings, efficiency, competitive advantage]

---

**Business Value**:
- [Quantified customer impact - time savings, cost reduction, efficiency gains]
- [Strategic business outcome - competitive advantage, revenue enablement]
- [VP-reportable metrics - market positioning, analyst productivity, capabilities]
- [Use [NEEDS VERIFICATION] for unclear areas]

**Details** (Timeline: [Phase/Quarter] | Dependencies: [List or "None"])

**Strategic Outcomes**:
- [ ] [Concise Given/When/Then outcome - focus on measurable business results]
- [ ] [Customer-focused outcome with quantified benefit]
- [ ] [Operational outcome with performance/reliability targets]
- [ ] [Strategic capability demonstration for executive review]
- [ ] [Use [NEEDS VERIFICATION] for unclear outcomes]

**Constraints**: [Pipe-separated list of key requirements/limitations]

**Key Risks**: [Brief risk description] (→ [mitigation approach])

**Success Metrics**: [Pipe-separated list of target values or [NEEDS VERIFICATION]]

**Related**: [Abbreviated references - Strategic Plan | Architecture | Future Spec | Implementation]
```

---

## Template Design Principles

### **Information Hierarchy (5-Second Scan)**
1. **Header**: ID and Strategic Capability Name (unique identifier + what it does)
2. **Roadmap Item Overview Table**: Clean separation of key fields in priority order
   - **Owner**: Developer codename (accountability)
   - **Status**: Current development state (Ready/Planning/Proposed)
   - **Goal**: Strategic outcome in one line
   - **Description**: 120-character implementation details
   - **Priority**: Criticality level (P0/P1/P2)
   - **Points**: Effort estimation (1-30)
3. **Quick Value**: Immediate business impact summary

### **Ownership Requirements (Small Company Context)**
- **Owner MUST be specific codename**: "Lyken", "AlexDev", "SarahK"
- **NO generic teams**: Avoid "Core Development Team", "Engineering", "Product Team"
- **Accountability model**: Single-person ownership for clear responsibility
- **Use [NEEDS VERIFICATION - assign codename]** only when assignment genuinely unclear

### **Content Organization**
- **Quick Scan Section**: Critical info visible without scrolling (Lines 1-4)
- **Business Value**: Strategic impact bullets (VP-reportable outcomes)
- **Details Section**: Timeline, dependencies, constraints, metrics (below fold)
- **Compressed Details**: Pipe-separated lists for constraints, risks, metrics

## Readiness Validation

**Ready Status Requirements (Score ≥8):**
- [ ] ID and Goal clearly stated in first 2 lines
- [ ] Specific person assigned as Owner (not generic team)
- [ ] Priority/Status/Points visible in quick scan section
- [ ] One-line Quick Value statement for business impact
- [ ] 3+ Strategic Outcomes focused on measurable business results
- [ ] Dependencies resolved or explicitly managed
- [ ] Success metrics quantified or marked [NEEDS VERIFICATION]

**Roadmap Planning Focus Areas:**
- Strategic capabilities that advance business goals
- Customer outcomes suitable for stakeholder communication
- Operational metrics for executive dashboards
- Clear accountability through specific person ownership

**The /spec command uses this structure to assess strategic readiness and create detailed specifications.**