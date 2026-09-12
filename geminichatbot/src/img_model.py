from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

def get_gemini_response(question, image):

    if question:
        contents = [question, image]
    else:
        contents = [image]

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents
    )

    return response.text


st.set_page_config(
    page_title="Gemini Pro Chatbot",
    page_icon="🤖"
)

st.header("Gemini Application 🤖")

input_text = st.text_input(
    "Ask a question about the image:",
    key="input"
)

uploaded_file = st.file_uploader(
    "Choose an image:",
    type=["jpg", "jpeg", "png"]
)

image = None

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

submit = st.button("Tell me about the image")

if submit:

    if image is not None:

        response = get_gemini_response(
            input_text,
            image
        )

        st.subheader("Response:")

        st.write(response)

    else:

        st.warning("Please upload an image first!")