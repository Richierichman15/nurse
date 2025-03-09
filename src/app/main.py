import streamlit as st
import pandas as pd
import os
from login import login_page, logout_button
from register import register_page, show_login_option
from home import home_page
from request import request_page
from services import services_page
from admin import admin_dashboard
from client_dashboard import client_dashboard

# Initialize session state for login status and page view
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'home'  # Default to home page instead of login

# Main application - now accessible to all users regardless of login status
def show_main_app():
    # Show different pages based on current_page value
    if st.session_state['current_page'] == 'home':
        home_page()
    elif st.session_state['current_page'] == 'services':
        services_page()
    elif st.session_state['current_page'] == 'for_nurses':
        st.title("For Nurses")
        st.write("Information and resources for nursing professionals.")
        # Add your for nurses page content here
    elif st.session_state['current_page'] == 'for_clients':
        st.title("For Clients")
        st.write("Information for healthcare facilities seeking staffing solutions.")
        # Add your for clients page content here
    elif st.session_state['current_page'] == 'jobs':
        st.title("Available Jobs")
        st.write("Browse current job openings.")
        # Add your jobs page content here
    elif st.session_state['current_page'] == 'contact':
        st.title("Contact Us")
        st.write("Get in touch with our team.")
        # Add your contact page content here
    elif st.session_state['current_page'] == 'request':
        request_page()
    elif st.session_state['current_page'] == 'admin':
        admin_dashboard()
    elif st.session_state['current_page'] == 'client_dashboard':
        client_dashboard()
    else:
        # Default to home page
        home_page()

# Display login/logout in sidebar based on current state
def show_auth_sidebar():
    st.sidebar.markdown("---")
    if not st.session_state['logged_in']:
        if st.sidebar.button("Login"):
            st.session_state['current_page'] = 'login'
            st.rerun()
        if st.sidebar.button("Register"):
            st.session_state['current_page'] = 'register'
            st.rerun()
    else:
        if logout_button():
            st.session_state['logged_in'] = False
            st.rerun()

# Main flow control
if st.session_state['current_page'] == 'login':
    # Show login page
    if login_page():
        st.session_state['logged_in'] = True
        st.session_state['current_page'] = 'home'  # Go to home page after login
        st.write(f"Current user role: {st.session_state.get('user_role', 'None')}")
        st.rerun()
    
    # Option to go to registration page
    if st.button("Create a new account"):
        st.session_state['current_page'] = 'register'
        st.rerun()
        
    # Option to go back to home without logging in
    if st.button("Back to Home"):
        st.session_state['current_page'] = 'home'
        st.rerun()

elif st.session_state['current_page'] == 'register':
    # Show registration page
    if register_page():
        # After successful registration, go to login page
        st.session_state['current_page'] = 'login'
        st.rerun()
    
    # Option to go back to login page
    if show_login_option():
        st.session_state['current_page'] = 'login'
        st.rerun()
        
    # Option to go back to home without logging in
    if st.button("Back to Home"):
        st.session_state['current_page'] = 'home'
        st.rerun()

else:
    # Show the main application with the requested page - now accessible to all users
    show_main_app()
    
    # Display login/register options in sidebar
    show_auth_sidebar()
