import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from text import fr_unkown_kai
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=18)

fr_text = """
Vous êtes réveillé par l'approche d'une troupe au lointain. Vous
apercevez alors, de l'autre côté du lac, des silhouettes de
Drakkarims vêtus de capes noires et une meute de Loups
Maudits chevauchés par leurs habituels cavaliers. Un Kraan
apparaît bientôt au-dessus des arbres et atterrit sur le toit de la
petite cabane de bois. Il est monté par une créature habillée de
rouge. Un instant plus tard, le Kraan prend à nouveau son vol et
traverse le lac en s'approchant de l'endroit où vous êtes caché.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si
vous souhaitez vous enfoncer plus profondément dans la forêt,
rendez-vous au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_239.py", label="239", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous maîtrisez la Discipline Kaï du
Camouflage, rendez-vous au""")
    )
    fi_1 = True
    if fi_1:
        if has_kai("Le Camouflage"):
            st.page_link("tomes/tome1/page_114.py", label="114", icon="📄")
        else:
            st.write_stream(
                    stream_text(
                            fr_unkown_kai
                    )
            )
            st.page_link("tomes/tome1/page_114.py", label="114", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            f"""Si vous préférez combattre la
créature, rendez-vous au"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_29.py", label="29", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
