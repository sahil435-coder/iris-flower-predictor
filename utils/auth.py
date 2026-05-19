import streamlit as st
import pandas as pd
import os

def login():
    st.title("🔐 Login System")

    # Check if users.csv exists and is not empty
    if not os.path.exists("users.csv") or os.stat("users.csv").st_size == 0:
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv("users.csv", index=False)
    else:
        df = pd.read_csv("users.csv")

    # Convert everything to string and clean spaces
    df['username'] = df['username'].astype(str).str.strip()
    df['password'] = df['password'].astype(str).str.strip()

    menu = ["Login", "Register"]
    choice = st.selectbox("Select Option", menu)

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    username = str(username).strip()
    password = str(password).strip()

    # LOGIN
    if choice == "Login":
        if st.button("Login"):
            if ((df['username'] == username) & (df['password'] == password)).any():
                st.session_state["logged_in"] = True
                st.session_state["user"] = username
                st.success("Login Successful")
                st.rerun()
            else:
                st.error("Invalid Credentials")

    # REGISTER
    elif choice == "Register":
        if st.button("Register"):
            new_user = pd.DataFrame([[username, password]], columns=["username", "password"])
            new_user.to_csv("users.csv", mode='a', header=False, index=False)
            st.success("User Registered Successfully")