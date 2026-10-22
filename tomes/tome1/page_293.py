import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=293)

fr_text = """
Banedon quitte les ruines du temple en vous adressant un signe
de la main, et vous poursuivez vous-même votre route en vous
enfonçant dans la forêt touffue qui s'étend devant vous. Quelques
centaines de mètres plus loin, vous sentez des regards se poser
sur vous. Des yeux jaunes brillent dans les sous-bois et, soudain,
une flèche noire vous frôle la tête. Ce sont des Gloks qui vous ont
tendu une embuscade, et il vous faut prendre la fuite aussi vite
que possible.
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
        st.page_link("tomes/tome1/page_281.py", label="281", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
