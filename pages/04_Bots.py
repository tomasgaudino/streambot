import pandas as pd
import streamlit as st
import os
import csv
import json
import subprocess

paths_file_path = os.getcwd()+'/data/bots/bots_sample.csv'
st.title("Manage your bots!")

# Get docker df
def docker_display_stdout():
    # Get docker output formatted as JSON
    result = subprocess.check_output(['docker','ps','-a','--format',"'{{json .}}'"])

    # Transform bytes to string
    my_json = result.decode('utf8')

    # Load the JSON to a Python list & dump it back out as formatted JSON
    data = json.loads("["+my_json[1:-2]+"]")
    s = json.dumps(data, indent=4, sort_keys=True)

    # Load the dump into Dataframe
    df=pd.read_json(s)
    
    return df

# Load to dataframe
bots = docker_display_stdout()

# Export table to page
st.table(bots.drop(columns=["Command","Labels","Mounts"]))

# Bots gallery with action buttons
for index, row in bots.iterrows():
    if row['State'] == "exited":
        temp_icon = "🛑"
    elif row['State'] == "running":
        temp_icon = "💸"

    with st.expander(label=temp_icon+"   "+row['Names'], expanded=False):

        col1, col2, col3 = st.columns([1,1,1])

        with col1: 
            if row['State'] == "exited":
                if st.button('Start'):
                    result = subprocess.Popen(['docker','start',row['Names']], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.stderr == None:
                        st.text('Bot started!')
            elif row['State'] == "running":
                if st.button('Stop'):
                    result = subprocess.Popen(['docker','stop',row['Names']], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.stderr == None:
                        st.text('Bot stopped')
        with col2: 
            if st.button('Export logs'):
                st.text('Aloha logs')

        with col3: 
            if st.button('Change strategy'):
                st.text('Aloha strategy')

        col1, col2, col3 = st.columns([1,1,1])

        with col1: 
            if st.button('Go dashboard'):
                st.text('Aloha dashboard')

        with col2: 
            if st.button('Remove'):
                st.text('Aloha remove')

        with col3: 
            if st.button('Change wallet'):
                st.text('Aloha wallet')