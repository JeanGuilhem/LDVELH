import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=126)

fr_text = """
Vous chevauchez de plus en plus loin dans la forêt et, dans votre
for intérieur, vous remerciez le Prince de vous avoir donné un si
bon cheval, car bien que le sol soit entièrement recouvert d'un
enchevêtrement de buissons et de racines, l'étalon blanc n'a
jamais fait le moindre faux pas. Bientôt les Loups Maudits sont
loin derrière vous et vous arrêtez votre cheval. La lumière
commence à décliner, il fait presque nuit, à présent.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez poursuivre votre chemin dans la même direction, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_46.py", label="46", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez aller à gauche (dans une direction parallèle au chemin que vous avez laissé loin derrière), rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_143.py", label="143", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
