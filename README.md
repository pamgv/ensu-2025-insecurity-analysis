# ENSU 2025 – Perceived Insecurity Analysis

## Overview

This project presents an analytical study of the **ENSU 2025 (Encuesta Nacional de Seguridad Pública Urbana)** dataset, using all four quarterly releases.

The objective is to identify patterns in **perceived insecurity across urban areas in Mexico**, using structured survey data and transforming it into interpretable metrics and actionable insights.

---

## Objective

The analysis aims to:

- Measure perceived insecurity through a synthetic indicator
- Identify differences across cities, time, and demographics
- Detect structural patterns in insecurity perception
- Segment the population into distinct perception profiles

---

## Dataset

The dataset corresponds to ENSU 2025 and includes:

- ~20,000+ records per quarter
- ~240 variables per record
- Individual-level survey responses

Each row represents a respondent and includes:

- demographic information (sex, age)
- geographic data (state, municipality, city)
- perception of insecurity
- incivilities and environmental conditions
- trust in authorities

---

## Included outputs

The repository includes precomputed outputs such as summary tables and visualizations to allow quick validation of results without running the full pipeline.

---

## Dashboard

Link to Looker Studio dashboard:
https://lookerstudio.google.com/s/sL4Og72Runo

---

## Important Note on Data Structure

The original test description referenced datasets with **free-text fields**. However, the ENSU dataset is fully structured and does not include open text.

Therefore, the analytical approach was adapted from NLP-based methods to:

- feature engineering
- structured analysis
- clustering-based segmentation

---

## Methodology

The analysis was developed through the following steps:

1. Load and integrate the four quarterly datasets
2. Identify common variables across quarters
3. Select a relevant subset of features (31 variables)
4. Clean non-informative values
5. Build derived metrics:
   - `insecurity_score`
   - `insecurity_level`
   - `incivility_score`
   - `trust_score`
6. Perform descriptive analysis
7. Analyze relationships between variables
8. Apply clustering (K-Means) to identify profiles
9. Export results for reporting and visualization

---

## Feature Selection

Although **127 common variables** were identified across quarters, only a subset of **31 variables** was selected.

The selection focused on:

- perceived insecurity (core variables)
- incivilities (environmental context)
- trust in authorities
- demographic and geographic context

This approach:
- reduces noise
- improves interpretability
- keeps the analysis aligned with the main objective

---

## Data Cleaning (Critical Step)

During validation, it was identified that several perception variables (`BP1_2_*`) included:

- `3 = Not applicable`
- `9 = No answer`

Initially, these values were incorrectly treated as valid insecurity levels, which inflated the results.

They were explicitly removed from the analysis to ensure that the **insecurity score reflects only valid responses**.

---

## Key Features

### Insecurity Score

A continuous metric (1–2) representing perceived insecurity:

- based on the average of perception variables
- higher values → higher perceived insecurity

### Insecurity Level

Categorical representation:

- Low
- Medium
- High

### Incivility Score

Captures perception of antisocial behaviors and environmental disorder.

### Trust Score

Represents confidence in security-related institutions.

---

## Key Insights

- Perceived insecurity is **significant but not dominant**, with ~39% in the high category
- The phenomenon is **heterogeneous**, not uniform across the population
- A **slight upward trend** is observed across 2025
- **Women consistently report higher insecurity than men**
- Insecurity is **geographically concentrated** in specific cities
- Clustering reveals **distinct perception profiles**, not a single pattern

---

## Project Structure

```text
conversation-intelligence-analyst-test/
│
├── data/
│   ├── raw/                  # Original ENSU ZIP files
│   └── processed/            # Consolidated and processed datasets
│
├── notebooks/
│   ├── 01_ensu_analysis.ipynb
│   └── 02_ensu_analysis_final.ipynb
│
├── outputs/
│   ├── figures/              # Exported charts
│   └── tables/               # Exported summary tables
│
├── report/
│   └── final_report.pdf
│
├── src/
│   ├── __init__.py
│   ├── load_data.py
│   ├── preprocess.py
│   ├── features.py
│   └── visualize.py
│
├── README.md
└── requirements.txt

---

## How to Run

1. Place ENSU ZIP files in:
data/raw/

2. Open the final notebook:
notebooks/02_ensu_analysis_final.ipynb

3. Run all cells from top to bottom

The notebook will:
- load and clean data
- generate features
- perform analysis
- export tables and figures
- produce a dashboard-ready dataset

---

## Outputs

Main outputs include:

- `ensu_2025_all_quarters.csv`
- `ensu_2025_model_final.csv`
- `dashboard_data_final.csv`
- summary tables (CSV)
- visualizations (PNG)

---

## Dashboard

A Looker Studio dashboard was built to explore:

- overall insecurity score
- distribution of levels
- temporal evolution
- city comparison
- gender differences
- cluster segmentation

---

## Tools Used

- Python
- pandas
- scikit-learn
- matplotlib
- Looker Studio

Additionally, **ChatGPT was used as a support tool** for:

- structuring the workflow
- refining analytical ideas
- improving code organization
- enhancing documentation clarity

All analytical decisions and validations were performed manually.

---

## Final Notes

This project adapts to real-world data constraints, demonstrating:

- critical thinking in data validation
- ability to adjust methodology
- structured analytical reasoning
- clear communication of insights

The result is a reproducible and interpretable analysis aligned with the original objective of extracting meaningful insights from real data.
