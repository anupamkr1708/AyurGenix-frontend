import streamlit as st

def load_styles():

    dark = st.session_state.get("theme") == "dark"

    if dark:
        bg = "#020617"
        side = "#020617"
        chat = "#020617"
        text = "#e5e7eb"
        sub = "#94a3b8"
        accent = "#22c55e"
    else:
        bg = "#f8fafc"
        side = "#ecfeff"
        chat = "#ffffff"
        text = "#020617"
        sub = "#475569"
        accent = "#15803d"

    st.markdown(f"""
    <style>

    html, body, .stApp {{
        background-color: {bg};
        color: {text};
    }}

    section[data-testid="stSidebar"] {{
        background-color: {side};
    }}

    .app-title {{
        font-size: 2.3rem;
        font-weight: 800;
        color: {accent};
        margin-bottom: 1rem;
    }}

    .chat-box {{
        background-color: {chat};
        border-radius: 18px;
        padding: 1.5rem;
    }}

    .active-chat button {{
        background-color: {accent} !important;
        color: white !important;
        font-weight: 700;
    }}

    small {{
        color: {sub};
    }}

    </style>
    """, unsafe_allow_html=True)
