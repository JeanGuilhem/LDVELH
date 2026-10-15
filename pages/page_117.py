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
                current_page_number=117)

fr_text = """
L'homme est grièvement blessé, et sa mort est proche. Si vous
maîtrisez la Discipline Kaï de la Guérison, vous pouvez soulager
quelque peu la douleur de ses plaies, mais il est si mal en point
que vos seuls talents ne suffiront pas à le tirer d'affaire. Bientôt,
l'homme perd à nouveau connaissance. Vous essayez alors de
l'installer aussi confortablement que possible en l'allongeant
sous un grand chêne, puis vous repartez en direction du nord-est
en vous frayant un chemin dans la forêt touffue.
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
        st.page_link("pages/page_330.py", label="330", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
