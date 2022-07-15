import pandas as pd
import streamlit as st
import os
import csv
import json
import subprocess

paths_file_path = os.getcwd()+'/data/bots/bots_sample.csv'
st.title("Manage your bots!")

# Get docker df
def dockerps_to_dataframe():
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
bots = dockerps_to_dataframe()

if bots.empty:
    st.text("Ups! Apparently there are no bots here. Ready to launch your first bot?")
    if st.button("Launch new bot"):
        subprocess.call(os.getcwd()+'/scripts/new_bot.sh')
else:
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
            # Start/stop button
            with col1: 
                if row['State'] == "exited":
                    if st.button('Start'):
                        result = subprocess.Popen(['docker','start',row['Names']], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        if result.stderr == None:
                            st.text('Bot started!')
                elif row['State'] == "running":
                    if st.button('Stop'):
                        result = subprocess.Popen(['docker','stop',row['ID']], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                        if result.stderr == None:
                            st.text('Bot stopped')

            with col2: 
                if st.button('Export logs'):
                    st.text('Aloha logs')

            # Change strategy button
            with col3: 
                if st.button('Change strategy'):
                    command = os.getcwd()+'/scripts/change_load_strategy.sh'
                    path = os.getcwd()
                    subprocess.run([
                        command,
                        path,
                        str(row['Names']),
                        'pure_market_making',
                        'conf_pure_mm_1.yml',
                        'admin',
                        str(row['State'])])

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