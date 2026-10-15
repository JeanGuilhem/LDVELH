import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button
from utils import stream_text, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=243)

fr_text = """
En courant dans la forêt, vous trébuchez bientôt contre une
racine et vous dévalez une pente escarpée en roulant sur vous-
même. Vous atterrissez sur un petit chemin caché sous les arbres
et vous y découvrez un cadavre étendu parmi les broussailles.
C'est celui d'un Glok, une de ces créatures monstrueuses et
répugnantes que les Maîtres des Ténèbres emploient à leurs
services. Il y a bien longtemps, les ancêtres des Gloks servaient
d'esclaves aux Maîtres des Ténèbres et ceux-ci leur firent bâtir la
ville infernale d'Helgedad située dans les déserts volcaniques qui
s'étendent au-delà des monts Durncrag. La construction de cette
cité représenta un long et douloureux cauchemar pour ces
créatures, dont seules les plus fortes survécurent à la terrible
épreuve. La chaleur et les vapeurs empoisonnées qui se
dégageaient des terrains alentour se révélaient, en effet,
mortelles pour la plupart d'entre elles. Le monstre mort qui gît à
vos pieds est, comme tous ses congénères, un descendant de ces
anciens esclaves Gloks. Il a été tué par un coup d'épée en pleine
tête et une Masse d'Armes est posée à côté de lui. Vous pouvez
prendre cette arme si vous le souhaitez en n'oubliant pas de
l'inscrire sur votre Feuille d'Aventure.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(stream_text("Vous pouvez ajouter la Masse d'Armes à votre inventaire :"))
    pickup_button("MASSE D'ARMES", key="mace", label="Prendre la Masse d'Armes")

    st.write_stream(
        stream_text(f"""Vous poursuivrez ensuite votre chemin le long du sentier en vous rendant au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_97.py", label="97", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
