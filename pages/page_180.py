import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=180)

fr_text = """
Ils vous voient lever votre arme et vous attaquent aussitôt. Si
vous souhaitez engager le combat, vous les affronterez à tour de
rôle.

Vous pouvez prendre la fuite à tout moment.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("CHEF DES SOLDATS", 15, 22), ("Premier SOLDAT", 13, 20), ("Deuxième SOLDAT", 12, 20)],
        flee_after=0,
    )

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes parvenu à les tuer tous les trois, rendez-vous au :"))
        st.page_link("pages/page_62.py", label="62", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite, rendez-vous au :"))
        st.page_link("pages/page_22.py", label="22", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
