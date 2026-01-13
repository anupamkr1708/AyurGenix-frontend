import streamlit as st

def init_state():
    defaults = {
        "token": None,
        "user": None,
        "messages": [],
        "active_conversation": None,
        "load_history": False,
        "pending_query": ""
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def reset_chat():
    st.session_state.messages = []
    st.session_state.active_conversation = None
    st.session_state.load_history = False
