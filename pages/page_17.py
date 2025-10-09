import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, table_des_hasards, fight, before_fight



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=17)

fr_text = """
Vous levez votre arme pour frapper la créature, dont la gueule
hérissée de crocs tranchants comme des rasoirs vient de se
refermer d'un claquement sec à quelques centimètres de votre
tête. Gêné par le battement de ses ailes, vous avez du mal à vous
tenir debout. 
Réduisez d'un point votre total d'HABILETÉ, et
combattez ce Kraan.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

if "done_fighting" not in st.session_state:
    st.session_state.done_fighting = False

with tab1:
    st.write(fr_text)

    st.subheader("KRAAN")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=16)
    col2.metric(label="Endurance", value=24)
    if st.session_state.done_fighting is False:
        if st.button(f"Commencer à combattre"):
            ls_hability = before_fight(ls_hability=st.session_state.hability - 1, ennemy_psychique_sensibility=True)
            fight(ls_hability=ls_hability,
                ls_endurance=st.session_state.endurance,
                ennemy_hability=16,
                ennemy_endurance=24,
                turn_before_flee=0,
                add_dammage_ennemy=0,
                add_dammage_LS=0,
                  )

            st.session_state.done_fighting = True

    if st.session_state.done_fighting:
        st.write_stream(
            stream_text(
                f"""Hâtez-vous de
    descendre le flanc opposé de la colline afin d'éviter les Gloks."""
            )
        )
        if st.button(label="Utilisez la Table de Hasard pour obtenir un chiffre."):
            st.session_state.number = table_des_hasards()
            st.write_stream(stream_text(f"*Vous avez tiré le {st.session_state.number}*"))
            if st.session_state.number == 10:
                st.write_stream(
                        stream_text(f"""Rendez-vous au:""")
                )
                fi = True
                if fi:
                    st.page_link("pages/page_53.py", label="53", icon="📄")
            elif st.session_state.number in [1,2]:
                st.write_stream(
                        stream_text(f"""Rendez-vous au:""")
                )
                fi_1 = True
                if fi_1:
                    st.page_link("pages/page_274.py", label="274", icon="📄")
            else:
                st.write_stream(
                    stream_text(
                        f"""Rendez-vous au:"""
                    )
                )
                fi_2 = True
                if fi_2:
                    st.page_link("pages/page_331.py", label="331", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

