import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, fight, before_fight

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=True,
                current_page_number=112)

fr_text = """
Soudain, le gros rocher derrière lequel vous vous êtes caché roule
sur lui-même, poussé par deux Gloks hurlants qui vous font face
et qui ont visiblement l'intention de vous tuer. L'entrée de la
grotte est étroite, et vous ne pouvez combattre qu'un Glok à la
fois. Vous devrez donc les affronter à tour de rôle.
"""
# Initialize a session state variable to track the combat stages
if "done_fighting_glok_1" not in st.session_state:
    st.session_state.done_fighting_glok_1 = False
if "done_fighting_glok_2" not in st.session_state:
    st.session_state.done_fighting_glok_2 = False

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    # Combat contre le premier Glok
    if not st.session_state.done_fighting_glok_1:
        st.subheader("Premier GLOK")
        col1, col2 = st.columns(2)
        col1.metric(label="Habilité", value=13)
        col2.metric(label="Endurance", value=10)
        if st.button(f"Commencer à combattre le premier Glok"):
            ls_hability = before_fight(ls_hability=st.session_state.hability)
            fight(ls_hability=ls_hability,
                ls_endurance=st.session_state.endurance,
                ennemy_hability=13,
                ennemy_endurance=10,
                turn_before_flee=0,
                add_dammage_ennemy=0,
                add_dammage_LS=0,
                  )
            st.session_state.done_fighting_glok_1 = True

    # Combat contre le deuxième Glok
    if st.session_state.done_fighting_glok_1 and not st.session_state.done_fighting_glok_2:
        st.subheader("Deuxième GLOK")
        col1, col2 = st.columns(2)
        col1.metric(label="Habilité", value=12)
        col2.metric(label="Endurance", value=10)
        if st.button(f"Continuer à combattre le deuxième Glok"):
            ls_hability = before_fight(ls_hability=st.session_state.hability)
            fight(ls_hability=ls_hability,
                ls_endurance=st.session_state.endurance,
                ennemy_hability=12,
                ennemy_endurance=10,
                turn_before_flee=0,
                add_dammage_ennemy=0,
                add_dammage_LS=0,
                  )
            st.session_state.done_fighting_glok_2 = True
    
    # Redirections après les deux combats
    if st.session_state.done_fighting_glok_1 and st.session_state.done_fighting_glok_2:
        st.write_stream(
            stream_text(
                f"""Si vous êtes vainqueur, vous pouvez explorer la grotte plus avant en vous rendant au:"""
            )
        )
        fi = True
        if fi:
            st.page_link("pages/page_33.py", label="33", icon="📄")

        st.write_stream(
            stream_text(
                f"""Mais vous pouvez également quitter les lieux et descendre le flanc de la colline ; rendez-vous pour cela au:"""
            )
        )
        fi_1 = True
        if fi_1:
            st.page_link("pages/page_248.py", label="248", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")