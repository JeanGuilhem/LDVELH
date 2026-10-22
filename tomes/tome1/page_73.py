import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=73)

fr_text = """
Vous ramenez votre cape autour de vos épaules et vous vous
fondez dans les rochers et les feuillages. Puis vous observez
attentivement les nouveaux arrivants et vous vous apercevez
alors avec un frisson d'horreur qu'il ne s'agit pas du tout de
soldats du Roi. Ce sont, en fait, des Drakkarims qui comptent
parmi les plus cruels serviteurs des Maîtres des Ténèbres. Ils se
sont déguisés en gardes de l'armée royale pour n'être pas
reconnus et pouvoir ainsi traverser la forêt sans encombre. Votre
initiation aux Disciplines Kaï vous a sauvé la vie et vous
remerciez intérieurement vos maîtres. Quelques instants plus
tard, vous avez quitté la rive du cours d'eau et vous vous enfoncez
dans la forêt en prenant garde à ne pas faire de bruit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(
        stream_text(
            f"""Rendezvous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_243.py", label="243", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
