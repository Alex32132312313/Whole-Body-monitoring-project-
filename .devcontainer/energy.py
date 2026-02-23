import streamlit as st
import random

def run():
    st.header("Energy Score")

    score = random.randint(1, 100)
    st.progress(score / 100)
    st.write(score)
