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
                current_page_number=135)

fr_text = """
Parvenu au bord de l'escarpement de la berge, vous jetez un coup
d'œil en contrebas et vous apercevez un enchevêtrement de
débris de bois portés là par le courant. Un gros tronc d'arbre,
notamment, s'est échoué sur la rive, à côté d'un petit canoë.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez utiliser le tronc d'arbre pour descendre le cours
de la rivière, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_223.py", label="223", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous servir du canoë, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_4.py", label="4", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
