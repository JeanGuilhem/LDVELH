import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=114)

fr_text = """
Vous amenez votre cheval à se coucher et vous le recouvrez, ainsi
que vous-même, de branches et de feuilles mortes. Vous
entendez les battements d'ailes du Kraan lorsqu'il passe au-dessus
des arbres : il se met à tournoyer au-dessus de vous, mais
repart bientôt en direction du lac qu'il traverse dans l'autre sens.
Vous décidez alors de partir au plus vite de peur qu'il ne revienne
avec quelques-uns de ses compagnons.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("pages/page_239.py", label="239", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
