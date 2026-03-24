"""
==========================================================
Professional Credit Risk Dashboard - Streamlit
==========================================================
"""

import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Load Model
# ---------------------------------------------------------
model = joblib.load("credit_risk_model.pkl")

st.set_page_config(page_title="Credit Risk Dashboard", layout="wide")

st.title("🏦 Credit Risk Analytics Dashboard")
st.markdown("### Customer Risk Prediction & Analysis System")
st.divider()

# ---------------------------------------------------------
# Layout Columns
# ---------------------------------------------------------
col1, col2 = st.columns([1, 1])

# ================= LEFT SIDE (INPUTS) ====================
with col1:
    st.subheader("📌 Customer Information")

    age = st.slider("Age", 18, 80, 30)
    income = st.number_input("Annual Income", value=50000.0)
    employment_length = st.slider("Employment Length", 0, 40, 5)
    loan_amount = st.number_input("Loan Amount", value=10000.0)
    interest_rate = st.slider("Interest Rate (%)", 5.0, 30.0, 12.0)
    loan_percent_income = st.slider("Loan Percent Income", 0.0, 1.0, 0.2)
    credit_history = st.slider("Credit History Length", 0.0, 30.0, 5.0)

    home_ownership = st.selectbox("Home Ownership",
                                   ["RENT", "OWN", "MORTGAGE", "OTHER"])

    loan_intent = st.selectbox("Loan Purpose",
                               ["EDUCATION", "MEDICAL", "VENTURE",
                                "PERSONAL", "DEBTCONSOLIDATION",
                                "HOMEIMPROVEMENT"])

    loan_grade = st.selectbox("Loan Grade",
                              ["A", "B", "C", "D", "E", "F", "G"])

    default_history = st.selectbox("Previous Default?",
                                   ["Y", "N"])

    predict_btn = st.button("🚀 Predict Risk")

# ================= RIGHT SIDE (OUTPUT KPI STYLE) ====================
with col2:
    st.subheader("📊 Risk Analysis Result")

    if predict_btn:

        input_data = {
            "person_age": age,
            "person_income": income,
            "person_emp_length": employment_length,
            "loan_amnt": loan_amount,
            "loan_int_rate": interest_rate,
            "loan_percent_income": loan_percent_income,
            "cb_person_cred_hist_length": credit_history,
        }

        input_df = pd.DataFrame([input_data])

        categorical_data = {
            "person_home_ownership": home_ownership,
            "loan_intent": loan_intent,
            "loan_grade": loan_grade,
            "cb_person_default_on_file": default_history
        }

        for col, value in categorical_data.items():
            input_df[col] = value

        input_df = pd.get_dummies(input_df)

        model_features = model.feature_names_in_
        input_df = input_df.reindex(columns=model_features, fill_value=0)

        probability = model.predict_proba(input_df)[0][1]
        risk_percentage = round(probability * 100, 2)

        # KPI Cards
        kpi1, kpi2 = st.columns(2)

        with kpi1:
            st.metric("Default Probability", f"{risk_percentage}%")

        with kpi2:
            if probability <= 0.3:
                st.success("🟢 Low Risk")
                color = "green"
            elif probability <= 0.7:
                st.warning("🟡 Medium Risk")
                color = "orange"
            else:
                st.error("🔴 High Risk")
                color = "red"

        # Risk Gauge Style Bar
        st.markdown("### Risk Level Indicator")

        fig, ax = plt.subplots()
        ax.barh(["Risk"], [risk_percentage])
        ax.set_xlim(0, 100)
        ax.set_xlabel("Risk %")
        st.pyplot(fig)

st.divider()
st.markdown("© 2026 Credit Risk ML System | Developed for Major Project")
