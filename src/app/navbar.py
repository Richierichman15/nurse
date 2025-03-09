import streamlit as st

def navbar():
    """
    Renders a navigation bar for the nursing staffing agency website
    """
    cols = st.columns(8 if 'user_role' in st.session_state and st.session_state['user_role'] == 'admin' else 7)
    
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
    
    # Show Admin link only for admin users
    if 'user_role' in st.session_state and st.session_state['user_role'] == 'admin':
        with cols[7]:
            if st.button("Admin", type="primary"):
                st.session_state['current_page'] = 'admin'
                st.rerun()
    
    st.divider()  # Add a divider below the navbar
