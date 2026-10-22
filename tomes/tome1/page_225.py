import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=225)

fr_text = """
Ce langage est celui des Kakarmis, une race d'animaux forestiers,
doués d'intelligence, qui habitent les forêts du Sommerlund.
Vous n'avez rien à redouter de ces créatures timides et paisibles
et votre Sens de la Communication Animale vous permet de leur
parler dans leur étrange dialecte. Que désirez-vous leur dire ?
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("« N'ayez pas peur, je viens en ami » ? Rendez-vous dans ce cas au :"))
    st.page_link("tomes/tome1/page_187.py", label="187", icon="📄")

    st.write_stream(
        stream_text(
            "« Je suis un Seigneur Kaï, je ne vous veux aucun mal, je souhaite simplement "
            "parler avec vous » ? Rendez-vous alors au :"
        )
    )
    st.page_link("tomes/tome1/page_39.py", label="39", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
