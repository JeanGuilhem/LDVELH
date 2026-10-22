import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=131)

fr_text = """
Vous avez parcouru environ cinq cents mètres lorsque vous
entendez des cris et des bruits semblables au fracas du tonnerre.
En vous approchant, vous apercevez bientôt une clairière que
vous connaissez déjà. C'est là que s'élèvent les ruines de Raumas,
un ancien temple de la forêt. Une troupe de Gloks dont vous
évaluez le nombre à vingt-cinq ou trente sont en train d'attaquer
les ruines qu'ils encerclent. D'autres Gloks, plus nombreux
encore, sont étendus raides morts ou agonisent parmi les
vestiges de marbre du temple.
L'assaut des Gloks survivants ne faiblit pas pour autant et ils
continuent de mener l'attaque contre les ruines. Qui s'y cache ?
Vous l'ignorez. Or, soudain, un éclair jaillit et vient frapper le
premier rang des Gloks. Les monstres revêtus de leurs armures
sont alors projetés en tous sens, trébuchant et roulant sur eux-
mêmes. L'un d'eux, plus grand que les autres et couvert de la tête
aux pieds d'une grosse cotte de mailles noire, lance des jurons à
ses congénères et les incite à repartir à l'attaque en les frappant à
grands coups d'un fouet aux lanières de fer barbelé. Vous
dégainez votre arme et vous vous approchez de la clairière en
restant à l'abri du feuillage. Vous essayez de voir qui défend ainsi
les ruines du temple et, à votre grand étonnement, vous vous
apercevez bientôt que c'est un jeune homme seul, guère plus âgé
que vous, qui tient ainsi tête aux créatures déchaînées. Vous
reconnaissez aussitôt sa toge bleu ciel brodée d'étoiles : c'est un
jeune Théurgiste de la Guilde des Magiciens de Toran, un
apprenti en magie blanche. Cinq Gloks, la lance brandie,
chargent le jeune homme qui bat rapidement en retraite à
l'intérieur des ruines. Vous le voyez alors se tourner et lever la
main gauche : au même instant, un éclair bleu jaillit du bout de
ses doigts et vient frapper les Gloks hurlants. Non loin de
l'endroit où vous êtes caché, un autre Glok contourne les ruines
en courant et grimpe au sommet d'une des colonnes du temple. Il
serre entre ses dents un long poignard à la lame recourbée et
s'apprête à sauter sur le jeune sorcier qui se tient debout juste
au-dessous de lui.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez crier pour avertir le sorcier du danger qui le menace, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_241.py", label="241", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous voulez vous précipiter en avant pour attaquer le Glok au moment où il bondira, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_55.py", label="55", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous préférez ramasser une pierre dans les ruines et la jeter à la tête du Glok, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_302.py", label="302", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous estimez plus judicieux de quitter ce champ de bataille et de poursuivre votre chemin en retournant dans la forêt, rendez-vous au:"""
        )
    )
    fi_3 = True
    if fi_3:
        st.page_link("pages/page_101.py", label="101", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
