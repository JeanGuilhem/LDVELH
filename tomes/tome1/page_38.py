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
                current_page_number=38)

fr_text = """
Pendant plus d'une demi-heure, vous poursuivez votre chemin
dans la forêt, parmi les fougères et les feuillages touffus des
arbres et des buissons. Bientôt, vous parvenez au bord d'un
ruisseau où vous vous arrêtez quelques instants pour vous laver
le visage et boire un peu d'eau. Lorsque vous vous sentez
rafraîchi, vous traversez le ruisseau et vous reprenez votre
marche. Quelques instants plus tard, vous sentez une odeur de
bois brûlé qui semble venir du nord.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""" Si vous souhaitez aller voir
d'où vient cette odeur, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_128.py", label="128", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez ne
pas y prêter attention, rendez-vous au """)
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_347.py", label="347", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
