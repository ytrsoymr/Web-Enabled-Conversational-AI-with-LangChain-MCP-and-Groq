import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def chat():
    # Load environment variables
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    # Load MCP config
    config_file = "E:/MCP_Demo/MCPDemo/browser_mcp.json"
    client = MCPClient.from_config_file(config_file)

    # Create LLM
    llm = ChatGroq(model="qwen-qwq-32b")  # or try "llama3-8b-8192" or "mixtral-8x7b-32768"

    # Create agent
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    print("🤖 Hello! I'm your AI assistant. Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            result = await agent.run(user_input)
            print(f"Assistant: {result}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}\n")

if __name__ == "__main__":
    asyncio.run(chat())
