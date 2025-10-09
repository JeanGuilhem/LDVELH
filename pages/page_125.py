import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=125)

fr_text = """
Le chemin mène à une grande clairière. Vous remarquez aussitôt
sur le sol d'étranges empreintes de pattes griffues. De toute
évidence, des Kraans se sont posés ici même. A en juger par le
nombre d'empreintes et la surface qu'elles couvrent, ce sont au
moins cinq de ces répugnantes créatures qui se sont rassemblées
là dans les dernières douze heures. De l'autre côté de la clairière,
deux chemins s'enfoncent dans la forêt. L'un est orienté à l'ouest,
l'autre au sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez emprunter le sentier orienté au sud, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_27.py", label="27", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez prendre celui qui va vers l'ouest, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_214.py", label="214", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au:"""
        )
    )
    
    if "L'Orientation" in list(st.session_state.kai.to_dict()["Mastery"].values()):
        st.page_link("pages/page_301.py", label="301", icon="📄")
    else:
        st.write_stream(
                stream_text(
                        fr_unkown_kai
                )
        )
        st.page_link("pages/page_301.py", label="301", icon="📄", disabled=True)
    
    # SAUVEGARDE DE LA PAGE ACTUELLE POUR LES FUTURS RE-RUNS
    st.session_state.last_page_number = st.session_state.current_page_number


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")