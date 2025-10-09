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
                current_page_number=98)

fr_text = """
Les soldats semblent croire votre récit et ils s'inclinent
respectueusement, eu égard à votre rang de Seigneur Kaï. L'un
d'eux tire sur une grosse corde dissimulée dans le mur et les
lourdes portes commencent aussitôt à s'ouvrir. Les gardes vous
font alors entrer dans une cour intérieure tandis que les portes se
referment derrière vous.
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
        st.page_link("pages/page_139.py", label="139", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")