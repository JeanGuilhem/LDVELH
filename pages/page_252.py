
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
                current_page_number=252)

fr_text = """
Au milieu d'une clairière, trois hommes, une femme et deux enfants parlent avec vivacité en faisant de grands gestes. Ils portent en bandoulière des sacs remplis d'objets et de vêtements. Leurs habits semblent de bonne coupe, mais ils sont sales et déchirés.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous approcher d'eux et leur demander qui ils sont, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_155.py", label="155", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez les éviter et poursuivre votre route, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_70.py", label="70", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
