# api.py

import requests
import streamlit as st
from config import API_URL, TIMEOUT


def _headers():
    if st.session_state.get("token"):
        return {"Authorization": f"Bearer {st.session_state.token}"}
    return {}


# ------------------ AUTH ------------------

def signup(email, password):
    return requests.post(
        f"{API_URL}/auth/signup",
        json={"email": email, "password": password},
        timeout=TIMEOUT,
    )


def login(email, password):
    return requests.post(
        f"{API_URL}/auth/login",
        json={"email": email, "password": password},
        timeout=TIMEOUT,
    )


def get_me():
    return requests.get(
        f"{API_URL}/me",
        headers=_headers(),
        timeout=TIMEOUT,
    )


# ------------------ SYSTEM ------------------

def health():
    return requests.get(f"{API_URL}/health", timeout=10)


# ------------------ PLACEHOLDERS (next phases) ------------------

def chat(query, conversation_id=None):
    payload = {"query": query, "conversation_id": conversation_id}
    return requests.post(
        f"{API_URL}/chat/",
        json=payload,
        headers=_headers(),
        timeout=TIMEOUT,
    )


def list_conversations():
    return requests.get(
        f"{API_URL}/chat/conversations",
        headers=_headers(),
        timeout=TIMEOUT,
    )


def get_conversation(conversation_id):
    return requests.get(
        f"{API_URL}/chat/conversation/{conversation_id}",
        headers=_headers(),
        timeout=TIMEOUT,
    )


def get_usage():
    return requests.get(
        f"{API_URL}/usage/me",
        headers=_headers(),
        timeout=TIMEOUT,
    )
