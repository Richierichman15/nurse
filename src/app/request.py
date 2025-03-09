import streamlit as st
import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from navbar import navbar
import datetime

# Email configuration - replace with your actual email settings
EMAIL_SENDER = "GRNLLC8@gmail.com"  # Your email address
EMAIL_PASSWORD = "uhrs yyhv pfov pjxx"    # Your email password or app password
EMAIL_RECIPIENT = "GRNLLC8@gmail.com"  # Where to send notifications
SMTP_SERVER = "smtp.gmail.com"          # SMTP server (example for Gmail)
SMTP_PORT = 587                         # SMTP port (example for Gmail TLS)

def send_email_notification(request_data):
    """
    Sends an email notification with the request details
    
    Args:
        request_data: Dictionary containing the request information
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECIPIENT
        msg['Subject'] = f"New Nurse Request from {request_data['Name']}"
        
        # Create email body
        body = f"""
        A new nursing assistance request has been submitted:
        
        Name: {request_data['Name']}
        Phone: {request_data['Phone']}
        Address: {request_data['Address']}
        
        Request Description:
        {request_data['Description']}
        
        This request has been recorded in your database.
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Connect to server and send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Enable TLS encryption
        
        # Debug information
        st.write(f"Connecting to: {SMTP_SERVER}:{SMTP_PORT}")
        
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        return True
    except Exception as e:
        st.error(f"Failed to send email notification: {str(e)}")
        return False

def request_page():
    """
    Renders the nurse request page with form to request nursing assistance
    """
    # Display navbar
    navbar()
    
    st.title("Nurse Help Request")
    st.write("If you need assistance from a nurse, please fill out the form below.")

    file_path = 'nurse_requests.csv'

    with st.form(key='nurse_request_form'):
        # If user is logged in, use their username, otherwise ask for name
        if 'logged_in' in st.session_state and st.session_state['logged_in'] and 'username' in st.session_state:
            name = st.session_state['username']
            st.write(f"Requesting as: {name}")
        else:
            name = st.text_input("Your Name:")
        
        phone = st.text_input("Your Phone Number:")
        address = st.text_input("Your Address:")
        request_description = st.text_area("Describe your request:")

        submit_button = st.form_submit_button("Send Request")

        if submit_button:
            if name and phone and address and request_description:
                # Get current date
                today = datetime.datetime.now().strftime("%Y-%m-%d")
                
                # Create request data with required fields
                request_data = {
                    'Name': name,
                    'Phone': phone,
                    'Address': address,
                    'Description': request_description,
                    'Status': 'New',  # Initialize with New status
                    'Request_Date': today,  # Add request date
                    'Assigned_Nurse': 'Unassigned'  # Initialize as unassigned
                }
                
                # Create DataFrame for CSV storage
                new_request = pd.DataFrame([request_data])
                
                # Save to CSV
                if os.path.exists(file_path):
                    # Check if file has all required columns
                    existing_df = pd.read_csv(file_path)
                    
                    # Add any missing columns
                    for col in request_data.keys():
                        if col not in existing_df.columns:
                            existing_df[col] = None
                    
                    # Save the updated DataFrame with the new row
                    pd.concat([existing_df, new_request], ignore_index=True).to_csv(file_path, index=False)
                else:
                    new_request.to_csv(file_path, mode='w', header=True, index=False)
                
                # Send email notification
                email_sent = send_email_notification(request_data)
                
                # Show success message
                st.success("Submitted successfully! Getting your local nurse soon.")
                if email_sent:
                    st.info("A notification has been sent to our team.")
            else:
                st.error("Please fill out all fields before submitting.")
