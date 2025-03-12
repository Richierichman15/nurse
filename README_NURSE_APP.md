# Nurse Staffing Application

A Streamlit-based web application for managing nurse staffing services, client requests, and administrative tasks.

## Features

- User authentication (admin, client, and regular user roles)
- Service offerings and information
- Nurse request management
- Administrative dashboard
- Client dashboard
- AI-powered chat support for customer service

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Create a virtual environment:
```bash
python -m venv .venv
```

3. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Configure environment variables:
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key for the chat support feature
```bash
cp .env.example .env
# Edit the .env file with your values
```

### Running the Application

```bash
streamlit run src/app/main.py
```

Visit http://localhost:8501 in your browser to access the application.

## Chat Support Feature

The application includes an AI-powered chat support system that:

1. Provides automated customer service using OpenAI's GPT models
2. Preserves chat history for logged-in users
3. Allows administrators to view all customer conversations
4. Offers an option to escalate to human support when needed

### Setting Up Your OpenAI API Key

1. Create an account at [OpenAI](https://platform.openai.com/) if you don't have one
2. Generate an API key in your OpenAI dashboard
3. Add the API key to your `.env` file:
```
OPENAI_API_KEY=your_api_key_here
```

### Customizing the AI Agent

You can customize the AI agent's behavior by modifying the system message in the `generate_ai_response` function in `src/app/chat_support.py`.

## License

[MIT License](LICENSE) 