import streamlit as st
from google import genai

# 🔑 API KEY
client = genai.Client(api_key="AIzaSyC4wi4lTfdmvWJEkNiehdpkvyDOX47GJW4")

st.title("🤖 AI Plant Assistant (Real AI)")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
user_input = st.chat_input("Ask anything about plants...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=user_input
        )
        reply = response.text

    except Exception as e:
        reply = f"Error: {str(e)}"

    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()