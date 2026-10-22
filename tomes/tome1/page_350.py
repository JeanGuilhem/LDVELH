import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, is_new_page, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=350)

fr_text = """
Vous entrez dans la grande Salle du Conseil, une pièce immense
magnifiquement décorée de tentures blanc et or. Le Roi et ses
plus proches conseillers sont en train d'examiner une grande
carte étalée sur une table de marbre, au centre de la salle. Leurs
visages expriment l'inquiétude et la concentration. Lorsque vous
faites le récit de la mort de vos compagnons et des périls que
vous avez dû affronter pour atteindre la citadelle, tout le monde
vous écoute en silence sans jamais vous interrompre. Enfin,
quand vous en avez terminé, le Roi s'approche de vous et prend
votre main droite dans la sienne. « Loup Solitaire, tu as fait
preuve de courage et d'abnégation : ce sont là les qualités d'un
véritable Seigneur Kaï. Ton voyage a été semé de dangers et bien
que tu nous apportes des nouvelles qui nous plongent dans le
chagrin, ta détermination illumine ces heures sombres d'un
rayon d'espoir. Tu as grandement honoré la mémoire de tes
Maîtres et nous t'en portons louange. » Toutes les personnes
rassemblées dans la salle se joignent à cet hommage et vous
expriment leur profonde gratitude. Devant tant d'honneur, vous
ne pouvez vous empêcher de rougir. Le Roi alors lève la main et
tout le monde fait silence. « Tu as fait tout ce que le Royaume du
Sommerlund pouvait attendre d'un de ses fidèles sujets, reprend
le monarque, mais notre patrie a encore grand besoin de toi. Les
Maîtres des Ténèbres ont, en effet, retrouvé leur puissance, et
leur ambition ne connaît plus de bornes. Notre seul espoir de les
repousser se trouve désormais au royaume de Durenor. C'est là
que repose l'instrument de la puissance qui les a vaincus
autrefois. Loup Solitaire, tu es le dernier des Seigneurs Kaï et tu
possèdes la science que t'ont enseignée tes maîtres. Iras-tu à
Durenor pour y chercher le Glaive de Sommer, l'Épée du Soleil ?
Seul ce don des Dieux nous permettra d'écraser l'ennemi et de
sauver le royaume. »
Si vous acceptez de partir en quête du Glaive de Sommer, vous
pourrez le faire en vivant l'aventure que vous propose le
deuxième volume de la série du Loup Solitaire :
La Traversée Infernale
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.balloons()
    st.success(
        "**Mission accomplie !** Vous avez atteint Holmgard et averti le Roi. "
        "Le Loup Solitaire reprendra la route dans le tome 2, *La Traversée Infernale*."
    )
    st.page_link("accueil.py", label="Retour à l'accueil", icon="🏠")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
