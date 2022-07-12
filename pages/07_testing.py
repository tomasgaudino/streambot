import streamlit as st
import subprocess
import os
def run_and_display_stdout(*cmd_with_args):
    result = subprocess.call(cmd_with_args, stdout=subprocess.PIPE)
    for line in iter(lambda: result.stdout.readline(), b""):
        st.text(line.decode("utf-8"))

if st.button("Run"):
    run_and_display_stdout(os.getcwd()+"/scripts/first_install.sh")