
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
                current_page_number=249)

fr_text = """
Vous descendez une volée de marches qui mène à une vaste
crypte où vous attend un spectacle peu réjouissant. L'étrange
lumière verte est, en effet, produite par deux rangées de crânes
dont chacun repose sur un socle de pierre. Ces crânes se font face
de part et d'autre de la pièce, formant ainsi une allée macabre.
De l'autre côté de la crypte, dans le mur du fond, une arcade
sculptée ouvre sur un couloir qui s'enfonce dans les ténèbres.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez traverser la pièce pour aller explorer le couloir, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_169.py", label="169", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez attaquer ces crânes, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_107.py", label="107", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
