import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=343)

fr_text = """
Vous êtes prisonnier des branches et des racines, mais vous
parvenez finalement à dégager votre main droite, à empoigner
votre Hache et à vous tailler un chemin à travers l'épaisse
végétation. Un peu plus loin, la forêt s'éclaircit et vous avancez
dans cette direction. Votre cape est déchirée en plusieurs
endroits et votre bras gauche écorché au-dessus du coude.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if st.session_state.last_page_number != st.session_state.current_page_number:
    st.session_state.endurance -= 2
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)


tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Vous perdez 2 points d'ENDURANCE avant de vous rendre au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_213.py", label="213", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
