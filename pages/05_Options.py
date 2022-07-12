import streamlit as st
import json

uploaded_file = st.file_uploader("Choose a file", type='yml')
if uploaded_file:
    for line in uploaded_file:
        st.write(line)