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
                current_page_number=30)

fr_text = """
Tous ces gens semblent fatigués et affamés. Ils ont parcouru des
dizaines de kilomètres pour fuir leur ville incendiée. Soudain,
vous entendez en direction du nord de forts battements d'ailes. «
Des Kraans ! Cachez-vous ! » hurlent des voix tout au long du
chemin. En face de vous, un chariot transportant des enfants
casse un essieu : l'une des roues s'est coincée dans une ornière
profonde. Les enfants, saisis de panique, se mettent à hurler.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si
vous souhaitez aider ces enfants, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_194.py", label="194", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous
préférez vous mettre à l'abri des arbres, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_261.py", label="261", icon="📄")

    show_illustrations()



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
