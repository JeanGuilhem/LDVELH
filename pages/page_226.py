import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=226)

fr_text = """
Tout d'abord, la descente vous paraît facile mais, bientôt, votre
vue se brouille et vous sentez vos jambes faiblir. Les Dents de
Sommeil commencent à produire leur effet et, soudain, vous
trébuchez et vous perdez connaissance en tombant tête la
première.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("pages/page_277.py", label="277", icon="📄")
    elif number is not None:
        st.page_link("pages/page_338.py", label="338", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
