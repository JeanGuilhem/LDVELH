import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies
from text import fr_unkown_kai


st.session_state.current_page_number = 1

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=1)

fr_text = """
Il faut vous hâter, car quelque chose vous dit qu'il serait
imprudent de vous attarder parmi les ruines fumantes du
monastère détruit. Les monstres volants peuvent, en effet,
reparaître à tout moment. Il n'y a d'ailleurs pas de temps à
perdre : vous devez au plus vite prendre la route de Holmgard, la
capitale du Sommerlund, pour aller annoncer au Roi cette
terrible nouvelle : les Guerriers Kaï, l'élite du pays, ont tous été
massacrés, à l'exception de vous-même. Or sans l'autorité et le
savoir des Seigneurs Kaï pour commander l'armée, le royaume
du Sommerlund se trouve à la merci de ses plus anciens
ennemis: les Maîtres des Ténèbres. En retenant vos larmes à
grand-peine, vous dites adieu à vos compagnons morts et vous
faites le serment de les venger. Vous tournez alors le dos aux
ruines et vous descendez avec précaution le sentier escarpé qui
s'ouvre devant vous. Au pied de la colline, le chemin aboutit à
une bifurcation. Là, deux autres sentiers mènent l'un et l'autre à
une grande forêt en empruntant deux directions différentes.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez prendre le sentier de droite, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_85.py", label="85", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez suivre celui de gauche, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_275.py", label="275", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        if has_kai("Le Sixième Sens"):
            st.page_link("pages/page_141.py", label="141", icon="📄")
        else:
            st.write_stream(
                    stream_text(
                            fr_unkown_kai
                    )
            )
            st.page_link("pages/page_141.py", label="141", icon="📄", disabled=True)



with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
