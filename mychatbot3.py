import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("Missing GEMINI_API_KEY in .env file. Please add it and restart the app.")
    st.stop()

# Configure Gemini
genai.configure(api_key=API_KEY)
MODEL_NAME = "gemini-2.5-flash"

# Streamlit UI
st.set_page_config(page_title="GSK Bot", layout="wide")
st.title("GSK Bot")
st.markdown("An intelligent text Search assistant powered by **Gemini** and **Streamlit**.")

# User input
user_input = st.text_input("Type your message here...")

if st.button("Search"):
    if user_input.strip():
        with st.spinner("GSK Bot is thinking..."):
            try:
                model = genai.GenerativeModel(MODEL_NAME)
                response = model.generate_content(user_input)
                reply = response.text
            except Exception as e:
                reply = f"Error: {e}"

        st.write(reply)
    else:
        st.warning("😎 Please enter a message before searching.")

