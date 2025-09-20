# AI Agent with Python 🤖

A simple yet powerful AI conversational agent built with Python, Streamlit, and Google's Gemini Pro. This application provides a clean web interface for users to ask questions and receive intelligent answers from a large language model.

![AI Agent Demo](https://i.imgur.com/your-demo-image.gif)
*Optional: You can create a short GIF of your app and upload it to a site like Imgur to embed here.*

---

## 📋 Table of Contents

- [Features](#-features)
- [Technologies Used](#-technologies-used)
- [Setup and Installation](#-setup-and-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## ✨ Features

- **Interactive Web UI**: A clean and user-friendly interface powered by Streamlit.
- **Powered by Gemini Pro**: Leverages Google's state-of-the-art Generative AI model for accurate and conversational responses.
- **Easy to Set Up**: Get the agent running locally with just a few commands.
- **Secure API Key Handling**: Uses environment variables to keep your API keys safe and private.

---

## 🛠️ Technologies Used

- **Backend**: Python
- **AI/LLM Framework**: LangChain
- **LLM Provider**: Google Gemini Pro
- **Web Framework**: Streamlit
- **API Key Management**: `python-dotenv`

---

## 🚀 Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. **Clone the Repository**

```bash
git clone [https://github.com/Divine-Emperor/Ai_agent_with_python.git](https://github.com/Divine-Emperor/Ai_agent_with_python.git)
cd Ai_agent_with_python
2. Create a Virtual Environment
It's recommended to use a virtual environment to manage project dependencies.

Bash

# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install all the required libraries from the requirements.txt file.

Bash

pip install -r requirements.txt
4. Set Up Environment Variables
You need a Google API key to use the Gemini model.

Get your API key from Google AI Studio.

Create a file named .env in the root of your project directory.

Add your API key to the .env file like this:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
The .gitignore file is already configured to prevent this file from being uploaded to GitHub.

💻 Usage
Once the installation is complete, you can run the Streamlit application with a single command:

Bash

streamlit run main.py
This will open a new tab in your web browser at http://localhost:8501. You can now start interacting with your AI agent!

📁 Project Structure
Ai_agent_with_python/
├── .gitignore         # Specifies intentionally untracked files to ignore
├── main.py            # The main application script
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.
