
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
                current_page_number=311)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le flanc de la colline est escarpé et le sol, meuble et glissant.
Vous jetez un coup d'œil par-dessus votre épaule et vous
apercevez deux Gloks qui surgissent de la forêt. Ils entreprennent
aussitôt d'escalader la colline pour tenter de vous rattraper.
Arrivé à mi-chemin, vous repérez une grotte à votre droite.
L'entrée en est presque entièrement cachée par un glissement de
terrain qui a formé comme un mur de rocailles.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous cacher dans cette grotte, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_279.py", label="279", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez continuer à grimper le flanc de la colline, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_47.py", label="47", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Camouflage, rendez-vous au:"""
        )
    )
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome1/page_324.py", label="324", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome1/page_324.py", label="324", icon="📄", disabled=True)

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
