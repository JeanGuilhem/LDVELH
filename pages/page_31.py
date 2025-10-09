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
                current_page_number=1)

fr_text = """
Vous essayez de réconforter de votre mieux l'homme blessé, mais
ses plaies sont profondes et il perd à nouveau connaissance. Vous
le couvrez alors de sa cape et vous poursuivez votre chemin en
vous enfonçant plus profondément dans la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_264.py", label="264", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

