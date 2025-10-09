import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=100)

fr_text = """
Le couloir glacial tourne brusquement vers l'est et vous
apercevez au loin une lueur verdâtre qui diffuse une faible clarté.
Vous constatez bientôt que le couloir aboutit à une grande pièce,
et que l'étrange lumière provient d'une sorte de coupe, posée sur
le haut dossier d'un trône de granité. Devant le trône, se trouve
une statue sur son socle. Elle représente un serpent ailé dont le
corps a la forme d'un S.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous asseoir sur ce trône, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_161.py", label="161", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez examiner la statue, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_133.py", label="133", icon="📄")
    
    st.write_stream(
        stream_text(
            f"""Enfin, s'il vous semble plus judicieux de 
chercher une sortie qui vous permettrait de quitter cet endroit,
rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_257.py", label="257", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")