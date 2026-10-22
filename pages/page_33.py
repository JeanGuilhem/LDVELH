import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, receive_gold, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=33)

fr_text = """
Le sol de la grotte est sec et poussiéreux. Vous vous enfoncez un
peu plus profondément dans la pénombre et vous détectez alors
une odeur de viande en putréfaction. Des os, des peaux et des
dents de petits animaux sont entassés dans une crevasse. Vous
trouvez parmi ces restes un petit sac qui contient 3 Pièces d'Or.
Vous les empochez et vous quittez cet endroit où quelque bête
sauvage a probablement établi sa tanière, puis vous descendez le
flanc de la colline.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    receive_gold(3)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_248.py", label="248", icon="📄")

    show_illustrations()



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
