import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from fpdf import FPDF
from datetime import datetime
import base64

# Load dataset
df = pd.read_csv("heart.csv")

# Features and target
X = df.drop("HeartDisease", axis=1)
y = df["HeartDisease"]

# Preprocessing
categorical = ["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"]
numerical = X.columns.difference(categorical)

encoder = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical)
], remainder="passthrough")

# Model
model = Pipeline([
    ("encoder", encoder),
    ("clf", RandomForestClassifier(random_state=42))
])
model.fit(X, y)

# Doctor Info
DOCTOR_NAME = "Dr. Sharon Karabel"
DOCTOR_ID = "D-2025"
SIGNATURE = "SharonKarabel"

# Streamlit UI
st.title("Heart Disease Predictor & Prescription Generator")

st.header("Enter Patient Details")
input_data = {}
input_data["Age"] = st.number_input("Age", 20, 100, 45)
input_data["Sex"] = st.selectbox("Sex", ["M", "F"])
input_data["ChestPainType"] = st.selectbox("Chest Pain Type", ["ATA", "NAP", "ASY", "TA"])
input_data["RestingBP"] = st.number_input("Resting Blood Pressure", 80, 200, 120)
input_data["Cholesterol"] = st.number_input("Cholesterol", 100, 600, 200)
input_data["FastingBS"] = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
input_data["RestingECG"] = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
input_data["MaxHR"] = st.number_input("Max Heart Rate", 60, 220, 150)
input_data["ExerciseAngina"] = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
input_data["Oldpeak"] = st.number_input("Oldpeak", 0.0, 6.0, 1.0, step=0.1)
input_data["ST_Slope"] = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

if st.button("Predict & Prescribe"):
    input_df = pd.DataFrame([input_data])
    prediction = model.predict(input_df)[0]

    # Always recommend 3 medicines
    if prediction == 1:
        diagnosis = "High risk of heart disease"
        meds = ["Aspirin 75mg", "Atorvastatin 10mg", "Bisoprolol 5mg"]
        tests = ["ECG", "Echocardiogram", "Treadmill Test"]
        diet = "Low-fat, low-salt diet. Eat more fruits, vegetables, and whole grains."
        exercise = "Walk for 30 minutes a day, 5 days a week. Avoid heavy lifting."
        remarks = "Patient is advised to consult a cardiologist for further management."
    else:
        diagnosis = "Low risk of heart disease"
        meds = ["Multivitamin", "Vitamin D3 1000 IU", "Omega-3 capsules"]
        tests = ["Annual check-up", "BP monitoring", "Lipid profile"]
        diet = "Balanced diet with controlled fat intake. Stay hydrated."
        exercise = "Regular moderate exercise. 30 minutes of brisk walking daily."
        remarks = "Patient is doing well. Continue healthy habits and follow-up annually."

    # Show on screen
    st.subheader("Diagnosis")
    st.write(diagnosis)

    st.subheader("Medications:")
    for m in meds:
        st.markdown(f"- {m}")

    st.subheader("Recommended Tests:")
    for t in tests:
        st.markdown(f"- {t}")

    st.subheader("Diet Advice:")
    st.write(diet)

    st.subheader("Exercise Advice:")
    st.write(exercise)

    st.subheader("Doctor's Remarks:")
    st.write(remarks)

    # Create PDF
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Heart Prescription", ln=True, align="C")
    pdf.cell(200, 10, txt=f"Doctor: {DOCTOR_NAME} (ID: {DOCTOR_ID})", ln=True)
    pdf.cell(200, 10, txt=f"Date: {timestamp}", ln=True)
    pdf.ln(5)

    for key, val in input_data.items():
        pdf.cell(200, 10, txt=f"{key}: {val}", ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Diagnosis:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=diagnosis, ln=True)

    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Medications:", ln=True)
    pdf.set_font("Arial", size=12)
    for med in meds:
        pdf.cell(200, 10, txt=f"- {med}", ln=True)

    pdf.ln(3)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Recommended Tests:", ln=True)
    pdf.set_font("Arial", size=12)
    for test in tests:
        pdf.cell(200, 10, txt=f"- {test}", ln=True)

    pdf.ln(3)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Diet Advice:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, diet)

    pdf.ln(3)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Exercise Advice:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, exercise)

    pdf.ln(3)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(200, 10, txt="Doctor's Remarks:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, remarks)

    pdf.ln(10)
    pdf.set_font("Arial", "I", 10)
    pdf.cell(200, 10, txt=f"Signed by {DOCTOR_NAME} ({SIGNATURE})", ln=True)

    # PDF download
    pdf_output = pdf.output(dest="S").encode("latin1")
    b64_pdf = base64.b64encode(pdf_output).decode("utf-8")
    download_link = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="heart_prescription.pdf">📥 Download Prescription PDF</a>'
    st.markdown(download_link, unsafe_allow_html=True)
