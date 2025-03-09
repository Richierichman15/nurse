import streamlit as st

def navbar():
    """
    Renders a navigation bar for the nursing staffing agency website
    """
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        if st.button("Home"):
            st.session_state['current_page'] = 'home'
            st.rerun()
    
    with col2:
        if st.button("Services"):
            st.session_state['current_page'] = 'services'
            st.rerun()
    
    with col3:
        if st.button("For Nurses"):
            st.session_state['current_page'] = 'for_nurses'
            st.rerun()
    
    with col4:
        if st.button("For Clients"):
            st.session_state['current_page'] = 'for_clients'
            st.rerun()
    
    with col5:
        if st.button("Jobs"):
            st.session_state['current_page'] = 'jobs'
            st.rerun()
    
    with col6:
        if st.button("Request"):
            st.session_state['current_page'] = 'request'
            st.rerun()
    
    with col7:
        if st.button("Contact Us"):
            st.session_state['current_page'] = 'contact'
            st.rerun()
    
    st.divider()  # Add a divider below the navbar
