import streamlit as st
from utils import get_cards, validate_guess
from session import init_session_state

# Initialisation de l'état de session
init_session_state()

st.title("🕵️ AML 1v1 - Jeu de devinettes")

# Simule deux joueurs en local avec un bouton
if 'player_ready' not in st.session_state:
    st.session_state.player_ready = False

if not st.session_state.player_ready:
    if st.button("Rejoindre la partie"):
        st.session_state.player_ready = True
        st.success("En attente d'un autre joueur... (simulation)")
else:
    st.write(f"🎮 Manche {st.session_state.round} : Chat")

    # Affichage de la carte (uniquement pour le joueur qui doit faire deviner)
    current_card = st.session_state.cards[st.session_state.current_index]
    st.write(f"Carte à faire deviner : **{current_card}**")  # À cacher pour devin

    if 'hint_given' not in st.session_state:
        st.session_state.hint_given = False

    if not st.session_state.hint_given:
        hint = st.text_input("Entrez un indice (sans utiliser le mot cible) :")
        if hint:
            st.session_state.hint = hint
            st.session_state.hint_given = True
    else:
        st.info(f"Indice : {st.session_state.hint}")
        guess = st.text_input("Essayez de deviner le mot AML :", key="guess_input")
        if guess:
            correct = validate_guess(current_card, guess)
            if correct:
                st.success("✅ Bonne réponse !")
                st.session_state.score += 1
                if st.button("Carte suivante"):
                    st.session_state.current_index += 1
                    st.session_state.hint_given = False
                    st.session_state.hint = ""
            else:
                st.warning("❌ Mauvaise réponse. Essayez encore.")

    # Fin de manche
    if st.session_state.current_index >= len(st.session_state.cards):
        st.success(f"🎉 Fin de la Manche {st.session_state.round}. Score : {st.session_state.score}/5")
        if st.button("Inverser les rôles / Rejouer"):
            st.session_state.round += 1
            st.session_state.cards = get_cards()
            st.session_state.current_index = 0
            st.session_state.hint = ""
            st.session_state.hint_given = False
