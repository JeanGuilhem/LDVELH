import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

st.session_state.current_page_number = 147
check_inventory(is_fighting=False,
                current_page_number=147)

fr_text = """
Après avoir marché pendant quelques minutes, vous passez
devant une petite hutte couverte de mousse qui a été bâtie à
l'écart du chemin. Vous avez faim et il vous faut prendre un
Repas, sinon, vous perdez 3 points d'ENDURANCE. Vous
constatez bientôt que le chemin tourne vers l'est.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    handle_repas()

    st.write_stream(
        stream_text(
            f"""Si vous voulez continuer à le suivre, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_42.py", label="42", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez revenir sur vos pas, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_28.py", label="28", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
