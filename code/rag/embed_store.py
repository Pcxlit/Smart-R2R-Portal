"""
Build manually:  python -m rag.embed_store
"""

import os
from functools import lru_cache

import chromadb
from chromadb.utils import embedding_functions

from rag.config import COLLECTION_NAME, EMBEDDING_MODEL_NAME, VECTOR_STORE_DIR
from rag.ingestion import load_and_chunk_documents


def get_embedding_function():
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL_NAME
    )


def get_collection(client: chromadb.ClientAPI = None):
    if client is None:
        client = chromadb.PersistentClient(path=VECTOR_STORE_DIR)

    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=get_embedding_function(),
        metadata={"hnsw:space": "cosine"},
    )


@lru_cache(maxsize=1)
def get_collection_cached():
    """Opens the collection once and reuses it, so the embedding model
    isn't reloaded on every query."""
    return get_collection()


def build_store(raw_dir: str = None) -> int:
    """Chunks all raw documents and upserts them into the vector store.
    Re-running updates existing chunks instead of duplicating them."""
    kwargs = {"raw_dir": raw_dir} if raw_dir else {}
    chunks = load_and_chunk_documents(**kwargs)

    if not chunks:
        print("No chunks found -- add .txt/.pdf files to data/raw/ first.")
        return 0

    collection = get_collection()

    ids = [f"{c.source}::{c.chunk_index}" for c in chunks]
    documents = [c.text for c in chunks]
    metadatas = [{"source": c.source, "chunk_index": c.chunk_index} for c in chunks]

    batch = 500  # Chroma limits how many items one call accepts
    for i in range(0, len(ids), batch):
        collection.upsert(
            ids=ids[i:i + batch],
            documents=documents[i:i + batch],
            metadatas=metadatas[i:i + batch],
        )
    return len(chunks)


def ensure_store() -> None:
    """Builds the vector store only if it doesn't exist yet."""
    if os.path.isdir(VECTOR_STORE_DIR) and os.listdir(VECTOR_STORE_DIR):
        return
    build_store()


if __name__ == "__main__":
    count = build_store()
    print(f"Stored {count} chunks in Chroma at {VECTOR_STORE_DIR}")