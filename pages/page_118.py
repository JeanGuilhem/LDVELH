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
                current_page_number=118)

fr_text = """
Vous lancez votre cheval au galop le long du chemin droit. Vous
apercevez à l'horizon les contours de Holmgard dont les hautes
murailles et les tours scintillent sous les rayons du soleil. Le
sentier que vous suivez rejoint bientôt une grande route orientée
nord-sud. C'est la voie principale qui relie le port de Toran à la
capitale. Vous prenez donc la direction de Holmgard en
surveillant le ciel clair de peur que n'y apparaisse la silhouette
d'un Kraan.
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
        st.page_link("pages/page_224.py", label="224", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
