import streamlit as st
import time


st.write("""
# My first app
Hello *World!*
""")

st.write("""
## This is how streamlit works
""")

name = st.text_input("What is your name")

st.write(name)

