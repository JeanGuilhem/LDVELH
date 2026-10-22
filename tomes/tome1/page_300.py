import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=300)

fr_text = """
Vous avez marché pendant plus d'une heure en surveillant le ciel
de peur de voir apparaître des Kraans. Par deux fois, vous avez
aperçu leurs silhouettes caractéristiques qui se dessinaient au
loin, mais la promptitude de vos réflexes vous a gardé d'être
repéré. Cette longue marche vous a affamé cependant et il vous
faut prendre un Repas, sinon vous perdrez 3 points
d'ENDURANCE.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    handle_repas()

    st.write_stream(stream_text("Vous poursuivrez ensuite votre chemin en vous rendant au :"))
    st.page_link("tomes/tome1/page_13.py", label="13", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
