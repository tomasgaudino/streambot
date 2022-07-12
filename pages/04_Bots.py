import pandas as pd
import streamlit as st

st.title('List of bots installed')

df = pd.read_csv("/home/drupman/hummingbots/hummingbots/data/bots/bots_sample.csv")

st.write(df)
