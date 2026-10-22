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
                current_page_number=102)

fr_text = """
Vous descendez le flanc rocheux de la colline en direction du
Cimetière des Anciens et vous apercevez au loin l'étrange nuage
de brume qui baigne en permanence ces lieux grisâtres et
lugubres. Ce brouillard maléfique, qui jamais ne se lève, est si
dense qu'il empêche le soleil de briller sur les tombes. Lorsque
vous arrivez à proximité du cimetière, l'air se rafraîchit et devient
bientôt glacial. Avec un sentiment de terreur, vous pénétrez alors
dans cette sinistre nécropole.
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
        st.page_link("pages/page_284.py", label="284", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
