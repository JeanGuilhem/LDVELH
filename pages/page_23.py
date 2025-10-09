import streamlit as st
from inventory import display_inventory, check_inventory
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=23)

fr_text = """
Le couloir aboutit bientôt à une vaste chambre mortuaire dont
les murs sont gravés de motifs anciens. Dans le coin opposé, un
escalier de pierre mène à une porte immense. De chaque côté des
marches, deux chandelles noires diffusent une faible clarté. Vous
remarquez alors qu'aucune cire ne coule le long des chandelles,
et tandis que vous vous approchez, vous constatez que leurs
flammes ne diffusent aucune chaleur. Soucieux de quitter au plus
vite cet endroit sinistre, vous examinez la serrure de la porte.
Une broche sculptée semble fermer le panneau, mais un trou de
serrure apparaît également.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez retirer la broche,
rendez-vous au"""
        )
    )
    st.write_stream(
            stream_text(
                    f"""Si vous possédez la Discipline Kaï de la
Maîtrise Psychique de la Matière, rendez-vous au"""
            )
    )
    fi_2 = True
    if fi_2:
        if "Maîtrise Psychique de la Matière" in list(st.session_state.kai.to_dict()["Mastery"].values()):
            st.page_link("pages/page_151.py", label="151", icon="📄")
        else:
            st.write_stream(
                    stream_text(
                            fr_unkown_kai
                    )
            )
            st.page_link("pages/page_151.py", label="151", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Enfin, si
vous avez une Clé d'Or, rendez-vous au""")
    )
    if "Clé d'Or" in list(st.session_state.backpack['Nom'].values()):
        fi = True
        if fi:
            st.page_link("pages/page_326.py", label="326", icon="📄")
    else:
        st.write_stream(stream_text("*Vous ne possédez pas cet objet.*"))
        fi = True
        if fi:

            st.page_link("pages/page_326.py", label="326", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

