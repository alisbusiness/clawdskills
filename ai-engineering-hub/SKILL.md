---
name: ai-engineering-hub
description: Access to the patchy631/ai-engineering-hub GitHub repository — a library of 93+ production-ready AI engineering projects covering LLMs, RAG, Agents, MCP, fine-tuning, multimodal AI, voice/audio, and more. Use this skill whenever the user needs to (1) build an AI feature and wants a reference implementation, (2) implement RAG, agents, MCP servers, voice bots, OCR, or any AI workflow, (3) compare or evaluate AI models, (4) fine-tune or train models, (5) needs boilerplate or starter code for an AI project, or (6) asks about AI engineering patterns, architectures, or best practices. The skill enables fetching specific project code directly from GitHub for adaptation and use.
---

# AI Engineering Hub

This skill provides access to the **[patchy631/ai-engineering-hub](https://github.com/patchy631/ai-engineering-hub)** GitHub repository — a comprehensive collection of 93+ production-ready AI engineering projects.

## Repository Access

The full repository is available at:
```
https://github.com/patchy631/ai-engineering-hub
```

### How to Fetch Resources

To pull code from any project in the repository, use one of these methods:

#### 1. Clone a Specific Project (Sparse Checkout)

Use sparse checkout to fetch only the project folder needed, keeping the workspace clean:

```bash
git clone --depth 1 --filter=blob:none --sparse https://github.com/patchy631/ai-engineering-hub.git /tmp/ai-eng-hub
cd /tmp/ai-eng-hub
git sparse-checkout set <project-folder-name>
```

Then copy the relevant files into the user's workspace.

#### 2. Fetch a Single File via Raw URL

For individual files, use the raw GitHub URL pattern:

```
https://raw.githubusercontent.com/patchy631/ai-engineering-hub/main/<project-folder>/<filename>
```

Use `curl` or the `read_url_content` tool to fetch file contents directly.

#### 3. Browse Project Structure via GitHub API

To inspect a project's file tree before fetching:

```
https://api.github.com/repos/patchy631/ai-engineering-hub/contents/<project-folder>
```

#### 4. Clone the Full Repository

If multiple projects are needed:

```bash
git clone --depth 1 https://github.com/patchy631/ai-engineering-hub.git /tmp/ai-eng-hub
```

### Usage Workflow

1. **Identify the relevant project** from the catalog (see `references/project-catalog.md`).
2. **Browse the project structure** using the GitHub API to understand what files are available.
3. **Fetch the specific files** needed using raw URLs or sparse checkout.
4. **Adapt the code** to the user's requirements — adjust model names, API keys, file paths, and dependencies.
5. **Install dependencies** — most projects use Python with `requirements.txt` or `pip install`.

### Key Conventions in the Repository

- Most projects are Python-based, using frameworks like **LlamaIndex**, **LangChain**, **CrewAI**, **Streamlit**, **Chainlit**, and **FastAPI**.
- Projects often use **Ollama** for local model inference or cloud APIs (OpenAI, Groq, SambaNova).
- Vector databases commonly used: **Qdrant**, **Milvus**, **ChromaDB**.
- Each project folder typically contains a README, a main script or notebook, and a `requirements.txt`.

## Project Catalog

For the full categorized list of all 93+ projects with descriptions, folder names, and technologies used, consult:

→ `references/project-catalog.md`

This catalog is organized by domain (RAG, Agents, MCP, Voice, OCR, Fine-tuning, etc.) and includes the exact folder name needed for fetching.

## Quick Project Selection Guide

| User Need | Recommended Projects |
|---|---|
| Basic RAG implementation | `simple-rag-workflow`, `document-chat-rag`, `fastest-rag-stack` |
| Agentic RAG with fallback | `agentic_rag`, `firecrawl-agent`, `deploy-agentic-rag` |
| MCP server/client | `mcp-agentic-rag`, `llamaindex-mcp`, `mcp-voice-agent` |
| Voice/audio AI | `real-time-voicebot`, `rag-voice-agent`, `chat-with-audios` |
| OCR/vision | `llama-ocr`, `gemma3-ocr`, `qwen-2.5VL-ocr` |
| Local ChatGPT clone | `local-chatgpt`, `local-chatgpt with DeepSeek`, `deepseek-thinking-ui` |
| Fine-tuning models | `DeepSeek-finetuning`, `Build-reasoning-model` |
| Multi-agent systems | `hotel-booking-crew`, `book-writer-flow`, `paralegal-agent-crew` |
| Model comparison | `llama-4_vs_deepseek-r1`, `sonnet4-vs-o4`, `code-model-comparison` |
| Multimodal RAG | `deepseek-multimodal-RAG`, `Colivara-deepseek-website-RAG`, `video-rag-gemini` |
| Production systems | `notebook-lm-clone`, `groundX-doc-pipeline`, `stock-portfolio-analysis-agent` |
| AI learning roadmap | `ai-engineering-roadmap` |
