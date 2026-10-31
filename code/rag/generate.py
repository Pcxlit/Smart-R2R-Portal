"""Turns retrieved chunks into a grounded answer using the Claude API."""

import os

import anthropic

# Chunks farther than this are treated as irrelevant.
MAX_DISTANCE = 0.6

MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-sonnet-5-5")


def filter_relevant(chunks, sources, distances):
    kept = [
        (c, s) for c, s, d in zip(chunks, sources, distances) if d <= MAX_DISTANCE
    ]
    return [k[0] for k in kept], [k[1] for k in kept]


def generate_answer(query: str, chunks: list[str], sources: list[dict]) -> str:
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

    context = "\n\n".join(
        f"[Source: {s['source']}]\n{c}" for c, s in zip(chunks, sources)
    )
    prompt = f"""You are a laptop repair assistant. Answer the user's problem
using ONLY the context below. Explain what is likely wrong and the repair steps
in plain language. Mention any safety warnings. If the context does not cover
the problem, say so honestly instead of guessing.

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