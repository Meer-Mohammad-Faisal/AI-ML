import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load saved model, scaler, and expected columns
model = joblib.load("models/insurance_model.pkl")
scaler = joblib.load("scaler.pkl")
expected_cols = joblib.load("expected_columns.pkl")

st.set_page_config(page_title="Insurance Charge Prediction", page_icon="💰")
st.title("💰 Insurance Charge Prediction App")
st.markdown("Predict insurance cost based on personal and lifestyle factors.")

# --- Input fields ---
age = st.slider("Age", 18, 100, 30)
sex = st.radio("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=70.0, value=25.0, step=0.1)
children = st.number_input("Number of Children", 0, 10, 0)
smoker = st.radio("Smoker", ["No", "Yes"])
region_southeast = st.checkbox("Region: Southeast")
bmi_category_obese = st.checkbox("BMI Category: Obese")

# --- Prepare input ---
input_df = pd.DataFrame(columns=expected_cols, index=[0])
input_df.loc[0] = 0  # fill default 0

input_df.loc[0, "age"] = age
input_df.loc[0, "bmi"] = bmi
input_df.loc[0, "children"] = children
input_df.loc[0, "is_female"] = 1 if sex == "Female" else 0
input_df.loc[0, "is_smoker"] = 1 if smoker == "Yes" else 0
input_df.loc[0, "region_southeast"] = 1 if region_southeast else 0
input_df.loc[0, "bmi_category_Obse"] = 1 if bmi_category_obese else 0

# --- Apply scaler ---
num_cols = ['age', 'bmi', 'children']
input_df[num_cols] = scaler.transform(input_df[num_cols])

# --- Predict ---
if st.button("Predict Insurance Charge"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Insurance Charge: **${prediction:,.2f}**")
