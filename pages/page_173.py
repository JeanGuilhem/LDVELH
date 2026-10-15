import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_item
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=173)

fr_text = """
Lorsque vous atteignez la porte, un énorme bloc de pierre
tombant du plafond s'écrase au sol, juste derrière vous. Vous
faites volte-face et vous constatez que la sortie est à présent
entièrement obstruée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    has_key = has_item("CLÉ D'ARGENT")

    st.write_stream(
        stream_text(
            "Si vous possédez une Clé d'Argent, vous pouvez vous en servir pour essayer "
            "d'ouvrir la porte. Rendez-vous pour cela au :"
        )
    )
    st.page_link("pages/page_158.py", label="158", icon="📄", disabled=not has_key)

    st.write_stream(stream_text("Si vous n'avez pas cette Clé, rendez-vous au :"))
    st.page_link("pages/page_259.py", label="259", icon="📄", disabled=has_key)

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
