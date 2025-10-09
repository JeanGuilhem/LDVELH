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
                current_page_number=49)

fr_text = """
Tandis que vous lisez l'inscription, une ombre se dessine derrière
le paravent.
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
            st.page_link("pages/page_339.py", label="339", icon="📄")
        else:
            st.write_stream(
                stream_text(
                    f"""Rendez-vous au:"""
                )
            )
            fi_2 = True
            if fi_2:
                st.page_link("pages/page_60.py", label="60", icon="📄")



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

