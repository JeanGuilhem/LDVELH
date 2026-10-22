import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=253)

fr_text = """
Les Loups Maudits sont bientôt sur vous et il vous faut les
combattre un par un.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [
            ("Premier LOUP MAUDIT", 13, 24),
            ("Deuxième LOUP MAUDIT", 14, 23),
            ("Troisième LOUP MAUDIT", 14, 22),
            ("Quatrième LOUP MAUDIT", 15, 21),
        ]
    )

    if outcome == "win":
        st.write_stream(stream_text("Vous les avez tous tués, rendez-vous au :"))
        st.page_link("pages/page_278.py", label="278", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
