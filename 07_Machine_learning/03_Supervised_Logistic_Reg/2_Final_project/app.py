import streamlit as st
import pandas as pd
import sys

# Check if required packages are installed
try:
    import joblib
except ImportError:
    st.error("❌ joblib is not installed. Please add it to requirements.txt")
    st.stop()

try:
    import sklearn
except ImportError:
    st.error("❌ scikit-learn is not installed. Please add it to requirements.txt")
    st.stop()

# Load model with error handling
@st.cache_resource
def load_model():
    try:
        model = joblib.load("knn_heart.pkl")
        scaler = joblib.load("scaler.pkl")
        expected_columns = joblib.load("columns.pkl")
        return model, scaler, expected_columns
    except FileNotFoundError as e:
        st.error(f"❌ Model file not found: {e}")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading model: {e}")
        st.stop()

# Load the model
model, scaler, expected_columns = load_model()

st.title("Heart Stroke Prediction by Faisal 💖")
st.markdown("Provide The Following Details")

# Input fields
age = st.slider("Age", 18, 100, 40)
sex = st.selectbox("SEX", ['M', 'F'])
chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.slider("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict"):
    try:
        # Create input dictionary
        raw_input = {
            'Age': age,
            'RestingBP': resting_bp,
            'Cholesterol': cholesterol,
            'FastingBS': fasting_bs,
            'MaxHR': max_hr,
            'Oldpeak': oldpeak,
            'Sex_' + sex: 1,
            'ChestPainType_' + chest_pain: 1,
            'RestingECG_' + resting_ecg: 1,  # Fixed typo: RestingECS_ -> RestingECG_
            'ExerciseAngina_' + exercise_angina: 1,
            'ST_Slope_' + st_slope: 1
        }

        # Create DataFrame
        input_df = pd.DataFrame([raw_input])
        
        # Add missing columns with 0
        for col in expected_columns:
            if col not in input_df.columns:
                input_df[col] = 0

        # Reorder columns to match training
        input_df = input_df[expected_columns]        

        # Scale input
        scaled_input = scaler.transform(input_df)
        
        # Make prediction
        prediction = model.predict(scaled_input)[0]
        prediction_proba = model.predict_proba(scaled_input)[0]

        # Display results
        st.subheader("Prediction Results")
        
        if prediction == 1:
            st.error("⚠️ High Risk of Heart Disease")
            st.write(f"Probability of Heart Disease: {prediction_proba[1]:.2%}")
        else: 
            st.success("👍 Low Risk of Heart Disease")
            st.write(f"Probability of Heart Disease: {prediction_proba[1]:.2%}")
            
        # Show confidence
        confidence = max(prediction_proba)
       # st.write(f"Model Confidence: {confidence:.2%}")
        
    except Exception as e:
        st.error(f"❌ Prediction error: {e}")
        st.write("Please check your input values and try again.")