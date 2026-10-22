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
                current_page_number=74)

fr_text = """
Les Kraans et leurs maîtres atterrissent sur le chemin, à trois
mètres à peine de l'endroit où vous vous êtes caché. Les Gloks
sautent alors de leurs montures volantes à la peau couverte
d'écaillés et s'avancent vers vous, la lance levée : ils vous ont vu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous décidez de les combattre, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_138.py", label="138", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous
préférez prendre la fuite en courant dans la forêt, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_281.py", label="281", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
