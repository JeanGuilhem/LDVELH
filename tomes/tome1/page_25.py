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
                current_page_number=25)

fr_text = """
Vous atterrissez si brutalement sur l'autre toit que vous en avez
le souffle coupé. La tête vous tourne, et vous restez étendu sur le
dos. Au bout d'une minute environ, vous comprenez enfin que
vous avez réussi à passer de l'autre côté et que vous êtes
indemne. Lorsque vous êtes vraiment sûr que tout va bien, vous
vous relevez d'un bond et vous poussez un cri de victoire pour
saluer votre adresse et votre audace. Puis vous vous hâtez de
gagner le bord opposé du toit où une longue gouttière vous
permet de descendre dans la rue. Les hautes portes de fer de la
citadelle sont ouvertes et un chariot, tiré par deux grands
chevaux, essaie de sortir dans la rue. Mais les chevaux effrayéspar le bruit de la foule se cabrent soudain et l'une des roues avant
du véhicule se brise en heurtant violemment la porte. Profitant
de la confusion, vous vous glissez à l'intérieur de la citadelle juste
avant que les gardes aient refermé les lourds battants
métalliques.
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
        st.page_link("tomes/tome1/page_139.py", label="139", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
