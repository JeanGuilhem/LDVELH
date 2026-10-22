import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, ls_death


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=286)

fr_text = """
Ces messagers de la mort que sont les Loups Maudits, trop heureux de vous annoncer la vôtre, vous encerclent et vous attaquent. Vous vous défendez vaillamment, mais c'est inutile car ils sont trop nombreux. Votre corps bientôt se vide de son sang et l'ombre éternelle vous envahit. Avant de fermer les yeux, vous apercevez les tours de Holmgard qui scintillent au soleil : c'est la dernière vision que vous emporterez de ce monde. Votre mission a échoué.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
