import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=44)

fr_text = """
Le sentier aboutit brusquement à une pente en à-pic. Le sol, très
instable à cet endroit, se dérobe sous vos pas : vous perdez
l'équilibre et vous tombez tête la première au bas de la pente.
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
