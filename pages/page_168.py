import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, handle_repas

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=168)

fr_text = """
Vous vous hissez au sommet de la luxueuse roulotte et vous vous
installez au milieu des malles et des valises. La nuit bientôt
tombera sur la grand-route. Un vent frais souffle de l'ouest, qui
vous oblige à bien serrer votre cape autour de vous pour n'avoir
pas trop froid. Au-dessous, à l'intérieur de la roulotte, vous
entendez des gens parler et une délicieuse odeur de viande rôtie
vous monte aux narines. Elle vient vous rappeler que vous avez
très faim et qu'il vous faut prendre un Repas, sinon, vous perdrez
3 points d'ENDURANCE. La fatigue a tôt fait d'avoir raison de
vous et vous finissez par sombrer dans un sommeil agité.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    handle_repas()

    st.write_stream(stream_text("Rendez-vous au :"))
    st.page_link("pages/page_64.py", label="64", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
