import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, before_fight, fight

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=43)

fr_text = """
Un énorme ours noir apparaît derrière le rocher et s'avance
lentement vers vous, la gueule ouverte. Vous remarquez aussitôt
qu'il a l'air d'avoir mal et que sa douleur le rend furieux. Il est
gravement blessé, en effet, et du sang coule sur son cou et dans
son dos. Il vous faut le combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.subheader("OURS NOIR")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=16)
    col2.metric(label="Endurance", value=10)
    if st.session_state.done_fighting is False:
        if st.button(f"Commencer à combattre"):
            ls_hability = before_fight(ls_hability=st.session_state.hability, ennemy_psychique_sensibility=True)
            fight(ls_hability=ls_hability,
                  ls_endurance=st.session_state.endurance,
                  ennemy_hability=17,
                  ennemy_endurance=25,
                  turn_before_flee=3,
                  add_dammage_ennemy=0,
                  add_dammage_LS=0,
                  )
            st.session_state.done_fighting = True


    st.write_stream(
        stream_text(
            f"""Si vous êtes vainqueur, rendez-vous au"""
        )
        )
    fi = True
    if fi:
        if st.session_state.done_fighting:
            st.page_link("pages/page_195.py", label="195", icon="📄")
        else:
            st.page_link("pages/page_195.py", label="195", icon="📄", disabled=True)


    st.write_stream(
        stream_text(
            f"""Au bout du
troisième assaut, vous avez réussi à vous placer de telle sorte
qu'il vous est possible de vous enfuir en courant au bas de la
colline. Si vous souhaitez vous échapper après avoir livré ces
trois assauts obligatoires, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        if st.session_state.flee:
            st.page_link("pages/page_106.py", label="106", icon="📄")
        else:
            st.page_link("pages/page_106.py", label="106", icon="📄", disabled=True)




with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

