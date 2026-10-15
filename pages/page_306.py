
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
                current_page_number=306)

fr_text = """
Les échos de la bataille s'évanouissent peu à peu derrière vous.
Et soudain, vous vous retrouvez plaqué au sol : trois Drakkarims,
cachés dans le feuillage d'un arbre, juste au-dessus de votre tête,
vous ont sauté dessus. Il est inutile d'essayer de lutter : ils sont
trop nombreux et trop robustes pour espérer pouvoir leur
échapper. Vous les entendez alors grogner de plaisir tandis qu'ils
lèvent leurs lances pour vous achever : c'est la dernière vision
que vous emporterez de ce monde. Votre mission s'achève ici, en
même temps que votre vie.
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
