
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
                current_page_number=280)

fr_text = """
Alors que vous commencez votre ascension, vous entendez des battements d'ailes qui s'approchent de vous en provenance de l'ouest. Ce sont des Kraans ! D'après le bruit qu'ils font, vous estimez leur nombre à dix au moins, peut-être davantage. Vous maudissez alors votre malchance, car le flanc de la colline n'offre aucun abri, et, si on vous attaque au cours de cette escalade difficile, vous ne pourrez pratiquement pas vous défendre: il est en effet impossible de rester debout sur cette pente escarpée.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si choisissez dégainer rester complètement immobile en espérant que les Kraans ne vous verront pas, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_327.py", label="327", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous hâter de redescendre la colline pour vous mettre à l'abri dans le tunnel, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_170.py", label="170", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
