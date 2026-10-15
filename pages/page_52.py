import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=52)

fr_text = """
A présent que vous vous êtes approché, vous vous apercevez qu'il
ne s'agit pas là de voix humaines. On dirait plutôt des
grognements et des cris d'animaux.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la
Discipline Kaï de la Communication animale, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        if not has_kai("Communication Animale"):
            st.write_stream(stream_text(fr_unkown_kai))
            st.page_link("pages/page_225.py", label="225", icon="📄", disabled=True)
        else:
            st.page_link("pages/page_225.py", label="225", icon="📄")

    st.write_stream(
        stream_text(f"""Sinon, montez sur le tronc de l'arbre pour aller voir qui se
cache derrière. Rendez-vous pour cela au """)
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_250.py", label="250", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
