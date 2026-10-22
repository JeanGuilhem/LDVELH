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
                current_page_number=91)

fr_text = """
La petite boutique est sombre et humide. Les murs sont couverts
d'étagères, remplies de livres et de bouteilles de toutes les tailles
et de toutes les couleurs. Lorsque vous refermez la porte, un petit
chien noir se met à aboyer et un homme chauve apparaît en
sortant de derrière un grand paravent. L'homme vous souhaite le
bonjour et vous demande poliment s'il peut vous être utile, vous
proposant notamment un choix d'herbes et de potions rangées
dans les cases d'un comptoir de verre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez jeter un coup d'œil à ces produits, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_152.py", label="152", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez décliner son offre et ressortir, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_7.py", label="7", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_198.py", label="198", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
