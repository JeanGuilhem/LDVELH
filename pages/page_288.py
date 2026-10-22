
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=288)

fr_text = """
Lorsque vous atteignez la palissade du camp fortifié, les grandes
portes de chêne s'ouvrent sur votre passage et vous êtes conduit à
l'intérieur de l'enceinte militaire. Un sergent, aux vêtements
tachés de sang et déchirés dans la bataille, appelle un officier qui
se tourne vers vous et reconnaît aussitôt votre cape de Seigneur
Kaï. « Où sont les autres Seigneurs Kaï, My Lord ? demande-t-il.
Nous avons désespérément besoin de leur science. Les Maîtres
des Ténèbres mettent notre armée à rude épreuve et nos pertes
sont lourdes. » Vous révélez alors à votre interlocuteur le sort
qu'ont subi vos compagnons et vous l'informez de la mission
dont vous vous êtes chargé : prévenir le Roi. L'officier fait
aussitôt signe à un soldat d'amener deux chevaux. Un instant
plus tard, vous galopez tous deux en direction des hautes
murailles de Holmgard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_129.py", label="129", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
