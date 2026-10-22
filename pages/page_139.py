import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death, handle_repas



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=139)

fr_text = """
Il règne dans la cour une intense activité. Des éclaireurs de la
cavalerie attendent à côté de leurs chevaux que leurs
commandants d'unité, rassemblés au Quartier Général, leur
confient des messages à porter. A chaque instant, l'un de ces
hommes quitte la cour au galop, porteur d'une dépêche destinée
aux officiers en poste dans le camp fortifié. A peine sont-ils partis
que d'autres reviennent, à bout de souffle et souvent blessés.
Vous avez fait une douzaine de pas dans la cour lorsqu'une voix
retentit soudain : « Arrêtez cet homme ! » ordonne-t-elle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_66.py", label="66", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
