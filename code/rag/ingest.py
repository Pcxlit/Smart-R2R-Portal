
import os
import re
from dataclasses import dataclass

from pypdf import PdfReader

from rag.config import RAW_DATA_DIR, CHUNK_SIZE, CHUNK_OVERLAP

@dataclass
class Chunk:
    text: str
    source: str
    chunk_index: int


def _read_txt(path: str) -> str:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def _read_pdf(path: str) -> str:
    reader = PdfReader(path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return "\n".join(pages)


def _clean(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def _split_into_chunks(text: str, chunk_size: int, overlap: int) -> list[str]:
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    chunks = []
    start = 0
    text_len = len(text)
    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == text_len:
            break
        start = end - overlap
    return chunks


def load_and_chunk_documents(raw_dir: str = RAW_DATA_DIR) -> list[Chunk]:
    if not os.path.isdir(raw_dir):
        raise FileNotFoundError(
            f"Raw data directory not found: {raw_dir}. "
            "Add .txt or .pdf repair guides there first."
        )

    all_chunks: list[Chunk] = []

    for filename in sorted(os.listdir(raw_dir)):
        path = os.path.join(raw_dir, filename)
        if not os.path.isfile(path):
            continue

        if filename.lower().endswith(".txt"):
            raw_text = _read_txt(path)
        elif filename.lower().endswith(".pdf"):
            raw_text = _read_pdf(path)
        else:
            continue

        cleaned = _clean(raw_text)
        if not cleaned:
            continue

        pieces = _split_into_chunks(cleaned, CHUNK_SIZE, CHUNK_OVERLAP)
        for i, piece in enumerate(pieces):
            all_chunks.append(Chunk(text=piece, source=filename, chunk_index=i))

    return all_chunks


if __name__ == "__main__":
    chunks = load_and_chunk_documents()
    print(f"Loaded {len(chunks)} chunks from {RAW_DATA_DIR}")
    for c in chunks[:3]:
        print(f"\n--- {c.source} [chunk {c.chunk_index}] ---")
        print(c.text[:200], "...")
