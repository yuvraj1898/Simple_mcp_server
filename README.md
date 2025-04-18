# Simple_mcp_server
# 📚 Simple MCP Info Server

A FastMCP-powered microservice that provides search tools for **Wikipedia** and **Arxiv** using the LangChain Community utilities.

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
  > _Install via_ `cargo install uv` _or_ `brew install astral-sh/uv/uv`
-Claude Desktop(whcih will be mcp host) to test mcp server
  > https://claude.ai/download

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

🚀 Run the Server
Ensure you’re in the virtual environment, then:

```bash
uv run server.py
```

The server will run over stdio, ready to be called as an MCP tool.Just verify if there are any error.
### Update claude_desktop_config.json
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
✅ Make sure:

Command:The path to uv is correct (you can confirm with which uv in shell).
args:Path to the root of the project
run:You’re pointing to the correct .py file (server.py).






