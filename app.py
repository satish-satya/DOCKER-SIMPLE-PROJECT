

"""A tiny Streamlit chatbot used to demonstrate Docker.

The app reads GEMINI_API_KEY and GEMINI_MODEL from the environment.
Locally, python-dotenv loads them from a .env file.
In Docker, pass that file at startup with --env-file. It is not copied
into the image.
"""

import os

import streamlit as st
from dotenv import load_dotenv
from google import genai

# Load a local .env file when one exists. Variables already set in the
# environment are kept, so a key passed with --env-file is not replaced.
load_dotenv()

st.set_page_config(page_title="GenAI Chatbot")
st.title("GenAI Chatbot")

st.write(
    "A simple chatbot for a Docker lesson. "
    "Your message and the chat history are sent to a Gemini model, "
    "and the reply is shown below."
)

api_key = os.getenv("GEMINI_API_KEY", "").strip()
model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()

st.caption(f"Model: {model}")

if not api_key:
    st.error(
        "No Gemini API key found. Copy .env.example to .env, paste your key "
        "into GEMINI_API_KEY, and start the app again. When you use Docker, "
        "pass that file at runtime with --env-file .env."
    )
    st.stop()

# session_state keeps the conversation for this browser tab.
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_message = st.chat_input("Type a message")

if not user_message:
    st.stop()

st.session_state.messages.append(
    {"role": "user", "content": user_message}
)

with st.chat_message("user"):
    st.markdown(user_message)

client = genai.Client(api_key=api_key)

try:
    with st.spinner("Waiting for Gemini..."):

        chat_history = ""

        for msg in st.session_state.messages:
            role = msg["role"]
            content = msg["content"]
            chat_history += f"{role}: {content}\n"

        prompt = f"""
You are a helpful assistant in a beginner Docker and GenAI class.
Keep answers clear and short.

Conversation History:
{chat_history}
"""

        response = client.models.generate_content(
            model=model,
            contents=prompt
        )

        answer = response.text

except Exception as error:
    st.error(
        "The Gemini request failed. Check the API key, the model name, "
        f"and your network connection.\n\nDetails: {error}"
    )
    st.stop()

with st.chat_message("assistant"):
    st.markdown(answer)

st.session_state.messages.append(
    {"role": "assistant", "content": answer}
)