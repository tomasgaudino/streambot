import pandas as pd
import streamlit as st
import os
import csv

paths_file_path = os.getcwd()+'/data/paths/paths.csv'
st.title("Load game!")


with open(paths_file_path, 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            i=0
            for row in reader:
                 
                if i==0:
                    i = i+1
                    continue
                for field in row:
                    print(field)
                    with st.expander(label=str(field), expanded=False):
                        col1, col2 = st.columns([1,1])
                        with col1: 
                            if st.button('Load '+str(i)):
                                st.text('Aloha '+str(i))
                        with col2: 
                            if st.button('Delete '+str(i)):
                                st.text('Aloha '+str(i))
                i = i+1
                    
#def load_data():
#    data = pd.read_csv(DATA_URL)
#    lowercase = lambda x: str(x).lower()
#    data.rename(lowercase, axis='columns', inplace=True)
#    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#    return data