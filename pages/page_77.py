import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=77)

fr_text = """
Les Gloks sont des créatures des montagnes peu habituées à
poursuivre leurs proies dans les forêts, et vous parvenez bientôt à
les distancer. Leurs grognements et leurs jurons s'évanouissent
au lointain : ils ont abandonné la course. Vous faites alors une
courte halte pour reprendre votre souffle et vérifier votre
équipement. Puis vous vous remettez en route après avoir
soigneusement rangé les quelques objets que vous avez réussi à
arracher aux décombres du monastère. L'image de ses ruines
fumantes vous revient en mémoire, et vous serrez les dents
tandis que la forêt s'épaissit autour de vous.
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
        st.page_link("pages/page_19.py", label="19", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
