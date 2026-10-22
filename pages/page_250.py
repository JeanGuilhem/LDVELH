
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
                current_page_number=250)

fr_text = """
Deux petites créatures au pelage ras se cachent derrière le tronc. Ce sont des Kakarmis, une race d'animaux doués d'intelligence qui habitent les forêts du Sommerlund. Vous avez sauté du tronc juste en face d'eux et avant que vous ayez eu le temps de vous expliquer, les deux Kakarmis, affolés par votre apparition soudaine, s'enfuient dans la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez les suivre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_186.py", label="186", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
