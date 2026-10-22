import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=29)

fr_text = """
Vous vous approchez de la rive du lac en vous préparant à
combattre. Le Kraan et la créature qui le chevauche vous
aperçoivent aussitôt et foncent vers vous en volant à ras de l'eau.
C'est alors que le maître du Kraan lance un cri qui vous glace le
sang. Cette créature est un Vordak, un féroce lieutenant des
Maîtres des Ténèbres. Il se rue sur vous, et il vous faut le
combattre. Votre adversaire vous attaque à l'aide d'une grosse
Masse d'Armes, mais il est également doué d'une redoutable
Puissance Psychique dont il va faire usage au cours de
l'affrontement. Si vous ne maîtrisez pas la Discipline Kaï du
Bouclier Psychique, sa force mentale vous fera perdre 2 points
d'HABILETÉ pendant toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VORDAK", 17, 25)], psychic_attack=True)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_270.py", label="270", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
