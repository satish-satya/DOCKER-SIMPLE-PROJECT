GenAI Chatbot with Streamlit & Gemini
A simple AI chatbot built with Streamlit and Google Gemini. This project is designed for beginners who want to learn GenAI, Python, and Docker deployment.

Features
Chat interface built with Streamlit
Uses Google Gemini API for AI responses
Stores conversation history during the session
Environment variable support with .env
Docker-ready application
Beginner-friendly code structure
Project Structure
.
├── app.py
├── requirements.txt
├── commands.txt
├── Dockerfile
├── .env.example
└── README.md
Requirements
Python 3.10+
Google Gemini API Key
Docker (optional)
Installation
1. Clone the Repository
git clone <your-repository-url>
cd <project-folder>
2. Create Virtual Environment
python -m venv .venv
Activate the environment:

Windows

.venv\Scripts\activate
Linux / macOS

source .venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Environment Variables
Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
Run the Application
streamlit run app.py
Open your browser:

http://localhost:8501
Docker Setup
Build Docker Image
docker build -t genai-chatbot .
Run Docker Container
docker run -d --name genai-chatbot -p 8501:8501 --env-file .env genai-chatbot
Open:

http://localhost:8501
View Logs
docker logs genai-chatbot
Stop Container
docker stop genai-chatbot
Remove Container
docker rm genai-chatbot
Remove Image
docker rmi genai-chatbot
Technologies Used
Python
Streamlit
Google Gemini API
python-dotenv
Docker
How It Works
User enters a message in the Streamlit chat interface.
The application reads the Gemini API key from environment variables.
Current conversation history is combined into a prompt.
Gemini generates a response.
The response is displayed in the chatbot interface.
Security Notes
Never commit your .env file to GitHub.
Keep your Gemini API key private.
Use .env.example as a template for team members.
Learning Purpose
This project was created as a beginner-friendly example to learn:

Streamlit
Generative AI APIs
Environment Variables
Docker Fundamentals
Containerized Python Applications
License
This project is available for educational and learning purposes