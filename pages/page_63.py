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
                current_page_number=63)

fr_text = """
Le vieil homme vous insulte à grands cris. Il vous rend
responsable de la guerre en maudissant les Seigneurs Kaï qui
sont, selon lui, les agents des Maîtres des Ténèbres. Impossible
de lui faire entendre raison, il va falloir le combattre.

"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.subheader("VIEIL HOMME FOU")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=11)
    col2.metric(label="Endurance", value=10)
    if st.session_state.done_fighting is False:
        if st.button(f"Commencer à combattre"):
            ls_hability = before_fight(ls_hability=st.session_state.hability, ennemy_psychique_sensibility=True)
            fight(ls_hability=ls_hability,
                  ls_endurance=st.session_state.endurance,
                  ennemy_hability=11,
                  ennemy_endurance=10,
                  turn_before_flee=0,
                  add_dammage_ennemy=0,
                  add_dammage_LS=0,
                  )
        st.session_state.done_fighting = False

    if st.session_state.done_fighting:
        st.write_stream(
            stream_text(
                f"""Si vous êtes vainqueur, rendez-vous au"""
            )
        )
        fi = True
        if fi:
            st.page_link("pages/page_269.py", label="269", icon="📄")



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

