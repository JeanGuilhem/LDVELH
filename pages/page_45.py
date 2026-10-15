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
                current_page_number=45)

fr_text = """
Ces hommes ne sont pas, en réalité, ce qu'ils semblent être. La
tunique de leur chef est authentique, mais elle est tachée de sang
autour du col comme si son véritable propriétaire avait été tué.
Quant aux armes dont disposent ces prétendus soldats, elles
n'appartiennent pas à l'armée ; elles sont, en effet, richement
ouvragées comme celles que fabriquent les armuriers du
Royaume de Durenor. Le chef porte une arbalète en bandoulière,
et une tentative de fuite équivaudrait à un suicide. Vous décidez
alors de combattre ces trois hommes, sinon ils vous tueront dès
que vous aurez lâché votre arme.
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
        st.page_link("pages/page_180.py", label="180", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
