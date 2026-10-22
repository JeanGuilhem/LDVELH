import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 216

check_inventory(is_fighting=False,
                current_page_number=st.session_state.current_page_number)

fr_text = """
Vous posez une main sur son front et l'autre sur la plaie de son
bras. Vous sentez alors la chaleur de votre Pouvoir de Guérison
quitter votre corps et se répandre dans celui de l'homme blessé.
Des forces lui reviennent ; il parle et vous dit s'appeler Trimis.
C'est un soldat de l'armée du Prince Pellagayo. Le Prince et sa
troupe ont engagé une bataille un peu plus loin au sud, sur le
pont d'Alema, qu'une meute de créatures au service des Maîtres
des Ténèbres a attaqué le matin même. Le soldat vous raconte
que, au cours des combats, il a été emporté dans les airs par un
Kraan qui l'a ensuite laissé tomber dans la forêt où vous venez de
le trouver. Vous installez le blessé aussi confortablement que
possible et vous poursuivez votre chemin.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if st.session_state.last_page_number != st.session_state.current_page_number:
    # Le texte indique que la guérison a eu lieu, donc on applique la perte d'ENDURANCE.
    # Dans le jeu, la guérison coûte 3 points d'ENDURANCE.
    st.session_state.endurance -= 3
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)


tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_264.py", label="264", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
