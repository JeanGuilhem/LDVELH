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
                current_page_number=322)

fr_text = """
Au bout de ce qui vous semble une éternité, vous parvenez enfin
au sommet de la colline escarpée. Derrière vous, les ruines du
monastère sont encore visibles. Au nord, une colonne de fumée
d'un noir de jais s'élève haut dans le ciel et de petites flammes
orange dansent à sa base : c'est le port de Toran qui est en feu, et
ce spectacle vous déchire le cœur. Soudain, un cri perçant au-
dessus de votre tête vous avertit qu'un Kraan se prépare à vous
attaquer. Il est à une trentaine de mètres de distance et il fond
sur vous, prêt à tuer.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez l'attendre pour le combattre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_17.py", label="17", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez prendre la fuite en vous précipitant au bas de la colline, sur le flanc opposé, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_89.py", label="89", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
