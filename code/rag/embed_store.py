
import chromadb
from chromadb.utils import embedding_functions

from rag.config import VECTOR_STORE_DIR, COLLECTION_NAME, EMBEDDING_MODEL_NAME
from rag.ingest import load_and_chunk_documents


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


def build_store(raw_dir: str = None) -> int:
    kwargs = {"raw_dir": raw_dir} if raw_dir else {}
    chunks = load_and_chunk_documents(**kwargs)

    if not chunks:
        print("No chunks found ,add .txt/.pdf files to data/raw/ first.")
        return 0

    collection = get_collection()

    ids = [f"{c.source}::{c.chunk_index}" for c in chunks]
    documents = [c.text for c in chunks]
    metadatas = [{"source": c.source, "chunk_index": c.chunk_index} for c in chunks]

    collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
    return len(chunks)


if __name__ == "__main__":
    count = build_store()
    print(f"Stored {count} chunks in Chroma at {VECTOR_STORE_DIR}")