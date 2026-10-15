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
                current_page_number=159)

fr_text = """
Le marchand refuse votre offre : il ne vous laissera pas monter
dans la roulotte. Et, soudain, il claque des doigts à l'adresse d'un
de ses gardes du corps qui empoigne aussitôt le pommeau de son
arme.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez le combattre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_191.py", label="191", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez sauter de la roulotte, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_234.py", label="234", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
