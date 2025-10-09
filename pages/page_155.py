import streamlit as st
from inventory import display_inventory, check_inventory
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=155)

fr_text = """
A votre approche, leur conversation s'interrompt. Vous constatez
par l'expression de leurs visages que tous ces gens ont reconnu
en vous un Seigneur Kaï. Alors, lentement, l'un des hommes tend
la main vers vous en un geste amical.
«Seigneur, dit-il, nous avons entendu dire que le Monastère Kaï
avait été détruit et tous ceux qui l'occupaient impitoyablement
massacrés. Heureusement, votre présence ici montre qu'il
s'agissait là de fausses rumeurs. Nous avions peur que tout ne
soit perdu. » Vous préférez ne pas leur révéler que le Monastère a
bel et bien été anéanti : ce serait, en effet, enlever tout espoir à
ces hommes et à ces femmes qui ont fui la ville de Toran dévastée
par les armées ennemies. Ils ont dû abandonner tous leurs biens
et les voilà qui errent sur les chemins pour tenter d'échapper à la
guerre, en espérant que les Seigneurs Kaï conduiront à la victoire
l'armée du Sommerlund. Vous apprenez par leurs récits que le
port de Toran a été attaqué par mer et par air et que les armées
des Maîtres des Ténèbres surpassaient largement en nombre la
garnison de la ville. En dépit de la vaillance dont ils ont fait
preuve, les soldats du Roi ont ainsi dû s'incliner. Vous essayez de
rassurer de votre mieux ces malheureux réfugiés en affirmant
que le Sommerlund ne tombera jamais aux mains des
envahisseurs. Puis vous leur souhaitez bonne chance au long de
leur exode et vous reprenez vous-même votre chemin.
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
        st.page_link("pages/page_70.py", label="70", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number