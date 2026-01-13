import streamlit as st
from api import list_conversations, get_usage
from state import reset_chat


def sidebar():

    st.markdown("## 🌿 AyurGenix")
    st.caption("Ayurvedic AI Consultant")

    st.divider()

    # ---------- ACCOUNT ----------
    st.markdown("### 👤 Account")
    st.caption(st.session_state.user["email"])

    try:
        usage = get_usage().json()
        st.metric("Daily queries", usage["daily_queries"])
        st.metric("Daily tokens", usage["daily_tokens"])
    except:
        st.info("Usage unavailable")

    if st.button("➕ New chat", use_container_width=True):
        reset_chat()
        st.rerun()

    st.divider()

    # ---------- CONVERSATIONS ----------
    st.markdown("### 💬 Chats")

    try:
        convos = list_conversations().json()

        if not convos:
            st.caption("No chats yet")

        for c in convos:
            if st.button("🗨 " + c["title"][:32], key=c["id"], use_container_width=True):
                st.session_state.active_conversation = c["id"]
                st.session_state.messages = []
                st.session_state.load_history = True
                st.rerun()

    except Exception as e:
        st.caption("No chats yet")

    st.divider()

    if st.button("🚪 Logout", use_container_width=True):
        st.session_state.clear()
        st.rerun()
