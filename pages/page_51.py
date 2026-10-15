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
                current_page_number=51)

fr_text = """
Après avoir escaladé en toute hâte la berge boisée de la rivière,
vous apercevez un peu plus loin la palissade en rondins du camp
fortifié dressé autour de la capitale. La bataille fait rage à trois
kilomètres environ et le mur en rondins s'est écroulé en plusieurs
endroits, là où les Maîtres des Ténèbres ont porté leur attaque.
Le camp est presque désert, la plupart des soldats ayant dû le
quitter pour rejoindre le champ de bataille. Une porte est
aménagée dans la palissade.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous en
approcher, rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_288.py", label="288", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez escalader le
mur de rondins, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_221.py", label="221", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
