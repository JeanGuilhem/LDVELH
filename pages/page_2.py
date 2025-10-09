import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, table_des_hasards, set_cookies, called_cookies

fr_text = """
Tandis que vous courez à perdre haleine dans la forêt qui
s'épaissit, les cris des Gloks s'évanouissent peu à peu derrière
vous. Vous les avez presque semés lorsque vous trébuchez
soudain en tombant tête la première dans un enchevêtrement de
branches basses.
"""

if "weapon_mastery" not in st.session_state:
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=2)

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.button(label="Utilisez la Table de Hasard pour obtenir un chiffre."):
        st.session_state.number = table_des_hasards()
        st.write_stream(stream_text(f"*Vous avez tiré le {st.session_state.number}"))
        if st.session_state.number in [1,2,3,4]:
            st.write_stream(
                stream_text(
                    f"""Rendez-vous au"""
                )
            )
            fi = True
            if fi:
                st.page_link("pages/page_342.py", label="343", icon="📄")
        else:
            st.write_stream(
                stream_text(f"""Rendez-vous au:""")
            )
            fi_1 = True
            if fi_1:
                st.page_link("pages/page_276.py", label="276", icon="📄")



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

