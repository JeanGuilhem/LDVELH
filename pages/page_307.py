
import streamlit as st
from inventory import display_inventory, check_inventory, end_page, is_new_page, add_to_inventory, pickup_button, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=307)

fr_text = """
Vous n'avez aucune difficulté à atteindre la cabane et, tandis que
vous escaladez l'arbre, des souvenirs d'enfance vous reviennent
en mémoire : vous vous rappelez le temps où, tout jeune garçon,
vous montiez également aux arbres, non loin de la ville de Toran,
pour aller cueillir des fruits ou admirer la campagne
environnante. Vous ouvrez la porte de la cabane et vous tombez
nez à nez avec un vieil ermite recroquevillé dans un coin de la
pièce. Une expression d'intense soulagement apparaît sur son
visage lorsqu'il reconnaît votre cape de Seigneur Kaï. Il vous
raconte alors que toute la région est envahie par des Gloks et
qu'il a dénombré plus de quarante Kraans volant au-dessus de sa
maison dans les trois heures qui ont précédé. Ils se dirigeaient
tous vers l'est. Il s'approche ensuite d'un buffet et vous apporte
une assiette de fruits. Vous le remerciez et vous rangez les fruits
dans votre Sac à Dos. Ils représentent l'équivalent d'un Repas,
notez-le sur votre Feuille d'Aventure. L'ermite vous montre
également un magnifique Marteau de Guerre qu'il pose sur une
table, près de la porte. « Vous en avez plus besoin que moi,
Seigneur Kaï, dit-il. Prenez ce Marteau si vous le désirez, c'est
une Arme à laquelle vous pourrez vous fier. » Vous n'aurez le
droit de prendre ce Marteau de Guerre qu'à la condition de
l'échanger contre une autre Arme que vous possédez déjà, car
vous ne pouvez laisser l'ermite sans aucune défense contre
l'ennemi. Faites, le cas échéant, les ajustements nécessaires sur
votre Feuille d'Aventure. Vous remerciez alors le vieil homme et
vous redescendez de l'arbre pour continuer votre route.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    if is_new_page():
        if add_to_inventory("REPAS"):
            st.success("Les fruits de l'ermite (1 Repas) sont rangés dans votre Sac à Dos.")

    st.write_stream(stream_text(
        "Vous pouvez prendre le Marteau de Guerre, mais seulement en échange d'une Arme que vous "
        "possédez déjà : jetez d'abord cette Arme depuis l'onglet Inventaire (l'ermite la garde), "
        "puis prenez le Marteau."
    ))
    pickup_button("MARTEAU DE GUERRE", key="warhammer", label="Échanger une Arme contre le Marteau de Guerre")

    st.write_stream(
        stream_text(f"""Rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_213.py", label="213", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
