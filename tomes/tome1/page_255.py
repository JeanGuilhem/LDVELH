import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, pickup_button, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=255)

fr_text = """
La créature qui vous fait face à présent est un Gourgaz, un de ces
reptiles monstrueux qui infestent les profondeurs des marais de
Maakenmire. Leur nourriture préférée est la chair humaine...
L'épée du Prince repose à vos pieds. Vous pouvez la ramasser et
vous en servir pour combattre si vous le désirez. Le Gourgaz
s'apprête à vous frapper. Il vous faut l'affronter jusqu'à la mort
de l'un d'entre vous.

Ce monstre est insensible à la Discipline Kaï de la Puissance
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    pickup_button("ÉPÉE DU PRINCE", key="sword", label="Ramasser l'Épée du Prince")

    outcome = combat([("GOURGAZ", 20, 30)], psychic_immune=True)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome1/page_82.py", label="82", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
