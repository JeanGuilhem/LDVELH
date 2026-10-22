import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=7)

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
manière. Après avoir bondi et sauté de maison en maison, vous
parvenez au bout d'une rangée de toits et il ne vous reste bientôt
plus qu'une seule rue à franchir pour atteindre la citadelle. Cette
rue, malheureusement, est plus large que les autres et il vous
faudra réussir un bond spectaculaire si vous voulez passer de
l'autre côté. La gorge un peu serrée, le sang battant à vos tempes,
vous prenez donc votre élan en courant sur toute la longueur du
toit, puis vous vous élancez, le regard fixé sur la maison d'en face.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 2:
        st.page_link("tomes/tome1/page_108.py", label="108", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome1/page_25.py", label="25", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
