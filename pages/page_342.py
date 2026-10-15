import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=342)

fr_text = """
Tandis que votre voix se répercute en écho parmi les arbres,
l'étranger se tourne lentement vers vous. Votre cœur se met alors
à battre à tout rompre et votre sang se glace, car l'être qui vous
fait face n'est pas un homme : il s'agit d'un Vordak, l'un des plus
redoutables lieutenants des Maîtres des Ténèbres. C'est une
créature de l'Au-Delà, un mort vivant. Le monstre pousse un cri
perçant puis brandit une énorme Masse d'Armes et se rue sur
vous. Paralysé par la terreur, vous sentez également que le
Vordak vous attaque avec toute la force de sa Puissance
Psychique. Si vous ne maîtrisez pas la Discipline Kaï du Bouclier
Psychique, vous devrez réduire de 2 points votre total
d'HABILETÉ au cours de ce combat. Il vous faut affronter cette
créature qui est elle-même invulnérable à votre propre Puissance
Psychique.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("VORDAK", 18, 26)], psychic_attack=True, psychic_immune=True)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_123.py", label="123", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
