import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=34)

fr_text = """
Sans crier gare, une terrifiante apparition fond sur vous. C'est
une créature vêtue de longs vêtements rouges et montée sur le
dos d'un Kraan. Votre assaillant pousse un cri à vous glacer le
sang : il s'agit d'un Vordak, un féroce lieutenant des Maîtres des
Ténèbres. Il est juste au-dessus de vous et il vous faut le
combattre. Le monstre vous attaque à l'aide d'une grosse Masse
d'Armes et il est également doué d'une redoutable Puissance
Psychique, dont il va faire usage au cours de l'affrontement. Si
vous ne maîtrisez pas la Discipline Kaï du Bouclier Psychique,
vous devrez réduire de 2 points votre total d'HABILETÉ pendant
toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VORDAK", 17, 25)], psychic_attack=True)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome1/page_328.py", label="328", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
