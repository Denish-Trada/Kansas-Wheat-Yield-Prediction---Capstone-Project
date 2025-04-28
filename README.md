# Kansas Wheat Yield Prediction — Capstone Project
#### Author: Denish Trada
#### GitHub: https://github.com/Denish-Trada/Kansas-Wheat-Yield-Prediction---Capstone-Project
---

## 📄 Project Overview

This repository contains the end-to-end analysis and predictive modeling for forecasting wheat crop yields in Kansas.  
The project addresses yield variability by integrating multi-source datasets including county-level wheat yield data, growing season climate data, static soil characteristics, and satellite-derived vegetation health indices (NDVI) from 2010–2020.

---

## 🎯 Problem Area

- **Challenge:**  
  Wheat yield prediction is inherently complex due to natural climate variability, soil heterogeneity, and operational factors (irrigation, crop management practices).  
  These challenges create **economic uncertainty** for farmers and **planning difficulties** for policymakers and agribusinesses.

- **Affected Stakeholders:**  
  - **Kansas Farmers:**  
    Optimize irrigation, fertilizer application, and planting decisions based on better yield forecasts.
  - **Agricultural Policymakers:**  
    Guide funding, crop insurance, and resource allocation policies more accurately.
  - **Local Agribusinesses:**  
    Improve logistics and supply chain risk management by anticipating yield fluctuations.

---

## 💡 Proposed Data Science Solution

- **Data Integration:**  
  Combine historical wheat yield, multi-year climate records, county-level soil features, and NDVI vegetation health indices.

- **Exploratory Data Analysis (EDA):**  
  Perform descriptive statistics, missing data analysis, outlier detection, feature distribution visualization, and feature-target relationship mapping.

- **Baseline Modeling:**  
  Build initial predictive models using Linear Regression, Decision Tree Regressor, and Random Forest Regressor.  
  Evaluate baseline performance to set a reference point for future modeling improvements.

- **Feature Engineering:**  
  Create engineered features such as:
  - Soil quality composite score
  - Slope average
  - Temperature × Precipitation interaction term
  - Lagged Yield (if available)

- **Outcome:**  
  Provide actionable insights into factors driving wheat yield variability, establishing a scalable predictive modeling framework.

---

## 🌎 Impact of the Solution

- **Economic Efficiency:**  
  Improved forecasts help farmers allocate inputs efficiently, reducing waste and stabilizing income.

- **Environmental Sustainability:**  
  Targeted resource use minimizes emissions, soil degradation, and water resource depletion.

- **Policy Formulation:**  
  Data-driven models can support government policies on food security, crop insurance, and climate adaptation strategies.

---

## 📚 Dataset Description

The project uses the following key datasets:

| Dataset | Source | Description |
|:--------|:-------|:------------|
| Wheat Yield / County Data | USDA NASS | Annual wheat yield (bu/acre) per Kansas county |
| Climate Data | NASA / NOAA | Growing season temperature, precipitation |
| Soil Characteristics | Kaggle (US Drought Data) | County-level slope, elevation, aspect, land use, soil fertility |
| NDVI Vegetation Health Data | MODIS (NASA LP DAAC) | April–August mean NDVI values per county |

---

## 📂 Expanded Data Dictionary

| **Variable Name**           | **Description**                                                | **Data Type** | **Units / Notes** |
|:-----------------------------|:---------------------------------------------------------------|:--------------|:------------------|
| `County`                     | County name in Kansas                                           | String        | Merged key |
| `Year`                       | Observation year                                                | Integer       | 2010–2020 |
| `Yield`                      | Wheat yield                                                     | Float         | Bushels per acre |
| `Growing_Season_Temp_C`       | Avg temperature during growing season (Apr–Aug)                | Float         | Degrees Celsius |
| `Growing_Season_Precip_mm`    | Total precipitation during growing season                     | Float         | Millimeters (mm) |
| `soil_quality_score`          | Composite score across 7 soil fertility indices (SQ1–SQ7)      | Float         | Dimensionless |
| `slope_avg`                   | Average terrain slope across 8 slope categories                | Float         | Percent (%) |
| `temp_precip_interaction`     | Feature engineering: Temperature × Precipitation              | Float         | Derived unit |
| `lag_yield`                   | Yield of previous year (if available)                          | Float         | Temporal dependency feature |
| `NDVI`                        | Vegetation health index for growing season                     | Float         | NDVI (0–1 scale) |
| `CV (%)`                      | Coefficient of variation in yield (survey-based)               | Float         | Optional quality check |

✅ *Note:* Additional slope features (`slope1`–`slope8`), aspect features (`aspectN`, `aspectS`, etc.), and land cover types were aggregated as part of feature engineering.

---

## 🗂️ Project Organization

```plaintext
Kansas-Wheat-Yield-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│       └── final_merged_cleaned.csv
│
├── notebooks/
│   ├── Sprint 2 - Denish_Trada_Kansas_Wheat _Yield_Prediction
│   └── Baseline_Modeling_Denish_Trada.ipynb