import streamlit as st
from utils import get_cards

def init_session_state():
    """Initialise les variables de session si nécessaire."""
    if "cards" not in st.session_state:
        st.session_state.cards = get_cards()
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "round" not in st.session_state:
        st.session_state.round = 1
    if "hint" not in st.session_state:
        st.session_state.hint = ""
    if "hint_given" not in st.session_state:
        st.session_state.hint_given = False
    if "attempts" not in st.session_state:
        st.session_state.attempts = 0
    if "timer_start" not in st.session_state:
        st.session_state.timer_start = None
    if "player_name" not in st.session_state:
        st.session_state.player_name = None
    if "player_ready" not in st.session_state:
        st.session_state.player_ready = False
