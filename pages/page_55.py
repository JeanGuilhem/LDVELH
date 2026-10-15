import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=55)

fr_text = """
Au moment où le Glok bondit, vous vous ruez sur lui et vous le
frappez de votre arme, l'empêchant ainsi d'atterrir sur le dos du
jeune sorcier. Vous profitez de votre avantage pour frapper à
nouveau la créature qui se débat et l'effet de surprise de votre
attaque vous permet d'ajouter 4 points à votre total d'HABILETÉ
pendant toute la durée de ce combat. N'oubliez pas cependant de
ramener ce total à son niveau antérieur dès la fin de
l'affrontement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("GLOK", 9, 9)], hability_modifier=4)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_325.py", label="325", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
