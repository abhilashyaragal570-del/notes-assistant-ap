from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from rag_core import answer

app = FastAPI()


@app.get("/")
def home():
    return FileResponse(Path(__file__).parent / "index.html")


@app.get("/add")
def add(a: int, b: int):
    return {"result": a + b}


@app.get("/ask")
def ask(question: str):
    return {"question": question, "answer": answer(question)}