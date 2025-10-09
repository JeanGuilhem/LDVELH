import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=134)

fr_text = """
Vos talents de Seigneur Kaï vous permettent de déceler des
traces de Gloks tout autour de la clairière. Les empreintes sont
fraîches, et il ne fait aucun doute que ces cruels serviteurs des
Maîtres des Ténèbres se trouvaient là il y a moins de deux
heures.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous décidez d'inspecter les maisons, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_305.py", label="305", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez éviter cette clairière, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_40.py", label="40", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number