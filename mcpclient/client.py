import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables
    load_dotenv() #make sure add Groq API 

    # Create configuration dictionary
    config = {
        "mcpServers": {
            "info-server": {  # This needs to be a named server
                "command": "/Users/yuvrajfirodiya/.local/bin/uv",
                "args": [
                    "--directory",
                    "/Users/yuvrajfirodiya/Source/Python-Langchain-Projects/simple_mcp_server",
                    "run",
                    "server.py"
                ],
                "env": {
                    "DISPLAY": ":1"
                }
            }
        }
    }

    # Create MCPClient from configuration dictionary
    client = MCPClient.from_dict(config)

    # Create LLM
    llm = ChatGroq(
        model_name="Llama3-8b-8192",
        streaming=True
    )

    # Create agent with the client
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Run the query
    result = await agent.run(
        "tell me about donald trump",
    )
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())