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
            # Debug info
            st.write(f"Attempting login with username: '{username}'")
            
            # For demonstration - hardcoded credentials
            # In a real app, use a secure authentication system with database
            if username == "admin" and password == "adminpass":
                # Set admin role
                st.session_state['user_role'] = 'admin'
                st.success("Admin login successful!")
                return True
            elif username == "user" and password == "password":
                # Set regular user role
                st.session_state['user_role'] = 'user'
                st.success("User login successful!")
                return True
            else:
                st.error(f"Invalid username or password: '{username}'/'{password}'")
    
    return False

def logout_button():
    """
    Renders a logout button
    Returns True if logout button is clicked
    """
    if st.button("Logout"):
        # Clear user role when logging out
        if 'user_role' in st.session_state:
            del st.session_state['user_role']
        return True
    return False
