import streamlit as st

def run():
    st.header("Menstrual Cycle")

    day = st.slider("Cycle Day", 1, 28, 14)

    if day < 6:
        phase = "Menstrual"
    elif day < 14:
        phase = "Follicular"
    elif day < 16:
        phase = "Ovulation"
    else:
        phase = "Luteal"

    st.write("Phase:", phase)
