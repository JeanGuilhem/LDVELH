import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies, before_fight, fight, ls_death, handle_repas


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

current_page_number = 136
check_inventory(is_fighting=True,
                current_page_number=current_page_number)

fr_text = """
Les Gloks se rapprochent puis s'accroupissent, prêts à bondir.
Vous apercevez les pointes dentelées de leurs lances et vous
entendez les sons gutturaux qu'ils produisent en parlant. « Rob
Gaye Oring Ahrr oho key ! Pamark élbhûtt ! » s'écrie la plus
grande des deux créatures qui vous attaque aussitôt. Il vous faut
combattre les deux Gloks à tour de rôle. Vous ajouterez un point
d'HABILETÉ à votre total en raison de l'avantage que vous
donne votre position plus élevée sur le terrain.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "done_fighting_glok_1" not in st.session_state:
    st.session_state.done_fighting_glok_1 = False
if "done_fighting_glok_2" not in st.session_state:
    st.session_state.done_fighting_glok_2 = False


tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.subheader("Premier GLOK")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=13)
    col2.metric(label="Endurance", value=10)

    if st.session_state.done_fighting_glok_1 is False:
        if st.button(f"Commencer à combattre le premier Glok"):
            ls_hability = before_fight(ls_hability=st.session_state.hability + 1)
            fight(ls_hability=ls_hability,
                  ls_endurance=st.session_state.endurance,
                  ennemy_hability=13,
                  ennemy_endurance=10,
                  turn_before_flee=0,
                  add_dammage_ennemy=0,
                  add_dammage_LS=0,
                  )
            st.session_state.done_fighting_glok_1 = True

    if st.session_state.done_fighting_glok_1:
        st.subheader("Deuxième GLOK")
        col1, col2 = st.columns(2)
        col1.metric(label="Habilité", value=12)
        col2.metric(label="Endurance", value=10)

        if st.session_state.done_fighting_glok_2 is False:
            if st.button(f"Commencer à combattre le deuxième Glok"):
                ls_hability = before_fight(ls_hability=st.session_state.hability + 1)
                fight(ls_hability=ls_hability,
                      ls_endurance=st.session_state.endurance,
                      ennemy_hability=12,
                      ennemy_endurance=10,
                      turn_before_flee=0,
                      add_dammage_ennemy=0,
                      add_dammage_LS=0,
                      )
                st.session_state.done_fighting_glok_2 = True

    if st.session_state.done_fighting_glok_1 and st.session_state.done_fighting_glok_2:
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au:"))
        fi = True
        if fi:
            st.page_link("pages/page_313.py", label="313", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number