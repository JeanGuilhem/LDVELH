import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=235)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
Le cheval du Prince est un magnifique animal, rapide et au pied
sûr. Il galope le long du sentier sinueux comme s'il s'agissait
d'une route large et droite et, bientôt, les échos de la bataille se
dissipent derrière vous. Vous avez faim, et il vous faut prendre
un Repas tandis que vous chevauchez l'étalon blanc, sinon, vous
perdrez 3 points d'ENDURANCE. Quelques kilomètres plus loin,
le sentier aboutit à un croisement en forme de T. Il y a là un
panneau indicateur, mais il est illisible.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    handle_repas()

    st.write_stream(
        stream_text(f"""Si vous voulez prendre à gauche, rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_32.py", label="32", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez tourner à droite, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_146.py", label="146", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au:"""
        )
    )
    if has_kai("L'Orientation"):
        st.page_link("pages/page_254.py", label="254", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_254.py", label="254", icon="📄", disabled=True)

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
