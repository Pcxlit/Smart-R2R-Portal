import sys
import time
from dataclasses import dataclass, field

from rag.config import TOP_K
from rag.embed_store import get_collection


@dataclass
class RetrievalResult:
    query: str
    chunks: list[str]
    sources: list[dict]
    latency_seconds: float
    timestamp: float = field(default_factory=time.time)


def retrieve(query: str, top_k: int = TOP_K) -> RetrievalResult:
    collection = get_collection()

    start = time.perf_counter()
    results = collection.query(query_texts=[query], n_results=top_k)
    latency = time.perf_counter() - start

    documents = results.get("documents", [[]])[0]
    metadatas = results.get("metadatas", [[]])[0]

    return RetrievalResult(
        query=query,
        chunks=documents,
        sources=metadatas,
        latency_seconds=latency,
    )


def log_retrieval(result: RetrievalResult) -> None:
    print(f"[retrieve] query={result.query!r} "
          f"latency={result.latency_seconds:.3f}s "
          f"n_results={len(result.chunks)} "
          f"sources={[s.get('source') for s in result.sources]}")


if __name__ == "__main__":
    user_query = " ".join(sys.argv[1:]) or "laptop screen not turning on"
    res = retrieve(user_query)
    log_retrieval(res)
    for chunk, meta in zip(res.chunks, res.sources):
        print(f"\n--- from {meta.get('source')} (chunk {meta.get('chunk_index')}) ---")
        print(chunk[:300])