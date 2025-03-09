import streamlit as st

def navbar():
    """
    Renders a navigation bar for the nursing staffing agency website
    """
    # Determine the number of columns based on user role
    if 'user_role' in st.session_state:
        if st.session_state['user_role'] == 'admin':
            # Admin gets Home, Services, For Nurses, For Clients, Jobs, Request, Contact, Admin
            cols = st.columns(8)
        else:  # Regular user/client gets a dashboard
            # User gets Home, Services, For Nurses, For Clients, Jobs, Request, Contact, Dashboard
            cols = st.columns(8)
    else:  # Not logged in
        # Not logged in gets Home, Services, For Nurses, For Clients, Jobs, Request, Contact
        cols = st.columns(7)
    
    with cols[0]:
        if st.button("Home"):
            st.session_state['current_page'] = 'home'
            st.rerun()
    
    with cols[1]:
        if st.button("Services"):
            st.session_state['current_page'] = 'services'
            st.rerun()
    
    with cols[2]:
        if st.button("For Nurses"):
            st.session_state['current_page'] = 'for_nurses'
            st.rerun()
    
    with cols[3]:
        if st.button("For Clients"):
            st.session_state['current_page'] = 'for_clients'
            st.rerun()
    
    with cols[4]:
        if st.button("Jobs"):
            st.session_state['current_page'] = 'jobs'
            st.rerun()
    
    with cols[5]:
        if st.button("Request"):
            st.session_state['current_page'] = 'request'
            st.rerun()
    
    with cols[6]:
        if st.button("Contact Us"):
            st.session_state['current_page'] = 'contact'
            st.rerun()
    
    # Show Admin link for admin users or Dashboard link for regular users
    if 'user_role' in st.session_state:
        with cols[7]:
            if st.session_state['user_role'] == 'admin':
                if st.button("Admin", type="primary"):
                    st.session_state['current_page'] = 'admin'
                    st.rerun()
            else:
                if st.button("My Dashboard", type="primary"):
                    st.session_state['current_page'] = 'client_dashboard'
                    st.rerun()
    
    st.divider()  # Add a divider below the navbar
