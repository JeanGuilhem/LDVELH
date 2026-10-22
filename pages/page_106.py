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
                current_page_number=106)

fr_text = """
Vous arrivez un peu plus tard au bord d'un ruisseau aux eaux
glacées, agitées d'un fort courant. Son eau blanche d'écume court
parmi les rocs moussus et disparaît au loin, en direction de l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous désirez longer ce ruisseau vers l'est, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_263.py", label="263", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez en remonter le cours, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_334.py", label="334", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
