import pandas as pd
import streamlit as st
import os
import csv

paths_file_path = os.getcwd()+'/data/bots/bots_sample.csv'
st.title("Manage your bots!")

with open(paths_file_path, 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            i=0
            for row in reader:
                 
                if i==0:
                    i = i+1
                    continue
                else:
                    with st.expander(label=str(row[2]), expanded=False):
                        col1, col2, col3 = st.columns([1,1,1])
                        with col1: 
                            if st.button('Go dashboard ('+str(i)+')'):
                                st.text('Aloha '+str(i))
                        with col2: 
                            if st.button('Export logs ('+str(i)+')'):
                                st.text('Aloha '+str(i))
                        with col3: 
                            if st.button('Change strategy ('+str(i)+')'):
                                st.text('Aloha '+str(i))
                        col1, col2, col3 = st.columns([1,1,1])
                        with col1: 
                            if st.button('Start/stop ('+str(i)+')'):
                                st.text('Aloha '+str(i))
                        with col2: 
                            if st.button('Remove ('+str(i)+')'):
                                st.text('Aloha '+str(i))
                        with col3: 
                            if st.button('Change wallet ('+str(i)+')'):
                                st.text('Aloha '+str(i))
                i = i+1
