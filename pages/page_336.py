import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=336)

fr_text = """
Vous vous ruez dans la clairière en prenant les Gloks au
dépourvu. Sans la moindre seconde d'hésitation, vous frappez
celui qui se trouve le plus proche de vous et vous le tuez avant
même que son corps se soit écroulé sur le sol. Les autres Gloks
dégainent leurs épées à la lame recourbée et vous attaquent, il
vous faut les combattre un par un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("Premier GLOK", 14, 11), ("Deuxième GLOK", 13, 11)])

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, vous libérez le soldat et vous vous rendez au :"))
        st.page_link("pages/page_117.py", label="117", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
