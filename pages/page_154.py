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
                current_page_number=154)

fr_text = """
Votre blessure vous donne le tournis et vous titubez parmi les
arbres comme un aveugle. Soudain, vous tombez en avant
comme si le sol s'était dérobé sous vos pieds ; c'est, d'ailleurs, ce
qui s'est passé : vous venez d'être précipité tête la première dans
un piège à ours. Vous levez alors les yeux et vous distinguez les
silhouettes de quatre Drakkarims qui tendent leurs arcs en vous
visant de leurs flèches. Ils tirent tous les quatre en même temps
et vous entendez des grognements de triomphe s'échapper de
leurs lèvres, tordues en un rictus répugnant. Les quatre flèches
s'enfoncent profondément dans votre poitrine et toute lumière
s'éteint. Votre mission a échoué.
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
