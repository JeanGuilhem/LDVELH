import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, has_item, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=170)

fr_text = """
Le tunnel est sombre et il y fait beaucoup plus froid qu'au-dehors.
Vous avancez prudemment en tâtonnant la paroi et au
bout de trois minutes passées dans une obscurité totale, vous
sentez soudain une odeur répugnante de viande pourrie. Si vous
disposez d'une Torche et d'un Briquet d'Amadou, vous pourrez
vous en servir pour vous éclairer. Soudain, une lourde masse
tombe du plafond du tunnel et atterrit sur votre dos. Sous le
choc, vos jambes fléchissent et vous vous retrouvez à genoux.
C'est un Gluâtre des Profondeurs qui vient de vous attaquer en
essayant de vous étrangler de ses longs tentacules visqueux.

Si vous n'avez pas de Torche pour vous éclairer, vous devrez
réduire de 3 points votre total d'HABILETÉ pendant toute la
durée du combat. Le Gluâtre est insensible aux Disciplines Kaï de
la Puissance Psychique et de la Communication Animale.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("GLUÂTRE DES PROFONDEURS", 17, 7)],
        hability_modifier=0 if has_item("TORCHE") else -3,
        psychic_immune=True,
    )

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_319.py", label="319", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
