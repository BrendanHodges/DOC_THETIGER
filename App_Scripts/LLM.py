from openai import OpenAI
from dotenv import load_dotenv
import os, json, random, re
from App_Scripts.FAQ import retrieve_answer
from pathlib import Path
import yaml
from App_Scripts.Styling import should_drop_ai_club_plug, stylize_reply, has_greeting
from App_Scripts.GetText import Grab_text

load_dotenv()
ROOT = Path(__file__).parent.parent
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
PERSONA = (ROOT / "data" / "persona.txt").read_text(encoding="utf-8")
LINKS = yaml.safe_load((ROOT / "data" / "links.yml").read_text(encoding="utf-8"))
OFFICIAL = LINKS.get("official_site", "https://www.towson.edu/")

def _build_system_prompt(persona_text: str) -> str:
    safety = (
        "Never claim to be officially affiliated with the university. "
        "If asked about policies, dates, deadlines, prices, or specifics you don't know, "
        "do not guess; politely defer to the official site and keep replies short."
    )
    length_rule = "Keep answers to 2–3 sentences max."
    style_rule = "Sound like Towson’s tiger mascot: neutral, supportive, funny, high-energy and school-proud; light emoji use (🐯 or 🎓 only)."
    return "\n\n".join([persona_text.strip(), safety, length_rule, style_rule])


def llm_reply(user_msg: str, persona_text: str, context_snippets, official_url: str) -> str:
    system = _build_system_prompt(persona_text)

    context_block = ""
    if context_snippets:
        joined = "\n\n".join(s for s in context_snippets if s)[:1200]
        context_block = f"Helpful campus context snippets (non-authoritative):\n{joined}\n\n"

    user_block = (
        f"{context_block}"
        f"User message:\n{user_msg}\n\n"
        f"If the user asks for official info or specifics you don't know, "
        f"say you’re not sure and direct them to {official_url}."
    )

    resp = client.chat.completions.create(
        model=OPENAI_MODEL,
        temperature=0.4,
        max_tokens=220,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user_block},
        ],
    )
    return resp.choices[0].message.content.strip()

def answer_llm(user_msg: str, turns: int) -> str:
    # Optional FAQ context
    item, score, _ = retrieve_answer(user_msg)
    context_snippets = []
    if item and score >= 60:
        a = (item.get("a", "") or "").strip()
        if a:
            context_snippets.append(a)

    reply = llm_reply(
        user_msg=user_msg,
        persona_text=PERSONA,
        context_snippets=context_snippets,
        official_url=OFFICIAL,
    )

    if should_drop_ai_club_plug(turns):
        reply += " " + Grab_text('AI_CLUB_PLUGS')

    # Greeting/sign-off control
    add_greet   = (turns == 0) and (not has_greeting(reply))  # greet first turn only if LLM didn’t
    add_signoff = (turns % 4 == 0)                           # every 4th reply
    reply = stylize_reply(reply, add_greet=add_greet, add_signoff=add_signoff)

    return reply