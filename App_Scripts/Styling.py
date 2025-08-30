import os, json, random, re
from App_Scripts.GetText import Grab_text

def should_drop_ai_club_plug(turn_count: int) -> bool:
    # Subtle: ~every 5th assistant reply
    return turn_count > 0 and (turn_count % 3 == 0)

# Greeting detector (avoid double "Hey there, Tiger!")
GREET_REGEX = re.compile(
    r'^\s*(hey there,\s*tiger!?|high paw!?|hello,\s*future\s*towson\s*legend!?)(\s*[🐯🎓])?\s*',
    flags=re.IGNORECASE
)
def has_greeting(text: str) -> bool:
    return bool(GREET_REGEX.match(text or ""))

def stylize_reply(core: str, add_greet: bool = False, add_signoff: bool = False) -> str:
    core = (core or "").strip()
    greet = Grab_text('GREETS') if add_greet else ""
    sign  = Grab_text('SIGNOFFS') if add_signoff else ""
    parts = [p for p in [greet, core, sign] if p]
    out = " ".join(parts)
    # keep it short (max 3 sentences)
    sentences = [s.strip() for s in out.split(".") if s.strip()]
    if len(sentences) > 3:
        sentences = sentences[:3]
    return (". ".join(sentences) + ".").replace("..", ".")