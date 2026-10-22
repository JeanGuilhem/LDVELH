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
                current_page_number=129)

fr_text = """
Vous parvenez devant la porte principale de la ville et vous
contemplez avec révérence les murs gigantesques qui se dressent
devant vous. Hautes de soixante mètres, les murailles de
Holmgard ont résisté tout à la fois au Temps et aux Maîtres des
Ténèbres. L'officier et vous-même parcourez au pas de course le
tunnel d'une centaine de mètres de long qui traverse le poste
fortifié et vous arrivez enfin devant l'entrée de la grande Tour de
Guet. Des civils et des soldats en grand nombre courent en tous
sens, chacun s'activant à sa tâche.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez continuer à suivre l'officier, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_3.py", label="3", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous pensez que vous arriverez plus vite à la citadelle qui abrite le Palais du Roi en vous débrouillant tout seul, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_144.py", label="144", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
