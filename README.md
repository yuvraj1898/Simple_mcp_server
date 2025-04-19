# 📚 Simple MCP Info Server

A FastMCP-powered microservice that provides search tools for **Wikipedia** and **Arxiv** using the LangChain Community utilities.

---
This project demonstrates how to create and run an **MCP (Model Context Protocol)** server using [`FastMCP`](https://github.com/anthropics/mcp). It provides simple tools that Claude Desktop can use to **search Wikipedia** and **fetch academic papers from Arxiv**.

---

## 🚀 What is MCP?

**Model Control Protocol (MCP)** is a protocol that allows language models like Claude to communicate with external tools (called "capabilities") in a standardized way. These capabilities can be:

- Functions written in any language
- Web APIs
- Local scripts

Using MCP, Claude can **invoke your tools**, get the response, and continue the conversation.

---

## 📚 What This Project Does

This Info Server exposes two tools via MCP:

1. `get_info(searchterm: str)` — Searches **Wikipedia** for short summaries
2. `get_research_paper(searchterm: str)` — Searches **Arxiv** for academic paper metadata

---
## ⚡ Overview

This tool exposes two FastMCP-compatible endpoints:

- `get_info`: Fetches summarized information from **Wikipedia**.
- `get_research_paper`: Retrieves academic paper details from **Arxiv**.

Designed for plug-and-play use in modular AI systems or agent runtimes.

---

## 🧰 Setup Guide

### ✅ Prerequisites

- Python 3.12+
- [`uv`](https://github.com/astral-sh/uv) installed  
  > _Install via_ `curl -LsSf https://astral.sh/uv/install.sh | sh` _or_ `brew install astral-sh/uv/uv`
  > 
  > _Windows_ `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
- Claude Desktop
  > ['Claude Desktop'](https://claude.ai/download) installed

---

### 🛠️ Project Initialization

```bash
uv init simple_mcp_server
cd simple_mcp_server
uv venv
source .venv/bin/activate
```
### 📦 Install Dependencies
```bash
uv add "mcp[cli]"
uv add langchain_community
uv add wikipedia
uv add arxiv
```
server.py (FastMCP)
Runs your Wikipedia + Arxiv search server locally.


🚀 Run the Server
Ensure you’re in the virtual environment, then:

```bash
uv run server.py
```

The server will run over stdio, ready to be called as an MCP tool.Just verify if there are any error.
### Option 1: Update claude_desktop_config.json (for Claude Desktop)
Run this command to open the config file in VS Code (or use any editor):
```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```
Replace or add the following mcpServers block:
```bash
{
  "mcpServers": {
    "info-server": {
      "command": "/Users/yuvrajfirodiya/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/yuvrajfirodiya/Source/Python-Langchain-Projects/simple_mcp_server",
        "run",
        "server.py"
      ]
    }
  }
}
```
✅Verify the following:

command: Make sure it points to your uv binary (which uv in terminal to confirm).

args: Points to the root of your MCP project.

"run", "server.py": You’re running the correct server file.



Or 
 ### Option 2: Use a Custom MCP Client (Host)

 You can also run the server using a custom MCP client built with the mcpclient library.

This is useful for advanced workflows, testing, or when integrating with your own LLM setup.

📄 client.py includes the full server specification and config
Set up the client using a structured config method like this:
import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

```bash
import asyncio
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient

async def main():
    # Load environment variables (e.g., GROQ_API_KEY)
    load_dotenv()

    # Define the MCP server config
    config = {
        "mcpServers": {
            "info-server": {
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

    # Initialize the client
    client = MCPClient.from_dict(config)

    # Initialize the Groq LLM (Llama 3)
    llm = ChatGroq(
        model_name="Llama3-8b-8192",
        streaming=True
    )

    # Build your agent
    agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # Ask a question
    result = await agent.run("tell me about donald trump")
    print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```
✅ Benefits of This Approach
🔓 No dependency on Claude Desktop UI

🧩 Easily swap out LLMs (Groq, OpenAI, etc.)

🧠 Full control over how your agent interacts with tools

⚙️ Configurable, scriptable, and scalable
 





