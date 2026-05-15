import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hospital Expert System")

st.title("Hospital and Medical Facilities Expert System")

st.subheader("Patient Information")

name = st.text_input("Patient Name")

age = st.number_input(
    "Age",
    min_value=1,
    max_value=100
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)

st.subheader("Select Symptoms")

fever = st.checkbox("Fever")
cough = st.checkbox("Cough")
headache = st.checkbox("Headache")
chest_pain = st.checkbox("Chest Pain")
breathing = st.checkbox("Breathing Problem")

if st.button("Generate Diagnosis"):

    disease = ""
    medicine = ""
    severity = ""

    if fever and cough:

        disease = "Flu"
        medicine = "Paracetamol"
        severity = "Medium"

    elif headache and fever:

        disease = "Migraine"
        medicine = "Pain Killer"
        severity = "Low"

    elif chest_pain or breathing:

        disease = "Heart/Lung Issue"
        medicine = "Emergency Consultation"
        severity = "High"

    else:

        disease = "Normal"
        medicine = "General Observation"
        severity = "Low"

    st.success(f"Possible Disease: {disease}")

    st.info(f"Suggested Treatment: {medicine}")

    if severity == "High":
        st.error("Emergency Case Detected")

    st.subheader("Medical Report")

    report = pd.DataFrame({
        "Patient": [name],
        "Age": [age],
        "Disease": [disease],
        "Severity": [severity]
    })

    st.table(report)