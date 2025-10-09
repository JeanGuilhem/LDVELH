import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, table_des_hasards

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=89)

fr_text = """
Vous dévalez le flanc escarpé de la colline dans un nuage de
poussière et de cailloux. Le Kraan continue de tournoyer audessus de votre tête comme pour guider les Gloks vers vous. 
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.button(label="Utilisez la Table de Hasard pour obtenir un chiffre."):

        st.session_state.number = table_des_hasards()
        st.write_stream(stream_text(f"*Vous avez tiré le {st.session_state.number}"))

        if st.session_state.number in [1,10]:
            st.write_stream(
                stream_text(
                    f"""Rendez-vous au"""
                )
            )
            fi = True
            if fi:
                st.page_link("pages/page_53.py", label="53", icon="📄")

        elif st.session_state.number in [2,3,4]:
            st.write_stream(
                stream_text(
                    f"""Rendez-vous au"""
                )
            )
            fi = True
            if fi:
                st.page_link("pages/page_274.py", label="274", icon="📄")

        else:
            st.write_stream(
                stream_text(
                    f"""Rendez-vous au"""
                )
            )
            fi = True
            if fi:
                st.page_link("pages/page_316.py", label="316", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

