import streamlit as st
from inventory import display_inventory, check_inventory, end_page, is_new_page, lose_all_weapons, lose_backpack
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=294)

if is_new_page():
    lose_all_weapons()
    lose_backpack()

fr_text = """
Après être resté sous l'eau aussi longtemps que vous le
permettait votre capacité respiratoire, vous refaites enfin surface
et vous constatez que les Gloks se trouvent loin derrière vous.
Vous avez perdu Arme(s) et Sac à Dos, mais au moins, vous êtes
vivant. Vous sortez alors de cette eau boueuse et vous poursuivez
votre chemin à l'abri des arbres qui bordent la rive droite du
cours d'eau.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 2:
        st.page_link("pages/page_230.py", label="230", icon="📄")
    elif number is not None and number <= 6:
        st.page_link("pages/page_190.py", label="190", icon="📄")
    elif number is not None:
        st.page_link("pages/page_321.py", label="321", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
