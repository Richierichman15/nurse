import streamlit as st
import pandas as pd
import os

st.title("Nurse Dashboard")

file_path = 'nurse_requests.csv'

if os.path.exists(file_path):
    requests = pd.read_csv(file_path)
    st.write("### Incoming Requests")
    st.dataframe(requests)  
else:
    st.write("No incoming requests.")
