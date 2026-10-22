
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 248
check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Vous parvenez au pied de la colline et vous vous hâtez de courir
dans la forêt. Quelques minutes plus tard, vous découvrez un
ancien sentier forestier qui forme ici une courbe à angle droit.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez suivre ce sentier en direction du nord, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_44.py", label="44", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez le suivre en direction de l'est, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_300.py", label="300", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
