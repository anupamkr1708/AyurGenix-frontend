# auth_ui.py

import streamlit as st
from api import login, signup, get_me


def auth_screen():
    st.markdown("## 🔐 AyurGenix Login")
    st.markdown("## 🌿 AyurGenix")
    st.markdown("### Ayurvedic AI Consultant")
    st.caption("Daily lifestyle planner • Classical knowledge • AI powered")
    st.divider()


    tab1, tab2 = st.tabs(["Login", "Signup"])

    # ---------------- LOGIN ----------------
    with tab1:
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login", use_container_width=True):
            with st.spinner("Authenticating..."):
                res = login(email, password)
                if res.status_code != 200:
                    st.error(res.text)
                else:
                    token = res.json()["access_token"]
                    st.session_state.token = token

                    me = get_me()
                    if me.status_code == 200:
                        st.session_state.user = me.json()
                        st.success("Login successful")
                        st.rerun()
                    else:
                        st.error("Login failed")


    # ---------------- SIGNUP ----------------
    with tab2:
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", type="password", key="signup_pass")

        if st.button("Create account", use_container_width=True):
            with st.spinner("Creating account..."):
                res = signup(email, password)
                if res.status_code != 200:
                    st.error(res.text)
                else:
                    st.success("Account created. You can login now.")
