import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=128)

fr_text = """
Vous écartez prudemment le feuillage, et une vision d'horreur
s'offre aussitôt à vous : un peu plus loin, dans une petite clairière,
trois Gloks ont attaché un homme à un poteau et sont en train de
mettre le feu à un tas de broussailles disposé à ses pieds. Sa
tunique est celle d'un Garde-Frontière, il appartient au régiment
chargé de surveiller les frontières occidentales du royaume, en
bordure des monts Durncrag. L'homme a reçu une sévère
correction et il est à demi inconscient.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    
    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï de la Chasse, rendez-vous au:"""
        )
    )
    
    # LOGIQUE DISCIPLINE KAÏ DE LA CHASSE
    if has_kai("La Chasse"):
        st.page_link("pages/page_297.py", label="297", icon="📄")
    else:
        st.write_stream(
                stream_text(
                        fr_unkown_kai
                )
        )
        st.page_link("pages/page_297.py", label="297", icon="📄", disabled=True)
    
    st.write_stream(
        stream_text(
            f"""Dans le cas contraire, vous n'avez plus qu'à attaquer les Gloks pour sauver la
vie du soldat. Rendez-vous alors au:"""
        )
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_336.py", label="336", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
