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
                current_page_number=84)

fr_text = """
Au moment où vous sentez le vent de ses ailes sur votre dos, vous
vous laissez tomber de votre cheval et vous roulez sur vousmême en terminant votre course dans la bouc d'un fossé, au bord
de la route. Vous êtes indemne et vous vous relevez d'un bond
pour courir vous mettre à l'abri des arbres ; mais il vous reste
une trentaine de mètres à parcourir et le Kraan se prépare à
fondre sur vous une nouvelle fois.
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
        st.page_link("pages/page_188.py", label="188", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

