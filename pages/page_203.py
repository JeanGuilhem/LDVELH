import streamlit as st
from inventory import display_inventory, check_inventory, end_page, change_endurance, is_new_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=203)

fr_text = """
Une douleur fulgurante vous traverse la poitrine alors que
quelque chose vient d'exploser tout contre vous dans une gerbe
d'étincelles rouges. Vous perdez 10 points d'ENDURANCE et, si
vous n'êtes pas déjà mort, vous voyez à travers la fumée le Sage
s'apprêter à vous lancer une nouvelle charge explosive.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        change_endurance(-10)
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-10)

    if st.session_state.endurance >= 10:
        st.write_stream(stream_text("Il vous reste 10 points d'ENDURANCE ou plus, rendez-vous au :"))
        st.page_link("pages/page_80.py", label="80", icon="📄")
    else:
        st.write_stream(stream_text("Il vous reste moins de 10 points d'ENDURANCE, rendez-vous au :"))
        st.page_link("pages/page_344.py", label="344", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
