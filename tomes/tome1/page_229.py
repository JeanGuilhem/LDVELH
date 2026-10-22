import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=229)

fr_text = """
Le Kraan vole au-dessus de votre tête en soulevant des nuages de
poussière par le seul battement de ses ailes immenses. Bientôt,
vous avez le nez et les yeux pleins de poussière et vous vous
mettez à tousser et à cligner les paupières. Puis, soudain, le
monstre vous attaque. Vous allez devoir le combattre jusqu'à la
mort de l'un de vous deux, mais en raison de la poussière qui
vous désavantage, il vous faut réduire de 1 point votre total
d'HABILETÉ pendant toute la durée de l'affrontement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("KRAAN", 16, 25)], hability_modifier=-1)

    if outcome == "win":
        st.write_stream(stream_text("Vous pouvez vérifier si la créature ne transportait pas quelque objet qui pourrait mériter votre intérêt. Rendez-vous alors au :"))
        st.page_link("tomes/tome1/page_267.py", label="267", icon="📄")
        st.write_stream(stream_text("Ou poursuivre votre chemin le long du sentier orienté à l'est. Rendez-vous pour cela au :"))
        st.page_link("tomes/tome1/page_125.py", label="125", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
