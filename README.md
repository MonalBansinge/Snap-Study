# 📚 Snap Study

**Snap Study** is an AI-powered study assistant built with Python and Streamlit. It helps students interact with study content through a simple and user-friendly web interface.

The application uses the **Google Gemini API** to generate AI-based responses and supports image processing using **Pillow**. It also includes Gmail integration for sending information through email.

## ✨ Features

* 🤖 AI-powered study assistance
* 💬 Interactive chat-based interface
* 🖼️ Image input and processing
* 🧠 AI responses using Google Gemini
* 📧 Gmail integration
* 🌐 Simple web-based interface
* 📱 Easy-to-use Streamlit application

## 🛠️ Technologies Used

* **Python** – Core programming language
* **Streamlit** – Web application framework
* **Google Gemini API** – AI-powered responses
* **Pillow (PIL)** – Image processing
* **Gmail** – Email integration
* **Git & GitHub** – Version control and project hosting

## 📂 Project Structure

```text
Snap-Study/
│
├── app.py
├── prompts.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

> `secrets.toml` contains private credentials and should never be uploaded to GitHub.

## ⚙️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/MonalBansinge/Snap-Study.git
```

### 2. Open the Project Folder

```bash
cd Snap-Study
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell shows an execution-policy error, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔐 Configure Secrets

Create a folder named `.streamlit` in the project directory and create a file named:

```text
secrets.toml
```

Add the required credentials:

```toml
GMAIL_ADDRESS = "your-email@gmail.com"
GMAIL_APP_PASSWORD = "your-app-password"
```

If your application uses additional API credentials, add them to `secrets.toml` according to the variables used in `app.py`.

### Important

Never commit or upload `secrets.toml` to GitHub.

The project includes `.gitignore` to prevent private credentials and the virtual environment from being uploaded.

## ▶️ Run the Application

After activating the virtual environment, run:

```bash
python -m streamlit run app.py
```

Streamlit will start the application and provide a local URL in the terminal.

## 🌐 Deployment

Snap Study can be deployed using **Streamlit Community Cloud** by connecting the GitHub repository.

For deployment:

1. Connect the GitHub repository.
2. Select the `main` branch.
3. Select `app.py` as the main application file.
4. Add the required secrets in the Streamlit Cloud **Secrets** section.
5. Deploy the application.

After deployment, the application can be accessed through its Streamlit Cloud URL.

## 🔄 Updating the Project

After making changes locally:

```bash
git add .
git commit -m "Updated Snap Study"
git push origin main
```

If the GitHub repository is connected to Streamlit Cloud, the deployed application can be updated automatically after the new changes are pushed.

## 🔒 Security

Do not upload:

```text
.streamlit/secrets.toml
venv/
```

Never expose:

* Gmail App Password
* API keys
* Other private credentials

## 🎯 Purpose

The main purpose of Snap Study is to provide students with a simple AI-assisted platform for interacting with study-related content and making learning more convenient.

## 👨‍💻 Developer

**Monal Bansinge**

Electronics and Communication Engineering Student

GitHub: [MonalBansinge](https://github.com/MonalBansinge)

