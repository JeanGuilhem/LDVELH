import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=283)

fr_text = """
Vous êtes à trois mètres environ de l'étranger lorsque son
corbeau se met à croasser pour l'avertir de votre approche.
L'homme fait aussitôt volte-face et vous vous immobilisez saisi
de terreur : car en fait ce n'est pas un homme que vous avez
devant vous, mais un Vordak, l'un des plus redoutables
lieutenants des Maîtres des Ténèbres. Cette créature appartient
au monde des morts vivants et vous allez devoir la combattre
dans un affrontement sans merci. La surprise de votre attaque
vous permet d'ajouter 2 points à votre total d'HABILETÉ lors du
premier assaut. Dès le deuxième assaut, en revanche, et au cours
des suivants, vous devrez réduire de 2 points ce même total
d'HABILETÉ à moins que vous ne maîtrisiez la Discipline Kaï du
Bouclier Psychique. Le Vordak vous attaque, en effet, en utilisant
simultanément deux armes redoutables : une énorme Masse
d'Armes et sa formidable Puissance Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat(
        [("VORDAK", 17, 25)],
        first_round_modifier=2,
        psychic_attack=True,
        psychic_attack_from_round=2,
    )

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_123.py", label="123", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
