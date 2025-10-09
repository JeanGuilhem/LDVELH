import streamlit as st
from text import *


def explanation():
    st.title("Comment jouer ?")

    with st.expander(label="Règles du jeu", expanded=False):
        st.write(fr_rules_1)
    with st.expander(label="Les Disciplines Kaï", expanded=False):
        st.write(fr_kai_mastery)
    with st.expander(label="Equipement", expanded=False):
        st.write(fr_equipment)
    with st.expander(label="Comment utiliser votre équipement ?", expanded=False):
        st.write(fr_use_the_equipment)
    with st.expander(label="Règles de combat", expanded=False):
        st.write(fr_combat_rule)
    with st.expander(label="Possibilités de fuite", expanded=False):
        st.write(fr_flee)
    with st.expander(label="La sagesse Kaï", expanded=False):
        st.write(fr_kai_wisdom)

    st.divider()
    st.page_link("hero.py", label="Retour au menu", icon="🏠")


explanation()
