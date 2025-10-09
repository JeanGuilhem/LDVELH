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
                current_page_number=116)

fr_text = """
Des flèches noires s'abattent tout autour de vous lorsque vous
vous hissez hors de l'eau boueuse. Vous vous précipitez vers les
arbres pour vous mettre à couvert et attendre que les Gloks aient
quitté la rive opposée. Vous reprenez ensuite votre chemin en
direction de la capitale.
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
        st.page_link("pages/page_321.py", label="321", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")