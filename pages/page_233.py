
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
                current_page_number=233)

fr_text = """
Il vous faut presque une heure pour rattraper le cheval et
parvenir à le calmer. Vous vous êtes éloigné de la cabane en
direction du nord mais vous êtes sûr de pouvoir retrouver votre
chemin. Vous montez sur le dos du cheval et vous retournez
jusqu'à la cabane, puis vous poursuivez votre route en direction
du sud.
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
        st.page_link("pages/page_206.py", label="206", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
