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
                current_page_number=287)

fr_text = """
Le sentier disparaît bientôt dans un enchevêtrement de ronces et
de branches basses.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez retourner à la bifurcation et prendre la direction de l'est, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_13.py", label="13", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous frayer un chemin dans les épaisses broussailles en poursuivant dans la même direction, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_330.py", label="330", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
