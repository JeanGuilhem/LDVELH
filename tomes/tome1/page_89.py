import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=89)

fr_text = """
Vous dévalez le flanc escarpé de la colline dans un nuage de
poussière et de cailloux. Le Kraan continue de tournoyer au-dessus de votre tête comme pour guider les Gloks vers vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 1:
        st.page_link("tomes/tome1/page_53.py", label="53", icon="📄")
    elif number is not None and number <= 4:
        st.page_link("tomes/tome1/page_274.py", label="274", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome1/page_316.py", label="316", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
