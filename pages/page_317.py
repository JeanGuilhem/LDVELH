import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=317)

fr_text = """
Instinctivement, vous plongez de côté et vous atterrissez sur le
sol de pierre. La promptitude de vos réflexes vient de vous sauver
la vie, car au même moment un énorme bloc de granité s'est
écrasé sur les marches de l'escalier, juste devant la porte !
Quelque peu malmené, mais indemne, vous vous relevez et vous
regardez au plafond : un rayon de lumière grise filtre à travers
l'ouverture ménagée par la chute du bloc de pierre et diffuse dans
la pièce une faible clarté. Vous pouvez même apercevoir un coin
de ciel nuageux et quelques ronces enchevêtrées. Vous vous
hissez alors hors du caveau et vous vous dirigez aussi vite que
possible vers la porte située au sud de la nécropole. Au loin, vous
apercevez la palissade en rondins du camp fortifié dressé autour
de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_61.py", label="61", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
