import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=63)

fr_text = """
Le vieil homme vous insulte à grands cris. Il vous rend
responsable de la guerre en maudissant les Seigneurs Kaï qui
sont, selon lui, les agents des Maîtres des Ténèbres. Impossible
de lui faire entendre raison, il va falloir le combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VIEIL HOMME FOU", 11, 10)])

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_269.py", label="269", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
