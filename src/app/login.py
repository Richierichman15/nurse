import streamlit as st

def login_page():
    """
    Renders a login page and handles authentication
    Returns True if login is successful, False otherwise
    """
    st.title("Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            # For demonstration - hardcoded credentials
            # In a real app, use a secure authentication system
            if username == "admin" and password == "password":
                return True
            else:
                st.error("Invalid username or password")
    
    return False

def logout_button():
    """
    Renders a logout button
    Returns True if logout button is clicked
    """
    if st.button("Logout"):
        return True
    return False
