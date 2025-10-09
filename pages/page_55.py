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
                current_page_number=55)

fr_text = """
Au moment où le Glok bondit, vous vous ruez sur lui et vous le
frappez de votre arme, l'empêchant ainsi d'atterrir sur le dos du
jeune sorcier. Vous profitez de votre avantage pour frapper à
nouveau la créature qui se débat et l'effet de surprise de votre
attaque vous permet d'ajouter 4 points à votre total d'HABILETÉ
pendant toute la durée de ce combat. N'oubliez pas cependant de
ramener ce total à son niveau antérieur dès la fin de
l'affrontement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.subheader("GLOK")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=9)
    col2.metric(label="Endurance", value=9)
    if st.session_state.done_fighting is False:
        if st.button(f"Commencer à combattre"):
            ls_hability = before_fight(ls_hability=st.session_state.hability+4, ennemy_psychique_sensibility=True)
            fight(ls_hability=ls_hability,
                  ls_endurance=st.session_state.endurance,
                  ennemy_hability=9,
                  ennemy_endurance=9,
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
        fi_2 = True
        if fi_2:
            st.page_link("pages/page_325.py", label="325", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

