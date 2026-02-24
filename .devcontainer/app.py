import streamlit as st

from modules import (
    steps, calories, heart_rate, ecg, spo2,
    menstrual, stress, body_composition,
    sleep, sleep_apnea, blood_pressure,
    energy, antioxidants, fall_detection
)

st.set_page_config(layout="wide")
st.title("🧬 Health Metrics Dashboard")

tab = st.tab([
    "Steps", "Calories", "Heart Rate", "ECG", "SpO2",
    "Menstrual", "Stress", "Body", "Sleep",
    "Sleep Apnea", "Blood Pressure", "Energy",
    "Antioxidants", "Fall Detection"
])

modules = [
    steps, calories, heart_rate, ecg, spo2,
    menstrual, stress, body_composition,
    sleep, sleep_apnea, blood_pressure,
    energy, antioxidants, fall_detection
]

for tab, module in zip(tabs, modules):
    with tab:
        module.run()
