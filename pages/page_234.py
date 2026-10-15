import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, ls_death


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=234)

fr_text = """
Vous sautez de la roulotte qui file à bonne allure, mais vous vous
recevez mal et vous vous brisez la cheville en tombant. La
douleur est insupportable : elle vous fait perdre connaissance.
Hélas ! vous ne vous réveillerez jamais. Peut-être, cependant,
serez-vous intéressé d'apprendre que votre tête orne désormais
la selle d'un Kraan ? Votre mission s'est achevée ici, en même
temps que votre vie.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    ls_death()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
