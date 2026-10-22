import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_gold, show_illustrations
from utils import stream_text, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=263)

fr_text = """
Vous suivez prudemment le cours d'eau qui coule vers l'est puis
soudain, vous vous immobilisez : vous venez, en effet,
d'apercevoir la silhouette d'un Kraan mort qui gît dans l'eau tel
un grand barrage noir. En restant à l'abri du feuillage, vous
avancez avec précaution vers le cadavre de la créature : trois
flèches sont profondément enfoncées dans son poitrail. Un autre
corps est coincé sous le Kraan mort: c'est celui d'un Glok qui le
chevauchait. Les Gloks sont des êtres méprisables et malfaisants
entièrement dévoués à la cause des Maîtres des Ténèbres. Il y a
bien longtemps, les ancêtres des Gloks servaient d'esclaves aux
Maîtres des Ténèbres et ceux-ci leur firent bâtir la ville infernale
d'Helgedad, située dans les déserts volcaniques qui s'étendent
au-delà des monts Durncrag. La construction de cette cité
représenta un long et douloureux cauchemar pour ces créatures,
dont seules les plus fortes survécurent à la terrible épreuve. La
chaleur et les vapeurs empoisonnées qui se dégageaient des
terrains alentour se révélaient, en effet, mortelles pour la plupart
d'entre eux. Le monstre mort qui repose dans le lit du cours
d'eau est l'un des descendants de ces anciens esclaves.
Apparemment, il s'est noyé.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(stream_text("Dans une bourse accrochée à sa ceinture, vous trouvez 3 Pièces d'Or que vous pouvez prendre si vous le souhaitez."))
    pickup_gold(3)

    st.write_stream(
        stream_text(
            f"""Vous pourrez ensuite continuer votre chemin le long du cours d'eau en vous rendant au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_70.py", label="70", icon="📄")

    st.write_stream(
        stream_text(f"""Mais vous pouvez également quitter sa berge et prendre la direction du sud ; rendez-vous pour cela au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_157.py", label="157", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
