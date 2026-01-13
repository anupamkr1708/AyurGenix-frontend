import streamlit as st
from state import init_state
from ui.auth_ui import auth_screen
from ui.sidebar_ui import sidebar
from ui.chat_ui import chat_screen
from api import health

st.set_page_config(page_title="🌿 AyurGenix", layout="wide")

init_state()

# ---------- AUTH ----------
if not st.session_state.token:
    auth_screen()
    st.stop()

# ---------- SIDEBAR ----------
with st.sidebar:
    try:
        if health().status_code == 200:
            st.success("Backend online")
        else:
            st.error("Backend issue")
    except:
        st.error("Backend offline")

    sidebar()

# ---------- MAIN ----------
st.markdown("## 🌿 AyurGenix — Ayurvedic Consultation")
chat_screen()

st.divider()
st.caption("⚕️ Educational use only • Not a medical diagnosis")
