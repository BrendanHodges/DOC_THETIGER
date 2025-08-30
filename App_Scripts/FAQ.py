import os, json, random, re
from pathlib import Path
from rapidfuzz import process, fuzz

ROOT = Path(__file__).parent.parent
print(ROOT)
FAQ = json.loads((ROOT / "data" / "faq.json").read_text(encoding="utf-8"))

def retrieve_answer(user_msg: str):
    try:
        if not FAQ:
            return None, 0.0, None
        choices = [item.get("q", "") for item in FAQ if isinstance(item, dict) and item.get("q")]
        if not choices:
            return None, 0.0, None
        result = process.extractOne(user_msg, choices, scorer=fuzz.WRatio)
        if not result:
            return None, 0.0, None
        _, score, idx = result
        if idx is None:
            return None, 0.0, None
        return FAQ[idx], float(score or 0.0), idx
    except Exception:
        return None, 0.0, None