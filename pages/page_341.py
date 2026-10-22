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
                current_page_number=341)

fr_text = """
Les soldats ne croient pas votre histoire et refusent de vous laisser entrer. L'homme qui vous escortait disparaît alors dans la foule, et vous vous retrouvez seul dans la ville. Démoralisé par cet échec, vous vous laissez emporter par la foule qui envahit les rues et vous arrivez bientôt devant l'entrée du Temple de la Guilde. Le bâtiment s'élève à l'une des extrémités du Pont de la Guilde qui traverse le fleuve Eledil, près de son embouchure où il se jette dans le golfe de Holm.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez entrer dans le Temple de la Guilde, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_210.py", label="210", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez chercher un autre moyen d'atteindre la citadelle, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_37.py", label="37", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au:"""
        )
    )
    if has_kai("L'Orientation"):
        st.page_link("pages/page_310.py", label="310", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_310.py", label="310", icon="📄", disabled=True)

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
