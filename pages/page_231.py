import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=231)

fr_text = """
Au moment où vous allez demander le prix des potions, un jeune
homme bondit sur vous en renversant le paravent. Votre
assaillant tient dans sa main un poignard à la longue lame
recourbée. Il vous faut le combattre.

Vous avez le droit de prendre la fuite après avoir livré deux assauts au moins.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VOLEUR AU POIGNARD", 13, 20)], max_rounds=4, flee_after=2)

    if outcome == "win":
        st.write_stream(stream_text("Vous l'avez tué en quatre assauts ou moins, rendez-vous au :"))
        st.page_link("pages/page_94.py", label="94", icon="📄")
    elif outcome == "rounds_over":
        st.write_stream(stream_text("Après quatre assauts, il est toujours vivant, rendez-vous au :"))
        st.page_link("pages/page_203.py", label="203", icon="📄")
    elif outcome == "fled":
        st.write_stream(
            stream_text(
                "Vous filez par la porte de la boutique et vous courez jusqu'à la grand-rue, rendez-vous au :"
            )
        )
        st.page_link("pages/page_7.py", label="7", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
