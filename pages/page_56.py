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
                current_page_number=56)

fr_text = """
Vous entendez un cri au-dessus des arbres : c'est un Kraan, une
de ces grandes créatures volantes et sanguinaires qui comptent
parmi les plus redoutables serviteurs des Maîtres des Ténèbres.
Vous plongez aussitôt dans l'épaisseur des fougères pour vous
cacher jusqu'à ce que le cri du monstre se soit évanoui au
lointain. 
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous à présent au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_222.py", label="222", icon="📄")
x

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

