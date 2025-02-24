# Kansas-Wheat-Yield-Prediction---Capstone-Project
## Project Overview

This repository contains the end-to-end analysis and predictive modeling for forecasting wheat crop yields in Kansas. The project was designed to address the challenge of yield variability by integrating county-level wheat yield data with climate data spanning 2010–2020. 

### Problem Area
- **Challenge:**  
  Predicting wheat crop yields in Kansas is complex due to natural climate variability, resource allocation differences, and inherent data gaps. This variability directly affects the profitability and sustainability of farming operations.
- **Affected Stakeholders:**  
  - **Kansas Farmers:** Gain insights to optimize irrigation, fertilizer usage, and planting schedules.  
  - **Agricultural Agencies & Policymakers:** Leverage predictions to design targeted interventions, support sustainable farming practices, and improve resource management.  
  - **Local Agribusinesses:** Use forecasts for better logistical planning and to mitigate risk in supply chain operations.

### Proposed Data Science Solution
- **Data Integration:**  
  Combine historical wheat yield/county data with multi-year climate records.
- **Exploratory Analysis:**  
  Utilize descriptive statistics, interactive visualizations (histograms, box plots, scatter plots, time-series graphs, and geospatial maps), and data sanity checks to uncover key patterns and outliers.
- **Advanced Modeling:**  
  Implement regression models, statistical hypothesis testing, and clustering to capture the relationships between climate variables and yield outcomes. Feature engineering techniques (e.g., creation of lag variables and interaction terms) are applied to enhance predictive performance.
- **Outcome:**  
  The analysis provides actionable insights that can lead to more accurate yield predictions, ultimately helping stakeholders optimize resource allocation and reduce economic risk.

### Impact of the Solution
- **Economic Efficiency:**  
  Improved yield prediction accuracy can help reduce input costs, prevent resource misallocation, and stabilize farm incomes.
- **Environmental Benefits:**  
  Optimized resource use (e.g., water and fertilizer) minimizes waste, reducing emissions and promoting sustainable practices.
- **Policy Formulation:**  
  Data-driven insights can support policy decisions that enhance food security and promote climate adaptation strategies in agricultural planning.

---

## Dataset Description

The project uses the following key datasets:

- **Wheat Yield/County Data:**  
  Contains county-level wheat yield statistics in Kansas, including measurements in bushels per acre.
  
- **Climate Data (2010–2020):**  
  Comprises climate variables such as average temperature, precipitation, and summer rainfall relevant to the growing season.

### Data Dictionary

| **Variable Name**         | **Description**                                                                          | **Data Type** | **Units/Notes**                                |
|---------------------------|------------------------------------------------------------------------------------------|---------------|------------------------------------------------|
| `county`                  | County name in Kansas                                                                    | String        | Primary geographic identifier                  |
| `year`                    | Year of observation                                                                      | Integer       | 2010-2020                                      |
| `wheat_yield`             | Wheat yield per county                                                                   | Float         | Measured in bushels per acre                   |
| `avg_temp`                | Average temperature during the growing season                                            | Float         | Degrees Fahrenheit                             |
| `precipitation`           | Total precipitation during the growing season                                            | Float         | Inches                                         |
| `summer_rainfall`         | Rainfall during the peak growing months                                                  | Float         | Inches                                         |
| `soil_quality`            | Qualitative measure of soil quality (if available)                                       | Categorical   | e.g., Poor, Fair, Good, Excellent              |
| `additional_climate_var`  | Placeholder for any additional climate variable introduced during advanced analysis       | Varies        | Specify unit during analysis                   |
| `lag_yield`               | Yield of the previous year (derived feature)                                             | Float         | Supports temporal dependency analysis          |

*Note: The data dictionary has been refined post-initial data inspection to include derived features and granular data definitions for clarity and reproducibility.*

---

## Repository Structure & Contents

- **Jupyter Notebooks:**  
  Contains detailed exploratory data analysis (EDA), advanced analytical techniques, and predictive modeling steps.
  
- **Data Files:**  
  - `wheat_yield_county_data.csv` – Wheat yield data by county.
  - `climate_data_2010_2020.xlsx` – Historical climate data for the growing season.
  
- **Documentation:**  
  This README file and inline notebook documentation provide a comprehensive overview of the project rationale, methodology, and findings.

