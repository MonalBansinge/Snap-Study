# 📚 Snap & Study

Snap & Study is an AI-powered study assistant that helps students understand problems, diagrams, notes, and study material using image analysis.

## 🚀 Features

* 📸 Upload study images
* 🤖 Analyze images using Google Gemini AI
* 💬 Ask questions about the uploaded image
* 📖 Get simple and easy-to-understand explanations
* 🖥️ Simple and user-friendly Streamlit interface

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Google GenAI SDK
* Pillow

## ⚙️ How It Works

1. Upload a problem, diagram, notes, or study image.
2. Enter an optional question about the image.
3. Click **Get Explanation**.
4. Gemini analyzes the image and question.
5. Snap & Study displays the explanation.

## 📁 Project Structure

```text
Snap-Study/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

> `secrets.toml` contains the API key and is excluded from GitHub using `.gitignore`.

## 🔑 API Key Setup

Create:

```text
.streamlit/secrets.toml
```

Add your Gemini API key:

```toml
GEMINI_API_KEY = "your-api-key-here"
```

Never upload your API key to GitHub.

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/MonalBansinge/Snap-Study.git
```

Go to the project folder:

```bash
cd Snap-Study
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 🎯 Purpose

The purpose of Snap & Study is to make learning easier by allowing students to use images of their study material and receive AI-powered explanations in a simple format.

## 🔮 Future Improvements

* Voice-based questions
* Multiple language support
* Step-by-step problem solving
* Study history
* Quiz generation
* Personalized learning assistance


## 📄 License

This project is created for learning and educational purposes.
