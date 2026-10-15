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
                current_page_number=64)

fr_text = """
Vous êtes réveillé par les cris d'un Kraan qui tournoie au-dessus
de la roulotte. Il est tôt et le ciel est clair. A moins de cinq cents
mètres, vous apercevez alors une meute de Loups Maudits qui
s'avancent le long de la route, prêts à attaquer. Il va falloir agir
vite.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f""" Si vous décidez de ramasser vos affaires et de courir vous
cacher à l'abri des arbres, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_188.py", label="188", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez
détacher l'un des chevaux de la roulotte et foncer vers la meute
en espérant pouvoir la traverser et vous enfuir, rendez-vous au """)
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_16.py", label="16", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
