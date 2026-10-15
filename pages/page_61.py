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
                current_page_number=61)

fr_text = """
Vous atteignez enfin la palissade en rondins du camp fortifié qui
a été dressé autour de la ville. Et tandis que vous courez vers le
poste de garde, vous entendez les soldats pousser des
acclamations enthousiastes : les Dieux en soient loués, ils vous
ont reconnu en dépit de vos vêtements déchirés et de votre triste
apparence ! Votre cape est en lambeaux, votre visage écorché et
taché de sang, et vous êtes couvert de la tête aux pieds de la
poussière du cimetière.

Pataugeant dans un petit ruisseau qu'il vous faut traverser, vous
avancez en titubant vers l'une des entrées du camp. Peu à peu, la
vision que vous venez d'avoir dans le cimetière vous apparaît
dans toute son horreur ; vous êtes épuisé, affaibli, glacé et, juste
avant de perdre connaissance, vous vous laissez tomber dans les
bras tendus de deux soldats accourus à votre rencontre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendezvous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_268.py", label="268", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
