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
                current_page_number=259)

fr_text = """
La pièce devient de plus en plus froide. Peu à peu, vous sentez
une odeur de soufre puis, bientôt, les échos d'un chant vous
parviennent : il y a quelqu'un d'autre dans ces souterrains.
Soudain, une brèche s'ouvre dans le mur et l'extrémité d'un
bâton noir apparaît. Un éclair bleu jaillit alors de ce bâton et
vient vous frapper en pleine poitrine. Vos forces lentement vous
quittent tandis que la silhouette d'un vieil homme vêtu d'une
ample toge noire se dessine devant vous, dans une sorte de
brouillard. L'homme lève un poignard et s'apprête à vous égorger
: c'est la dernière vision que vous emporterez de ce monde. Votre
mission s'achève ici, en même temps que votre vie.
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
