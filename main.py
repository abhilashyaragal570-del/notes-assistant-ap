from fastapi import FastAPI
from rag_core import answer


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello from my first API"}


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}

@app.get("/ask")
def ask(question: str):
    return {"question": question, "answer": answer(question)}