import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, fight, before_fight

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=72)

fr_text = """
Il vous faut affronter un Glok grimaçant chevauchant sa monture
à la gueule hérissée de dents pointues. Vous devez les combattre
tous deux en les considérant comme un seul et même adversaire.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.subheader("GLOK+ LOUP MAUDIT")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=15)
    col2.metric(label="Endurance", value=24)
    if st.session_state.done_fighting is False:
        if st.button(f"Commencer à combattre"):
            ls_hability = before_fight(ls_hability=st.session_state.hability, ennemy_psychique_sensibility=True)
            fight(ls_hability=ls_hability,
                  ls_endurance=st.session_state.endurance,
                  ennemy_hability=15,
                  ennemy_endurance=24,
                  turn_before_flee=0,
                  add_dammage_ennemy=0,
                  add_dammage_LS=0,
                  )

            st.session_state.done_fighting = True

    if st.session_state.done_fighting:

        st.write_stream(
            stream_text(
                f"""Si vous êtes vainqueur, rendez-vous au"""
            )
        )
        fi = True
        if fi:
            st.page_link("pages/page_265.py", label="265", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

