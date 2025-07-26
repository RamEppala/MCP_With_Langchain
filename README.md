# Multi-Agent System with LangChain, MCP, Groq API, and Custom Tool Servers

This project implements a multi-agent system using **LangChain**, **MCP**, and **Groq API**, designed for two external tools:
 **Math API** — runs via `stdio` (subprocess-based interface)
 **Weather API** — served over HTTP transport protocol

Built in **Cursor IDE** with AI-native development workflow.

---

##  Project Overview

The system uses:
-  **LangChain Agents** to delegate tasks
-  **MCP Protocol** for multi-agent collaboration
-  **Groq API** for ultra-fast LLM responses
- 🔧 Tool interfaces:
  - Math tool (invoked via command line using `subprocess`)
  - Weather tool (invoked via HTTP)

---

## Tech Stack

| Component     | Description                                   |
|---------------|-----------------------------------------------|
| LangChain     | LLM tool orchestration                        |
| MCP           | Agent protocol for task coordination          |
| Groq API      | Fast LLM inference (e.g., LLaMA, Mistral)     |
| Python 3.10+  | Main language                                 |
| Cursor IDE    | AI-assisted development                       |
| Math API      | Runs via `stdio` CLI                         |
| Weather API   | Accessible via `HTTP` (e.g., Flask/FastAPI)   |

---

**Cursor IDE Usage**
This project is best developed using Cursor IDE:

AI-enhanced autocomplete and function generation

Easy in-place documentation with LLMs

Integrated terminal to test stdio/HTTP APIs quickly

Tip: Activate Cursor’s LangChain plugin and Python agent to boost productivity.
