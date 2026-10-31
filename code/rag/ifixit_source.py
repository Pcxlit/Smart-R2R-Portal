import html
import os
import re
import time
from urllib.parse import quote

import requests

API = "https://www.ifixit.com/api/2.0"
HEADERS = {"User-Agent": "RepairFlow-student-project"}
OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "data", "raw")

FAULTS = [
    "hinge repair", "battery replacement", "screen replacement", "keyboard replacement",
    "fan replacement", "charging port", "SSD replacement", "RAM upgrade",
    "trackpad replacement", "motherboard", "speaker replacement", "wifi card",
    "thermal paste", "liquid damage", "disassembly",
]
BRANDS = ["", "Dell", "HP", "Lenovo", "Asus", "Acer", "MacBook", "Microsoft Surface"]
MAX_GUIDES = 600  # keeps the corpus a few MB


def get_json(url, params=None, retries=3):
    for attempt in range(retries):
        try:
            r = requests.get(url, params=params, headers=HEADERS, timeout=15)
            r.raise_for_status()
            return r.json()
        except requests.RequestException:
            time.sleep(2 * (attempt + 1))
    return None


def clean(text: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", text or "")).strip()


def is_laptop(title: str, category: str) -> bool:
    blob = f"{title} {category}".lower()
    return any(w in blob for w in ("laptop", "macbook", "notebook", "thinkpad", "surface"))


def guide_to_text(g: dict) -> str:
    title = clean(g.get("title", "Untitled"))
    lines = [
        title,
        f"Source URL: {g.get('url', '')}",
        f"Device category: {clean(g.get('category', ''))}",
        f"Difficulty: {g.get('difficulty', 'unknown')}",
    ]
    tools = [clean(t.get("text", "")) for t in g.get("tools", []) if isinstance(t, dict)]
    if tools:
        lines.append("Tools needed: " + ", ".join(t for t in tools if t))
    lines.append("")
    for i, step in enumerate(g.get("steps", []), start=1):
        text = " ".join(
            clean(l.get("text_raw") or l.get("text_rendered") or "")
            for l in step.get("lines", [])
        ).strip()
        if text:
            lines.append(f"Step {i}: {text}")
    return "\n\n".join(lines)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    seen, saved = set(), 0

    for brand in BRANDS:
        for fault in FAULTS:
            if saved >= MAX_GUIDES:
                print(f"Reached {MAX_GUIDES} guides, stopping.")
                return
            query = f"{brand} laptop {fault}".strip()
            data = get_json(f"{API}/search/{quote(query)}", {"filter": "guide", "limit": 10})
            for hit in (data or {}).get("results", []):
                gid = hit.get("guideid")
                if gid is None or gid in seen:
                    continue
                seen.add(gid)
                path = os.path.join(OUT_DIR, f"ifixit_{gid}.txt")
                if os.path.exists(path):
                    continue
                guide = get_json(f"{API}/guides/{gid}")
                if not guide or not is_laptop(guide.get("title", ""), str(guide.get("category", ""))):
                    continue
                text = guide_to_text(guide)
                if len(text) < 300:  # skip empty/stub guides
                    continue
                with open(path, "w", encoding="utf-8") as f:
                    f.write(text)
                saved += 1
                time.sleep(0.4)
            print(f"{query!r}: {saved} saved so far")

    print(f"Done. {saved} new guides in {OUT_DIR}")


if __name__ == "__main__":
    main()