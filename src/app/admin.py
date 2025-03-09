import streamlit as st
import pandas as pd
import os
from navbar import navbar
import datetime

def admin_dashboard():
    """
    Admin dashboard to manage nurse requests, assignments, and track status
    """
    # Check if user has admin privileges
    if 'user_role' not in st.session_state or st.session_state['user_role'] != 'admin':
        st.error("You do not have permission to access the admin dashboard.")
        return
    
    # Display navbar
    navbar()
    
    st.title("Admin Dashboard")
    
    # Create tabs for different dashboard sections
    tab1, tab2, tab3 = st.tabs(["Request Management", "Nurse Assignment", "Analytics"])
    
    # Request Management Tab
    with tab1:
        display_request_management()
    
    # Nurse Assignment Tab
    with tab2:
        display_nurse_assignment()
    
    # Analytics Tab
    with tab3:
        display_analytics()

def display_request_management():
    """Display and manage nurse requests"""
    st.header("Request Management")
    
    # Load requests data
    requests_file = 'nurse_requests.csv'
    if not os.path.exists(requests_file):
        st.warning("No requests have been submitted yet.")
        return
    
    # Load existing requests
    requests_df = pd.read_csv(requests_file)
    
    # Add status column if it doesn't exist
    if 'Status' not in requests_df.columns:
        requests_df['Status'] = 'New'
    
    # Add date column if it doesn't exist
    if 'Request_Date' not in requests_df.columns:
        requests_df['Request_Date'] = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # Add assigned nurse column if it doesn't exist
    if 'Assigned_Nurse' not in requests_df.columns:
        requests_df['Assigned_Nurse'] = 'Unassigned'
    
    # Filtering options
    st.subheader("Filter Requests")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        status_filter = st.multiselect(
            "Status", 
            options=['New', 'Assigned', 'In Progress', 'Completed', 'Cancelled'],
            default=['New', 'Assigned', 'In Progress']
        )
    
    with col2:
        if 'Assigned_Nurse' in requests_df.columns:
            nurse_options = ['Unassigned'] + list(requests_df['Assigned_Nurse'].unique())
            nurse_filter = st.multiselect(
                "Assigned Nurse",
                options=nurse_options,
                default=['Unassigned']
            )
        else:
            nurse_filter = ['Unassigned']
    
    with col3:
        if 'Scheduled_Date' in requests_df.columns:
            date_options = ['All Dates'] + list(requests_df['Scheduled_Date'].dropna().unique())
            date_filter = st.selectbox(
                "Scheduled Date",
                options=date_options,
                index=0
            )
        else:
            date_filter = 'All Dates'
    
    # Apply filters
    filtered_df = requests_df
    if status_filter:
        filtered_df = filtered_df[filtered_df['Status'].isin(status_filter)]
    if nurse_filter and 'Assigned_Nurse' in requests_df.columns:
        filtered_df = filtered_df[filtered_df['Assigned_Nurse'].isin(nurse_filter)]
    if date_filter != 'All Dates' and 'Scheduled_Date' in requests_df.columns:
        filtered_df = filtered_df[filtered_df['Scheduled_Date'] == date_filter]
    
    # Display requests
    st.subheader("Requests")
    if not filtered_df.empty:
        # Make dataframe editable
        edited_df = st.data_editor(
            filtered_df,
            column_config={
                "Status": st.column_config.SelectboxColumn(
                    "Status",
                    options=["New", "Assigned", "In Progress", "Completed", "Cancelled"],
                    required=True,
                ),
                "Assigned_Nurse": st.column_config.TextColumn(
                    "Assigned Nurse",
                    help="Enter the name of the assigned nurse",
                ),
                "Scheduled_Date": st.column_config.TextColumn(
                    "Scheduled Date",
                    help="The date and time slot scheduled for this service",
                    disabled=True,  # Make this field read-only to prevent errors
                )
            },
            hide_index=True,
            num_rows="dynamic"
        )
        
        # Save button to update the changes
        if st.button("Save Changes"):
            # Update original dataframe with edited values
            for index, row in edited_df.iterrows():
                if index < len(requests_df):
                    for col in edited_df.columns:
                        requests_df.at[index, col] = row[col]
            
            # Save updated dataframe
            requests_df.to_csv(requests_file, index=False)
            st.success("Changes saved successfully!")
    else:
        st.info("No requests match the selected filters.")

