import streamlit as st
import subprocess
import pandas as pd
import os

st.title("New game")
st.write("""By clicking in first install button, you'll install everything you need to run hummingbot. 

Me falta ver cómo hacer para elegir la ruta donde se instala el archivo
"""
)

if st.button("First install"):
    result = subprocess.Popen(os.getcwd()+"/scripts/first_install.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in iter(lambda: result.stdout.readline(), b""):
        st.text(line)
















#def run_bash(multiple, command, msg):
#    # If several commands per iteration
#    if multiple:
#        result = subprocess.run(command, stderr=subprocess.PIPE, shell=True)
#    else:
#        result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#    # If everything it's OK
#    if result.stderr == "":
#        st.text(msg)
#    else:
#        st.text(result.stderr)
#
#
#if st.button("First install"):
#    
#    # Read script sheet 
#    df = pd.read_excel(os.getcwd()+'/scripts/scripts.xlsx',sheet_name="first_install")
#
#    # Run bash for everyrow
#    for index, row in df.iterrows():
#        run_bash(row['multiple'], row['command'], row['msg'])
#    
#    