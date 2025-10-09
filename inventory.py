import variable
import streamlit as st
import pandas as pd

from utils import set_cookies
from variable import KAI
import extra_streamlit_components as stx


@st.fragment
def get_manager():
    return stx.CookieManager()


cookie_manager = get_manager()


def check_inventory(is_fighting: bool = False, current_page_number: int = 0):
    """
    Check nothing is wrong with the inventory and re-set automatically some things.
    To use everytime a new page is read.
    """
    st.session_state.current_page_number = current_page_number

    if st.session_state.last_page_number != st.session_state.current_page_number:
        # if they are the same, it means there was a rerun of the same page (sorting inventory or else) and we didn't actually change the page
        # reseting items visilibty
        (
            st.session_state.visibility_1,
            st.session_state.visibility_2,
            st.session_state.visibility_3,
            st.session_state.visibility_4,
            st.session_state.visibility_5,
            st.session_state.visibility_6
        ) = (False, False, False, False, False, False)



    # make sur the current endurance never passed the total
    st.session_state.endurance = min(
        st.session_state.endurance, st.session_state.total_endurance
    )

    # make sure the current gold amount never passed 50
    if st.session_state.purse > 50:
        st.info(
            f"Votre bourse ne peut contenir qu'un maximum de 50 couronnes, vous avez déposé le surplus."
        )
    st.session_state.purse = min(st.session_state.purse, 50)

    # make sure they are no more than 8 items in the backpack
    st.session_state.backpack = st.session_state.backpack.dropna()
    if len(st.session_state.backpack["Nom"]) > 8:
        st.write(st.session_state.backpack)
        st.error(
            "Votre Sac à Dos ne peut emporter qu'un maximum de 8 objets. Jeter un objet déjà présent ou laissez "
            "celui-ci."
        )
        # st.subheader("Sac à Dos")
        # st.session_state.backpack = st.dataframe(
        #     st.session_state.backpack,
        #     column_config={
        #         "use": st.column_config.CheckboxColumn(
        #             "Utiliser l'objet",
        #             help="Uniquement faisable si l'objet possède des propriétés actives",
        #         ),
        #         "delete": st.column_config.CheckboxColumn(
        #             "Jeter l'objet ?",
        #             help="Jeter un objet vous en fera perdre définitivement l'usage",
        #         ),
        #     },
        #     on_change=remove_from_backpack,
        #     disabled=["Nom"],
        #     hide_index=True)

    # if the LS got the Healing Kai mastery and is not fighting, then he gains +1 ENDURANCE
    if (
        "La Guérison" in list(st.session_state.kai["Mastery"])
        and is_fighting is False
        and (st.session_state.last_page_number != st.session_state.current_page_number)
    ):
        st.success(f"+1 ENDURANCE")
        st.session_state.endurance = min(
            st.session_state.endurance + 1, st.session_state.total_endurance
        )


    # RESET combat session_state
    st.session_state.done_fighting = False
    st.session_state.flee = False
    
    set_cookies()


def execute_item(name: str):
    """
    Excecute the effect of an active item
    name: name of the active item
    """
    print(f"{st.session_state.current_page_number}: Executing item: {name}")
    if name not in variable.ACTIVE_ITEMS:
        return
    if name == "POTION DE GUÉRISON":
        st.session_state.endurance = min(
            st.session_state.endurance + 4, st.session_state.total_endurance
        )
    elif name == "LAUMSPUR":
        st.session_state.endurance = min(
            st.session_state.endurance + 3, st.session_state.total_endurance
        )

