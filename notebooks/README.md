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

