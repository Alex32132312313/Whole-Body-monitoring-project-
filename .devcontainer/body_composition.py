import streamlit as st

def run():
    st.header("Body Composition")

    weight = st.number_input("Weight (kg)", 40, 200, 70)
    fat = st.slider("Body Fat %", 5, 50, 20)

    st.write(f"Lean Mass: {weight * (1 - fat/100):.1f} kg")
