import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies, hazard_roll

if "weapon_mastery" not in st.session_state:
    # rechargement du navigateur : on restaure la sauvegarde
    if not called_cookies():
        st.stop()

check_inventory(current_page_number=275)

fr_text = """
Vous avez suivi ce sentier sinueux pendant environ dix minutes
lorsque vous entendez soudain des battements d'ailes au-dessus
de vous. Vous levez les yeux et vous apercevez alors un immense
Kraan qui s'approche de l'endroit où vous êtes. La créature vient
du nord et, bientôt, ses grandes ailes noires projettent une ombre
gigantesque sur le feuillage des arbres. Deux êtres armés de
longues lances chevauchent le monstre : ce sont des Gloks, de
petites créatures d'une grande laideur, animées de haine et
vouées à la malfaisance. Autrefois, il y a de cela plusieurs siècles,
les Gloks servaient d'esclaves aux Maîtres des Ténèbres, et ceux-ci leur firent bâtir la cité infernale d'Helgedad, située dans les
déserts volcaniques qui s'étendent au-delà des monts Durncrag.
La construction de cette ville représenta une longue et
douloureuse épreuve pour ces créatures, dont seules les plus
fortes survécurent aux vapeurs empoisonnées qui se dégageaient
des terrains alentour. Les deux monstres portés par le Kraan sont
des descendants de ces anciens esclaves. Lorsque le Kraan passe
au-dessus de votre tête, vous vous cachez sous un arbre, le cœur
battant, en priant le ciel que le redoutable trio ne vous ait pas
repéré.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    number = hazard_roll()
    if number is not None and number <= 4:
        st.page_link("tomes/tome1/page_345.py", label="345", icon="📄")
    elif number is not None:
        st.page_link("tomes/tome1/page_74.py", label="74", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
