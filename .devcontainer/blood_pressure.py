import streamlit as st
import random

def run():
    st.header("Blood Pressure")

    sys = random.randint(100, 140)
    dia = random.randint(60, 90)

    st.metric("Blood Pressure", f"{sys}/{dia}")
