from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import get_answer

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask_question(query: Query):
    result = get_answer(query.question)
    return result