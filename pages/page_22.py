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
                current_page_number=22)

fr_text = """
D'un coup d'épaule, vous bousculez le chef et vous vous enfuyez à
toutes jambes le long de la route. Vous entendez aussitôt derrière
vous le déclic menaçant d'une arbalète que l'on tend. Un frisson
vous parcourt l'échiné et vous saisissez d'un geste prompt votre
Table de Hasard afin de tirer un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.button(label="Utilisez la Table de Hasard pour obtenir un chiffre."):
        st.session_state.number = table_des_hasards()
        if st.session_state.number in [1,2, 3, 4]:
            st.write_stream(
                    stream_text(f"""Rendez-vous au:""")
            )
            fi = True
            if fi:
                st.page_link("pages/page_181.py", label="181", icon="📄")
            else:
                st.write_stream(
                        stream_text(
                                f"""Rendez-vous au:"""
                        )
                )
                fi_2 = True
                if fi_2:
                    st.page_link("pages/page_145.py", label="145", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

