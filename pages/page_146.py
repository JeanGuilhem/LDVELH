import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=146)

fr_text = """
Vous avez parcouru deux kilomètres à cheval lorsque vous êtes
soudain jeté à bas de votre monture par une flèche qui vient de
vous écorcher le front.
Tandis que vous vous relevez, vous voyez surgir de la forêt, des
deux côtés de la route, une bande de Drakkarims qui vous ont
tendu une embuscade. Il vous faut prendre la fuite au plus vite en
courant vous cacher parmi les arbres.
"""

if st.session_state.last_page_number != st.session_state.current_page_number:
    st.session_state.endurance -= 3
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)


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
        st.page_link("pages/page_154.py", label="154", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number