def display_nurse_assignment():
    """Manage nurse assignments"""
    st.header("Nurse Assignment")
    
    # Create columns for different sections
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Available Nurses")
        
        # In a real app, this would load from a nurse database
        # For demo, we'll create a simple form to add nurses
        with st.expander("Add New Nurse"):
            with st.form("add_nurse_form"):
                nurse_name = st.text_input("Nurse Name")
                nurse_specialization = st.selectbox(
                    "Specialization",
                    ["General Care", "Home Visits", "Overnight Care", "Specialized Care"]
                )
                nurse_status = st.selectbox(
                    "Status",
                    ["Available", "Assigned", "Off Duty"]
                )
                
                if st.form_submit_button("Add Nurse"):
                    # In a real app, save to a nurse database
                    st.success(f"Nurse {nurse_name} added successfully!")
        
        # Sample nurse data - in a real app, load from database
        nurse_data = {
            "Name": ["Jane Doe", "John Smith", "Emily Johnson", "Michael Brown"],
            "Specialization": ["Home Visits", "Overnight Care", "General Care", "Specialized Care"],
            "Status": ["Available", "Assigned", "Available", "Off Duty"]
        }
        nurses_df = pd.DataFrame(nurse_data)
        
        # Display nurse table
        edited_nurses = st.data_editor(
            nurses_df,
            column_config={
                "Status": st.column_config.SelectboxColumn(
                    "Status",
                    options=["Available", "Assigned", "Off Duty"],
                    required=True,
                ),
            },
            hide_index=True
        )
        
        if st.button("Update Nurse Status"):
            st.success("Nurse status updated successfully!")
    
    with col2:
        st.subheader("Quick Assignment")
        
        # Load requests data for assignment
        requests_file = 'nurse_requests.csv'
        if os.path.exists(requests_file):
            requests_df = pd.read_csv(requests_file)
            
            # Filter for unassigned requests
            if 'Status' in requests_df.columns and 'Assigned_Nurse' in requests_df.columns:
                unassigned = requests_df[
                    (requests_df['Status'] == 'New') | 
                    ((requests_df['Status'] == 'Assigned') & (requests_df['Assigned_Nurse'] == 'Unassigned'))
                ]
                
                if not unassigned.empty:
                    # Create assignment form
                    st.write("Assign nurses to pending requests:")
                    
                    for index, row in unassigned.iterrows():
                        st.markdown(f"**Request from {row['Name']}**")
                        st.write(f"Description: {row['Description'][:50]}...")
                        
                        # Get available nurses
                        available_nurses = nurses_df[nurses_df['Status'] == 'Available']['Name'].tolist()
                        available_nurses = ['Unassigned'] + available_nurses
                        
                        # Dropdown to select nurse
                        selected_nurse = st.selectbox(
                            f"Assign nurse for request #{index}",
                            options=available_nurses,
                            key=f"nurse_select_{index}"
                        )
                        
                        if st.button("Assign", key=f"assign_{index}"):
                            # In a real app, update the database
                            st.success(f"Nurse {selected_nurse} assigned to request #{index}!")
                            
                        st.divider()
                else:
                    st.info("No unassigned requests available.")
            else:
                st.info("Request data needs Status and Assigned_Nurse fields.")
        else:
            st.info("No requests available to assign.")

def display_analytics():
    """Display analytics and metrics"""
    st.header("Analytics")
    
    # Create metrics tiles
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Requests", "24")
    
    with col2:
        st.metric("Active Requests", "8", "+2")
    
    with col3:
        st.metric("Completed Requests", "16", "+3")
    
    with col4:
        st.metric("Available Nurses", "6", "-1")
    
    # Request trend chart
    st.subheader("Request Trends")
    
    # Sample data for chart - in a real app, generate from actual data
    chart_data = pd.DataFrame({
        'Date': pd.date_range(start='2023-01-01', periods=12, freq='M'),
        'New Requests': [8, 10, 12, 15, 13, 18, 20, 17, 19, 22, 21, 24],
        'Completed': [7, 9, 10, 13, 11, 15, 17, 15, 16, 19, 18, 20]
    })
    
    # Convert to format suitable for plotting
    chart_data = chart_data.melt('Date', var_name='Metric', value_name='Count')
    
    # Display chart
    st.line_chart(chart_data, x='Date', y='Count', color='Metric')
    
    # Assignment distribution pie chart
    st.subheader("Request Status Distribution")
    
    # Sample data for pie chart
    status_data = {
        'Status': ['New', 'Assigned', 'In Progress', 'Completed', 'Cancelled'],
        'Count': [5, 8, 6, 16, 2]
    }
    status_df = pd.DataFrame(status_data)
    
    # Display pie chart
    st.bar_chart(status_df, x='Status', y='Count')
