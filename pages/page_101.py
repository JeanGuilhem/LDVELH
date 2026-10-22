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
                current_page_number=101)

fr_text = """
Le tumulte de la bataille se dissipe derrière vous, mais, dans le
silence qui lui succède, une voix intérieure vous traite de poltron
et vous reproche d'avoir abandonné un homme en danger. Vous
essayez alors de faire taire votre conscience en vous disant que
votre mission est beaucoup plus importante, car ce n'est pas
seulement la vie de ce jeune magicien qui est menacée, mais celle
de tous vos compatriotes si vous n'atteignez pas vivant la capitale
du royaume. Or soudain, vous apercevez un peu plus loin une
meute de Gloks : vous vous mettez aussitôt à couvert pour leur
échapper, mais il est trop tard, ils vous ont vu et il ne vous reste
plus qu'à vous enfuir en courant aussi vite que possible.
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
        st.page_link("pages/page_281.py", label="281", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
