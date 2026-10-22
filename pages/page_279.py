import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=279)

fr_text = """
Vous grimpez sur l'amas de pierrailles qui s'entasse devant la
grotte à l'intérieur de laquelle vous vous engouffrez en prenant
soin d'en boucher l'entrée derrière vous à l'aide d'un gros rocher.
Quelques minutes plus tard, vous apercevez les Gloks qui
s'approchent de la grotte, leurs petits yeux jaunes et cruels
scrutant chaque fissure s'ouvrant au flanc de la colline. Ils sont si
près de vous que vous vous attendez à être découvert d'une
minute à l'autre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 6:
        st.page_link("pages/page_112.py", label="112", icon="📄")
    elif number is not None:
        st.page_link("pages/page_96.py", label="96", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
