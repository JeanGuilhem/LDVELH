import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death, handle_repas


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=137)

fr_text = """
Lorsque la dernière de ces répugnantes créatures meurt enfin, la
lumière verdâtre commence à diminuer. Vous constatez alors
que dans chacun des crânes fracassés se trouve une Pierre
Précieuse. Vous ramassez ces vingt Pierres juste avant que la
lueur s'éteigne, plongeant la chambre mortuaire dans une totale
obscurité. N'oubliez pas d'inscrire ces Pierres Précieuses sur
votre Feuille d'Aventure. Elles prennent place dans votre bourse.
Vous vous hâtez de quitter la Crypte et vous poursuivez votre
chemin.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if st.session_state.last_page_number != st.session_state.current_page_number:
    st.session_state.purse += 20
    st.metric(label="Couronnes", value=st.session_state.purse, delta=20)


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
        st.page_link("pages/page_23.py", label="23", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
