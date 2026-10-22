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
                current_page_number=310)

fr_text = """
Accrochée au mur d'un bâtiment, de l'autre côté de la rue, une
pancarte délavée porte l'inscription suivante :
Vous savez que les sessions du tribunal se tiennent à l'intérieur
de la citadelle et vous êtes certain que la rue orientée à l'ouest y
mène directement.
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
        st.page_link("pages/page_37.py", label="37", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
