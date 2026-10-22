import streamlit as st
from combat import combat
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=43)

fr_text = """
Un énorme ours noir apparaît derrière le rocher et s'avance
lentement vers vous, la gueule ouverte. Vous remarquez aussitôt
qu'il a l'air d'avoir mal et que sa douleur le rend furieux. Il est
gravement blessé, en effet, et du sang coule sur son cou et dans
son dos. Il vous faut le combattre.

Au bout du troisième assaut, vous avez réussi à vous placer de telle sorte
qu'il vous est possible de vous enfuir en courant au bas de la
colline.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    outcome = combat([("OURS NOIR", 16, 10)], flee_after=3)

    if outcome == "win":
        st.write_stream(stream_text("Vous êtes vainqueur, rendez-vous au :"))
        st.page_link("pages/page_195.py", label="195", icon="📄")
    elif outcome == "fled":
        st.write_stream(stream_text("Vous vous échappez en courant au bas de la colline, rendez-vous au :"))
        st.page_link("pages/page_106.py", label="106", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
