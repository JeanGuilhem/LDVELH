import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=246)

fr_text = """
Lorsque l'embarcation se trouve au beau milieu du lac, l'homme
ramène soudain sa perche et s'avance vers vous en éclatant d'un
rire sinistre. Il rejette alors le capuchon qui lui couvre la tête et
vous vous apercevez qu'il s'agit là d'un terrible Drakkarim. Il va
falloir le combattre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("DRAKKARIM", 15, 23)])

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("tomes/tome1/page_197.py", label="197", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
