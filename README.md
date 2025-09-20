# 🤖 AI Agent with Internet Access



[![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent AI agent, powered by **LangChain** and **OpenAI**, that can browse the internet in real-time to answer your questions with the most up-to-date information.

---

## ✨ Features

* 🌐 **Live Internet Access**: Uses DuckDuckGo to search the web for current information.
* 🧠 **Powered by LLMs**: Leverages the power of OpenAI's models for intelligent and coherent responses.
* 🛠️ **Built with LangChain**: Utilizes the robust LangChain framework to create powerful agentic workflows.
* 🚀 **Easy to Set Up**: Get up and running with just a few simple commands.

---

## 🎬 Demo

Here's a quick look at the agent answering a question about a recent event:

*(This is a great place to add a screenshot or a GIF of your terminal session!)*



---

## ⚙️ How It Works

This agent uses a framework called **LangChain** to orchestrate its actions. The workflow is simple:
1.  **User Input**: You ask the agent a question.
2.  **Tool Selection**: The agent, powered by an OpenAI model, decides if it needs to search the internet to find an answer.
3.  **Web Search**: If needed, it uses the `DuckDuckGoSearchRun` tool to perform a web search.
4.  **Synthesize Answer**: The agent processes the search results and its own knowledge to formulate a final, comprehensive answer for you.

---

## 🚀 Getting Started

Follow these steps to set up and run the AI agent on your local machine.

### 1. Prerequisites

* Python 3.9 or higher
* An OpenAI API key. You can get one from the [OpenAI Platform](https://platform.openai.com/api-keys).

### 2. Clone the Repository

Clone this project to your local machine.
```bash
git clone [https://github.com/Divine-Emperor/Ai_agent_with_python.git](https://github.com/Divine-Emperor/Ai_agent_with_python.git)
cd Ai_agent_with_python
```

### 3. Install Dependencies

It's recommended to use a virtual environment.
```bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (macOS/Linux)
source venv/bin/activate
```
Now, install the required packages using the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

You need to provide your OpenAI API key.

1.  Create a file named `.env` in the root of your project directory.
2.  Add your API key to this file as follows:

    ```env
    OPENAI_API_KEY="your_super_secret_api_key_here"
    ```

### 5. Run the Agent!

You're all set! Run the `main.py` script to start interacting with your AI agent.
```bash
python main.py
```
The script will then prompt you to ask a question. Type your query and press Enter.

---

## 📝 Example Usage

Here is an example of an interaction with the agent:

```bash
> python main.py
> Ask your question: What is the latest news about the Artemis program?

> Entering new AgentExecutor chain...
 I need to find the most recent news about the Artemis program.
Action: duckduckgo_search
Action Input: "latest news Artemis program"
Observation: NASA's Artemis II crew, from left, Mission Specialist Christina Koch, Pilot Victor Glover, Commander Reid Wiseman and Mission Specialist Jeremy Hansen of the Canadian Space Agency. NASA astronaut and ...
Thought: I have found some recent news about the Artemis II crew and other updates. I should summarize this information to answer the user's question.

The latest news on the Artemis program includes updates on the Artemis II mission, which will be the first crewed flight. The crew has been announced and consists of NASA astronauts Reid Wiseman, Victor Glover, and Christina Koch, along with Canadian Space Agency astronaut Jeremy Hansen. They are currently undergoing intensive training for their mission around the Moon.

> Finished chain.
```
