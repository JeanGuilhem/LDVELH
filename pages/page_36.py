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
                current_page_number=36)

fr_text = """
Le bois de l'échelle qui monte à la vieille tour de guet, est pourri
et plusieurs barreaux cèdent sous votre poids.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.button(f"""Utilisez la Table de
Hasard pour obtenir un chiffre."""):
        st.session_state.number =table_des_hasards()
        if st.session_state.number <= 4:
            st.write_stream(
                    stream_text(
                            f"""Vous perdez donc 2 points
d'ENDURANCE et vous vous rendez au"""
                    )
            )
            st.session_state.endurance -= 2
            st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
            i_2 = True
            if i_2:
                st.page_link("pages/page_140.py", label="140", icon="📄")

        else:
            st.write_stream(
                    stream_text(
                            f"""Vous ne tombez pas et vous vous rendez au"""
                    )
            )
            i_2 = True
            if i_2:
                st.page_link("pages/page_323.py", label="323", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

