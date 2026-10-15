import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies, handle_repas, ls_death, table_des_hasards



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=200)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La nuit tombe et les ombres de la forêt s'étirent. Vous vous
apprêtez à faire halte pour vous reposer lorsque vous apercevez à
travers les arbres une foule qui avance sur une large route
orientée au sud. En vous approchant, vous distinguez une
roulotte tirée par six grands chevaux ; le véhicule occupe le
milieu de la chaussée et se déplace à grande vitesse parmi les
piétons et les autres voitures à chevaux. C'est peut-être là votre
chance d'atteindre la capitale plus vite que prévu.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez sauter sur la roulotte, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_78.py", label="78", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du Camouflage, vous pourrez vous
accrocher à la roulotte et vous dissimuler parmi les bagages
attachés sur le toit en vous rendant au:"""
        )
    )
    if has_kai("Le Camouflage"):
        st.page_link("pages/page_168.py", label="168", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_168.py", label="168", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
