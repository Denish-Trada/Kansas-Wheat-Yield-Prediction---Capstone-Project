# Kansas Wheat Yield Prediction – Data Science Capstone

**Author:** Denish Trada  
**Project:** Predicting Kansas Wheat Yield Using Environmental and Climate Data  
**Submission:** BrainStation Data Science Capstone, 2025
**GitHub:** https://github.com/Denish-Trada/Kansas-Wheat-Yield-Prediction---Capstone-Project

---

## 🌾 Project Summary

Accurate prediction of wheat crop yields is crucial for farm profitability, food security, and supply chain planning in Kansas and beyond.  
This project leverages 10 years of historical county-level wheat yield, weather, and soil data to build robust, interpretable machine learning models for yield forecasting.  
The final solution is delivered both as a transparent Jupyter notebook workflow and a user-friendly web dashboard, enabling actionable insights and scenario planning for growers, cooperatives, and agribusiness leaders.

---

## 📈 Problem Statement

**How can we predict wheat yield (tons per hectare) for Kansas counties, using historical weather, soil, and farm management data?**  
Key goals:
- Enable data-driven decisions for Kansas wheat farmers, cooperatives, and advisors.
- Identify the most impactful, actionable yield drivers.
- Deliver a transparent model and digital product that is practical for real-world use.

---

## 🗃️ Dataset Overview

**Source:**  
10 years (2010–2020) of county-level data for Kansas, including:
- Wheat yield records (tons per hectare)
- Climate variables (rainfall, temperature, weather condition)
- Soil type and region
- Management practices (fertilizer and irrigation use)

**Size:** 166,640 records, 10 columns

---

## 📑 Final Data Dictionary

| Column                   | Description                                                        | Data Type   | Example Value      |
|--------------------------|--------------------------------------------------------------------|-------------|--------------------|
| Region                   | Geographic region within Kansas                                    | Categorical | "west"             |
| Soil_Type                | Dominant soil type in the field                                   | Categorical | "clay"             |
| Crop                     | Crop type (filtered to "wheat")                                   | Categorical | "wheat"            |
| Rainfall_mm              | Total rainfall during growing season (mm)                         | Float       | 950.2              |
| Temperature_Celsius      | Average temperature during growing season (°C)                    | Float       | 22.8               |
| Fertilizer_Used          | Whether fertilizer was used (True/False)                          | Boolean     | True               |
| Irrigation_Used          | Whether irrigation was used (True/False)                          | Boolean     | False              |
| Weather_Condition        | Generalized weather descriptor                                    | Categorical | "cloudy"           |
| Days_to_Harvest          | Number of days from planting to harvest                           | Integer     | 120                |
| Yield_tons_per_hectare   | Observed wheat yield at harvest (target variable)                 | Float       | 7.23               |

---

## 🧠 Approach

1. **Data Wrangling:**  
   - Cleaned, validated, and merged all raw data sources.
   - Built a consistent schema for machine learning and business use.

2. **Exploratory Data Analysis (EDA):**  
   - Applied formal hypothesis testing, visual analytics, and feature selection.
   - Identified **rainfall** and **fertilizer use** as the dominant, actionable yield drivers.

3. **Modeling:**  
   - Developed and benchmarked multiple regression models: linear, ridge, lasso, random forest.
   - Performed extensive cross-validation and hyperparameter tuning.
   - Used SHAP explainability to visualize and interpret model decisions.

4. **Scenario Analysis:**  
   - Simulated “what if” scenarios to show how changes in rainfall or fertilizer use impact yield.

5. **Productization:**  
   - Developed a Streamlit web dashboard allowing end-users to input scenarios, see predictions, and get actionable recommendations and feature driver explanations.

---

## 🌟 Key Highlights

- **Model Accuracy:**  
  - Final model (Ridge Regression): **R² = 0.78**, **RMSE = 0.79 tons/ha**
  - Delivers reliable yield forecasts with clear, business-focused interpretability.

- **Top Insights:**  
  - **Rainfall** is the single strongest predictor of yield.
  - **Fertilizer use** consistently boosts yields by about 1.5 tons/ha.
  - Other variables (region, soil type, weather condition, temperature) had minimal impact in this dataset.

- **Business Value:**  
  - Farmers and co-ops can focus on rainfall monitoring and optimal fertilizer use for the best ROI.
  - Dashboard delivers instant, transparent yield forecasts and “what if” scenario planning.
  - Project empowers evidence-based decision making, with explainability for stakeholder trust.

---

## 🧭 Project Navigation

### **Files and Workflow**

- **1. Data Wrangling.ipynb**  
  Data import, cleaning, merging, and initial schema alignment.

- **2. Data Preprocessing & EDA.ipynb**  
  Data dictionary, preprocessing, EDA, formal hypothesis testing.

- **3. Baseline Modeling.ipynb**  
  Baseline regression models and metric evaluation.

- **4. Advanced Modeling Interpretation - EDA & Hypothesis Testing.ipynb**  
  Feature selection, refined EDA, cumulative statistical justification.

- **5. [Final Modeling Notebook].ipynb**  
  Advanced modeling (ridge/lasso/random forest), cross-validation, SHAP explainability, scenario analysis, business recommendations.

- **app.py**  
  Streamlit dashboard demo for scenario planning and business-facing recommendations.

- **shap_summary.png**  
  SHAP feature importance plot (used in the dashboard).

- **README.md**  
  (This file) – Project summary, instructions, results, and navigation.

---

### **How to Run the Project**

1. **Review notebooks in order:**  
   - Each notebook is modular and includes markdown explaining the thought process and reasoning behind every key step.
2. **For the dashboard demo:**  
   - Open your terminal.
   - Navigate to this project folder.
   - Run: `streamlit run app.py`
   - Interact with the app to explore scenario planning, predictions, SHAP impacts, and recommendations.

---

## 📌 Results for Stakeholders

- **For Farmers/Advisors:**  
  Use the dashboard for yield forecasts and scenario planning based on current rainfall and fertilizer strategy.

- **For Analysts/Researchers:**  
  Transparent workflow for EDA, modeling, and validation; fully reproducible.

- **For Business Leaders:**  
  Clear summary of drivers, model performance, and next steps for digital agriculture innovation.

---

## 🔮 Next Steps & Future Opportunities

- Integrate real-time weather APIs or higher-frequency climate data.
- Expand modeling to other crops or geographies.
- Add more business features (risk alerts, downloadable reports, integration with farm management systems).

---

## 🙏 Acknowledgments

Thanks to BrainStation, all instructor - Arun Marria & Ayon Ghosh, Teaching assistants - Reema Sipra & Clement Chan and Kansas wheat growers whose insights and challenges inspired this project.
---


