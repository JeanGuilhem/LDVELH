import streamlit as st
from inventory import display_inventory, check_inventory, end_page, change_endurance, is_new_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=212)

fr_text = """
Lorsque vous vous réveillez, la douleur n'est plus qu'un mauvais
souvenir et vous récupérez tous les points d'ENDURANCE dont
vous disposiez au départ de votre mission. Un homme de haute
taille, vêtu d'une toge blanche, se tient debout devant vous, une
coupe remplie d'herbes entre les mains. Il verse les herbes dans
l'eau bouillante d'un chaudron puis se tourne vers vous. « Vous
avez vu la mort de près, Seigneur Kaï, mais ce n'est pas encore
aujourd'hui que vous irez rejoindre le troupeau des bienheureux.
Votre corps est entièrement guéri en effet, pourtant, il me semble
que votre âme est blessée. Quelle est donc la raison de votre
tourment ? » Vous reconnaissez en cet homme l'un des grands
médecins du Roi : il porte, en effet, brodée sur sa manche, la
colombe blanche, symbole de sa vocation. Vous racontez alors au
vénérable savant les tristes événements qui vous ont amené
jusqu'ici. Lorsque vous avez terminé votre récit, le vieil homme
vous prend doucement le bras et vous fait lever de votre lit en
vous demandant de le suivre. C'est à cet instant seulement que
vous remarquez la magnificence des lieux : vous vous trouvez en
effet dans une pièce richement décorée à laquelle on accède par
un long couloir aux murs couverts de somptueuses tapisseries.
Vous comprenez alors peu à peu que vous êtes enfin parvenu au
bout de vos peines car cette fastueuse demeure n'est autre que le
Palais du Roi : vous êtes à l'intérieur de la citadelle de Holmgard,
et dans quelques instants vous apparaîtrez devant votre
souverain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        st.session_state.visibility_212_healed = st.session_state.total_endurance - st.session_state.endurance
        change_endurance(st.session_state.visibility_212_healed)
    st.metric(
        label="Endurance",
        value=st.session_state.endurance,
        delta=st.session_state.get("visibility_212_healed", 0),
    )

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("tomes/tome1/page_350.py", label="350", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
