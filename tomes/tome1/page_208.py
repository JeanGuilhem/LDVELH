import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=208)

fr_text = """
Les répugnantes créatures brandissent leurs lances et vous
attaquent. Il vous faut les combattre en les considérant comme
un seul et même ennemi.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GLOKS", 15, 13)])

    if outcome == "win":
        st.write_stream(stream_text("Vous pouvez aller vous réfugier dans la ferme en vous rendant au :"))
        st.page_link("tomes/tome1/page_148.py", label="148", icon="📄")
        st.write_stream(stream_text("Vous pouvez également retourner dans la forêt. Rendez-vous alors au :"))
        st.page_link("tomes/tome1/page_320.py", label="320", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
