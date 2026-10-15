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
                current_page_number=338)

fr_text = """
Lorsque vous reprenez conscience, vous êtes étendu au pied d'une pente escarpée, sur un tapis de hautes herbes. 
Vous ne voyez plus ni votre Sac à Dos ni votre Arme, et votre tête vous fait très mal. 
Vous ne sauriez dire combien de temps vous êtes resté sans connaissance, mais quoi qu'il en soit, le temps presse, 
et il vous faut au plus vite poursuivre votre route. Vous vous relevez donc aussitôt et vous apercevez votre Sac à Dos 
et votre Arme un peu plus haut sur la pente. Ils ont dû se détacher au cours de votre chute. 
Vous vous hâtez de les récupérer et vous repartez dans la forêt.
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
        st.page_link("pages/page_113.py", label="113", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
