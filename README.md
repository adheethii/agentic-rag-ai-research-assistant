# 🤖 Agentic RAG AI Research Assistant

![LangChain](https://img.shields.io/badge/LangChain-000000?style=flat&logo=chainlink&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-grey?style=flat)
![FAISS](https://img.shields.io/badge/FAISS-blue?style=flat)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)
![Local](https://img.shields.io/badge/Runs-100%25%20Local-purple?style=flat)

> **A fully local AI research assistant that reads your documents, answers questions, summarizes content, and searches the web — all without sending your data to any external API.**

---

## 🎯 Why I Built This

Most RAG demos rely on paid APIs like OpenAI — making them expensive and privacy-unfriendly. I wanted to build a **production-grade RAG system that runs entirely on your own machine** using open-source LLMs via Ollama, with no API costs and no data leaving your device.

This project combines agentic tool use, hybrid retrieval, and a clean Streamlit UI into one complete system.

---

## ⚡ What Makes This Different

| Feature | Basic RAG Demo | This Project |
|---------|---------------|--------------|
| LLM | OpenAI API (paid) | Ollama (100% local, free) |
| Retrieval | Simple vector search | Hybrid search + reranking |
| Tools | Q&A only | Q&A + Summarization + Web Search |
| Privacy | Data sent to cloud | Everything stays on your machine |
| Architecture | Single chain | Agentic — LLM decides which tool to use |

---

## ✨ Features

- 📄 **Document Q&A** — Upload PDFs and ask questions grounded in your documents
- 📑 **Document Summarization** — Auto-summarize uploaded documents using LLM
- 🌐 **Web Search Mode** — Search the web and get AI-synthesized answers
- 🧠 **Hybrid Retrieval** — Combines vector search with reranking for accurate context
- 🗂️ **Conversation History** — Tracks your queries within the session
- 🖥️ **Fully Local** — Runs on your machine using Ollama (no OpenAI API needed)

---

## 📸 Screenshots & Architecture

<table>
  <tr>
    <td align="center">
      <img src="images/home%20page..png" width="320"/><br>
      <b>🏠 Home Page</b>
    </td>
    <td align="center">
      <img src="images/document%20summarising.png" width="320"/><br>
      <b>📄 Document Summarization</b>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="images/web%20search.png" width="320"/><br>
      <b>🌐 Web Search</b>
    </td>
    <td align="center">
      <img src="images/architecture.svg" width="320"/><br>
      <b>🏗️ System Architecture</b>
    </td>
  </tr>
</table>

---

## 🏗️ System Architecture

```
User Query
    ↓
Streamlit UI (app.py)
    ↓
Agentic RAG Pipeline (rag_agent.py)
    ↓
LangChain Agent — decides which tool to use
    ├── 📄 Document Tool → Hybrid Retriever → FAISS + Reranker → LLM
    ├── 📑 Summarizer Tool → PDF Loader → Summarizer → LLM  
    └── 🌐 Web Search Tool → Search API → LLM
    ↓
Final Answer
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Ollama (`llama3.2:1b`) — runs locally |
| Framework | LangChain |
| Vector Store | FAISS |
| Embeddings | LangChain Ollama Embeddings |
| Retrieval | Hybrid search + reranking |
| Frontend | Streamlit |
| PDF Parsing | PyPDFLoader |
| Text Splitting | RecursiveCharacterTextSplitter |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/adheethii/agentic-rag-ai-research-assistant.git
cd agentic-rag-ai-research-assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and Run Ollama

Download Ollama from [https://ollama.com](https://ollama.com) and pull the model:

```bash
ollama pull llama3.2:1b
```

### 5. Build the Vector Store

Place your PDF files in `data/documents/`, then run:

```bash
python create_vector_db.py
```

### 6. Launch the App

```bash
streamlit run ui/app.py
```

---

## 🗂️ Project Structure

```
agentic_rag_ai_research_assistant/
│
├── data/
│   ├── documents/          # Uploaded PDF documents
│   ├── vector_store/       # FAISS vector store index
│   └── database/           # SQL database files
│
├── embeddings/
│   └── embedding_model.py  # Embedding model setup
│
├── rag_pipeline/
│   └── rag_agent.py        # Core agentic RAG pipeline
│
├── retriever/
│   ├── hybrid_retriever.py # Hybrid retrieval logic
│   ├── reranker.py         # Result reranking
│   └── vector_store.py     # Vector store load/save
│
├── tools/
│   ├── calculator.py       # Calculator tool
│   ├── sql_tool.py         # SQL query tool
│   └── web_search.py       # Web search tool
│
├── ui/
│   └── app.py              # Streamlit frontend
│
├── utils/
│   ├── pdf_loader.py       # PDF loading and chunking
│   └── summarizer.py       # Summarization helper
│
├── create_vector_db.py     # Script to build vector store
└── requirements.txt        # Python dependencies
```

---

## 📋 Requirements

- Python 3.10+
- [Ollama](https://ollama.com) installed and running locally
- Windows / macOS / Linux

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com)
- [Ollama](https://ollama.com)
- [Streamlit](https://streamlit.io)
- [FAISS](https://github.com/facebookresearch/faiss)
