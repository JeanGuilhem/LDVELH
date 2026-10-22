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
                current_page_number=39)

fr_text = """
Quelques secondes plus tard, deux petites têtes au pelage ras et à
la mine inquiète apparaissent derrière le tronc : ce sont des
Kakarmis qui se sont cachés là. Ils vous avertissent que les
Kraans sont partout et qu'ils ont attaqué leur village, un peu plus
loin à l'ouest, ne laissant que ruines sur leur passage. Les
Kakarmis essaient de retrouver le reste de leur tribu qui s'est
enfuie dans la forêt lorsque les Ailes Noires ont lancé leur assaut
sur le village. Les petites créatures apeurées vous montrent la
direction de l'est : le chemin semble aboutir à un cul-de-sac, mais
d'après elles, si vous vous enfoncez dans les sous-bois, vous
trouverez quelques mètres plus loin une tour de guet où le
sentier se divise en trois voies. En continuant alors vers l'est,
vous arriverez bientôt à la Route du Roi qui relie Holmgard, la
capitale, au port de Toran. Vous remerciez les Kakarmis et vous
prenez congé d'eux. 
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous ensuite au"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_228.py", label="228", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
