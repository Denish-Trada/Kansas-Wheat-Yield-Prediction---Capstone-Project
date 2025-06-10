import streamlit as st
import pandas as pd

# --- Demo prediction function (replace coefficients with your real model's if desired) ---
def predict_yield(rainfall, fertilizer_used):
    # Example: based on your Ridge Regression model
    return 2.2 + 0.0035 * rainfall + 1.5 * fertilizer_used

# --- Persona/Intro Section ---
st.title("Kansas Wheat Yield Forecast Demo")
st.markdown("""
👩‍🌾 *Meet Sarah: a Kansas wheat farmer and co-op leader planning her season.*  
This demo dashboard empowers Sarah (and all Kansas growers) to make smarter, data-driven yield decisions.
""")

# --- User Input Section ---
st.header("Your Field Scenario")
rainfall = st.slider("Rainfall during growing season (mm)", 100, 1000, 550)
fertilizer = st.selectbox("Fertilizer Applied?", ["Yes", "No"])
fertilizer_val = 1 if fertilizer == "Yes" else 0

# --- Prediction & Advice ---
if st.button("Predict Wheat Yield"):
    pred_yield = predict_yield(rainfall, fertilizer_val)
    st.metric(label="Predicted Yield (tons/hectare)", value=f"{pred_yield:.2f}")
    st.write("---")
    
    # Actionable advice
    if fertilizer_val == 0:
        st.warning("Tip: Applying fertilizer typically increases yield by about 1.5 tons/ha.")
    if rainfall < 350:
        st.info("Rainfall is low this season—consider risk management or alternate strategies.")
    
    # Scenario Table
    scenarios = pd.DataFrame({
        "Scenario": ["Your Input", "Low Rainfall", "High Rainfall"],
        "Rainfall_mm": [rainfall, 200, 900],
        "Fertilizer_Used": [fertilizer_val, fertilizer_val, fertilizer_val],
    })
    scenarios["Predicted_Yield"] = scenarios.apply(lambda row: predict_yield(row.Rainfall_mm, row.Fertilizer_Used), axis=1)
    st.write("### Scenario Comparison Table")
    st.dataframe(scenarios)

    # SHAP plot (static image)
    st.write("### What Drives Your Yield Forecast?")
    st.image("shap_summary.png", caption="SHAP Summary: Feature impacts on yield", use_column_width=True)

    # Recommendations and explanation
    st.write("### Recommendations Based on Your Scenario")
    if pred_yield >= 6:
        st.success("🎉 Expected yield is excellent! Maintain your current practices, and consider sharing insights with your co-op.")
    elif 4 <= pred_yield < 6:
        st.info("Yield is within the average range. Ensure your fertilizer application is optimal, and monitor rainfall forecasts for risk.")
    else:
        st.warning("Yield forecast is below average. Consider consulting with your local advisor on soil management, alternative crops, or irrigation options if available.")

    st.write("""
    **Result Explanation:**  
    - Your predicted yield is calculated based on the model's learned relationships: rainfall is the largest driver, followed by fertilizer use.
    - The SHAP plot above shows how each feature typically impacts yield across all Kansas fields in the data.
    - Recommendations are generated to help you take practical steps that can boost your results or manage risk.
    """)
    
    # Model Insights Box
    st.info("""
    **Model Insights:**  
    - Rainfall is the most important factor for yield in Kansas.
    - Fertilizer use increases yield by about 1.5 tons/ha.
    - Model: Ridge Regression (R² = 0.78, RMSE = 0.79)
    - Powered by 10 years of Kansas yield & weather data.
    """)
    
    st.write("---")
    st.markdown("🔍 *Try changing the values above to explore different scenarios!*")

else:
    st.write("👆 **Set your field's rainfall and fertilizer plan, then click 'Predict Wheat Yield' to get a forecast.**")

# Footer
st.caption("Demo by Denish Trada — Data Science Capstone 2025")
