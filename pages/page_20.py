import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory
from utils import stream_text, set_cookies, called_cookies, change_visiblity

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=20)

fr_text = """
Il semble que le ou les occupants de la péniche soient partis en
toute hâte il y a peu de temps. Les restes d'un repas à moitié
mangé traînent sur la table ainsi qu'une tasse de Jala encore
chaud. En fouillant un coffre et un petit placard, vous trouvez un
Sac à Dos, de la Nourriture (l'équivalent de 2 Repas) et un
Poignard.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])
visibility_1, visibility_2, visibility_3 = False, False, False

if len(st.session_state.backpack["Nom"]) >= 8:
    visibility_1, visibility_2 = True, True
if st.session_state.weapon1 and st.session_state.weapon2:
    visibility_3 = True


with tab1:
    st.write(fr_text)

    if st.checkbox(label="Repas", key="1", disabled=visibility_1, on_change=change_visiblity, args=(visibility_1,)):
        add_to_inventory(name="Repas")
    if st.checkbox(label="Repas", key="2", disabled=visibility_2, on_change=change_visiblity, args=(visibility_2,)):
        add_to_inventory(name="Repas")
    if st.checkbox(label="Poignard", disabled=visibility_3, on_change=change_visiblity, args=(visibility_3)):
        add_to_inventory(name="POIGNARD")

    st.write_stream(
        stream_text(
            f"""Si vous souhaitez prendre le sentier de droite, rendez-vous au:"""
        )
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_272.py", label="272", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

