import streamlit as st
import utils
import time

import variable
from utils import stream_text, initialize_session_state
from inventory import add_to_inventory, display_inventory
from text import (
    fr_kai_mastery,
    fr_first_items,
    fr_hazard_item,
    second_fr_kai_mastery,
    fr_determine_ability_endurance,
)
import pandas as pd
from variable import KAI

initialize_session_state()


def first_inventory_check() -> bool:
    """
    In the start of a new adventure, the LS chose (or not?) what to bring.
    """
    if "first_text" not in st.session_state:
        st.write_stream(stream_text(fr_first_items))
        st.session_state.first_text = False
    else:
        st.write(fr_first_items)
        st.session_state.first_text = True

    col3, col4 = st.columns(2)

    if not st.session_state.weapon1:
        st.session_state.weapon1 = "HACHE"
        col3.metric(label="Arme 1", value=st.session_state.weapon1)
    else:
        col3.metric(label="Arme 1", value=st.session_state.weapon1)

    if "first_meal" not in st.session_state:
        add_to_inventory(name="Repas")
        st.session_state.first_meal = True
    col4.metric(label="Objet trouvé", value="Repas")

    if not st.session_state.first_text:
        st.session_state.first_text = st.button(
            f"Déterminer votre nombre de pièces d'or",
        )
    else:
        if "number" not in st.session_state:
            with st.spinner():
                time.sleep(1)
            number = utils.table_des_hasards()
            st.session_state.number = number

        st.write(f"*Vous avez tiré le {st.session_state.number}.*")
        gold_ammount = st.session_state.number
        if st.session_state.purse == 0:
            st.session_state.purse += gold_ammount

        st.metric(
            label="Couronnes",
            value=gold_ammount,
            delta=gold_ammount,
        )

        if "second_text" not in st.session_state:
            st.write_stream(stream_text(fr_hazard_item))
            st.session_state.second_text = False
        else:
            st.write(fr_hazard_item)
            st.session_state.second_text = True

        if not st.session_state.second_text:
            st.session_state.second_text = st.button(
                f"Cliquez ici pour fouiller les ruines.."
            )

        else:
            if "first_item" not in st.session_state:
                with st.spinner():
                    time.sleep(1)
                random_item = utils.table_des_hasards()
                st.session_state.first_item = random_item
                st.write_stream(
                    stream_text(f"*Vous avez tiré le {st.session_state.first_item}.*")
                )
            if st.session_state.first_item == 1:
                st.session_state.weapon2 = "ÉPÉE"
                st.write_stream(
                    stream_text(
                        f"Vous déterrez une épée dans les décombres de votre monastère."
                    )
                )
                st.metric(label="Arme 2", value=st.session_state.weapon2)
                return True

            if st.session_state.first_item == 2:
                st.session_state.total_endurance += 2
                st.write_stream(
                    stream_text(
                        f"Vous déterrez un casque dans les décombres du monastère. Vous vous en coiffez et augmentez "
                        f"votre total d'endurance de 2."
                    )
                )
                tab10, tab11 = st.columns(2)
                tab10.metric(label="Objet trouvé", value="Casque")
                tab11.metric(
                    label="Endurance totale",
                    value=st.session_state.total_endurance,
                    delta=2,
                )
                return True

            if st.session_state.first_item == 3:
                add_to_inventory(name="Repas")
                add_to_inventory(name="Repas")
                col1, col2 = st.columns(2)
                col1.metric(label="Objet trouvé", value="Repas")
                col2.metric(label="Objet trouvé", value="Repas")
                st.write_stream(
                    stream_text(
                        f"Vous parvenez à extraire 2 Repas supplémentaires des ruines de votre monastère."
                    )
                )
                return True

            if st.session_state.first_item == 4:
                add_to_inventory(name="COTTE DE MAILLES")
                st.write_stream(
                    stream_text(
                        f"Vous déterrez une côte de mailles dans les décombres de votre monastère. Vous vous en "
                        f"vêtissez, ce qui augmente votre total d'endurance de 4."
                    )
                )
                st.metric(label="Objet trouvé", value="COTTE DE MAILLES")
                st.metric(
                    label="Endurance total",
                    value=st.session_state.total_endurance,
                    delta=st.session_state.total_endurance + 4,
                )
                st.session_state.total_endurance += 4
                return True

            if st.session_state.first_item == 5:
                st.session_state.weapon2 = "MASSE D'ARMES"
                st.write_stream(
                    stream_text(
                        f"Vous déterrez une masse d'armes dans les décombres de votre monastère."
                    )
                )
                st.metric(label="Arme 2", value=st.session_state.weapon2)
                return True

            if st.session_state.first_item == 6:
                add_to_inventory(name="POTION DE GUÉRISON")
                st.write_stream(
                    stream_text(
                        f"Vous trouvez une potion de guérison encore intact dans les décombres et ruines "
                        f"environnantes."
                    )
                )
                st.metric(label="Objet trouvé", value="POTION DE GUÉRISON")

                return True

            if st.session_state.first_item == 7:
                st.session_state.weapon2 = "BATON"
                st.write_stream(
                    stream_text(
                        f"Vous déterrez un baton dans les décombres de votre monastère."
                    )
                )
                st.metric(label="Arme 2", value=st.session_state.weapon2)

                return True

            if st.session_state.first_item == 8:
                ga = 12
                st.write_stream(
                    stream_text(
                        f"Vous trouvez une bourse en cuir dans laquelle se trouve 12 couronnes."
                    )
                )

                st.session_state.purse += ga
                st.metric(
                    label="Couronnes",
                    value=st.session_state.purse,
                    delta=ga,
                )

                return True

            if st.session_state.first_item == 9:
                st.session_state.weapon2 = "LANCE"
                st.write_stream(
                    stream_text(
                        f"Vous déterrez une lance dans les décombres de votre monastère."
                    )
                )
                st.metric(label="Arme 2", value=st.session_state.weapon2)

                return True

            if st.session_state.first_item == 10:
                st.session_state.weapon2 = "GLAIVE"
                st.write_stream(
                    stream_text(
                        f"Vous déterrez un glaive dans les décombres de votre monastère."
                    )
                )
                st.metric(label="Arme 2", value=st.session_state.weapon2)

                return True


