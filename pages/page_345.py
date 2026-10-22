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
                current_page_number=345)

fr_text = """
Vous rabattez sur votre tête le capuchon de votre cape de Seigneur Kaï et vous retenez votre souffle tandis que le Kraan tournoie au-dessus de vous. Quelques minutes plus tard, vous entendez les Gloks pousser des jurons furieux et les battements d'ailes des Kraans s'évanouissent bientôt: ils sont partis vers l'ouest. La promptitude de vos réflexes vous a sauvé d'une capture certaine et d'une mort probable.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Vous pouvez à présent revenir sur le sentier en vous rendant au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_272.py", label="272", icon="📄")

    st.write_stream(
        stream_text(f"""Mais vous pouvez également choisir de poursuivre votre chemin parmi les arbres de la forêt. Rendez-vous pour cela au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_19.py", label="19", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
