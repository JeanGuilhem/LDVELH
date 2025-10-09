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
                current_page_number=44)

fr_text = """
Le sentier aboutit brusquement à une pente en à-pic. Le sol, très
instable à cet endroit, se dérobe sous vos pas : vous perdez
l'équilibre et vous tombez tête la première au bas de la pente.
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
                st.page_link("pages/page_277.py", label="277", icon="📄")
            else:
                st.write_stream(
                        stream_text(
                                f"""Rendez-vous au:"""
                        )
                )
                fi_2 = True
                if fi_2:
                    st.page_link("pages/page_338.py", label="338", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

