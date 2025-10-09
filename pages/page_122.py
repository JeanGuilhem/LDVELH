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
                current_page_number=122)

fr_text = """
Dès que le cheval sent que vous communiquez directement avec
lui, il se calme. Vous vous approchez alors de ce magnifique
étalon et vous lui caressez la tête d'un geste rassurant. Vous
sentez à présent qu'il ne sait plus très bien s'il doit avoir peur ou
pas. Vous montez ensuite sur son dos et vous le lancez sur le
chemin, en prenant cette fois encore la direction du sud.
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
        st.page_link("pages/page_206.py", label="206", icon="📄")
    
    st.session_state.last_page_number =  st.session_state.current_page_number

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")