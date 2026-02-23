import streamlit as st
import numpy as np
import pandas as pd

def run():
    st.header("ECG (Simulated)")

    t = np.linspace(0, 1, 200)
    ecg = np.sin(5 * 2 * np.pi * t) + np.random.normal(0, 0.1, len(t))

    df = pd.DataFrame(ecg, columns=["ECG"])
    st.line_chart(df)
