from dotenv import load_dotenv
import os
import streamlit as st
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

st.set_page_config(
    page_title="GemiSni Pro Chatbot",
    page_icon="🤖"
)

st.header("Gemini Pro Chatbot")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


def get_gemini_response(question):

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question
    )

    return response.text


input_text = st.text_input(
    "Ask a question:",
    key="input"
)

submit_button = st.button("Ask the question")


if submit_button and input_text:

    response = get_gemini_response(input_text)

    st.subheader("Response:")

    st.write(response)

    st.session_state["chat_history"].append(
        ("You", input_text)
    )

    st.session_state["chat_history"].append(
        ("Bot", response)
    )


st.subheader("THE CHAT HISTORY IS:")

for role, text in st.session_state["chat_history"]:
    st.write(f"**{role}:** {text}")