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
                current_page_number=323)

fr_text = """
Au sommet de la tour, vous pouvez voir loin autour de vous, dans
toutes les directions. Au nord, à bonne distance, une colonne de
fumée d'un noir de jais s'élève haut dans le ciel et de petites
flammes orange dansent à sa base : c'est la ville de Toran qui est
en feu et ce spectacle vous déchire le cœur. En provenance du
sud-ouest, le vent apporte les échos d'une bataille : les combats
se déroulent à une dizaine de kilomètres tout au plus de l'endroit
où vous vous trouvez.
Sur le plancher de la Tour de Guet, une boîte oblongue est posée
dans un coin.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez ouvrir cette boîte, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_290.py", label="290", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez quitter la tour en descendant l'échelle et en
prenant soin de ne poser les pieds que sur les échelons encore
solides, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_140.py", label="140", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
