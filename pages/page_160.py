import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=160)

fr_text = """
Utilisez la Table de Hasard pour obtenir un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text('Vous avez été repéré.'))
        st.page_link("pages/page_286.py", label="286", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Ils ne vous ont pas vu et poursuivent leur chemin en s'éloignant de vous."))
        st.page_link("pages/page_10.py", label="10", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
