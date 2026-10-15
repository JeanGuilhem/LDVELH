import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=133)

fr_text = """
Quand vous vous approchez de la statue, celle-ci commence à se
craqueler et, soudain, elle explose devant vous tandis qu'un
véritable serpent ailé, débarrassé de son manteau de pierre vous
attaque férocement. Il vous faut combattre la créature.

Votre adversaire est insensible à la Discipline Kaï de la Puissance
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("SERPENT AILÉ", 16, 18)], psychic_immune=True)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_266.py", label="266", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
