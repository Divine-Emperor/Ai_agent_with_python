# 🤖 Local Code & File AI Agent with Gemini



[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An advanced AI agent that can interact with your local file system. Powered by **Google's Gemini Pro** and built with **LangChain**, this agent can read, write, and list files, as well as generate, debug, and execute Python code.

---

## ⚠️ Important Security Warning

> This agent is capable of modifying your local files and executing code. This grants it significant control over your system. **Do not run this agent in an environment with sensitive files.** Always review the code and understand the actions it's performing. It is highly recommended to run it in a sandboxed environment, like a Docker container or a dedicated virtual machine.
> 
> Furthermore, this is a demonstration project with only basic security guardrails. It is **not ready for production use** without significant refinement, rigorous testing, and the implementation of robust safety measures.

---

## ✨ Features

* 📂 **File System Interaction**: Can list directories, read files, and write to files.
* 💻 **Code Generation & Debugging**: Generate new Python scripts, analyze existing code for bugs, and write the fixes directly to the file.
* 🚀 **Code Execution**: Run Python scripts and see their output directly in the chat.
* 🧠 **Powered by Gemini**: Utilizes Google's advanced Gemini Pro model for reasoning and task planning.
* 💬 **Conversational Memory**: Remembers the context of your conversation to handle multi-step tasks.

---

## ⚙️ How It Works: The ReAct Agent Framework

This project uses a **ReAct Agent**. Instead of just chatting, the agent can reason and choose from a set of available **tools** to accomplish a task. The process for each request looks like this:

1.  **Thought**: The agent thinks about your request and breaks it down into steps.
2.  **Action**: It decides which tool to use (e.g., `ReadFile`).
3.  **Action Input**: It determines the input for that tool (e.g., the file path `'buggy_code.py'`).
4.  **Observation**: It receives the result from the tool (e.g., the code content).
5.  **Repeat**: It repeats this cycle of Thought-Action-Observation until it has gathered enough information to fulfill your original request and give you a final answer.

---

### Available Tools

The agent has access to the following custom tools:
* **ListFiles**: Lists files and folders in a directory.
* **ReadFile**: Reads the contents of a file.
* **WriteFile**: Creates or overwrites a file with new content.
* **RunPythonFile**: Executes a Python script and returns its output.

---

## 🚀 Getting Started

### 1. Prerequisites
* Python 3.9+
* A Google API Key from [Google AI Studio](https://makersuite.google.com/app/apikey).

### 2. Setup

```bash
# Clone the repository
git clone [https://github.com/Divine-Emperor/Ai_agent_with_python.git](https://github.com/Divine-Emperor/Ai_agent_with_python.git)
cd Ai_agent_with_python

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Create a .env file and add your API key
echo 'GOOGLE_API_KEY="your_google_api_key_here"' > .env
```

### 3. Run the Agent

Start the agent by running the `main.py` script.
```bash
python main.py
```

---

## ▶️ Example Usage

Here are a few examples of what you can ask the agent to do.

### Example 1: Generate and Run Code

```
>> You: Write a simple Python script that prints "Hello from my AI Agent!" and save it as hello.py. Then, run it.

> Entering new AgentExecutor chain...
Thought: The user wants me to create a Python script and then execute it. I need to use two tools in sequence: WriteFile and then RunPythonFile.

Action: WriteFile
Action Input: hello.py, print("Hello from my AI Agent!")
Observation: Successfully wrote to hello.py.
Thought: Now that the file is created, I need to run it.

Action: RunPythonFile
Action Input: hello.py
Observation: Output:
Hello from my AI Agent!

Thought: I have successfully created and executed the file. I can now give the final answer.
> Finished chain.

>> Agent: I have successfully created the `hello.py` script and ran it for you. The output was "Hello from my AI Agent!".
```

### Example 2: Find and Fix a Bug

```
>> You: I think there's a bug in 'hello.py', it should say "Hello World" instead. Please fix it.

> Entering new AgentExecutor chain...
Thought: The user wants to change the content of 'hello.py'. I need to use the WriteFile tool to overwrite the existing file with the corrected code.

Action: WriteFile
Action Input: hello.py, print("Hello World")
Observation: Successfully wrote to hello.py.
Thought: The file is now fixed. I should inform the user.
> Finished chain.

>> Agent: I have fixed the script. `hello.py` now prints "Hello World".
```
