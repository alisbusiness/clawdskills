# AI Engineering Hub — Full Project Catalog

Repository: `https://github.com/patchy631/ai-engineering-hub`

Base raw URL: `https://raw.githubusercontent.com/patchy631/ai-engineering-hub/main/`

API URL: `https://api.github.com/repos/patchy631/ai-engineering-hub/contents/`

---

## Table of Contents

- [OCR & Vision](#ocr--vision)
- [Chat Interfaces & UI](#chat-interfaces--ui)
- [Basic RAG](#basic-rag)
- [Advanced RAG](#advanced-rag)
- [Multimodal RAG](#multimodal-rag)
- [AI Agents & Workflows](#ai-agents--workflows)
- [Advanced Agent Systems](#advanced-agent-systems)
- [Voice & Audio](#voice--audio)
- [MCP (Model Context Protocol)](#mcp-model-context-protocol)
- [Advanced MCP & Infrastructure](#advanced-mcp--infrastructure)
- [Model Comparison & Evaluation](#model-comparison--evaluation)
- [Fine-tuning & Model Development](#fine-tuning--model-development)
- [Production Systems](#production-systems)
- [Other Tools & Utilities](#other-tools--utilities)
- [Learning Resources](#learning-resources)

---

## OCR & Vision

| Folder | Description | Key Tech |
|---|---|---|
| `LaTeX-OCR-with-Llama` | Convert LaTeX equation images to code | Llama 3.2 vision |
| `llama-ocr` | 100% local OCR app | Llama 3.2, Streamlit |
| `gemma3-ocr` | Local OCR with structured text extraction | Gemma-3 |
| `qwen-2.5VL-ocr` | Text extraction | Qwen 2.5 VL |

**Difficulty:** 🟢 Beginner

---

## Chat Interfaces & UI

| Folder | Description | Key Tech |
|---|---|---|
| `local-chatgpt with DeepSeek` | Mini-ChatGPT with visible reasoning | DeepSeek-R1, Chainlit |
| `local-chatgpt` | ChatGPT clone | Llama 3.2 vision |
| `local-chatgpt with Gemma 3` | Local chat interface | Gemma 3 |
| `deepseek-thinking-ui` | ChatGPT with visible reasoning chain | DeepSeek-R1 |
| `qwen3-thinking-ui` | Thinking UI | Qwen3:4B, Streamlit |
| `gpt-oss-thinking-ui` | Reasoning visualization | GPT-OSS |
| `streaming-ai-chatbot` | Real-time AI streaming | Motia framework |

**Difficulty:** 🟢 Beginner

---

## Basic RAG

| Folder | Description | Key Tech |
|---|---|---|
| `simple-rag-workflow` | Basic RAG implementation | LlamaIndex, Ollama |
| `document-chat-rag` | Chat with documents | Llama 3.3 |
| `fastest-rag-stack` | Fast RAG stack | SambaNova, LlamaIndex, Qdrant |
| `github-rag` | Chat with GitHub repos locally | — |
| `modernbert-rag` | RAG with modern embeddings | ModernBERT |
| `llama-4-rag` | RAG with Llama 4 | Meta Llama 4 |

**Difficulty:** 🟢 Beginner

---

## Advanced RAG

| Folder | Description | Key Tech |
|---|---|---|
| `rag-with-dockling` | RAG over Excel files | IBM Docling |
| `trustworthy-rag` | RAG over complex docs with trustworthiness | TLM |
| `fastest-rag-milvus-groq` | Sub-15ms retrieval latency | Milvus, Groq |
| `chat-with-code` | Chat with codebases | Qwen3-Coder |
| `rag-sql-router` | Agent with RAG and SQL routing | — |

**Difficulty:** 🟡 Intermediate

---

## Multimodal RAG

| Folder | Description | Key Tech |
|---|---|---|
| `deepseek-multimodal-RAG` | MultiModal RAG | DeepSeek-Janus-Pro |
| `Colivara-deepseek-website-RAG` | MultiModal RAG for websites | ColiVara, DeepSeek |
| `multimodal-rag-assemblyai` | Audio + vector DB + agents | AssemblyAI, CrewAI |
| `video-rag-gemini` | Chat with videos | Gemini AI |
| `imagegen-janus-pro` | Local image generation | DeepSeek Janus-Pro 7B |

**Difficulty:** 🟢 Beginner (video-rag, imagegen) / 🟡 Intermediate (others)

---

## AI Agents & Workflows

| Folder | Description | Key Tech |
|---|---|---|
| `Youtube-trend-analysis` | Analyze YouTube trends | CrewAI, BrightData |
| `autogen-stock-analyst` | Advanced stock analyst | Microsoft AutoGen |
| `agentic_rag` | RAG with document search + web fallback | — |
| `agentic_rag_deepseek` | Enterprise agentic RAG | GroundX, DeepSeek |
| `book-writer-flow` | Automated book writing | CrewAI |
| `content_planner_flow` | Content workflow automation | CrewAI Flow |
| `brand-monitoring` | Automated brand monitoring | — |
| `hotel-booking-crew` | Multi-agent hotel booking | DeepSeek-R1 |
| `deploy-agentic-rag` | Private Agentic RAG API | LitServe |
| `zep-memory-assistant` | AI Agent with human-like memory | Zep |
| `agent-with-mcp-memory` | Agents with persistent memory | Graphiti, Opik |
| `acp-code` | Agent Communication Protocol demo | ACP |
| `motia-content-creation` | Social media automation | Motia |
| `streaming-ai-chatbot` | Real-time AI streaming | Motia |

**Difficulty:** 🟡 Intermediate

---

## Advanced Agent Systems

| Folder | Description | Key Tech |
|---|---|---|
| `nvidia-demo` | Documentation writer | CrewAI Flows, NVIDIA NIM |
| `documentation-writer-flow` | Agentic documentation workflow | CrewAI |
| `Multi-Agent-deep-researcher-mcp-windows-linux` | MCP-powered deep researcher | MCP, multi-agent |
| `multiplatform_deep_researcher` | Multi-platform research | BrightData |
| `web-browsing-agent` | Browser automation | CrewAI, Stagehand |
| `paralegal-agent-crew` | Intelligent paralegal | RAG, CrewAI |
| `firecrawl-agent` | Corrective RAG with web fallback | FireCrawl |
| `context-engineering-workflow` | Research assistant | TensorLake, Zep |
| `parlant-conversational-agent` | Compliance-driven conversational agent | Parlant |
| `stock-portfolio-analysis-agent` | Portfolio analysis | React frontend |
| `guidelines-vs-traditional-prompt` | Structured guidelines comparison | — |

**Difficulty:** 🔴 Advanced

---

## Voice & Audio

| Folder | Description | Key Tech |
|---|---|---|
| `real-time-voicebot` | Conversational travel guide | AssemblyAI |
| `rag-voice-agent` | Real-time RAG Voice Agent | Cartesia |
| `chat-with-audios` | RAG over audio files | — |
| `audio-analysis-toolkit` | Audio analysis toolkit | AssemblyAI |
| `multilingual-meeting-notes-generator` | Auto meeting notes with language detection | — |

**Difficulty:** 🟡 Intermediate

---

## MCP (Model Context Protocol)

| Folder | Description | Key Tech |
|---|---|---|
| `cursor_linkup_mcp` | Custom MCP with deep web search | Linkup |
| `eyelevel-mcp-rag` | MCP for RAG over complex docs | EyeLevel |
| `llamaindex-mcp` | Local MCP client | LlamaIndex |
| `mcp-agentic-rag` | MCP-powered Agentic RAG | Cursor |
| `mcp-agentic-rag-firecrawl` | Agentic RAG with web crawling | Firecrawl |
| `mcp-video-rag` | Video RAG via MCP | Ragie |
| `mcp-voice-agent` | Voice agent | Firecrawl, Supabase |
| `sdv-mcp` | Synthetic Data Vault orchestration | SDV |
| `kitops-mcp` | ML model management | KitOps |
| `stagehand x mcp-use` | Web automation | Stagehand MCP |

**Difficulty:** 🟡 Intermediate

---

## Advanced MCP & Infrastructure

| Folder | Description | Key Tech |
|---|---|---|
| `mindsdb-mcp` | Unified MCP for all data sources | MindsDB |
| `financial-analyst-deepseek` | MCP financial analysis | DeepSeek |
| `graphiti-mcp` | Persistent memory graph | Zep Graphiti |
| `pixeltable-mcp` | Unified multimodal data orchestration | Pixeltable |
| `ultimate-ai-assitant-using-mcp` | Multi-MCP server interface | — |

**Difficulty:** 🔴 Advanced

---

## Model Comparison & Evaluation

| Folder | Description | Key Tech |
|---|---|---|
| `eval-and-observability` | E2E RAG evaluation | CometML Opik |
| `llama-4_vs_deepseek-r1` | Model comparison via RAG | Llama 4, DeepSeek-R1 |
| `qwen3_vs_deepseek-r1` | Model comparison | Opik |
| `o3-vs-claude-code` | Claude 3.7 vs o3 comparison | — |
| `sonnet4-vs-o4` | Code generation comparison | Sonnet 4, o4 |
| `sonnet4-vs-qwen3-coder` | Coder model comparison | Sonnet 4, Qwen3-Coder |
| `code-model-comparison` | Frontier model code comparison | — |
| `gpt-oss-vs-qwen3` | Reasoning capabilities comparison | GPT-OSS, Qwen3 |

**Difficulty:** 🟡 Intermediate

---

## Fine-tuning & Model Development

| Folder | Description | Key Tech |
|---|---|---|
| `DeepSeek-finetuning` | Fine-tune DeepSeek | Unsloth, Ollama |
| `Build-reasoning-model` | Build DeepSeek-R1-like reasoning models | — |
| `attention-is-all-you-need-impl` | Transformer architecture from scratch | PyTorch |

**Difficulty:** 🔴 Advanced

---

## Production Systems

| Folder | Description | Key Tech |
|---|---|---|
| `groundX-doc-pipeline` | World-class document processing | GroundX |
| `notebook-lm-clone` | Full NotebookLM with RAG, citations, podcasts | — |

**Difficulty:** 🔴 Advanced

---

## Other Tools & Utilities

| Folder | Description | Key Tech |
|---|---|---|
| `Website-to-API-with-FireCrawl` | Convert websites to APIs | FireCrawl |
| `ai_news_generator` | News generation | CrewAI, Cohere |
| `siamese-network` | Digit similarity detection on MNIST | — |

**Difficulty:** 🟢 Beginner

---

## Learning Resources

| Folder | Description | Key Tech |
|---|---|---|
| `ai-engineering-roadmap` | Complete guide from Python to production AI | — |

**Difficulty:** All levels
