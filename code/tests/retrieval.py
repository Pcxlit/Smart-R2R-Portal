
import pytest

from rag.ingest import load_and_chunk_documents, _split_into_chunks
from rag.embed_store import build_store
from rag.retrieve import retrieve


def test_chunking_respects_size_and_overlap():
    text = "x" * 2000
    chunks = _split_into_chunks(text, chunk_size=800, overlap=120)
    assert all(len(c) <= 800 for c in chunks)
    assert len(chunks) >= 3


def test_load_and_chunk_sample_docs():
    chunks = load_and_chunk_documents()
    assert len(chunks) > 0
    sources = {c.source for c in chunks}
    assert "hinge_repair_guide.txt" in sources
    assert "battery_replacement_guide.txt" in sources


@pytest.fixture(scope="module")
def built_store():
    count = build_store()
    assert count > 0
    return count


def test_retrieval_returns_relevant_source(built_store):
    result = retrieve("laptop hinge is loose and cracking", top_k=2)
    assert len(result.chunks) > 0
    sources = [s["source"] for s in result.sources]
    assert "hinge_repair_guide.txt" in sources


def test_retrieval_battery_query_is_relevant(built_store):
    result = retrieve("battery is swollen and pushing up the trackpad", top_k=2)
    sources = [s["source"] for s in result.sources]
    assert "battery_replacement_guide.txt" in sources


def test_retrieval_latency_is_logged(built_store):
    result = retrieve("laptop screen wont turn on", top_k=2)
    assert result.latency_seconds >= 0
    assert result.timestamp > 0