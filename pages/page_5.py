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
                current_page_number=5)

fr_text = """
Vous avez marché pendant environ une heure lorsque le sentier
s'oriente peu à peu vers l'est. Vous atteignez bientôt un gué qui
traverse un ruisseau coulant vers le sud. Le courant en est rapide
et le lit, rocheux et escarpé. Au-delà du gué, le sentier que vous
suivez croise un chemin plus large, orienté nord-sud. En allant
vers le nord, vous vous éloigneriez de la capitale et vous décidezdonc de prendre à droite, en direction du sud.
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
        st.page_link("pages/page_111.py", label="111", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
