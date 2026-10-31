import os
from rag.config import MAX_DISTANCE

def has_api_key() -> bool:
    return bool(os.environ.get("GEMINI_API_KEY"))


def filter_relevant(chunks, sources, distances):
    """Keeps only chunks close enough to the question (distance <= MAX_DISTANCE)."""
    kept = [(c, s) for c, s, d in zip(chunks, sources, distances) if d <= MAX_DISTANCE]
    return [k[0] for k in kept], [k[1] for k in kept]


def extractive_answer(chunks, sources) -> str:
    """No-LLM fallback: show the best guide excerpts directly."""
    parts = [f"From {s['source']}:\n{c}" for c, s in zip(chunks[:2], sources[:2])]
    return "\n\n".join(parts)


def build_prompt(query, chunks, sources) -> str:
    context = "\n\n".join(
        f"[Source: {s['source']}]\n{c}" for c, s in zip(chunks, sources)
    )
    return f"""You are a laptop repair assistant. Answer the user's problem
using ONLY the context below. Explain the likely cause and the repair steps in
plain language, and mention safety warnings. If the context does not cover the
problem, say so instead of guessing.

Context:
{context}

User's problem: {query}
"""


def generate_answer(query, chunks, sources) -> str:
    if not has_api_key():
        return extractive_answer(chunks, sources)

    try:
        from google import genai

        client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
        response = client.models.generate_content(
            model=os.environ.get("GEMINI_MODEL", "gemini-2.5-flash"),
            contents=build_prompt(query, chunks, sources),
        )
        text = (response.text or "").strip()
        return text if text else extractive_answer(chunks, sources)
    except Exception as e:
        # Rate limit, bad model name, network problem, etc.
        print(f"[generate] Gemini call failed, using retrieval-only: {e}")
        return extractive_answer(chunks, sources)
