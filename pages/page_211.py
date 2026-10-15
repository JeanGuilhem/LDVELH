import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai
from utils import stream_text, set_cookies, called_cookies


if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=211)

fr_text = """
Vous marchez le long d'un couloir plongé dans la pénombre et
vous arrivez bientôt dans une grande pièce carrée. Une porte de
chêne est aménagée dans le mur d'en face.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous diriger vers cette porte, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_173.py", label="173", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du Sixième Sens, rendez-vous au:"""
        )
    )
    if has_kai("Le Sixième Sens"):
        st.page_link("pages/page_244.py", label="244", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("pages/page_244.py", label="244", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            f"""Si, enfin, vous préférez retourner à l'air libre et poursuivre votre route, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_106.py", label="106", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
