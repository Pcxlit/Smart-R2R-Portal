"""
Turns retrieved chunks into an answer.
- With ANTHROPIC_API_KEY set: Claude writes a grounded answer.
- Without a key: returns the best guide excerpts (retrieval-only mode).
"""

import os

from rag.config import MAX_DISTANCE

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")


def has_api_key() -> bool:
    return bool(os.environ.get("ANTHROPIC_API_KEY"))


def filter_relevant(chunks, sources, distances):
    """Keeps only chunks close enough to the question (distance <= MAX_DISTANCE)."""
    kept = [(c, s) for c, s, d in zip(chunks, sources, distances) if d <= MAX_DISTANCE]
    return [k[0] for k in kept], [k[1] for k in kept]


def extractive_answer(chunks, sources) -> str:
    """No-LLM fallback: show the best guide excerpts directly."""
    parts = [f"From {s['source']}:\n{c}" for c, s in zip(chunks[:2], sources[:2])]
    return "\n\n".join(parts)


def generate_answer(query, chunks, sources) -> str:
    if not has_api_key():
        return extractive_answer(chunks, sources)

    import anthropic

    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    context = "\n\n".join(
        f"[Source: {s['source']}]\n{c}" for c, s in zip(chunks, sources)
    )
    prompt = f"""You are a laptop repair assistant. Answer the user's problem
using ONLY the context below. Explain the likely cause and the repair steps in
plain language, and mention safety warnings. If the context does not cover the
problem, say so instead of guessing.

Context:
{context}

User's problem: {query}
"""
    response = client.messages.create(
        model=MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text