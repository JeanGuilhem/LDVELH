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
                current_page_number=210)

fr_text = """
A peine avez-vous franchi la porte qu'un compagnon de la Guilde
vous barre le passage et vous demande ce que vous voulez. Vous
lui expliquez alors la nature de votre mission et il s'empresse
aussitôt de vous mener dans les appartements des Maîtres de la
Guilde. Un vieil homme distingué vêtu d'une toge violette vous
accueille et écoute votre récit. Puis, vous prenant par le bras, il
vous conduit dans une bibliothèque contiguë dont il ferme la
porte derrière lui. Il pousse ensuite l'un des milliers de livres
alignés sur les étagères et un pan de mur glisse alors sur le côté,
découvrant un passage secret. L'homme vous fait signe de le
suivre dans ce mystérieux couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez lui emboîter le pas, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_332.py", label="332", icon="📄")

    st.write_stream(
        stream_text(f"""Si cet homme ne vous inspire pas entièrement confiance, vous pouvez quitter les lieux et retourner au-dehors en vous rendant au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_37.py", label="37", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
