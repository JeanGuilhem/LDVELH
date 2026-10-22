
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
                current_page_number=325)

fr_text = """
En vous voyant apparaître, le chef des Gloks se met à hurler : « Groh Gaï oh ! Groh gaï oh !» à l'adresse de ses compagnons qui s'enfuient des ruines et courent se réfugier dans la forêt. L'officier Glok, vêtu de noir, se tourne alors vers vous en brandissant le poing. « Rob Gaï ohrringh âârh oho key ! Pamark hélbutt ! » s'écrie-t-il avec fureur avant de prendre la fuite à son tour. Vous jetez ensuite un coup d'oeil sur le champ de bataille : plus de quinze cadavres de Gloks sont étendus parmi les ruines du temple de Raumas. Le jeune sorcier essuie son front ruisselant de sueur et s'avance vers vous, la main tendue en signe d'amitié.
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
        st.page_link("pages/page_349.py", label="349", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
