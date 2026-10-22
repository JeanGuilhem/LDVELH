import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

current_page_number = 132
check_inventory(is_fighting=False,
                current_page_number=current_page_number)

fr_text = """
Le garde du corps vous observe d'un regard soupçonneux et vous
claque la porte au nez. Vous entendez parler à l'intérieur de la
roulotte puis, soudain, la porte s'ouvre à nouveau et le visage
d'un marchand prospère apparaît. Il reconnaît aussitôt votre
cape de Seigneur Kaï et vous demande de bien vouloir excuser la
conduite de son serviteur. Il vous fait entrer dans la roulotte et
vous raconte qu'il a été attaqué plusieurs fois depuis qu'il a quitté
le port de Toran, notamment par des Kraans et par des brigands.
Son garde du corps a tout de suite pensé que vous pouviez être
un bandit, ce qui explique son comportement. La roulotte est
remplie de soieries et d'épices. Le marchand vous propose
quelque chose à manger et vous acceptez avec gratitude. Après
avoir fait un somptueux repas, la fatigue accumulée au cours de
vos épreuves a raison de vous et vous sombrez dans un sommeil
profond.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if st.session_state.last_page_number != st.session_state.current_page_number:
        handle_repas()

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_64.py", label="64", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
