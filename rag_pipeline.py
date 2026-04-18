from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama

DB_PATH = "vectorstore/"

def load_db():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)

def get_answer(query):
    db = load_db()

    retriever = db.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)

    # Limit context (avoid crashes)
    context = "\n".join([doc.page_content[:200] for doc in docs])

    prompt = f"""
You are a helpful medical assistant.

Give a clear and short answer.
Use ONLY the context below.
If answer is not found, say "Not in document".

Context:
{context}

Question:
{query}

Answer:
"""

    llm = Ollama(
        model="tinyllama",
        base_url="http://host.docker.internal:11434"
    )

    try:
        response = llm.invoke(prompt)
    except Exception as e:
        return {
            "answer": f"LLM Error: {str(e)}",
            "sources": []
        }

    return {
        "answer": response,
        "sources": []
    }
