import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=201)

fr_text = """
Vous suivez le sentier pendant une heure environ, puis vous
découvrez un autre chemin plus large qui part en direction du
sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez suivre ce chemin orienté au sud, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_238.py", label="238", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous souhaitez aller à l'est, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_215.py", label="215", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous préférez aller vers l'ouest, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_130.py", label="130", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
