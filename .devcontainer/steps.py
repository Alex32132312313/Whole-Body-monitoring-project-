import streamlit as st

def run():
    st.header("Steps")
    if "steps" not in st.session_state:
        st.session_state.steps = 0

    if st.button("Add 1000 steps"):
        st.session_state.steps += 1000

    st.metric("Steps", st.session_state.steps)
