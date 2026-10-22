import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=112)

fr_text = """
Soudain, le gros rocher derrière lequel vous vous êtes caché roule
sur lui-même, poussé par deux Gloks hurlants qui vous font face
et qui ont visiblement l'intention de vous tuer. L'entrée de la
grotte est étroite, et vous ne pouvez combattre qu'un Glok à la
fois. Vous devrez donc les affronter à tour de rôle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("Premier GLOK", 13, 10), ("Deuxième GLOK", 12, 10)])

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur. Vous pouvez explorer la grotte plus avant en vous rendant au :"))
        st.page_link("tomes/tome1/page_33.py", label="33", icon="📄")
        st.write_stream(stream_text("Mais vous pouvez également quitter les lieux et descendre le flanc de la colline ; rendez-vous pour cela au :"))
        st.page_link("tomes/tome1/page_248.py", label="248", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
