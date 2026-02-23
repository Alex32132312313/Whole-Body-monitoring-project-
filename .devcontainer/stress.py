import streamlit as st
import random

def run():
    st.header("Stress Levels")

    stress = random.randint(1, 100)
    st.progress(stress / 100)
    st.write(f"Stress Score: {stress}")
