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
                current_page_number=35)

fr_text = """
La forêt devient de plus en plus dense, et un enchevêtrement de
buissons d'épines recouvre le chemin en s'épaississant à mesure
que vous avancez. Bien qu'il soit presque entièrement caché par
ces broussailles, vous découvrez un autre sentier orienté vers
l'est. Celui que vous suivez semble aboutir à un cul-de-sac de
buissons inextricables, et vous décidez donc d'emprunter ce
nouveau chemin en prenant la direction de l'est.
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
        st.page_link("tomes/tome1/page_207.py", label="207", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
