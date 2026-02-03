**Objective**
-------------

The objective of Task 1 is to explore the starter dataset on Ethiopia’s financial inclusion, understand its structure, and enrich it with additional data that can help improve forecasting of key indicators: **Access (Account Ownership)** and **Usage (Digital Payment Adoption)**.

**Dataset Overview**
--------------------

The starter dataset is provided in ethiopia\_fi\_unified\_data.xlsx and includes two sheets:

1.  **ethiopia\_fi\_unified\_data** — contains:
    
    *   **observations**: survey-reported values (e.g., Findex surveys, operator data)
        
    *   **events**: policy changes, product launches, infrastructure developments, milestones
        
    *   **targets**: official policy goals
        
2.  **Impact\_sheet** — contains modeled **impact\_links** showing how events influence inclusion indicators.
    

**Supporting file:** reference\_codes.xlsx — lists valid values for categorical fields.

**Exploratory Data Analysis**
-----------------------------

*   **Records by type:**
    
    *   Observation: 30
        
    *   Event: 10
        
    *   Target: 3
        
*   **Records by pillar:**
    
    *   ACCESS: 16
        
    *   USAGE: 11
        
    *   NaN (mostly events): 10
        
    *   GENDER: 5
        
    *   AFFORDABILITY: 1
        
*   **Temporal coverage:**
    
    *   Observations span from 2011 to 2025.
        
*   **Events of note:**
    
    *   First mobile money service launch: May 2021
        
    *   National financial inclusion strategy: Sep 2021
        
    *   M-Pesa market entry: Aug 2023
        
    *   National digital ID system: Jan 2024
        
*   **Impact links:**
    
    *   Relationships between events and indicators captured in Impact\_sheet.
        
    *   Existing links reviewed; new impact link added for smartphone penetration effect on digital payment usage.
        

**Data Enrichment**
-------------------

### **New Impact Link Added**

*   **Event:** REC\_ENRICH\_001 (Smartphone penetration impact)
    
*   **Indicator:** USG\_DIGITAL\_PAYMENT
    
*   **Pillar:** USAGE
    
*   **Impact magnitude:** +0.20 (positive)
    
*   **Lag:** 12 months
    
*   **Evidence:** Kenya, Rwanda, and GSMA reports
    
*   **Notes:** Accounts for smartphone penetration enabling digital payments. Conservative estimate due to P2P dominance, low POS/QR density, and affordability constraints.
    
*   **Confidence:** High
    

This addition ensures the forecasting model considers key infrastructure and behavioral enablers.

**Files Produced**
------------------

*   data\_enrichment\_log.md — documents all additions and rationale.
    
*   Updated df\_impact including the new impact link.
    
*   Task 1 notebook (notebooks/task1\_data\_exploration.ipynb) with:
    
    *   Data loading
        
    *   Schema exploration
        
    *   Basic EDA (counts, temporal coverage, event list)
        
    *   Data enrichment steps
        

**Next Steps**
--------------

*   Proceed to **Task 2 — Exploratory Data Analysis & Visualization**:
    
    *   Explore indicator trends
        
    *   Visualize account ownership and digital payment usage
        
    *   Identify potential leading indicators and gaps
# Task 2 — Exploratory Data Analysis (EDA)
## Objective
Perform exploratory data analysis on the enriched Ethiopia financial inclusion dataset to identify trends, patterns, and factors influencing access and usage of financial services. Insights from this task will guide forecasting and impact modeling.

## Overview
This task covers:
- Dataset overview and quality assessment
- Analysis of access (account ownership) trends
- Analysis of digital payments usage
- Examination of infrastructure and enablers
- Event timeline visualization
- Correlation analysis between indicators
- Documentation of key insights

## Steps Taken

### 1. Dataset Overview
- Summarized data by `record_type`, `pillar`, and `source_type`.
- Examined temporal coverage of observations (2011–2024).
- Assessed data quality using confidence levels.
- Identified indicators with sparse coverage or missing data.

### 2. Access Analysis
- Plotted account ownership trajectory over time.
- Calculated growth rates between survey years.
- Explored gender and urban-rural differences where data was available.
- Investigated slowdown in account ownership growth between 2021–2024.

### 3. Usage Analysis
- Plotted trends in mobile money account penetration.
- Examined adoption patterns for digital payments.
- Explored gaps between registered and active accounts (where data was available).
- Reviewed P2P and merchant payment trends.

