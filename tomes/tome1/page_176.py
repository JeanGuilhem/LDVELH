
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
                current_page_number=176)

fr_text = """
Vous vous cachez derrière d'épais buissons en espérant que le Loup Maudit et son cavalier ne verront pas votre cheval blanc. Par chance, votre ruse réussit et les malfaisantes créatures passent devant vous sans vous remarquer, puis s'éloignent le long du sentier que vous venez de quitter.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez attaquer les autres Loups Maudits et leurs cavaliers, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_253.py", label="253", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez poursuivre votre chemin en vous enfonçant plus avant dans la forêt, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_126.py", label="126", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
