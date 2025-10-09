import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies, before_fight, fight, ls_death, handle_repas


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 133
check_inventory(is_fighting=True,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Quand vous vous approchez de la statue, celle-ci commence à se
craqueler et, soudain, elle explose devant vous tandis qu'un
véritable serpent ailé, débarrassé de son manteau de pierre vous
attaque férocement. Il vous faut combattre la créature.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "done_fighting_serpent_aile" not in st.session_state:
    st.session_state.done_fighting_serpent_aile = False

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.subheader("SERPENT AILÉ")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=16)
    col2.metric(label="Endurance", value=18)

    if st.session_state.done_fighting_serpent_aile is False:
        if st.button(f"Commencer à combattre le Serpent Ailé"):
            ls_hability = before_fight(ls_hability=st.session_state.hability, ennemy_psychique_sensibility=False)
            fight(ls_hability=ls_hability,
                ls_endurance=st.session_state.endurance,
                ennemy_hability=16,
                ennemy_endurance=18,
                turn_before_flee=0,
                add_dammage_ennemy=0,
                add_dammage_LS=0,
                )
            st.session_state.done_fighting_serpent_aile = True

    if st.session_state.done_fighting_serpent_aile:
        st.write_stream(stream_text("Si vous êtes vainqueur, rendez-vous au:"))
        fi = True
        if fi:
            st.page_link("pages/page_266.py", label="266", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number