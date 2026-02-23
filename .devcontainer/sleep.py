import streamlit as st
import random

def run():
    st.header("Sleep Apnea")

    events = random.randint(0, 30)

    if events < 5:
        status = "Normal"
    elif events < 15:
        status = "Mild"
    else:
        status = "Severe"

    st.metric("Apnea Events", events)
    st.write("Status:", status)
