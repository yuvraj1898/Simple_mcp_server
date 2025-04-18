# 📚 Simple MCP Info Server

A FastMCP-powered microservice that provides search tools for **Wikipedia** and **Arxiv** using the LangChain Community utilities.

---
This project demonstrates how to create and run an **MCP (Modular Capability Protocol)** server using [`FastMCP`](https://github.com/anthropics/mcp). It provides simple tools that Claude Desktop can use to **search Wikipedia** and **fetch academic papers from Arxiv**.

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






