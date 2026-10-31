"""
A query is a HIT if any of the top-k chunks contains at least one expected keyword.
"""

import statistics

from rag.config import MAX_DISTANCE
from rag.embed_store import ensure_store
from rag.retrieve import retrieve

# (query, keywords that a correct chunk should contain). Grow this to 30+.
TEST_CASES = [
    ("my laptop hinge is loose", ["hinge"]),
    ("screen wobbles when I open the lid", ["hinge", "display"]),
    ("battery is swollen", ["battery"]),
    ("laptop only works when plugged in", ["battery"]),
    ("keyboard keys not working", ["keyboard"]),
    ("how to replace laptop keyboard", ["keyboard"]),
    ("laptop fan making loud noise", ["fan"]),
    ("laptop overheating", ["fan", "thermal", "heat"]),
    ("charging port is loose", ["charging", "dc jack", "port"]),
    ("upgrade laptop RAM", ["ram", "memory"]),
    ("replace laptop SSD", ["ssd", "drive"]),
    ("cracked laptop screen", ["screen", "display"]),
    ("trackpad not clicking", ["trackpad", "touchpad"]),
    ("wifi card replacement", ["wifi", "wi-fi", "wireless"]),
]

# These should be rejected: best distance must be above MAX_DISTANCE.
OUT_OF_DOMAIN = [
    "how do I bake a cake",
    "who won the cricket match",
    "best places to visit in Goa",
    "how to learn guitar",
]


def main(top_k: int = 4):
    ensure_store()
    retrieve("warm up")  # first call loads the model; don't count it in latency

    hits, ranks, latencies = 0, [], []
    for query, keywords in TEST_CASES:
        res = retrieve(query, top_k=top_k)
        latencies.append(res.latency_seconds)

        rank = None
        for i, chunk in enumerate(res.chunks):
            if any(k in chunk.lower() for k in keywords):
                rank = i + 1
                break

        if rank:
            hits += 1
            ranks.append(1 / rank)
        else:
            ranks.append(0)
        best = res.distances[0] if res.distances else float("nan")
        print(f"{'HIT ' if rank else 'MISS'} rank={rank} dist={best:.3f} | {query}")

    print("\n--- Out-of-domain (should be rejected) ---")
    rejected = 0
    for query in OUT_OF_DOMAIN:
        res = retrieve(query, top_k=1)
        d = res.distances[0]
        ok = d > MAX_DISTANCE
        rejected += ok
        print(f"{'REJECTED' if ok else 'WRONGLY ACCEPTED'} dist={d:.3f} | {query}")

    n = len(TEST_CASES)
    print(f"\nHit rate@{top_k}:           {hits}/{n} = {hits / n:.0%}")
    print(f"MRR:                     {statistics.mean(ranks):.2f}")
    print(f"Off-topic rejected:      {rejected}/{len(OUT_OF_DOMAIN)}")
    print(f"Median retrieval time:   {statistics.median(latencies):.3f}s")


if __name__ == "__main__":
    main()