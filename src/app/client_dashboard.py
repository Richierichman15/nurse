import streamlit as st
import pandas as pd
import os
from navbar import navbar
import datetime

def client_dashboard():
    """
    Client dashboard to view request history and track request status
    """
    # Check if user is logged in
    if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
        st.error("Please log in to access your dashboard.")
        return
    
    # Display navbar
    navbar()
    
    # Get current username
    current_user = st.session_state.get('username', 'Anonymous')
    
    st.title(f"Client Dashboard - {current_user}")
    st.write("Welcome to your personal dashboard. Here you can view and track your nursing service requests.")
    
    # Debug information
    st.write(f"Logged in as: {current_user}")
    
    # Create tabs for different dashboard sections
    tab1, tab2, tab3 = st.tabs(["Active Requests", "Request History", "Account"])
    
    # Active Requests Tab
    with tab1:
        display_active_requests(current_user)
    
    # Request History Tab
    with tab2:
        display_request_history(current_user)
    
    # Account Tab
    with tab3:
        display_account_info(current_user)

def display_active_requests(current_user):
    """Display active requests and their status"""
    st.header("Active Requests")
    
    # Load requests data
    requests_file = 'nurse_requests.csv'
    if not os.path.exists(requests_file):
        st.info("You don't have any active requests.")
        return
    
    # Load existing requests
    try:
        requests_df = pd.read_csv(requests_file)
        
        # Debug information - show the available columns
        st.write("Available columns in the requests file:", list(requests_df.columns))
        
        # Debug information - display all requests to understand the data
        with st.expander("Debug - All Requests Data"):
            st.dataframe(requests_df)
        
        # Filter requests by exact username match
        user_requests = requests_df[requests_df['Name'] == current_user]
        
        # Debug information
        st.write(f"Found {len(user_requests)} requests for user: {current_user}")
        
        # Filter for active requests - if Status column exists
        if 'Status' in user_requests.columns:
            active_requests = user_requests[user_requests['Status'].isin(['New', 'Assigned', 'In Progress'])]
            
            if not active_requests.empty:
                st.write(f"You have {len(active_requests)} active requests")
                
                # Display each active request
                for index, request in active_requests.iterrows():
                    with st.expander(f"Request from {request.get('Request_Date', 'Unknown Date')}", expanded=True):
                        # Status indicator
                        status = request.get('Status', 'New')
                        if status == 'New':
                            st.info("Status: New - Your request has been received")
                        elif status == 'Assigned':
                            st.success(f"Status: Assigned to {request.get('Assigned_Nurse', 'a nurse')}")
                        elif status == 'In Progress':
                            st.warning("Status: In Progress - Service is being provided")
                        
                        # Request details
                        st.write("**Request Details:**")
                        st.write(f"**Description:** {request['Description']}")
                        st.write(f"**Address:** {request['Address']}")
                        st.write(f"**Phone:** {request['Phone']}")
                        
                        # Assigned nurse (if any)
                        if 'Assigned_Nurse' in request and request['Assigned_Nurse'] != 'Unassigned':
                            st.write(f"**Assigned Nurse:** {request['Assigned_Nurse']}")
            else:
                st.info("You don't have any active requests.")
        else:
            st.warning("Status field not found in the requests data. Contact administrator for help.")
    except Exception as e:
        st.error(f"Error loading requests: {str(e)}")
    
    # Button to create a new request
    if st.button("Create New Request"):
        st.session_state['current_page'] = 'request'
        st.rerun()

def display_request_history(current_user):
    """Display request history"""
    st.header("Request History")
    
    # Load requests data
    requests_file = 'nurse_requests.csv'
    if not os.path.exists(requests_file):
        st.info("You don't have any request history.")
        return
    
    # Load existing requests
    try:
        requests_df = pd.read_csv(requests_file)
        
        # Filter requests by exact username match
        user_requests = requests_df[requests_df['Name'] == current_user]
        
        # Filter for completed or cancelled requests
        if 'Status' in user_requests.columns:
            history_requests = user_requests[user_requests['Status'].isin(['Completed', 'Cancelled'])]
            
            if not history_requests.empty:
                st.write(f"You have {len(history_requests)} completed or cancelled requests")
                
                # Optional sorting
                sort_by = st.selectbox(
                    "Sort by:", 
                    options=["Most Recent", "Oldest First"],
                    index=0
                )
                
                if sort_by == "Most Recent" and 'Request_Date' in history_requests:
                    history_requests = history_requests.sort_values(by='Request_Date', ascending=False)
                elif sort_by == "Oldest First" and 'Request_Date' in history_requests:
                    history_requests = history_requests.sort_values(by='Request_Date', ascending=True)
                
                # Display each historical request in an expandable container
                for index, request in history_requests.iterrows():
                    with st.expander(f"{request.get('Request_Date', 'Unknown Date')} - {request.get('Status', 'Unknown')}"):
                        # Request details
                        st.write("**Request Details:**")
                        st.write(f"**Description:** {request['Description']}")
                        st.write(f"**Address:** {request['Address']}")
                        st.write(f"**Phone:** {request['Phone']}")
                        
                        # Nurse who provided service
                        if 'Assigned_Nurse' in request and request['Assigned_Nurse'] != 'Unassigned':
                            st.write(f"**Service Provided By:** {request['Assigned_Nurse']}")
                        
                        # Request a similar service option
                        if st.button("Request Similar Service", key=f"similar_{index}"):
                            # In a real app, you'd pre-fill the request form with this data
                            st.session_state['current_page'] = 'request'
                            st.rerun()
            else:
                st.info("You don't have any completed or cancelled requests.")
        else:
            st.info("You don't have any request history.")
    except Exception as e:
        st.error(f"Error loading request history: {str(e)}")

def display_account_info(current_user):
    """Display account information and settings"""
    st.header("Account Information")
    
    # Display account info
    st.write(f"**Username:** {current_user}")
    st.write("**Account Type:** Client")
    st.write("**Member Since:** 2023")  # Placeholder - would come from user database
    
    # Preferred contact method
    contact_method = st.radio(
        "Preferred Contact Method:",
        options=["Email", "Phone", "Text Message"],
        index=0
    )
    
    # Notification settings
    st.subheader("Notification Preferences")
    email_notifications = st.checkbox("Email Notifications", value=True)
    sms_notifications = st.checkbox("SMS Notifications", value=False)
    
    # Save preferences button
    if st.button("Save Preferences"):
        # In a real app, save these preferences to user database
        st.success("Preferences saved successfully!")
    
    # Change password section
    st.subheader("Change Password")
    with st.form("change_password_form"):
        current_password = st.text_input("Current Password", type="password")
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        
        if st.form_submit_button("Change Password"):
            if not current_password or not new_password or not confirm_password:
                st.error("All fields are required")
            elif new_password != confirm_password:
                st.error("New passwords do not match")
            else:
                # In a real app, validate current password and update to new password
                st.success("Password changed successfully!")
