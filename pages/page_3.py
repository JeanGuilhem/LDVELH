import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies

fr_text = """
Vous emboîtez le pas à l'officier qui franchit une porte en arcade,
puis monte quelques marches menant à un grand hall. Des
soldats courent en tous sens, porteurs de parchemins ornés qu'ils
doivent remettre à des officiers postés le long des murs de la
ville. Un homme au visage couturé de cicatrices, l'air hagard,
s'approche de vous et vous offre de le suivre jusqu'à la citadelle.
Il porte la toge blanche et pourpre en usage à la cour du Roi.
"""

if "weapon_mastery" not in st.session_state:
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=3)


tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez suivre cet homme, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_196.py", label="196", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous
préférez décliner son offre et retourner dans les rues populeuses,
rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_144.py", label="144", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
