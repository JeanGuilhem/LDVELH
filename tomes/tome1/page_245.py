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
                current_page_number=245)

fr_text = """
Des flèches viennent frapper la surface de la rivière sans vous
faire le moindre mal : vous nagez sous l'eau, en effet, et il est
impossible de vous atteindre. Vous touchez bientôt la rive
opposée et vous vous hissez sur la terre ferme avant de courir
vous mettre à l'abri dans la forêt. Vous êtes maintenant hors
d'atteinte des Gloks qui enfourchent à nouveau leurs Loups
Maudits et reprennent leur poursuite.
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
        st.page_link("tomes/tome1/page_190.py", label="190", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
