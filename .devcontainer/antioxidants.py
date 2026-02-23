import streamlit as st
import random

def run():
    st.header("ანტioxidant Index")

    value = random.randint(20000, 80000)
    st.metric("Carotenoids", value)
