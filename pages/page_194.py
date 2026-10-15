
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
                current_page_number=194)

fr_text = """
Vous courez à toutes jambes en direction du chariot. La panique
s'est répandue parmi la foule, tandis que les Kraan attaquent et
emportent leurs malheureuses victimes dans un ciel obscurci par
leurs immenses ailes noires. Un Kraan, plus grand encore que les
autres, vole au-dessus du chariot et trois Gloks hurlants sautent
de son dos pour atterrir à califourchon sur les chevaux de
l'attelage. Il vous faut combattre les trois créatures ou quitter le
chariot pour aller vous réfugier dans une ferme proche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez combattre les Gloks, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_208.py", label="208", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez courir vous réfugier dans la ferme, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_148.py", label="148", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
