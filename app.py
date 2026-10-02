
import streamlit as st
from PIL import Image
from google import genai
from prompts import WELCOME_MESSAGE

import smtplib
from email.mime.text import MIMEText


# Page configuration
st.set_page_config(
    page_title="Snap & Study",
    page_icon="📚",
    layout="centered"
)


# Gemini API setup
@st.cache_resource
def get_genai_client():
    return genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )


# Gmail setup
GMAIL_ADDRESS = st.secrets["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]


# Send email function
def send_email(to_address, subject, body):
    message = MIMEText(body)

    message["Subject"] = subject
    message["From"] = GMAIL_ADDRESS
    message["To"] = to_address

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            GMAIL_ADDRESS,
            GMAIL_APP_PASSWORD
        )

        server.send_message(message)


# Store explanation
if "explanation" not in st.session_state:
    st.session_state.explanation = None


# App title
st.title("📚 Snap & Study")

st.write(
    "Upload a problem, diagram, or notes and get a simple explanation."
)


# Welcome message
st.info(WELCOME_MESSAGE)


# Image upload
uploaded_file = st.file_uploader(
    "📸 Upload your study image",
    type=["png", "jpg", "jpeg"]
)


# Show uploaded image
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Your uploaded study image",
        use_container_width=True
    )

    st.success("Image uploaded successfully! ✅")

    user_question = st.text_input(
        "💬 Ask a question about the image (optional)",
        placeholder="Type your question here..."
    )

    # Generate explanation
    if st.button("Get Explanation", type="primary"):

        with st.spinner(
            "Analyzing the image and generating explanation..."
        ):

            try:
                client = get_genai_client()

                prompt = (
                    user_question.strip()
                    if user_question.strip()
                    else
                    "Please explain the content of the uploaded study image in simple language."
                )

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=[
                        prompt,
                        image
                    ]
                )

                st.session_state.explanation = response.text

                st.success(
                    "Explanation generated successfully! ✅"
                )

            except Exception as e:
                st.error(
                    f"An error occurred: {e}"
                )


# Display explanation
if st.session_state.explanation:

    st.subheader("📖 Explanation")

    st.write(
        st.session_state.explanation
    )

    # Email section
    st.subheader("📧 Send Explanation by Email")

    recipient_email = st.text_input(
        "Enter recipient email address"
    )

    if st.button("📤 Send to Email"):

        if recipient_email:

            try:
                send_email(
                    recipient_email,
                    "📚 Snap & Study - Your Explanation",
                    st.session_state.explanation
                )

                st.success(
                    "✅ Explanation sent successfully!"
                )

            except Exception as e:

                st.error(
                    f"Failed to send email: {e}"
                )

        else:

            st.warning(
                "Please enter an email address."
            )

