import streamlit as st
from navbar import navbar

def services_page():
    """
    Renders the services page with information about different types of care offered
    """
    # Display navbar
    navbar()
    
    st.title("Our Nursing Services")
    st.write("We offer a comprehensive range of nursing care services to meet your healthcare needs.")
    
    # Introduction section
    st.markdown("""
    At our agency, we understand that each patient has unique care requirements. 
    Our team of skilled nurses is trained to provide personalized care across various 
    settings, ensuring the highest quality of healthcare services.
    """)
    
    st.divider()
    
    # Home Visits Service
    st.header("Home Visits")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # You can add an image here
        st.image("https://placehold.co/400x300?text=Home+Visits", use_column_width=True)
    
    with col2:
        st.subheader("Professional Nursing Care in the Comfort of Your Home")
        st.markdown("""
        Our home visit service provides professional nursing care right in the comfort of your own home. 
        Our skilled nurses will:
        
        * Perform health assessments and vital signs monitoring
        * Administer medications and treatments as prescribed
        * Provide wound care and dressing changes
        * Offer education on health conditions and self-care techniques
        * Coordinate with your healthcare providers
        
        Home visits can be scheduled as one-time visits or regular check-ins, 
        depending on your healthcare needs.
        """)
        
        if st.button("Request Home Visit Service"):
            st.session_state['current_page'] = 'request'
            st.rerun()
    
    st.divider()
    
    # Overnight Stays Service
    st.header("Overnight Stays")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # You can add an image here
        st.image("https://placehold.co/400x300?text=Overnight+Stays", use_column_width=True)
    
    with col2:
        st.subheader("Round-the-Clock Nursing Care")
        st.markdown("""
        Our overnight nursing service ensures continuous care during nighttime hours, 
        providing peace of mind for patients and their families. Our overnight nurses:
        
        * Monitor health status throughout the night
        * Administer medications on schedule
        * Assist with positioning and comfort measures
        * Provide immediate response to any health concerns
        * Support nighttime personal care needs
        
        This service is ideal for patients who require monitoring or assistance 
        during nighttime hours, post-surgical recovery, or those with chronic conditions.
        """)
        
        if st.button("Request Overnight Care"):
            st.session_state['current_page'] = 'request'
            st.rerun()
    
    st.divider()
    
    # Home Assistance Care Service
    st.header("Home Assistance Care")
    col1, col2 = st.columns([1, 2])
    
    with col1:
        # You can add an image here
        st.image("https://placehold.co/400x300?text=Home+Assistance", use_column_width=True)
    
    with col2:
        st.subheader("Comprehensive Support for Daily Living")
        st.markdown("""
        Our home assistance care provides comprehensive support to help patients 
        maintain independence while receiving necessary help with daily activities. 
        Our care providers assist with:
        
        * Personal care (bathing, grooming, dressing)
        * Meal preparation and nutrition monitoring
        * Light housekeeping and laundry
        * Medication reminders
        * Mobility assistance and fall prevention
        * Companionship and emotional support
        
        This service can be customized to include as much or as little assistance as needed,
        from a few hours a day to full-time care.
        """)
        
        if st.button("Request Home Assistance"):
            st.session_state['current_page'] = 'request'
            st.rerun()
    
    st.divider()
    
    # Call to action section
    st.subheader("Need a Customized Care Plan?")
    st.write("Contact us today to discuss your specific healthcare needs and let us create a personalized care plan for you or your loved one.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Contact Us", key="contact_cta"):
            st.session_state['current_page'] = 'contact'
            st.rerun()
    with col2:
        if st.button("Request Service", key="request_cta"):
            st.session_state['current_page'] = 'request'
            st.rerun()
