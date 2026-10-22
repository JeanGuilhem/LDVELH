import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=2)

fr_text = """
Tandis que vous courez à perdre haleine dans la forêt qui
s'épaissit, les cris des Gloks s'évanouissent peu à peu derrière
vous. Vous les avez presque semés lorsque vous trébuchez
soudain en tombant tête la première dans un enchevêtrement de
branches basses.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("pages/page_343.py", label="343", icon="📄")
    elif number is not None:
        st.page_link("pages/page_276.py", label="276", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
