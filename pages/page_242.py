import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

current_page_number = 242
check_inventory(is_fighting=False,
                current_page_number=current_page_number)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le couvercle du sarcophage glisse à terre avec un bruit sourd.
Vous contemplez alors les restes d'un ancien roi qui repose parmi
ses richesses. Une couronne ciselée coiffe son crâne et les
mâchoires grandes ouvertes de son squelette ressemblent à
l'orifice d'un puits sans fond. Un lointain grondement s'élève
bientôt des profondeurs de la terre.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du Bouclier Psychique, rendez-vous au:"""
        )
    )
    if has_kai("Le Bouclier Psychique"):
        st.page_link("pages/page_166.py", label="166", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_166.py", label="166", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Dans le cas contraire, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_9.py", label="9", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
