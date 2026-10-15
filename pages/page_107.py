import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=107)

fr_text = """
Vous traversez la pièce en courant et vous vous servez de votre
arme pour fracasser les crânes qui se brisent en mille morceaux.
Chacun des crânes est rempli d'une gelée grise et bouillonnante
qui se met à trembler et à changer de forme. A la surface luisante
de cette étrange substance apparaissent bientôt des ailes de
chauves-souris et des ventouses. Saisi d'horreur et de dégoût,
vous vous précipitez alors vers le couloir et vous quittez les lieux
au moment même où une lourde herse s'abat à l'entrée de la
pièce dont elle interdit désormais l'accès.
"""

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

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
