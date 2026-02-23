import streamlit as st
import time

def run():
    st.header("Fall Detection")

    if "fall" not in st.session_state:
        st.session_state.fall = False

    if st.button("Simulate Fall"):
        st.session_state.fall = True

    if st.session_state.fall:
        st.error("⚠️ FALL DETECTED")
        time.sleep(2)
        st.session_state.fall = False
    else:
        st.success("Normal")
