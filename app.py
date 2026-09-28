import os
import streamlit as st
from hindsight_client import Hindsight
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
BANK_ID = "deals"

hindsight = Hindsight(
    base_url="https://api.hindsight.vectorize.io",
    api_key=HINDSIGHT_API_KEY
)

llm = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def ensure_bank():
    try:
        hindsight.create_bank(bank_id=BANK_ID, name="Deal Intelligence")
    except Exception:
        pass

def remember(content: str):
    hindsight.retain(bank_id=BANK_ID, content=content)

def recall(query: str) -> str:
    result = hindsight.recall(bank_id=BANK_ID, query=query)
    if not result.results:
        return "No relevant memories yet."
    return "\n".join([m.text for m in result.results])

def ask_llm(messages):
    response = llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content

st.set_page_config(page_title="Deal Intelligence Agent", page_icon="💼")
st.title("Deal Intelligence Agent")
st.caption("Powered by Hindsight Memory")

ensure_bank()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hi! I'm your Deal Intelligence Agent. Tell me about a deal, "
                "objections, competitors, or pricing discussions. I will remember everything."
            )
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Talk about a deal..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    memories = recall(prompt)

    system_prompt = f"""You are a senior sales deal intelligence agent.
You help sales reps by remembering every important detail about deals.

Here is what you already know about this deal / customer from your memory bank:
{memories}

Use this knowledge to inform your response. Be specific, actionable, and helpful.
"""

    messages_for_llm = [{"role": "system", "content": system_prompt}]
    for m in st.session_state.messages[-6:]:
        messages_for_llm.append({"role": m["role"], "content": m["content"]})

    with st.chat_message("assistant"):
        with st.spinner("Thinking with memory..."):
            reply = ask_llm(messages_for_llm)
            st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    remember(prompt)
