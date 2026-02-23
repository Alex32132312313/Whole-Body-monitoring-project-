import streamlit as st

def run():
    st.header("Calories")
    if "calories" not in st.session_state:
        st.session_state.calories = 0

    if st.button("Add 500 kcal"):
        st.session_state.calories += 500

    st.metric("Calories Burned", st.session_state.calories)
