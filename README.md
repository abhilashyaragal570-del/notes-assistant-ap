# Notes Assistant API

A small FastAPI backend that answers questions from my own notes using RAG (retrieval-augmented generation) and the Gemini API.

**Live demo:** https://notes-assistant-ap.onrender.com

API docs: https://notes-assistant-ap.onrender.com/docs

The free server sleeps when idle, so the first request can take about a minute.

## How it works

1. `notes.txt` is split into paragraphs (chunks).
2. Each chunk is turned into an embedding vector at startup.
3. A question is embedded and compared with the chunks by cosine similarity.
4. The two best chunks are sent to Gemini, which answers using only those notes.

## Run it

1. Install the packages: `pip install fastapi uvicorn google-genai python-dotenv`
2. Create a `.env` file in this folder with: `GEMINI_API_KEY=your-key`
3. Start the server: `uvicorn main:app --reload`
4. Open `http://127.0.0.1:8000/docs` and try `GET /ask`.

## Example

`GET /ask?question=How do I activate a virtual environment?`

Returns JSON with the question and the answer.

## What I learned

- Building an API with FastAPI
- Turning a RAG script into a function that a web endpoint can call
- Keeping API keys out of Git with `.gitignore`
- Deploying a Python API to the internet with Render
- Building a simple HTML page that calls my API with fetch