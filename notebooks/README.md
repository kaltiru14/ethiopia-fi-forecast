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