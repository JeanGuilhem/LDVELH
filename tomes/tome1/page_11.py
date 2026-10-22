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
                current_page_number=11)

fr_text = """
Vous vous dissimulez dans l'entrée d'une écurie et vous cachez
votre blouse de médecin dans la paille. Il est en effet préférable
d'apparaître comme un Seigneur Kaï que comme un charlatan.
Puis, sans perdre une seconde, vous vous dirigez vers l'Entrée
Principale, située de l'autre côté de la cour.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_139.py", label="139", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
