import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=260)

fr_text = """
En nageant vers la rive, vous apercevez la silhouette du soldat
étendu sur la berge, les bras en croix. Vous vous approchez de
lui, mais il n'y a plus rien à faire : il s'est rompu le cou en
tombant et il est déjà mort. Or tandis que vous êtes agenouillé
auprès de lui, deux Gloks bondissent soudain sur vous et il vous
faut les combattre. Vous n'avez pas d'armes et vous devrez donc
vous battre à mains nues. De ce fait, votre total d'HABILETÉ se
trouvera diminué de 4 points. Vous affronterez les deux Gloks à
tour de rôle.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    # le malus de -4 à mains nues est appliqué par combat() (aucune arme en main)
    outcome = combat([("Premier GLOK", 11, 18), ("Deuxième GLOK", 12, 17)])

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome1/page_156.py", label="156", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
