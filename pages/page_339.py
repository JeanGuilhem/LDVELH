import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=339)

fr_text = """
Vous faites aussitôt un pas de côté, au moment où un Poignard
vient fracasser la vitre du comptoir. Un jeune homme vous
attaque et il vous faut le combattre.

Vous avez le droit de prendre la fuite à tout moment en quittant
la boutique pour rejoindre la grand-rue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VOLEUR", 13, 20)], max_rounds=4, flee_after=0)

    if outcome == "win":
        st.write_stream(stream_text("Vous l'avez tué en quatre assauts ou moins, rendez-vous au :"))
        st.page_link("pages/page_94.py", label="94", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Au bout de quatre assauts, il est toujours vivant, rendez-vous au :"))
        st.page_link("pages/page_203.py", label="203", icon="📄")
    elif outcome == "fled":
        st.write_stream(
            stream_text("Vous quittez la boutique pour rejoindre la grand-rue, rendez-vous au :")
        )
        st.page_link("pages/page_7.py", label="7", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
