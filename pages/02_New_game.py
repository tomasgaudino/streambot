import streamlit as st
import subprocess
import pandas as pd
import os
import csv
from csv import writer


st.title("New game")
st.write("""By clicking in first install button, you'll install everything you need to run hummingbot. 

Me falta ver cómo hacer para elegir la ruta donde se instala el archivo
"""
)

if st.button("First install"):

    # check if path is already covered
    paths_file_path = os.getcwd()+'/data/paths/paths.csv'
    if os.path.isfile(paths_file_path):
        with open(paths_file_path, 'rt') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                for field in row:
                    if field == os.getcwd():
                        st.write('Hummingbots already installed in directory!')
    else:        
        # if don't, run installation
        result = subprocess.Popen(os.getcwd()+"/scripts/first_install.sh", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in iter(lambda: result.stdout.readline(), b""):
            st.text(line)
        # terminate (for some reason this keeps using memory/cpu until crash, keep testing)
        result.terminate()

    