# 🧠 Web-Enabled LLM Chat Assistant with MCP Integration

This is a conversational AI chatbot built using **LangChain**, **Groq LLMs**, and **MCP (Multi-Component Protocol)**. It enables powerful interactions by leveraging external tools like **DuckDuckGo search**, **Playwright browser**, and more to fetch real-time information and enhance responses.

---

## 🚀 Features

- 🌐 Web-enabled chatbot with real-time search capabilities  
- 🧩 Tool usage powered by MCP and LangChain agents  
- 🗣️ Natural conversations using Groq's Qwen/QWQ/32B or LLaMA3 models  
- 🔧 Easily extendable with more tools (Airbnb search, Playwright, etc.)  
- 🧵 Streamlit-based user interface  

---

## 🧰 Technologies Used

- [LangChain](https://www.langchain.com/)
- [Groq](https://groq.com/) LLM API
- [MCP](https://github.com/mcp-lang/mcp)
- [Streamlit](https://streamlit.io/)
- Python 3.11+

---

## 🔐 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/MCPDemo.git
cd MCPDemo

2. Create and Activate Virtual Environment
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate  # For Windows
3. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
4. Add Environment Variable
Create a .env file:

ini
Copy
Edit
GROQ_API_KEY=your_groq_api_key_here
5. Create MCP Configuration
Create a file called browser_mcp.json with the following content:

json
Copy
Edit
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": ["@playwright/mcp@latest"]
    },
    "airbnb": {
      "command": "npx",
      "args": ["-y", "@openbnb/mcp-server-airbnb"]
    },
    "duckduckgo-search": {
      "command": "npx",
      "args": ["-y", "duckduckgo-mcp-server"]
    }
  }
}
💬 Running the Streamlit Chatbot
Make sure your virtual environment is activated, then run:

bash
Copy
Edit
streamlit run streamlit_app.py
🛠 Example Query
"Find the best Italian restaurants in San Francisco using Google Search"

The agent will automatically use tools like DuckDuckGo Search or Playwright Browser (if configured) to fetch results and respond.
