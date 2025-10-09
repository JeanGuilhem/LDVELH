import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=94)

fr_text = """
Voyant que vous avez tué son fils, le Sage fait volte-face et
s'enfuit de la boutique par la porte de derrière.
Vous trouvez 12 Pièces d'Or dans la bourse du Voleur et 4 autres
dans une boîte en bois, rangée sous le comptoir. Vous examinez
ensuite les potions et la baguette magique, et vous vous
apercevez qu'il s'agit de simples imitations sans aucune valeur. Il
n'y a rien dans la boutique qui mérite votre attention et vous
quittez les lieux pour rejoindre la grand-rue.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    st.session_state.purse += 16
    st.metric(label="Couronnes", value=st.session_state.purse, delta=+16)
    
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_7.py", label="7", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")