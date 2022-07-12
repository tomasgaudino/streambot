import streamlit as st
import pandas as pd
import numpy as np

st.title('Hummingbots')

def home():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")

def new_game():
    st.markdown("# New game ❄️")
    st.sidebar.markdown("# New game ❄️")

def load_game():
    st.markdown("# Load game 🎉")
    st.sidebar.markdown("# Load game 🎉")

def options():
    st.markdown("# Options ⚙️")
    st.sidebar.markdown("# Options ⚙️")

def bots():
    st.markdown("# Bots ⚙️")
    st.sidebar.markdown("# Bots ⚙️")

def help_page():
    st.markdown("# Help 🎉")
    st.sidebar.markdown("# Help 🎉")