### 4. Infrastructure and Enablers
- Analyzed infrastructure indicators: 4G coverage, mobile penetration, ATM density.
- Explored relationships between infrastructure and inclusion outcomes.
- Identified potential leading indicators for future account ownership trends.

### 5. Event Timeline & Visual Analysis
- Created timeline visualization of all cataloged events.
- Overlayed key events (e.g., Telebirr launch, M-Pesa entry, Safaricom market entry) on indicator trends.
- Visually assessed apparent relationships between events and inclusion outcomes.

### 6. Correlation Analysis
- Generated correlation matrix for numeric indicators.
- Identified which factors are most strongly associated with Access and Usage.
- Reviewed existing `impact_link` records for additional insights.

### 7. Key Insights
1. Account ownership has steadily increased from 2011–2020, with slower growth post-2021 despite mobile money expansion.
2. Gender gap persists but shows slight improvement over time.
3. Mobile money adoption is highly influenced by infrastructure (mobile coverage, smartphone penetration).
4. Key policy and product events (Telebirr launch, M-Pesa entry) appear to correlate with usage spikes.
5. Certain indicators (4G coverage, mobile penetration) are potential leading predictors for forecasting Access and Usage.

## Notes
- Missing or malformed dates were handled using `pd.to_datetime(..., errors='coerce')`.
- Duplicate entries were addressed with aggregation when pivoting for correlation analysis.
- Visualizations account for missing or `NaT` values to prevent plotting errors.

# Task 3: Event Impact Modeling

## Objective
Model how national events (policies, product launches, and infrastructure investments)
affect financial inclusion indicators in Ethiopia.

This task links major events to Access and Usage indicators and translates qualitative
impact assessments into a quantitative event–indicator impact model.

---

## Contents
- `notebooks/task_3_event_impact_modeling.ipynb`  
  Jupyter notebook implementing the event impact model and association matrix.

---

## Approach
1. Loaded the `Impact_sheet` and joined it with event records using `parent_id`.
2. Identified which events affect which financial inclusion indicators.
3. Converted qualitative impact magnitudes (high, medium, low) into estimated
   percentage-point effects.
4. Built an event–indicator association matrix summarizing the estimated impact
   of each event on each indicator.
5. Validated model outputs against historical data where available
   (e.g., Telebirr launch and mobile money adoption).

---

## Modeling Assumptions
- Event impacts occur after a short lag and persist over time.
- Impacts from multiple events affecting the same indicator are additive.
- Where Ethiopian pre/post data is limited, estimates are informed by comparable
  country evidence.
- The model is associative and intended for scenario analysis, not causal inference.

---

## Outputs
- Event–indicator association matrix (table and heatmap)
- Estimated impact sizes for key financial inclusion indicators
- Sanity check against historical mobile money adoption data

---

## Status
Analysis complete. Documentation may be refined in later iterations.

Task 4: Forecasting Account Ownership and Digital Payment Usage (2025–2027)
===========================================================================

Objective
---------

Forecast **Account Ownership (Access)** and **Digital Payment Usage** for Ethiopia over 2025–2027 using trend analysis and scenario modeling.

Data
----

*   Source: ethiopia\_fi\_unified\_data\_enriched.xlsx (Ethiopia financial inclusion dataset)
    
*   Indicators used:
    
    *   **Access:** ACC\_OWNERSHIP (% of adults with an account at a financial institution or mobile money)
        
    *   **Usage:** Digital payment proxies (including mobile money usage indicators)
        
*   Historical data is sparse (5 points for Findex over 13 years for access; usage is proxy-based)
    

Approach
--------

1.  **Trend Regression**
    
    *   Linear regression fitted on historical year vs value\_numeric data for each indicator.
        
    *   Projected baseline values for 2025–2027.
        
2.  **Scenario Analysis**
    
    *   **Pessimistic:** small decrease in adoption/usage
        
    *   **Base:** trend continuation
        
    *   **Optimistic:** accelerated adoption/usage
        
    *   Scenario adjustments applied to baseline values.
        
3.  **Forecast Table**
    
    *   Includes baseline projections and scenario ranges for each indicator.
        
4.  **Visualization**
    
    *   Line plots for Access and Usage under each scenario.
        

Forecast Table (Baseline and Scenario Ranges)
---------------------------------------------

