import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=169)

fr_text = """
Lorsque vous passez devant les crânes, chacun d'eux pivote
lentement sur lui-même comme pour suivre le moindre de vos
mouvements. Vous vous trouvez à présent au milieu de cette
chambre mortuaire et, soudain, vous entendez un bruit d'os qui
se brise. Des formes monstrueuses éclosent alors des crânes en
déployant des ailes semblables à celles des chauves-souris. Dix
de ces créatures à la peau gluante vous attaquent aussitôt, et il
vous faut les combattre en les considérant comme un seul et
même adversaire.

Après avoir livré le premier assaut (obligatoire), vous aurez le
droit de prendre la fuite en courant dans le couloir.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("MONSTRES DES CRYPTES", 16, 16)], flee_after=1)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome1/page_137.py", label="137", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous prenez la fuite en courant dans le couloir, rendez-vous au :"))
        st.page_link("tomes/tome1/page_23.py", label="23", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
