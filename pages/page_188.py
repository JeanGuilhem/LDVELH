import streamlit as st
from inventory import display_inventory, check_inventory, end_page, change_endurance, empty_backpack, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=188)

fr_text = """
L'ombre du Kraan grandit tout autour de vous et, soudain, le
monstre vous frappe dans le dos en vous jetant à terre sous la
force de son attaque.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None:
        if number <= 6:
            st.write_stream(
                stream_text(
                    "Le Kraan a déchiré de ses serres pointues la toile de votre Sac à Dos. "
                    "Tout votre Équipement se répand alors sur le sol et il ne vous reste plus "
                    "qu'à le rayer de votre Feuille d'Aventure."
                )
            )
            if not st.session_state.get("visibility_188_applied"):
                empty_backpack()
                st.session_state.visibility_188_applied = True
        else:
            st.write_stream(
                stream_text(
                    "Votre Sac à Dos est intact, mais vous avez été blessé aux deux bras et vous "
                    "perdez 3 points d'ENDURANCE avant de courir vous mettre à l'abri des arbres."
                )
            )
            if not st.session_state.get("visibility_188_applied"):
                change_endurance(-3)
                st.session_state.visibility_188_applied = True
            st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)

        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("pages/page_303.py", label="303", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
