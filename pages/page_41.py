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
                current_page_number=41)

fr_text = """
Trois soldats galopent le long de la rive, suivis de près par les
Gloks montés sur des Loups Maudits qui poussent des
grognements agressifs. La rive est surélevée et, bientôt, le chef
des Gloks vous aperçoit au fond du canoë. Il ordonne alors à cinq
de ses congénères de vous tirer dessus à l'aide de leurs arcs. Un
instant plus tard, une pluie de flèches noires s'abat sur vous.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""". Si
vous voulez essayer de vous enfuir en pagayant le plus vite
possible le long de la rivière, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_174.py", label="174", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous
préférez gagner la rive opposée et tenter de vous cacher à l'abri
des arbres, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_116.py", label="116", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

