
from pathlib import Path
import streamlit as st
import yaml
from App_Scripts.LLM import answer_llm

ROOT = Path(__file__).parent
LINKS = yaml.safe_load((ROOT / "data" / "links.yml").read_text(encoding="utf-8"))
OFFICIAL = LINKS.get("official_site", "https://www.towson.edu/")

st.set_page_config(page_title="Towson Tiger Chat (Demo)", page_icon="🐯", layout="centered")

with st.sidebar:
    st.markdown("#### About")
    st.caption(
        "This demo reads a local persona + a tiny FAQ (as optional context) and always uses an LLM "
        "to answer in a mascot voice. It is **not** an official Towson University service."
    )
    st.markdown(f"[Official Site]({OFFICIAL})")

st.title("Doc The Tiger Chat 🐯 (Demo)")
st.write("Ask about campus life or the AI club. For official dates or policies, I’ll point you to the TU site.")

if "history" not in st.session_state:
    st.session_state.history = []
if "turns" not in st.session_state:
    st.session_state.turns = 0

user_input = st.chat_input("Type your question…")

# Display history
for role, msg in st.session_state.history:
    with st.chat_message(role):
        st.write(msg)

if user_input:
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    reply = answer_llm(user_input, st.session_state.turns)

    st.session_state.turns += 1
    st.session_state.history.append(("assistant", reply))
    with st.chat_message("assistant"):
        st.write(reply)