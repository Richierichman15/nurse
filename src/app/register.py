import streamlit as st

def register_page():
    """
    Renders a registration page for new users to create an account
    Returns True if registration is successful, False otherwise
    """
    st.title("Create an Account")
    
    with st.form("register_form"):
        username = st.text_input("Choose a Username")
        password = st.text_input("Create a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Register")
        
        if submit:
            if not username or not password:
                st.error("Username and password are required")
                return False
                
            if password != confirm_password:
                st.error("Passwords do not match")
                return False
            
            # In a real application, you would:
            # 1. Check if username already exists
            # 2. Hash the password securely
            # 3. Store the new user in a database
            
            # For demonstration purposes only
            st.success(f"Account created successfully for {username}!")
            return True
    
    return False

def show_login_option():
    """
    Displays an option to go to the login page
    Returns True if the user wants to go to login
    """
    return st.button("Already have an account? Log in")
