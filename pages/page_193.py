
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=193)

fr_text = """
La bête sauvage et son cavalier sont étendus raides morts à vos pieds.
Vous remarquez alors un rouleau de Parchemin glissé dans la ceinture du Glok.
Les autres Loups Maudits se précipitent dans votre direction, le long du sentier.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez prendre le Parchemin et le noter sur votre Feuille d'Aventure dans la case Objets Spéciaux."))
    pickup_button("PARCHEMIN", key="scroll", label="Prendre le Parchemin")

    st.write_stream(
        stream_text(
            f"""Si vous souhaitez les combattre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_253.py", label="253", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez vous enfuir dans la forêt, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_126.py", label="126", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
