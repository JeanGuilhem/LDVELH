import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=17)

fr_text = """
Vous levez votre arme pour frapper la créature, dont la gueule
hérissée de crocs tranchants comme des rasoirs vient de se
refermer d'un claquement sec à quelques centimètres de votre
tête. Gêné par le battement de ses ailes, vous avez du mal à vous
tenir debout. Réduisez d'un point votre total d'HABILETÉ, et
combattez ce Kraan.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("KRAAN", 16, 24)], hability_modifier=-1)

    if outcome == "win":
        st.write_stream(
            stream_text(
                "Hâtez-vous de descendre le flanc opposé de la colline afin d'éviter les Gloks."
            )
        )
        number = hazard_roll()
        if number == 0:
            st.page_link("pages/page_53.py", label="53", icon="📄")
        elif number in [1, 2]:
            st.page_link("pages/page_274.py", label="274", icon="📄")
        elif number is not None:
            st.page_link("pages/page_331.py", label="331", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
