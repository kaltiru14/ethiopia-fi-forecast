# Data Enrichment Log — Task 1

**Author:** Kalkidan Belayneh Debas  
**Date:** 2026-01-30

This log documents all additional data points, events, or impact links added to the starter dataset for Ethiopia's financial inclusion forecasting project.

---

## 1. New Observation — Smartphone Penetration

| Field | Value |
|-------|-------|
| record_id | OBS_ENRICH_001 |
| record_type | observation |
| pillar | ENABLER |
| indicator | Smartphone penetration |
| indicator_code | ENB_SMARTPHONE_PCT |
| value_numeric | 28.0 |
| observation_date | 2023-01-01 |
| source_name | GSMA |
| source_url | https://www.gsma.com |
| confidence | medium |
| original_text | Smartphone penetration in Ethiopia reached approximately 28% in 2023. |
| collected_by | Kudu T |
| collection_date | 2026-01-30 |
| notes | Smartphone access enables app-based digital financial services. |

**Rationale for Addition:**
- Smartphone penetration is a key enabler for app-based digital payments.
- Provides the forecasting model context for infrastructure and behavioral enablers.

**Assumptions & Uncertainty:**
- Moderate effect assumed (28% penetration in 2023).
- Adoption may vary across regions, affecting actual usage.
- Scenario analysis will account for uncertainty in the forecasting stage.

---

## 2. New Event — Fayda Digital ID National Rollout

| Field | Value |
|-------|-------|
| record_id | EVT_ENRICH_001 |
| record_type | event |
| category | policy |
| event_name | Fayda Digital ID national rollout |
| event_date | 2023-06-01 |
| source_name | Government of Ethiopia |
| source_url | https://id.gov.et |
| confidence | medium |
| original_text | Ethiopia launched the Fayda Digital ID system to enable digital service access. |
| collected_by | Kudu T |
| collection_date | 2026-01-30 |
| notes | Digital ID reduces KYC barriers for account opening. |

**Rationale for Addition:**
- National digital ID improves access to financial accounts and reduces onboarding friction.
- Aligns with government initiatives and observed global patterns (e.g., Kenya’s digital ID impact on financial inclusion).

**Assumptions & Uncertainty:**
- Medium confidence because rollout speed and adoption may vary.
- Effect on account ownership will be modeled through an impact link.

---

## 3. New Impact Link — Digital ID → Account Ownership

| Field | Value |
|-------|-------|
| record_id | IMPACT_ENRICH_001 |
| record_type | impact_link |
| parent_id | EVT_ENRICH_001 |
| pillar | ACCESS |
| related_indicator | ACC_OWNERSHIP |
| impact_direction | positive |
| impact_magnitude | 0.15 |
| lag_months | 6 |
| evidence_basis | Comparable evidence from Kenya and Rwanda digital ID programs |
| confidence | medium |
| collected_by | Kudu T |
| collection_date | 2026-01-30 |
| original_text | Digital ID programs reduce onboarding friction for financial accounts. |
| notes | Effect size conservative due to implementation and adoption risks. |

**Rationale for Addition:**
- Links the new digital ID policy to measurable increase in account ownership.
- Uses evidence from similar emerging market implementations to inform magnitude.

**Assumptions & Uncertainty:**
- Moderate impact assumed (0.15) for Ethiopian market.
- Actual adoption may differ due to infrastructure, awareness, and policy implementation speed.
- Lag of 6 months applied to reflect realistic effect timing.

---

### Summary

- Added **1 new observation**, **1 new event**, and **1 impact link**.
- These enrichments provide historical context and enabler signals for forecasting digital financial inclusion in Ethiopia.
