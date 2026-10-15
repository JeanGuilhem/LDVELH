import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=136)

fr_text = """
Les Gloks se rapprochent puis s'accroupissent, prêts à bondir.
Vous apercevez les pointes dentelées de leurs lances et vous
entendez les sons gutturaux qu'ils produisent en parlant. « Rob
Gaye Oring Ahrr oho key ! Pamark élbhûtt ! » s'écrie la plus
grande des deux créatures qui vous attaque aussitôt. Il vous faut
combattre les deux Gloks à tour de rôle. Vous ajouterez un point
d'HABILETÉ à votre total en raison de l'avantage que vous
donne votre position plus élevée sur le terrain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("Premier GLOK", 13, 10), ("Deuxième GLOK", 12, 10)], hability_modifier=1)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_313.py", label="313", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
