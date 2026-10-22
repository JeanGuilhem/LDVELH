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
                current_page_number=189)

fr_text = """
Grâce à votre entraînement de Seigneur Kaï et à la promptitude
de vos réflexes, vous avez échappé à ce marécage qui aurait pu se
révéler tout aussi meurtrier qu'un Kraan ou un Drakkarim. Vous
êtes contrarié d'avoir perdu du temps et vous vous hâtez de
poursuivre votre chemin parmi les arbres, en direction du sud.
Un peu plus loin devant vous, un large chemin mène également
vers le sud.
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
        st.page_link("tomes/tome1/page_118.py", label="118", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
