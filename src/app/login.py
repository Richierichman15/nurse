import streamlit as st

def login_page():
    """
    Renders a login page and handles authentication
    Returns True if login is successful, False otherwise
    """
    st.title("Login")
    
    # Display test credentials for easy testing
    with st.expander("Test Credentials (For Development)"):
        st.write("**Admin:** username = 'admin', password = 'adminpass'")
        st.write("**Client:** username = 'client', password = 'clientpass'")
        st.write("**Regular User:** username = 'user', password = 'password'")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            # For demonstration - hardcoded credentials
            # In a real app, use a secure authentication system with database
            if username == "admin" and password == "adminpass":
                # Set admin role
                st.session_state['user_role'] = 'admin'
                st.session_state['username'] = username
                st.success("Admin login successful!")
                return True
            elif username == "client" and password == "clientpass":
                # Set client role
                st.session_state['user_role'] = 'client'
                st.session_state['username'] = username
                st.success("Client login successful!")
                return True
            elif username == "user" and password == "password":
                # Set regular user role
                st.session_state['user_role'] = 'user'
                st.session_state['username'] = username
                st.success("User login successful!")
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
        # Clear user role when logging out
        if 'user_role' in st.session_state:
            del st.session_state['user_role']
        if 'username' in st.session_state:
            del st.session_state['username']
        return True
    return False
