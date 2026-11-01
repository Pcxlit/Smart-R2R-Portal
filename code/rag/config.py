import os

from dotenv import load_dotenv

# Reads code/.env if it exists (holds ANTHROPIC_API_KEY). Safe if missing.
load_dotenv()

RAW_DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")
VECTOR_STORE_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "chroma_store")

COLLECTION_NAME = "laptop_repair_docs"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 120
TOP_K = 4

# Chunks with cosine distance above this are treated as irrelevant.
# Tune it by running `python -m rag.calibrate` once you have real guides.
MAX_DISTANCE = 0.68
