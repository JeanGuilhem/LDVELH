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
                current_page_number=123)

fr_text = """
Lorsque la créature meurt, son corps se dissout en une espèce de
liquide verdâtre et répugnant. Vous remarquez alors que les
herbes et les plantes sur lesquelles se répand cette substance
fumante se ratatinent et meurent aussitôt. Une Pierre Précieuse
de bonne taille apparaît parmi les herbes, près du corps en
décomposition. Plus loin sur le sentier, vous apercevez une
meute de Gloks qui se précipitent vers vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez ramasser la Pierre Précieuse, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_304.py", label="304", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez partir à l'instant en prenant vos jambes à votre cou, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_2.py", label="2", icon="📄")

    # SAUVEGARDE DE LA PAGE ACTUELLE POUR LES FUTURS RE-RUNS
    st.session_state.last_page_number = st.session_state.current_page_number

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")