import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=254)

fr_text = """
Votre Sens Kaï de l'Orientation vous permet de distinguer
plusieurs séries de traces qui partent du chemin de droite en
direction du chemin de gauche. Ces traces ont été laissées par des
Loups de grande taille. Ces animaux sont utilisés comme
éclaireurs par les armées des Maîtres des Ténèbres. Ce sont des
créatures malfaisantes et cruelles, souvent chevauchées par des
Gloks. Le chemin de gauche mène vers Holmgard, celui de droite
vers les monts Durncrag.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text("Quelle direction souhaitez-vous prendre ? Si vous voulez tourner à gauche, rendez-vous au :")
    )
    st.page_link("pages/page_32.py", label="32", icon="📄")

    st.write_stream(stream_text("Si vous préférez aller à droite, rendez-vous au :"))
    st.page_link("pages/page_146.py", label="146", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
