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
                current_page_number=75)

fr_text = """
En jetant un coup d'œil prudent, vous apercevez trois hommes
vêtus de vert qui chevauchent le long de la rive. Ce sont des
gardes-frontières ; ils appartiennent à un régiment royal chargé
de surveiller les frontières ouest du pays. L'un de ces hommes est
blessé ; il est affalé sur l'encolure de son cheval. Une vingtaine de
Loups Maudits suivent de près les trois soldats. Ils sont montés
par des Gloks qui tirent des flèches en direction des gardesfrontières. Bientôt, l'un de ces derniers tombe de son cheval et
roule sur la rive : une flèche noire l'a atteint à la jambe droite et
s'est profondément enfoncée dans sa cuisse.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""S Si vous souhaitez
vous porter au secours de ce soldat, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_260.py", label="260", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous
préférez rester caché et vous laisser dériver au fil du courant,
rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_163.py", label="163", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
