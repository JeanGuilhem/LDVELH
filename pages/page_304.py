
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 304
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

if "pierre_precieuse_picked_up_304" not in st.session_state:
    st.session_state.pierre_precieuse_picked_up_304 = False

fr_text = """
La Pierre dégage une intense chaleur et vous brûle la main. Vous perdez aussitôt 2 points d'ENDURANCE.
Vous ramassez la Pierre Précieuse en enveloppant votre main dans un pan de votre cape de Seigneur Kaï et vous la glissez dans votre Sac à Dos.
Une Pierre de cette taille doit valoir une bonne centaine de Couronnes.
Entre-temps, les Gloks se sont rapprochés et, bientôt, leurs flèches sifflent à vos oreilles alors que vous courez vous réfugier à l'abri de la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        st.session_state.endurance -= 2
        st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)

        if not st.session_state.pierre_precieuse_picked_up_304:
            add_to_inventory(name="Pierre Précieuse")
            st.session_state.purse += 100
            st.metric(label="Couronnes", value=st.session_state.purse, delta=100)
            st.session_state.pierre_precieuse_picked_up_304 = True

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_2.py", label="2", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
