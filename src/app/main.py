import streamlit as st
import pandas as pd
import os
from login import login_page, logout_button
from register import register_page, show_login_option

# Initialize session state for login status and page view
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'login'  # Options: 'login', 'register'

# Main application
def show_main_app():
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

# Show appropriate page based on user state
if not st.session_state['logged_in']:
    # Show login or registration page
    if st.session_state['current_page'] == 'login':
        # Show login page
        if login_page():
            st.session_state['logged_in'] = True
            st.rerun()
        
        # Option to go to registration page
        if st.button("Create a new account"):
            st.session_state['current_page'] = 'register'
            st.rerun()
    
    else:  # Registration page
        # Show registration page
        if register_page():
            # After successful registration, go to login page
            st.session_state['current_page'] = 'login'
            st.rerun()
        
        # Option to go back to login page
        if show_login_option():
            st.session_state['current_page'] = 'login'
            st.rerun()
else:
    # Show main app
    show_main_app()
    
    # Check if logout button clicked
    if logout_button():
        st.session_state['logged_in'] = False
        st.rerun()
