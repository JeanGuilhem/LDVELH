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
                current_page_number=333)

fr_text = """
Il y a presque une demi-heure que vous vous frayez un chemin
parmi les épaisses broussailles lorsque vous entendez un
battement d'ailes au-dessus des arbres. Vous levez les yeux et
vous distinguez la silhouette d'un Kraan qui vole dans le ciel en
provenance du nord. C'est l'un des monstres qui ont attaqué le
monastère ; sur son dos sont assises deux créatures à la peau
grise, armées de lances. Ce sont des Gloks, les cruels serviteurs
des maîtres des Ténèbres, animés de haine et dévoués à la cause
du mal. Il y a de cela plusieurs siècles, les ancêtres de ces
monstres servaient d'esclaves aux Maîtres des Ténèbres qui leur
firent bâtir la cité infernale d'Helgedad, située dans les déserts
volcaniques qui s'étendent au-delà des monts Durncrag. La
construction de cette ville représenta une longue et douloureuse
épreuve pour ces créatures, dont seules les plus fortes
survivèrent aux vapeurs empoisonnées qui baignent
l'atmosphère surchauffée d'Helgedad.
Caché par les arbres, vous vous figez sur place en restant
parfaitement immobile tandis que le Kraan passe au-dessus de
votre tête, puis disparaît en direction du sud. Lorsque vous êtes
certain qu'il s'est suffisamment éloigné, vous reprenez votre
chemin parmi les arbres de la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_131.py", label="131", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
