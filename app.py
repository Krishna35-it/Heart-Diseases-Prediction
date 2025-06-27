import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('heart_dis_pred.pkl', 'rb'))

st.title(" Heart Disease Prediction App")

st.markdown("### Enter the patient details below:")

# Input features
age = st.slider("Age", 20, 100, 50)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.slider("Resting Blood Pressure (mm Hg)", 80, 200, 120)
chol = st.slider("Serum Cholesterol (mg/dl)", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
restecg = st.selectbox("Resting ECG Results", ["Normal", "ST-T wave abnormality", "Left ventricular hypertrophy"])
thalach = st.slider("Max Heart Rate Achieved", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0, step=0.1)
slope = st.selectbox("Slope of Peak Exercise ST", ["Upsloping", "Flat", "Downsloping"])
ca = st.selectbox("Number of Major Vessels (0-4)", [0, 1, 2, 3, 4])
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# Convert to numeric (match dummy encoding used in training)
sex_1 = 1 if sex == "Male" else 0
cp_1 = 1 if cp == "Atypical Angina" else 0
cp_2 = 1 if cp == "Non-anginal Pain" else 0
cp_3 = 1 if cp == "Asymptomatic" else 0
fbs_1 = 1 if fbs == "True" else 0
restecg_1 = 1 if restecg == "ST-T wave abnormality" else 0
restecg_2 = 1 if restecg == "Left ventricular hypertrophy" else 0
exang_1 = 1 if exang == "Yes" else 0
slope_1 = 1 if slope == "Flat" else 0
slope_2 = 1 if slope == "Downsloping" else 0
ca_1 = 1 if ca == 1 else 0
ca_2 = 1 if ca == 2 else 0
ca_3 = 1 if ca == 3 else 0
ca_4 = 1 if ca == 4 else 0
thal_1 = 1 if thal == "Fixed Defect" else 0
thal_2 = 1 if thal == "Reversible Defect" else 0
thal_3 = 0 if thal in ["Fixed Defect", "Reversible Defect"] else 1  # Default to 1 for "Normal"

# Final input vector (order must match training)
input_data = np.array([[age, trestbps, chol, thalach, oldpeak,
                        sex_1, cp_1, cp_2, cp_3, fbs_1, restecg_1, restecg_2,
                        exang_1, slope_1, slope_2,
                        ca_1, ca_2, ca_3, ca_4,
                        thal_1, thal_2, thal_3]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error(" The patient is likely to have Heart Disease.")
    else:
        st.success("The patient is unlikely to have Heart Disease.")
