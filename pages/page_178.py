
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=178)

fr_text = """
Votre Sixième Sens vous permet de reconnaître à distance les bottes et les guêtres d'un soldat de l'armée royale. Vous sentez également que cet homme est blessé et qu'il a besoin d'aide.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez lui porter secours, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_88.py", label="88", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez l'abandonner à son sort et poursuivre votre chemin, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_264.py", label="264", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
