import streamlit as st
import time
from utils import get_cards, validate_guess, normalize
from session import init_session_state

# Initialisation de l'état de session
init_session_state()

st.title("🕵️ AML 1v1 - Jeu de devinettes")

# Entrée du nom du joueur (simulé)
if 'player_name' not in st.session_state:
    st.session_state.player_name = st.text_input("Entrez votre nom :")
    if st.session_state.player_name:
        st.experimental_rerun()
    else:
        st.stop()

# Simule deux joueurs
if not st.session_state.player_ready:
    if st.button("Rejoindre la partie"):
        st.session_state.player_ready = True
        st.success("En attente d'un autre joueur... (simulation)")
else:
    st.write(f"🎮 Manche {st.session_state.round} - Joueur : {st.session_state.player_name}")

    current_card = st.session_state.cards[st.session_state.current_index]

    # Pour test local, on affiche la carte à deviner si joueur 1
    if st.session_state.player_name == "Joueur 1":
        st.write(f"Carte à faire deviner : **{current_card}**")
    else:
        st.write("Indice en attente...")

    if 'hint_given' not in st.session_state:
        st.session_state.hint_given = False
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 0
    if 'timer_start' not in st.session_state:
        st.session_state.timer_start = None

    # Joueur 1 donne un indice
    if not st.session_state.hint_given and st.session_state.player_name == "Joueur 1":
        hint = st.text_input("Entrez un indice (sans le mot cible) :")
        if hint:
            normalized_hint = normalize(hint)
            normalized_card = normalize(current_card)
            if normalized_card in normalized_hint:
                st.warning("❌ L'indice contient le mot à deviner !")
            else:
                st.session_state.hint = hint
                st.session_state.hint_given = True
                st.session_state.timer_start = time.time()
                st.experimental_rerun()

    # Joueur 2 devine avec 2 essais et chrono 45s
    elif st.session_state.hint_given and st.session_state.player_name != "Joueur 1":
        st.info(f"Indice : {st.session_state.hint}")

        # Chrono
        elapsed = time.time() - st.session_state.timer_start
        remaining = 45 - int(elapsed)
        st.progress(min(elapsed / 45, 1.0))
        st.write(f"⏱️ Temps restant : {remaining} secondes")

        if remaining <= 0:
            st.warning("⏰ Temps écoulé ! Passez à la carte suivante.")
            if st.button("Carte suivante"):
                st.session_state.current_index += 1
                st.session_state.hint_given = False
                st.session_state.hint = ""
                st.session_state.attempts = 0
                st.session_state.timer_start = None
                st.experimental_rerun()
            st.stop()

        # Deviner
        guess = st.text_input("Essayez de deviner le mot AML :", key="guess_input")
        if guess:
            correct = validate_guess(current_card, guess)
            st.session_state.attempts += 1
            if correct:
                st.success("✅ Bonne réponse !")
                st.session_state.score += 1
                if st.button("Carte suivante"):
                    st.session_state.current_index += 1
                    st.session_state.hint_given = False
                    st.session_state.hint = ""
                    st.session_state.attempts = 0
                    st.session_state.timer_start = None
                    st.experimental_rerun()
            elif st.session_state.attempts >= 2:
                st.error("❌ 2 tentatives échouées.")
                if st.button("Carte suivante"):
                    st.session_state.current_index += 1
                    st.session_state.hint_given = False
                    st.session_state.hint = ""
                    st.session_state.attempts = 0
                    st.session_state.timer_start = None
                    st.experimental_rerun()
            else:
                st.warning(f"❌ Mauvaise réponse ({st.session_state.attempts}/2). Essayez encore.")

    # Fin de la manche
    if st.session_state.current_index >= len(st.session_state.cards):
        st.success(f"🎉 Fin de la Manche {st.session_state.round}. Score : {st.session_state.score}/5")
        if st.button("Inverser les rôles / Rejouer"):
            st.session_state.round += 1
            st.session_state.cards = get_cards()
            st.session_state.current_index = 0
            st.session_state.hint = ""
            st.session_state.hint_given = False
            st.session_state.attempts = 0
            st.session_state.timer_start = None
            st.experimental_rerun()
