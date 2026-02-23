import streamlit as st
import random

def run():
    st.header("Blood Oxygen (SpO2)")

    spo2 = random.randint(94, 100)
    st.metric("SpO2 %", spo2)
