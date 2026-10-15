
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, ls_death, handle_repas, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 185
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Vous plissez les yeux et vous scrutez le feuillage des arbres pour
voir s'il ne s'y cache pas un archer. Votre attente ne dure guère
car, quelques instants plus tard, une douleur fulgurante vous
déchire la poitrine et vous êtes projeté en arrière sous le choc de
trois flèches qui vous transpercent le corps. Deux de ces flèches
se sont enfoncées profondément dans votre thorax et la troisième
s'est plantée dans votre cuisse. Avant de sombrer dans les
ténèbres, vous contemplez dans une ultime vision le feuillage des
arbres qui forme un dôme au-dessus de vous et une libellule qui
vient se poser sur la boucle de votre ceinture. Votre mission
s'achève ici.
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
