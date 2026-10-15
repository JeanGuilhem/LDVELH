import streamlit as st
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=22)

fr_text = """
D'un coup d'épaule, vous bousculez le chef et vous vous enfuyez à
toutes jambes le long de la route. Vous entendez aussitôt derrière
vous le déclic menaçant d'une arbalète que l'on tend. Un frisson
vous parcourt l'échiné et vous saisissez d'un geste prompt votre
Table de Hasard afin de tirer un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("pages/page_181.py", label="181", icon="📄")
    elif number is not None:
        st.page_link("pages/page_145.py", label="145", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
