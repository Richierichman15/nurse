import streamlit as st
import pandas as pd
import os

st.title("Nurse Help Request")
st.write("If you need assistance from a nurse, please fill out the form below.")

file_path = 'nurse_requests.csv'

with st.form(key='nurse_request_form'):
    name = st.text_input("Your Name:")
    phone = st.text_input("Your Phone Number:")
    address = st.text_input("Your Address:")
    request_description = st.text_area("Describe your request:")

    submit_button = st.form_submit_button("Send Request")

    if submit_button:
        if name and phone and address and request_description:
            new_request = pd.DataFrame({
                'Name': [name],
                'Phone': [phone],
                'Address': [address],
                'Description': [request_description]
            })
            
            if os.path.exists(file_path):
                new_request.to_csv(file_path, mode='a', header=False, index=False)
            else:
                new_request.to_csv(file_path, mode='w', header=True, index=False)
            
            st.success("Submitted successfully! Getting your local nurse soon.")
        else:
            st.error("Please fill out all fields before submitting.")
