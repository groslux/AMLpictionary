import streamlit as st
from utils import get_cards

def init_session_state():
    if 'cards' not in st.session_state:
        st.session_state.cards = get_cards()
    if 'current_index' not in st.session_state:
        st.session_state.current_index = 0
    if 'round' not in st.session_state:
        st.session_state.round = 1
    if 'hint' not in st.session_state:
        st.session_state.hint = ""
    if 'hint_given' not in st.session_state:
        st.session_state.hint_given = False
    if 'score' not in st.session_state:
        st.session_state.score = 0
