import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=227)

fr_text = """
Vous avez maintenant de la vase jusqu'à la ceinture, l'air est
lourd et de petits insectes vous piquent le visage et vous
bouchent le nez. Puis soudain, quelque chose s'enroule autour de
vos jambes. C'est une Vipère des Marais qu'il vous faut
combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VIPÈRE DES MARAIS", 16, 6)], stop_when_wounded=True)

    if outcome == "wounded":
        st.write_stream(stream_text("Vous avez perdu des points d'ENDURANCE au cours du combat, rendez-vous au :"))
        st.page_link("tomes/tome1/page_271.py", label="271", icon="📄")
    elif outcome == "win":
        st.write_stream(stream_text("Vous avez tué la Vipère sans perdre aucun point d'ENDURANCE, rendez-vous au :"))
        st.page_link("tomes/tome1/page_348.py", label="348", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
