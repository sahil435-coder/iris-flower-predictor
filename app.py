import streamlit as st
from utils.auth import login

# Session setup
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

# If NOT logged in
if not st.session_state["logged_in"]:
    login()
    st.stop()

# After login
st.sidebar.write(f"👤 {st.session_state['user']}")

if st.sidebar.button("Logout"):
    st.session_state["logged_in"] = False
    st.rerun()

st.title("🌸 Smart Iris AI System")
st.write("Welcome to your dashboard 🚀")