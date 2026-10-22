import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=115)

fr_text = """
Vous entrez d'un pas chancelant dans la première maison et vous
vous écroulez sur le sol, complètement épuisé. Vous sentez alors
une odeur de viande cuite et vous apercevez une marmite
suspendue au-dessus des braises d'un feu mourant. Une grande
table de chêne est dressée au centre de la pièce : de toute
évidence, le ou les habitants de cette maison l'ont quittée en
toute hâte le matin même. Au milieu de la table sont posées une
cruche d'eau et une miche de pain.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez prendre rapidement un Repas, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_150.py", label="150", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous souhaitez inspecter la maison, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_177.py", label="177", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez quitter les lieux dès maintenant et reprendre votre course, rendez-vous au:""")
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_83.py", label="83", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
