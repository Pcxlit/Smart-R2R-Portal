import os

RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

VECTOR_STORE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "chroma_store")

COLLECTION_NAME = "laptop_repair_docs"

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 120

TOP_K = 4