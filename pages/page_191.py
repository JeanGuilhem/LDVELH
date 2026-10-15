import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=191)

fr_text = """
Le garde du corps dégaine un long cimeterre et s'apprête à vous
attaquer.

Vous pouvez prendre la fuite au cours du combat en sautant de la roulotte.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GARDE DU CORPS", 11, 21)], flee_after=0)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_24.py", label="24", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous sautez de la roulotte, rendez-vous au :"))
        st.page_link("pages/page_234.py", label="234", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
