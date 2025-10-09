
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

current_page_number = 148
check_inventory(is_fighting=False,
                current_page_number=current_page_number)

fr_text = """
Vous ouvrez la porte d'un coup de pied et vous vous ruez à
l'intérieur de la ferme. Un Kraan s'élève dans les airs en poussant
un cri de victoire : il tient une victime dans ses serres pointues.
Vous reprenez votre équilibre et vous jetez un coup d'œil autour
de vous : l'endroit est désert. En vous approchant de la cheminée,
vous trouvez un Marteau de Guerre posé contre le mur.
"""

if "visibility_1" not in st.session_state:
    st.session_state.visibility_1 = False

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez le prendre si vous le désirez."))
    if st.button(label="Marteau de Guerre", key="marteau_de_guerre", disabled=st.session_state.visibility_1):
        st.session_state.visibility_1 = True
        add_to_inventory(name="MARTEAU DE GUERRE")

    st.write_stream(
        stream_text(
            f"""Si vous souhaitez rester dans cette ferme, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_81.py", label="81", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous pensez que vous serez plus en sécurité dans la forêt, vous pouvez courir vous y réfugier en vous rendant au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_320.py", label="320", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous souhaitez inspecter plus avant la pièce dans laquelle vous vous trouvez, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_240.py", label="240", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number
