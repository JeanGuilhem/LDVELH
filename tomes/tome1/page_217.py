
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
                current_page_number=217)

fr_text = """
Vous vous hâtez de fuir le vieux fou et vous disparaissez dans une
ruelle obscure, bordée de petites maisons serrées les unes contre
les autres. Au bout de la ruelle, une enseigne accrochée au-
dessus d'une porte verte indique : KOLANIS Herboriste et Sage
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez pousser cette porte et entrer dans la boutique du Sage, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_91.py", label="91", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez attendre là quelques minutes pour être sûr que le vieux fou s'en est allé, puis revenir ensuite dans la grand-rue, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_7.py", label="7", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
