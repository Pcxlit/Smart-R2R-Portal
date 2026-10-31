"""
Web API for the RAG module. Run from the code/ folder:

    uvicorn rag.api:app --reload

Then open http://localhost:8000/docs to try it in the browser.
"""

import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from rag.embed_store import ensure_store
from rag.generate import filter_relevant, generate_answer, has_api_key
from rag.retrieve import retrieve


@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_store()  # builds the vector store on first start if it's missing
    yield


app = FastAPI(title="RepairFlow RAG", lifespan=lifespan)

# Lets the website frontend call this API from the browser.
# Restrict allow_origins to your real site address before going live.
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)


class QueryIn(BaseModel):
    query: str


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
            "mode": "none",
            "latency_seconds": round(time.perf_counter() - start, 3),
        }

    answer = generate_answer(body.query, chunks, sources)
    return {
        "found": True,
        "answer": answer,
        "sources": sorted({s["source"] for s in sources}),
        "mode": "llm" if has_api_key() else "retrieval_only",
        "latency_seconds": round(time.perf_counter() - start, 3),
    }