def determine_endurance_ability() -> bool:
    """
    Used to determine total endurance and ability of the LS
    Called before everything.
    """
    if "fae" not in st.session_state:
        st.session_state.abi, st.session_state.endu = False, False
        st.write_stream(stream_text(text=fr_determine_ability_endurance))
        st.session_state.fae = True
    else:
        st.write(fr_determine_ability_endurance)

    col1, col2 = st.columns(2)
    if "ability_number" not in st.session_state:
        st.session_state.ability_number = 0
    if "endurance_number" not in st.session_state:
        st.session_state.endurance_number = 0

    with col1:

        if st.button(
            f"Déterminer votre habilité au combat",
        ):
            with st.spinner():
                time.sleep(1)
            st.session_state.ability_number = utils.table_des_hasards()
            st.write_stream(
                stream_text(
                    text=f"*Vous avez tiré le {st.session_state.ability_number}*"
                )
            )

            st.session_state.hability = st.session_state.ability_number + 10
            st.metric(
                label="Habilité",
                value=st.session_state.hability,
                delta=st.session_state.ability_number,
            )
            st.session_state.abi = True
        elif st.session_state.hability != 0:
            st.write(f"*Vous avez tiré le {st.session_state.ability_number}*")
            st.metric(
                label="Habilité",
                value=st.session_state.hability,
                delta=st.session_state.ability_number,
            )
            st.session_state.abi = True

    with col2:
        if st.button(
            f"Déterminer votre endurance",
        ):
            with st.spinner():
                time.sleep(1)
            st.session_state.endurance_number = utils.table_des_hasards()
            st.write_stream(
                stream_text(
                    text=f"*Vous avez tiré le {st.session_state.endurance_number}*"
                )
            )
            st.session_state.endurance += 20
            st.session_state.total_endurance += 20
            st.metric(
                label="Endurance",
                value=st.session_state.total_endurance,
                delta=st.session_state.endurance_number,
            )
            st.session_state.endu = True

        elif st.session_state.total_endurance != 0:
            st.write(f"*Vous avez tiré le {st.session_state.endurance_number}*")
            st.metric(
                label="Endurance",
                value=st.session_state.total_endurance,
                delta=st.session_state.endurance_number,
            )

    if st.session_state.abi and st.session_state.endu:
        return True

    return False


