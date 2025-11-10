# Causal Impact of Delivery Delays on Customer Satisfaction
### A Causal Inference and Uplift Modeling Project Using the Olist E-commerce Dataset  
Author: **Xuhui Liu** (UIUC Statistics PhD)

---

## Project Overview

This project measures the **causal effect** of delivery delays on customer satisfaction using the Olist public e-commerce dataset (110k+ orders).  
The goal is to estimate how much late delivery reduces review scores and to identify customer segments that are particularly sensitive to delays.

This framework closely aligns with real business challenges faced by companies such as Uber, Instacart, DoorDash, Amazon Logistics, Airbnb, and Booking.com.

### Treatment Definition

An order is considered late when:

T = 1 if actual_delivery_date > estimated_delivery_date
T = 0 otherwise

### Core Methods Used

- Propensity Score Estimation  
- Inverse Probability Weighting (IPW)  
- Augmented IPW (AIPW, doubly-robust)  
- Causal Forest (for heterogeneous treatment effects / CATE)  
- Uplift Modeling for business targeting optimization  

---

## Goals

This project aims to:

1. Estimate **average treatment effect (ATE)** of delivery delay on review score.  
2. Improve covariate balance using **propensity score models** and **IPW weighting**.  
3. Use **AIPW** to obtain doubly-robust causal impact estimates.  
4. Estimate **heterogeneous treatment effects (HTE)** using causal forests.  
5. Recommend a **targeting strategy** based on uplift scores to maximize financial ROI.  

---

## Repository Structure
```text
causal-impact-delivery-delay-olist/
│
├── data/
│   ├── raw/                    # Original Olist datasets
│   ├── interim/                # Cleaned, merged tables
│   └── processed/              # Modeling-ready datasets
│
├── notebooks/
│   ├── 01_eda.ipynb                    # Exploratory data analysis
│   ├── 02_treatment_definition.ipynb   # Treatment, outcome, confounders
│   ├── 03_propensity_model.ipynb       # Propensity scores and covariate balance
│   ├── 04_ipw_aipw_estimation.ipynb    # ATE/ATT/ATC estimation
│   ├── 05_causal_forest_uplift.ipynb   # HTE and uplift modeling
│   ├── 06_sensitivity_analysis.ipynb   # (optional)
│   └── 07_business_impact.ipynb        # ROI analysis and targeting optimization
│
├── src/
│   ├── data/                # Data loading, merging, cleaning
│   ├── models/              # PS models, causal estimators
│   ├── utils/               # Helper functions
│   └── visualization/       # Plotting utilities
│
├── reports/
│   ├── report.md                      # Final written summary
│   ├── summary_at_optimal_K.csv       # Targeting results
│   └── figures/                       # Exported charts
│
├── environment.yml         # Reproducible conda environment
├── LICENSE
└── README.md
```

## Main Results

### Causal Effects (AIPW / IPW)

| Estimator | Estimated Effect on Review Score | 95% CI |
|----------|----------------------------------|--------|
| AIPW ATE | −1.64 | (−1.69, −1.58) |
| IPW ATE  | −1.52 | similar range |

Late delivery reduces customer review score by approximately:

**1.6 stars on average**

This is a large and economically meaningful impact.

---

## Heterogeneous Treatment Effects (CATE)

Using Causal Forests, we identify segments with the largest sensitivity to delay:

- Certain **fashion** categories  
- **Media** categories (DVDs, Blu-Ray)  
- Specific customer states  
- Certain payment types  

The top 10% most sensitive customers show extremely negative reactions to delays.

---

## Business Impact and ROI

A targeted intervention strategy based on uplift scores was evaluated.

### Economic assumptions
- Value per 1-point review improvement: **1.25 USD**
- Intervention cost per customer: **2.00 USD**

### Optimal Targeting Strategy

| Metric | Value |
|--------|--------|
| Targeting share | 30% |
| Customers targeted | 33,231 |
| Total benefit | 306,303 USD |
| Total cost | 66,462 USD |
| Net gain | 239,841 USD |
| ROI | 3.61 |

### Interpretation

Targeting only the top 30% high-sensitivity customers yields:

- Substantial net financial benefit  
- High ROI  
- Efficient resource allocation  
- Reduction of negative review risk  

---

## Reproducibility

Create the environment:
conda env create -f environment.yml
conda activate olist-causal

Run notebooks in order:
01 → 02 → 03 → 04 → 05 → 07

