import streamlit as st
from inventory import display_inventory, check_inventory, end_page, choose_item_to_lose
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=277)

fr_text = """
Lorsque vous reprenez conscience, vous êtes étendu au pied
d'une pente raide, parmi les hautes herbes. Vous n'apercevez ni
votre Arme ni votre Sac à Dos, et votre tête vous fait atrocement
souffrir. Vous êtes incapable de dire combien de temps vous êtes
resté sans connaissance, mais il est clair qu'il vous faut repartir
sans plus attendre. Vous vous relevez donc aussitôt et vous
retrouvez votre Sac à Dos intact. Votre Arme, en revanche, est
brisée et ne peut plus vous être d'aucune utilité. Rayez-la de
votre Feuille d'Aventure (si vous possédez plus d'une arme, seule
l'une d'elles est cassée et vous pouvez choisir laquelle). Une fois
votre Feuille d'Aventure modifiée, vous ramassez votre Sac à Dos
ainsi que l'Arme qui vous reste éventuellement et vous
poursuivez votre chemin dans la forêt qui s'étend devant vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if choose_item_to_lose(
        list(st.session_state.weapons), key="broken_weapon", label="Quelle arme est brisée ?"
    ):
        st.write_stream(stream_text("Rendez-vous au :"))
        st.page_link("pages/page_113.py", label="113", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
