"""Run from code/:  python -m rag.calibrate   (after building the store)"""

from rag.embed_store import build_store, get_collection

IN_SCOPE = [
    "laptop hinge is loose", "screen wobbles when opening lid",
    "battery is swollen", "laptop only works when plugged in",
    "keyboard keys not working", "how to replace laptop keyboard",
    "laptop screen cracked", "screen flickering",
    "laptop fan making loud noise", "laptop overheating",
    "laptop not charging", "charging port loose",
    "replace laptop SSD", "upgrade laptop RAM",
    "laptop wont turn on", "trackpad not clicking",
    "wifi card replacement", "laptop speakers crackling",
    "liquid spilled on laptop", "laptop black screen",
]
OUT_OF_SCOPE = [
    "how do I bake a cake", "who won the cricket match",
    "best places to visit in Goa", "how to learn guitar",
    "what is the capital of France", "tips for losing weight",
]


def top1_distances(collection, queries):
    out = []
    for q in queries:
        res = collection.query(query_texts=[q], n_results=1, include=["distances"])
        out.append(res["distances"][0][0])
    return out


def percentile(values, p):
    s = sorted(values)
    return s[min(len(s) - 1, int(p * len(s)))]


if __name__ == "__main__":
    build_store()
    col = get_collection()
    inside = top1_distances(col, IN_SCOPE)
    outside = top1_distances(col, OUT_OF_SCOPE)

    for q, d in zip(IN_SCOPE, inside):
        print(f"IN   {d:.3f}  {q}")
    for q, d in zip(OUT_OF_SCOPE, outside):
        print(f"OUT  {d:.3f}  {q}")

    in_high = percentile(inside, 0.9)
    out_low = min(outside)
    print(f"\n90th percentile of in-scope distances: {in_high:.3f}")
    print(f"Lowest out-of-scope distance:          {out_low:.3f}")

    if in_high < out_low:
        print(f"Recommended MAX_DISTANCE = {(in_high + out_low) / 2:.2f}")
    else:
        print("Groups overlap, so no clean cutoff exists.")
        print(f"Start with MAX_DISTANCE = {in_high + 0.02:.2f} and add more guides "
              "or better queries; consider hybrid search.")