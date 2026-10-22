import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=314)

fr_text = """
Il vous faut presque une heure pour atteindre la citadelle.
Lorsque vous arrivez, vous constatez qu'il règne dans les rues de
la ville panique et confusion. Le soldat qui vous escorte
s'approche des gardes à l'entrée principale de la citadelle et leur
explique que vous devez à tout prix voir le Roi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 6:
        st.page_link("pages/page_341.py", label="341", icon="📄")
    elif number is not None:
        st.page_link("pages/page_98.py", label="98", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
