"""
Run from the code/ folder:  uvicorn rag.api:app --reload
Docs for teammates appear automatically at http://localhost:8000/docs
"""

import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag.embed_store import ensure_store
from rag.generate import filter_relevant, generate_answer
from rag.retrieve import retrieve

app = FastAPI(title="RepairFlow RAG")

# Lets the website frontend call this API from the browser.
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class QueryIn(BaseModel):
    query: str


@app.on_event("startup")
def startup():
    ensure_store()  # builds the vector store if it doesn't exist yet


@app.post("/repair-query")
def repair_query(body: QueryIn):
    start = time.perf_counter()
    result = retrieve(body.query)
    chunks, sources = filter_relevant(result.chunks, result.sources, result.distances)

    if not chunks:
        return {
            "found": False,
            "answer": "I couldn't find a repair guide for that problem yet. "
                      "Try describing the symptom differently, or contact a verified shop.",
            "sources": [],
            "latency_seconds": round(time.perf_counter() - start, 3),
        }

    answer = generate_answer(body.query, chunks, sources)
    unique_sources = sorted({s["source"] for s in sources})
    return {
        "found": True,
        "answer": answer,
        "sources": unique_sources,
        "latency_seconds": round(time.perf_counter() - start, 3),
    }