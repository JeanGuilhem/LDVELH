import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=265)

fr_text = """
Vous vous hâtez de disparaître dans la forêt avant que d'autres
ennemis, Loups Maudits ou Kraan, se montrent. Au bout d'une
heure de marche, vous atteignez le sommet d'une colline
rocheuse. De l'autre côté vous attend une vision d'espoir, mais
vous êtes loin cependant d'être au bout de vos peines, car de
nombreux dangers vous menacent encore.
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
        st.page_link("pages/page_142.py", label="142", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
