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
                current_page_number=149)

fr_text = """
Tandis que vous parcourez la grand-route à cheval, la lumière du
jour diminue de plus en plus ; bientôt, il fera complètement nuit
et vous ne pourrez plus voir les ennerrus qui vous attendent dans
l'ombre. Vous décidez donc de vous arrêter en lisière de la forêt
et de vous cacher là jusqu'au matin. Vous pourrez par la même
occasion prendre quelque repos. Vous vous aménagez une
cachette sûre et vous vous y installez, emmitouflé dans votre cape
verte de Seigneur Kaï. Quelques instants plus tard, vous avez
sombré dans un sommeil sans rêves.
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
        st.page_link("pages/page_256.py", label="256", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
