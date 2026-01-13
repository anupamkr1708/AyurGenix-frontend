import streamlit as st
from api import chat, get_conversation


# ---------------------------
# Helpers
# ---------------------------

def normalize_messages(raw):
    messages = []
    for m in raw:
        conf = m.get("confidence")

        try:
            conf = float(conf) if conf is not None else None
        except:
            conf = None

        messages.append({
            "role": m["role"],
            "content": m["content"],
            "confidence": conf
        })
    return messages


def load_conversation():
    cid = st.session_state.active_conversation
    if not cid:
        return

    r = get_conversation(cid)
    if r.status_code == 200:
        st.session_state.messages = normalize_messages(r.json())


def confidence_badge(conf):
    if conf is None:
        return "⚪", "gray"
    if conf >= 0.7:
        return "🟢", "green"
    elif conf >= 0.45:
        return "🟡", "orange"
    else:
        return "🔴", "red"


# ---------------------------
# Main Chat Screen
# ---------------------------

def chat_screen():

    st.markdown("## 💬 Ayurvedic Consultation")

    # Load history once when chat is clicked
    if st.session_state.get("load_history"):
        load_conversation()
        st.session_state.load_history = False

    # ----------- CHAT DISPLAY -----------

    chat_container = st.container()

    with chat_container:
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                st.markdown(
                    f"<div class='user-msg'>🧑 {msg['content']}</div>",
                    unsafe_allow_html=True
                )
            else:
                conf = msg.get("confidence")
                badge, color = confidence_badge(conf)
                conf_text = "N/A" if conf is None else f"{conf*100:.1f}%"

                st.markdown(
                    f"""
                    <div class='bot-msg'>
                    🌿 <b>AyurGenix</b>
                    <span style="color:{color}">
                    {badge} {conf_text} confidence
                    </span><br><br>
                    {msg['content']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.divider()

    # ----------- INPUT FORM (SAFE MODE) -----------

    with st.form("chat_form", clear_on_submit=True):

        query = st.text_input(
            "Ask Ayurveda...",
            placeholder="Type your question and press Enter"
        )

        send = st.form_submit_button("🚀 Ask")

        if send and query.strip():

            user_query = query.strip()

            st.session_state.messages.append({
                "role": "user",
                "content": user_query
            })

            with st.spinner("🧠 Thinking..."):
                res = chat(user_query, st.session_state.active_conversation)
                data = res.json()

            st.session_state.active_conversation = data["conversation_id"]

            conf = data.get("confidence")
            try:
                conf = float(conf) if conf is not None else None
            except:
                conf = None

            st.session_state.messages.append({
                "role": "assistant",
                "content": data["answer"],
                "confidence": conf
            })

            st.rerun()
