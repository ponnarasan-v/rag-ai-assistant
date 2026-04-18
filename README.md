# 🧠 AI Document Assistant (RAG + Ollama)

## 🚀 Overview

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** system that enables users to ask questions based on PDF documents. It uses semantic search to retrieve relevant context and a local Large Language Model (LLM) via Ollama to generate accurate answers.

---

## 🧩 Architecture

1. **Document Ingestion**

   * Load PDF documents
   * Split into chunks
   * Generate embeddings
   * Store in FAISS vector database

2. **Query Processing**

   * User submits a question
   * Relevant chunks retrieved using similarity search

3. **Answer Generation**

   * Retrieved context passed to LLM (TinyLlama via Ollama)
   * LLM generates final answer

4. **Serving Layer**

   * FastAPI backend for inference
   * Streamlit UI for interaction

---

## 🛠️ Tech Stack

* **Backend**: FastAPI
* **Frontend**: Streamlit
* **LLM**: Ollama (TinyLlama)
* **Vector DB**: FAISS
* **Framework**: LangChain
* **Deployment**: Docker

---

## 📂 Project Structure

```
rag_project/
│
├── app.py                 # FastAPI backend
├── rag_pipeline.py        # RAG logic
├── ingest.py              # Data ingestion script
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
│
├── data/
│   └── diabetes.pdf       # Sample document
│
├── frontend/
│   └── streamlit_app.py   # UI
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/rag-ai-assistant.git
cd rag-ai-assistant
```

### 2️⃣ Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Run ingestion

```
python ingest.py
```

### 5️⃣ Start backend

```
uvicorn app:app --reload
```

### 6️⃣ Run UI

```
streamlit run frontend/streamlit_app.py
```

### 7️⃣ Start LLM (Ollama)

```
ollama run tinyllama
```

---

## 🐳 Docker Setup

### Build image

```
docker build -t rag-backend .
```

### Run container

```
docker run -p 8000:8000 rag-backend
```

⚠️ Note: Ollama must be running on the host machine.

---

## 🔌 API Usage

### Endpoint

```
POST /ask
```

### Example Request

```
{
  "question": "What is diabetes?"
}
```

### Example Response

```
{
  "answer": "Diabetes is a chronic disease that occurs when the pancreas does not produce enough insulin..."
}
```

---

## ✨ Features

* Document-based Question Answering
* Semantic search with embeddings
* Local LLM (no API cost)
* FastAPI REST API
* Interactive Streamlit UI
* Dockerized backend

---

## ⚠️ Limitations

* Requires local system resources (RAM for LLM)
* Ollama must run separately (not inside Docker)
* Single document ingestion (can be extended)

---

## 🚀 Future Improvements

* Multi-document support
* Chat history / conversational memory
* File upload UI
* Cloud deployment (AWS / GCP)
* Replace local LLM with scalable API

---

## 👨‍💻 Author

**Ponnarasan V**
M.Tech CSE (AI & ML)

---

## ⭐ Acknowledgements

* LangChain
* FAISS
* Ollama
* Streamlit
* FastAPI

---