| Year | Access Baseline (%) | Access Min | Access Max | Usage Baseline (proxy) | Usage Min  | Usage Max  |
|------|-------------------|------------|------------|----------------------|------------|------------|
| 2025 | 58.62             | 57.12      | 60.62      | 4.45e+11             | 3.78e+11   | 5.12e+11   |
| 2026 | 61.83             | 60.33      | 63.83      | 8.90e+11             | 7.57e+11   | 1.02e+12   |
| 2027 | 65.05             | 63.55      | 67.05      | 1.33e+12             | 1.13e+12   | 1.53e+12   |


> **Note:** Usage values are proxy-based; ranges reflect ±15% due to data sparsity.

Interpretation
--------------

*   **Access (Account Ownership)** is projected to increase steadily from ~58.6% (2025) to ~65.1% (2027).
    
*   **Digital Payment Usage** shows rapid growth, consistent with expansion of mobile money and fintech adoption.
    
*   **Key Influencers:**
 
    *   Mobile money platforms (e.g., Telebirr)
    *   Policy initiatives for digital financial services
    *   Telecom and infrastructure developments
        
*   **Uncertainty:**
    
    *   Sparse historical data for trend fitting
    *   Proxy indicators for digital payment usage  
    *   Scenario ranges provide indicative bounds; confidence intervals were not calculated.
        

Files in Task 4
---------------

*   task4\_forecasting.ipynb → Notebook containing:
    
    *   Data preparation
    *   Trend fitting
    *   Baseline and scenario forecasts
    *   Plots and interpretation
        
*   README.md → This documentation

# Task 5 – Financial Inclusion Dashboard & Forecasting (Ethiopia)

## Overview
This task delivers an **interactive Streamlit dashboard** that visualizes trends and short-term forecasts for **financial inclusion in Ethiopia**.  
The dashboard integrates cleaned survey indicators and transaction-based proxy data to support **exploratory analysis, scenario forecasting, and policy-relevant insights**.

The focus is on:
- Account ownership trends
- Usage proxies for digital payments
- Simple, explainable forecasts with scenario ranges (no confidence intervals)

---

## Objectives
- Build an interactive dashboard using **Streamlit**
- Present key financial inclusion indicators clearly
- Forecast account ownership for **2025–2027**
- Communicate uncertainty using **scenario ranges**
- Document assumptions and limitations transparently

---

## Data Sources
- **Primary dataset**:  
  `ethiopia_fi_unified_data_enriched.xlsx`

- **Key indicators used**
  - Account ownership (% of adults)
  - Digital payment usage (proxy indicators only)
  - P2P and ATM transaction counts

> ⚠ Survey-based digital usage percentages are not consistently available.  
> Transaction-based indicators are therefore used as **proxies**, not direct adoption rates.

---

## Dashboard Structure

### 1. Overview
- Latest account ownership value
- Digital payment usage availability check
- P2P / ATM transaction crossover ratio
- High-level insights and trends

### 2. Trends
- Interactive time-series visualization
- User-controlled year range slider
- Focus on account ownership growth over time

### 3. Forecasts (2025–2027)
- Linear trend model based on historical account ownership
- Scenario-based projections:
  - **Pessimistic**
  - **Base**
  - **Optimistic**
- Forecast results displayed as:
  - Table
  - Line chart

> ⚠ Scenario ranges are used; confidence intervals (CI) are intentionally excluded.

### 4. Inclusion Projections
- Comparison of forecast scenarios against a **60% inclusion target**
- Visual assessment of progress under different assumptions
- Discussion of uncertainties, impacts, and limitations

---

## Forecasting Methodology
- **Model**: Linear Regression
- **Target variable**: Account Ownership (%)
- **Forecast horizon**: 3 years (2025–2027)

### Scenario Design
| Scenario      | Adjustment |
|---------------|------------|
| Pessimistic   | −1.5 pp    |
| Base          | 0.0 pp     |
| Optimistic    | +2.0 pp    |

This approach prioritizes **interpretability and transparency** over complexity.

---

## Error Handling & Data Validation
The dashboard includes:
- Safe data loading with fallback handling
- Empty dataset checks
- Minimum data requirements for forecasting
- Graceful warnings when data is unavailable

Example:
- Digital payment usage shows **“Data unavailable”** when no survey-based percentage exists.

---

## Limitations
- Linear trend assumption may oversimplify real-world dynamics
- Digital payment usage measured via proxy indicators
- Sparse historical survey data
- No causal inference
- ⚠ Channel comparison is minimal (but not mandatory) due to inconsistent indicator coverage

---

## How to Run the Dashboard

```bash
cd dashboard
streamlit run app.py
