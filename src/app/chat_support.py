import streamlit as st
import openai
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to initialize session state variables for chat
def init_chat_session_state():
    """Initialize session state variables for the chat feature"""
    if 'chat_messages' not in st.session_state:
        st.session_state['chat_messages'] = []
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = {}  # Store chat history by user
    if 'is_chatting' not in st.session_state:
        st.session_state['is_chatting'] = False

def generate_ai_response(prompt, chat_history=None):
    """
    Generate AI response using OpenAI API
    
    Args:
        prompt (str): User message
        chat_history (list, optional): Previous conversation history
        
    Returns:
        str: AI response
    """
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
    
    try:
        # Create messages array for chat completion
        messages = []
        
        # System message to define the assistant's behavior
        system_message = """
        You are a helpful customer support assistant for a nurse services platform. 
        Your goal is to provide accurate information about our services, help users 
        understand how to request nurses, and answer general questions about healthcare.
        Be professional, empathetic, and concise in your responses.
        Do not provide medical advice or diagnoses.
        If you don't know an answer, be honest and offer to connect the user with a human representative.
        """
        messages.append({"role": "system", "content": system_message})
        
        # Add chat history if provided
        if chat_history:
            for msg in chat_history:
                messages.append(msg)
        
        # Add the current user message
        messages.append({"role": "user", "content": prompt})
        
        # Create chat completion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200,
            temperature=0.7,
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

def chat_support_page():
    """Render the chat support page"""
    st.title("Chat Support")
    
    # Initialize session state variables
    init_chat_session_state()
    
    # Display chat interface
    st.write("Welcome to our chat support! How can we help you today?")
    
    # Create columns for chat display and controls
    col1, col2 = st.columns([3, 1])
    
    with col1:
        # Chat input
        user_message = st.text_input("Type your message here:", key="chat_input")
        
        # Send button
        if st.button("Send") and user_message:
            # Add user message to chat history
            st.session_state['chat_messages'].append({"role": "user", "content": user_message})
            
            # Get AI response
            with st.spinner("Generating response..."):
                ai_response = generate_ai_response(
                    user_message, 
                    st.session_state['chat_messages']
                )
            
            # Add AI response to chat history
            st.session_state['chat_messages'].append({"role": "assistant", "content": ai_response})
            
            # Save to user's chat history if logged in
            if 'username' in st.session_state:
                if st.session_state['username'] not in st.session_state['chat_history']:
                    st.session_state['chat_history'][st.session_state['username']] = []
                
                st.session_state['chat_history'][st.session_state['username']].append({
                    "user_message": user_message,
                    "ai_response": ai_response,
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
            
            # Clear input
            st.session_state['chat_input'] = ""
    
    with col2:
        # Chat controls
        if st.button("Start New Chat"):
            st.session_state['chat_messages'] = []
            st.experimental_rerun()
        
        if st.button("Talk to Human Agent"):
            st.info("We'll connect you with a human agent shortly. Please wait.")
            # In a real implementation, this could trigger a notification to human agents
    
    # Display chat messages
    st.subheader("Conversation")
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state['chat_messages']:
            if msg["role"] == "user":
                st.markdown(f"**You:** {msg['content']}")
            else:
                st.markdown(f"**Support Agent:** {msg['content']}")
            st.write("---")

def admin_chat_dashboard():
    """Admin dashboard for viewing customer chat histories"""
    if 'user_role' not in st.session_state or st.session_state['user_role'] != 'admin':
        st.error("You don't have permission to access this page.")
        return
    
    st.title("Customer Chat Dashboard")
    
    if not st.session_state['chat_history']:
        st.info("No chat histories available yet.")
        return
    
    # Select user to view chat history
    user_select = st.selectbox(
        "Select user to view chat history:",
        options=list(st.session_state['chat_history'].keys())
    )
    
    if user_select:
        st.subheader(f"Chat history for {user_select}")
        
        for i, chat in enumerate(st.session_state['chat_history'][user_select]):
            with st.expander(f"Conversation {i+1} - {chat['timestamp']}"):
                st.write(f"**User:** {chat['user_message']}")
                st.write(f"**AI:** {chat['ai_response']}") 