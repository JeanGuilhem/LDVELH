import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=237)

fr_text = """
Déployant pleinement vos talents de Seigneur Kaï en matière de
Camouflage, vous vous enfouissez dans le sol meuble du flanc de
la colline. Puis vous vous couvrez de votre cape et vous disposez
quelques branches d'arbre sur cet abri improvisé pour mieux le
dissimuler aux regards.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.write_stream(stream_text('Personne ne vous découvre.'))
        st.page_link("tomes/tome1/page_265.py", label="265", icon="📄")
    elif number is not None:
        st.write_stream(stream_text("Vous avez encore des progrès à faire dans la Discipline Kaï du Camouflage, car l'un de vos ennemis a tôt fait de vous trouver et de vous attaquer. Rendez-vous au 72 pour voir à qui vous avez affaire."))
        st.page_link("tomes/tome1/page_72.py", label="72", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