def display_inventory():
    """
    Display the current inventory of the LS
    t.session_state.purse: the purse containing your gold.
    """
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Gold", value=st.session_state.purse)
    col2.metric(
        label="Endurance",
        value=f"{st.session_state.endurance}/{st.session_state.total_endurance}",
    )

    col3.metric(label="Hability", value=st.session_state.hability)

    col4, col5 = st.columns(2)
    col4.metric(label="Arme 1", value=st.session_state.weapon1)
    disabled_1 = False if st.session_state.weapon1  else True
    if col4.button(label="Jeter l'Arme 1",disabled=disabled_1):
        st.session_state.weapon1 = None
        st.rerun()
    col5.metric(label="Arme 2", value=st.session_state.weapon2)
    disabled_2 = False if st.session_state.weapon2  else True
    if col5.button(label="Jeter l'Arme 2",disabled=disabled_2):
        st.session_state.weapon2 = None
        st.rerun()

    if not st.session_state.weapon1 and not st.session_state.weapon2:
        st.error(
            f"*Ne possédant aucune arme, vous subirez un malus de -4 points d'HABILITE au combat.*"
        )

    st.divider()
    col6, col7 = st.columns(2)
    col6.subheader(f"Equipement Spécial")
    col6.dataframe(
        st.session_state.special, hide_index=True
    )  # st.session_state.special is dataframe
    st.subheader("Sac à Dos")
    for index, row in st.session_state.backpack.iterrows():

        if row["Nom"] == "":
            st.session_state.backpack = st.session_state.backpack.drop(
                index, axis=0
            ).reset_index(drop=True)
            st.rerun()

        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        with col1:
            st.write(f"**{row['Nom']}**")
        with col2:
            if st.button("Utiliser", key=f"use_{index}"):
                if row["Nom"] not in variable.ACTIVE_ITEMS:
                    st.warning(
                        f"Cet objet n'a aucunes propriétés actives, vous l'utilisez mais il ne se passe rien."
                    )
                if row["Nom"] in variable.ACTIVE_ITEMS:
                    st.info(variable.ACTIVE_ITEMS[row["Nom"]])
                    execute_item(name=row["Nom"])
                st.session_state.backpack = st.session_state.backpack.drop(
                    index, axis=0
                ).reset_index(drop=True)
                st.rerun()
        with col3:
            if st.button("Jeter", key=f"drop_{index}"):
                st.warning(f"Vous avez jeté : {row['Nom']}")
                st.session_state.backpack = st.session_state.backpack.drop(
                    index, axis=0
                ).reset_index(drop=True)
                st.rerun()

        with col4:
            st.write(row["Description"])

    # backpack_edited = col7.data_editor(
    #     st.session_state.backpack,
    #     column_config={
    #         "use": st.column_config.CheckboxColumn(
    #             "Utiliser l'objet",
    #             help="Uniquement faisable si l'objet possède des propriétés actives",
    #             default=False
    #         ),
    #         "delete": st.column_config.CheckboxColumn(
    #             "Jeter l'objet ?",
    #             help="Jeter un objet vous en fera perdre définitivement l'usage",
    #             default=False
    #         ),
    #     },
    #     on_change=remove_from_backpack,
    #     disabled=["Nom"],
    #     hide_index=True,
    #     column_order=["Nom", "use", "delete", "Description"]
    # )
    # if not backpack_edited.equals(st.session_state.backpack):
    #     st.session_state.backpack= backpack_edited

    if st.session_state.weapon_mastery:
        st.divider()
        st.write(
            f"Vous maitrisez le ou les armes suivantes: {', '.join(st.session_state.weapon_mastery)}. Posséder "
            f"une arme que vous maitrisez "
            f"parfaitement augmentera votre HABILITE de 2 lors des combat."
        )

    st.divider()
    st.subheader("Vos Maîtrise Kaï")

    st.session_state.kai = st.session_state.kai.dropna()
    st.session_state.kai = st.session_state.kai.drop_duplicates(subset=["Mastery"])

    for item in st.session_state.kai["Mastery"]:
        item = item.strip()
        st.write(f"**{item}**")
        st.caption(KAI.get(item.strip()))


def add_to_inventory(name: str):
    """
    Called when want to add an item to inventory.
    name: name of the wanted item
    """
    print(f"{st.session_state.current_page_number} Adding item {name} to inventory ")
    if name in variable.SPECIAL_ITEMS:
        new_item = {"Nom": name, "Description": variable.SPECIAL_ITEMS[name]}
        # st.session_state.special.append(new_item, ignore_index=True)
        st.session_state.special = pd.concat(
            [st.session_state.special, pd.DataFrame([new_item])], ignore_index=True
        )
    elif name in variable.WEAPON:
        if st.session_state.weapon1 and st.session_state.weapon2:
            st.error(f"Vous ne pouvez porter que 2 armes à la fois.")
        else:
            if not st.session_state.weapon1:
                st.session_state.weapon1 = name
            else:
                st.session_state.weapon2 = name

    else:
        if len(st.session_state.backpack["Nom"]) >= 8:
            st.write(st.session_state.backpack)
            st.error(
                "Votre Sac à Dos ne peut emporter qu'un maximum de 8 objets. Jeter un objet déjà présent ou laissez "
                "celui-ci."
            )
        else:
            if name in variable.ACTIVE_ITEMS:
                new_item = {
                    "Nom": name,
                    "Description": variable.ACTIVE_ITEMS[name],
                    "use": False,
                    "delete": False,
                }
            elif name in variable.RANDOM_ITEMS:
                new_item = {
                    "Nom": name,
                    "Description": variable.RANDOM_ITEMS[name],
                    "use": False,
                    "delete": False,
                }
            else:
                new_item = {
                    "Nom": name,
                    "Description": "Unknown..",
                    "use": False,
                    "delete": False,
                }
            # st.session_state.backpack.append(new_item, ignore_index=True)
            st.session_state.backpack = pd.concat(
                [st.session_state.backpack, pd.DataFrame([new_item])], ignore_index=True
            )


# def remove_from_backpack(name: str = None):
#     """
#     When the LS check his inventory and want to change its backpack (make place, use options...)
#     We check what columns is affected and what it does (if it's an active item).
#     After this, we update st.sessions_state.backpack
#     # https://discuss.streamlit.io/t/deleting-rows-in-st-data-editor-progmatically/46337
#     """
#     print(f"User is going to use/delete an item : {name}")
#     # remove one specific object such as a Meal
#     if name:
#         name = name.strip()
#         for idx, ele in st.session_state.backpack.iterrows():
#             if ele["Nom"] == name:
#                 st.session_state.backpack = st.session_state.backpack.drop(idx, axis=0).reset_index(drop=True)
#     else:
#         for idx, ele in st.session_state.backpack.iterrows():
#             if ele["use"] is True:
#                 if ele["Nom"] not in variable.ACTIVE_ITEMS:
#                     st.warning(f"Cet objet n'a aucunes propriétés actives, vous l'utilisez mais il ne se passe rien.")
#                 if ele["Nom"] in variable.ACTIVE_ITEMS:
#                     execute_item(name=ele["Nom"])
#                 st.session_state.backpack = st.session_state.backpack.drop(idx, axis=0).reset_index(drop=True)

#             if ele["delete"] is True:
#                 st.session_state.backpack = st.session_state.backpack.drop(idx, axis=0).reset_index(drop=True)
#                 st.info(f"Vous avez jeté {ele['Nom']}")
