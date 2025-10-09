import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies, before_fight, fight

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=34)

fr_text = """
Sans crier gare, une terrifiante apparition fond sur vous. C'est
une créature vêtue de longs vêtements rouges et montée sur le
dos d'un Kraan. Votre assaillant pousse un cri à vous glacer le
sang : il s'agit d'un Vordak, un féroce lieutenant des Maîtres des
Ténèbres. Il est juste au-dessus de vous et il vous faut le
combattre. Le monstre vous attaque à l'aide d'une grosse Massed'Armes et il est également doué d'une redoutable Puissance
Psychique, dont il va faire usage au cours de l'affrontement. Si
vous ne maîtrisez pas la Discipline Kaï du Bouclier Psychique,
vous devrez réduire de 2 points votre total d'HABILETÉ pendant
toute la durée du combat.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.subheader("VORDAK")
    col1, col2 = st.columns(2)
    col1.metric(label="Habilité", value=17)
    col2.metric(label="Endurance", value=25)
    if st.session_state.done_fighting is False:
        if st.button(f"Commencer à combattre"):
            if "Bouclier Psychique," not in list(st.session_state.kai.to_dict()["Mastery"].values()):
                st.write_stream(stream_text("""*Vous ne maitrisez pas le Bouclier Psychique et perdrez en conséquence 2 points
    d'HABILETÉ pendant toute la durée du combat"""))
                ls_hability = before_fight(ls_hability=st.session_state.hability - 2, ennemy_psychique_sensibility=True)
            else:
                ls_hability = before_fight(ls_hability=st.session_state.hability, ennemy_psychique_sensibility=True)

            fight(ls_hability=ls_hability,
                  ls_endurance=st.session_state.endurance,
                  ennemy_hability=17,
                  ennemy_endurance=25,
                  turn_before_flee=0,
                  add_dammage_ennemy=0,
                  add_dammage_LS=0,
                  )

            st.session_state.done_fighting = True

    if st.session_state.done_fighting:

        st.write_stream(
                stream_text(
                        f"""Si vous êtes vainqueur, rendez-vous au"""
                )
        )
        fi_2 = True
        if fi_2:
            st.page_link("pages/page_328.py", label="328", icon="📄")

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

