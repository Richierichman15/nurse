import streamlit as st
from navbar import navbar

def home_page():
    """
    Renders the home page for the nursing staffing agency
    """
    # Display navbar
    navbar()
    
    # Hero section
    st.title("Quality Nursing Staff When You Need It")
    st.markdown("### Your Trusted Partner in Healthcare Staffing Solutions")
    
    # Main content
    st.write("""
    Welcome to NurseConnect - the premier nursing staffing agency dedicated to connecting 
    qualified nursing professionals with healthcare facilities nationwide. With years of experience 
    in the healthcare industry, we understand the critical importance of having the right staff 
    at the right time.
    """)
    
    # Featured services section
    st.subheader("Our Services")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### Temporary Staffing")
        st.write("Quick access to qualified nurses for short-term needs.")
        if st.button("Learn More", key="temp_staffing"):
            st.session_state['current_page'] = 'services'
            st.rerun()
    
    with col2:
        st.markdown("#### Permanent Placement")
        st.write("Find the perfect long-term addition to your healthcare team.")
        if st.button("Learn More", key="perm_placement"):
            st.session_state['current_page'] = 'services'
            st.rerun()
    
    with col3:
        st.markdown("#### Specialized Care")
        st.write("Skilled nurses for specialized care requirements.")
        if st.button("Learn More", key="specialized"):
            st.session_state['current_page'] = 'services'
            st.rerun()
    
    # Call to action section
    st.divider()
    st.subheader("Join Our Network")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### For Nurses")
        st.write("Looking for flexible assignments or permanent positions? Join our team of dedicated nursing professionals.")
        if st.button("Apply Now", key="nurse_apply"):
            st.session_state['current_page'] = 'for_nurses'
            st.rerun()
    
    with col2:
        st.markdown("### For Healthcare Facilities")
        st.write("Need qualified nursing staff? We can provide skilled professionals to meet your staffing needs.")
        if st.button("Request Staff", key="request_staff"):
            st.session_state['current_page'] = 'for_clients'
            st.rerun()
