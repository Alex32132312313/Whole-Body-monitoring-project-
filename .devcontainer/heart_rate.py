import streamlit as st
import random
import pandas as pd

def run():
    st.header("Heart Rate")

    if "hr" not in st.session_state:
        st.session_state.hr = []

    if st.button("Simulate Heart Rate"):
        st.session_state.hr.append(random.randint(60, 140))
        st.session_state.hr = st.session_state.hr[-20:]

    if st.session_state.hr:
        df = pd.DataFrame(st.session_state.hr, columns=["BPM"])
        st.line_chart(df)
