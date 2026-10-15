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
                current_page_number=140)

fr_text = """
Vous vous trouvez dans une clairière au centre de laquelle on a
élevé une tour branlante à l'aide de troncs d'arbres grossièrement
taillés. Au pied de la tour, trois sentiers partent dans différentes
directions.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez prendre le sentier qui mène au sud, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_14.py", label="14", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez celui qui mène à l'est, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_252.py", label="252", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si le sentier orienté au sud-ouest vous paraît plus attrayant, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_215.py", label="215", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si l'envie vous prend plutôt de monter dans la tour, rendez-vous au:"""
        )
    )
    fi_3 = True
    if fi_3:
        st.page_link("pages/page_36.py", label="36", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
