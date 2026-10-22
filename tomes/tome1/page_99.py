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
                current_page_number=99)

fr_text = """
Vous plongez dans les broussailles au moment même où le
monstre s'apprêtait à vous saisir dans ses serres pointues. Vous
entendez son cri lorsqu'il passe au-dessus de votre tête, et vous le
voyez virer dans les airs pour se préparer à un nouvel assaut.
Vous vous remettez alors sur pied et vous vous enfoncez dans
l'épaisseur de la forêt pour vous mettre à l'abri.
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
        st.page_link("tomes/tome1/page_222.py", label="222", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
