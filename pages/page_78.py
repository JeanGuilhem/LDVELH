import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=1)

fr_text = """
Au moment où la roulotte passe devant vous, vous faites un bond
en avant et vous parvenez à vous y agripper; vous vous retrouvez
sur l'échelon inférieur d'un petit escabeau qui permet d'accéder à
la porte arrière du véhicule. Vous vous redressez avec précaution
en vous efforçant de maintenir votre prise et, soudain, la partie
supérieure de la porte qui vous fait face s'ouvre à la volée. Le
visage furieux d'un garde du corps apparaît alors dans
l'encadrement.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""" Si vous souhaitez lui expliquer que vous êtes un
Seigneur Kaï, porteur d'un message urgent destiné au Roi,
rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_132.py", label="132", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous choisissez de lui offrir de l'Or pour
payer votre voyage jusqu'à la capitale, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_12.py", label="12", icon="📄")

    st.write_stream(
        stream_text(
            f""". Enfin,
si vous décidez d'attaquer le garde avec votre arme, rendez-vous
au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_220.py", label="220", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