def determine_kai_mastery() -> bool:
    """
    Used to determine which Kai mastery the LS chose.
    Called before first_inventory_check
    """
    finished = False
    if "dka" not in st.session_state:
        st.write_stream(stream_text(second_fr_kai_mastery))
        st.write_stream(
            stream_text("Quelles Maîtrises Kaï choisissez-vous (5 au maximum)?")
        )
        st.session_state.dka = True
    else:
        st.write(second_fr_kai_mastery)
        st.write("Quelles Maîtrises Kaï choisissez-vous (5 au maximum)?")

    option_1 = st.checkbox("Le Camouflage")
    option_2 = st.checkbox("La Chasse")
    option_3 = st.checkbox("Le Sixième Sens")
    option_4 = st.checkbox("L'Orientation")
    option_5 = st.checkbox("La Guérison")
    option_6 = st.checkbox("La Maîtrise des armes")
    if option_6:
        if "wm" not in st.session_state or st.session_state.wm is False:
            number = utils.table_des_hasards()
            if number == 10:
                number = 1
            st.session_state.wm = number
            st.write_stream(
                stream_text(
                    f"*Vous avez tiré le {number}*. Vous maitrisez cette arme: {variable.WEAPON[number-1]}"
                )
            )
            st.session_state.weapon_mastery.append(variable.WEAPON[number - 1])
        elif "wm" in st.session_state:
            st.write(
                f"*Vous avez tiré le {st.session_state.wm}*. Vous maitrisez cette arme: {variable.WEAPON[st.session_state.wm-1]}"
            )

    if not option_6:
        st.session_state.weapon_mastery = []
        st.session_state.wm = False

    option_7 = st.checkbox("Bouclier psychique")
    option_8 = st.checkbox("Puissance psychique")
    option_9 = st.checkbox("Communication Animale")

    lst = [
        option_1,
        option_2,
        option_3,
        option_4,
        option_5,
        option_6,
        option_7,
        option_8,
        option_9,
    ]

    if len([ele for ele in lst if ele is True]) == 5:
        kai = {
            "Mastery": [None for _ in range(0, 6)],
            "Description": [None for _ in range(0, 6)],
        }
        st.session_state.kai = pd.DataFrame(kai)
        for index, element in enumerate(lst):
            if element is True:
                master = list(KAI.keys())[index]
                new_item = {
                    "Mastery": master,
                    "Description": KAI.get(master),
                }
                if master not in list(st.session_state.kai["Mastery"]):
                    st.session_state.kai = pd.concat(
                        [st.session_state.kai, pd.DataFrame([new_item])],
                        ignore_index=True,
                    )
        finished = True
    elif len([ele for ele in lst if ele is True]) > 5:
        st.error(f"Vous ne pouvez maitriser que 5 disciplines.")

    return finished


tab1, tab2 = st.tabs(["Loup Solitaire", "Maitrise Kaï"])

with tab1:
    fini = determine_endurance_ability()
    if fini:
        st.divider()
        finished = determine_kai_mastery()
        if finished is True:
            st.divider()
            f = first_inventory_check()
            if f:
                st.divider()
                with st.expander(label="Afficher mon inventaire"):
                    display_inventory()
                st.page_link(
                    "pages/pages_intro.py", label="Commencez votre aventure", icon="📜"
                )
with tab2:
    st.write(fr_kai_mastery)
