import streamlit as st
from PIL import Image 
from google import genai 
from prompts import WELCOME_MESSAGE


# Page configuration
st.set_page_config(
    page_title="Snap & Study",
    page_icon="📚",
    layout="centered"
)
#Gemini API setup 
@st.cache_resource 
def get_genai_client():
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])


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
        uploaded_file,
        caption="Your uploaded study image",
        use_container_width=True
    )

    st.success("Image uploaded successfully! ✅") 
    user_question = st.text_input( 
        
        "💬 Ask a question about the image (optional)",
        placeholder="Type your question here..."
    ) 

    if st.button("Get Explanation" , type="primary"):
        with st.spinner("Analyzing the image and generating explanation..."):
            # Get the GenAI client
            try:
                client = get_genai_client()
                prompt=user_question.strip() if user_question.strip() else "Please explain the content of the uploaded image."
                
                response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[prompt, image]
               )

            # Display the explanation
                st.subheader("📖 Explanation")
                st.write(response.text) 

            except Exception as e:  
                
                st.error(f"An error occurred: {e}")

            