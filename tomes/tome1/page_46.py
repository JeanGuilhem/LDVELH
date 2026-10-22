import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, spend_gold, show_illustrations
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=46)

fr_text = """
Vous avez parcouru trois kilomètres environ, et le feuillage des
arbres commence à s'éclaircir. Vous apercevez alors, au bord
d'un lac, une petite cabane de bois. Un homme vêtu d'une cape
s'approche bientôt de vous et vous offre de vous faire traverser le
lac sur son bateau, vous et votre cheval, pour la somme de 2
Couronnes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous acceptez son offre, rendez-vous au """
        )
    )
    if st.button("Payer 2 Couronnes (246)", disabled=st.session_state.purse < 2):
        if spend_gold(2):
            st.switch_page("tomes/tome1/page_246.py")
    if st.session_state.purse < 2:
        st.caption("Vous ne possédez pas la somme demandée.")

    st.write_stream(
        stream_text(f"""Si
vous préférez refuser et contourner le lac à cheval, rendez-vous
au """)
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_90.py", label="90", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        if not has_kai("Sixième Sens"):
            st.write_stream(stream_text(fr_unkown_kai))
            st.page_link("tomes/tome1/page_296.py", label="296", icon="📄", disabled=True)
        else:
            st.page_link("tomes/tome1/page_296.py", label="296", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
