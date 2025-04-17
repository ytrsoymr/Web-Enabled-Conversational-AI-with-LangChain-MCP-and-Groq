# 🧠 Web-Enabled LLM Chat Assistant with MCP Integration

A powerful conversational AI chatbot built using **LangChain**, **Groq LLMs**, and **MCP (Multi-Component Protocol)**. It enables enhanced interactions by leveraging external tools like **DuckDuckGo search**, **Playwright browser**, and more to fetch real-time information and provide intelligent responses.

## 🚀 Features

- 🌐 **Web-enabled:** Access real-time information through search and web browsing
- 🧩 **Tool integration:** Powered by MCP and LangChain agents
- 🗣️ **Advanced LLMs:** Uses Groq's Qwen/QWQ/32B or LLaMA3 models for natural conversations
- 🔧 **Extensible architecture:** Easily add more tools (Airbnb search, etc.)
- 🧵 **User-friendly interface:** Built with Streamlit

## 🧰 Technologies Used

- [LangChain](https://www.langchain.com/) - Framework for developing applications powered by language models
- [Groq](https://groq.com/) - Ultra-fast LLM inference API
- [MCP](https://github.com/mcp-lang/mcp) - Multi-Component Protocol for tool integration
- [Streamlit](https://streamlit.io/) - Web interface framework
- Python 3.11+

## 🔐 Setup

### Prerequisites

- Python 3.11 or higher
- Node.js and npm (for MCP servers)
- Groq API key

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/MCPDemo.git
   cd MCPDemo
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv .venv
   
   # For Windows
   .venv\Scripts\activate
   
   # For macOS/Linux
   source .venv/bin/activate
   ```

3. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**
   
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Create MCP Configuration**
   
   Create a file called `browser_mcp.json` with the following content:
   ```json
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
   ```

## 💬 Running the Application

1. **Start the Streamlit Server**
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Access the Web Interface**
   
   Open your browser and navigate to `http://localhost:8501`

## 🚀 Usage Examples

### Example Queries

- "Find the best Italian restaurants in San Francisco"
- "What are the latest news about artificial intelligence?"
- "Show me vacation rentals in Miami for next weekend"
- "Summarize the content from https://example.com/article"

The assistant will automatically select and use appropriate tools like DuckDuckGo Search or Playwright Browser to fetch results and respond to your queries.

## 🧩 Adding New Tools

The MCP architecture makes it easy to extend the assistant with new capabilities:

1. Find or create an MCP-compatible tool server
2. Add the tool configuration to `browser_mcp.json`
3. Update the agent's tool selection logic in the code if necessary


## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [LangChain](https://www.langchain.com/) for the agent framework
- [Groq](https://groq.com/) for the LLM API
- [MCP](https://github.com/mcp-lang/mcp) for the tool integration protocol
- All MCP tool providers

