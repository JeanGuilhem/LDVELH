import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=7)

fr_text = """
Pendant un moment qui vous semble une éternité, le flot de la
foule vous entraîne comme une feuille au fil du courant. Vous
essayez désespérément de rester debout, mais vos épreuves vous
ont affaibli, vous avez le vertige et vos jambes sont lourdes
comme du plomb.
Soudain, vous apercevez un escalier de pierre, long et étroit, qui
mène sur le toit d'une auberge. Rassemblant vos dernières
forces, vous vous frayez un chemin jusqu'à ces marches que vous
grimpez péniblement. Parvenu au sommet, vous contemplez
alors une vue magnifique : les toits et les tours de Holmgard
s'étendent sous vos yeux et les hauts murs de pierre de la
citadelle resplendissent au soleil. Les maisons et tous les
bâtiments de la capitale ont été construits très près les uns des
autres et il est tout à fait possible de sauter de toit en toit.
Autrefois, les habitants de Holmgard empruntaient volontiers ce
« Chemin des Toits » (comme on l'appelle ici) lorsque de trop
fortes pluies rendaient impraticables certaines rues non pavées.
Mais les accidents ont été si nombreux qu'il est désormais
interdit, par décret du Roi, de se déplacer ainsi. Dans votre cas,
cependant, seul le Chemin des Toits peut vous mener jusqu'au
souverain, et vous décidez donc de vous rendre au palais de cette
manière. Après avoir bondi et sauté de maison en maison, vousparvenez au bout d'une rangée de toits et il ne vous reste bientôt
plus qu'une seule rue à franchir pour atteindre la citadelle. Cette
rue, malheureusement, est plus large que les autres et il vous
faudra réussir un bond spectaculaire si vous voulez passer de
l'autre côté. La gorge un peu serrée, le sang battant à vos tempes,
vous prenez donc votre élan en courant sur toute la longueur du
toit, puis vous vous élancez, le regard fixé sur la maison d'en face.
Utilisez la Table de Hasard pour obtenir un chiffre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    if st.button(label="Utilisez la Table de Hasard pour obtenir un chiffre."):
        st.session_state.number = table_des_hasards()
        if st.session_state.number in [1, 2, 3]:
            st.write_stream(
                    stream_text(
                            f"""Rendez-vous au"""
                    )
            )
            fi = True
            if fi:
                st.page_link("pages/page_108.py", label="108", icon="📄")

        else:
            st.write_stream(
                    stream_text(f"""Rendez-vous au:""")
            )
            fi_1 = True
            if fi_1:
                st.page_link("pages/page_25.py", label="25", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

