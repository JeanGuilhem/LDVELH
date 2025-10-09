import streamlit as st
from inventory import display_inventory, check_inventory, remove_from_inventory
from utils import stream_text, set_cookies, called_cookies


current_page_number = 144

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    is_good = called_cookies()
    if not is_good:
        st.stop()

check_inventory(is_fighting=False, current_page_number=current_page_number)

fr_text = """
Vous vous frayez un chemin à coups de coude dans la foule qui se
presse sur la grand-rue. Vous apercevez un peu plus loin la
silhouette massive de la citadelle qui abrite le Palais du Roi. Les
habitants de Holmgard, saisis de panique, courent en tous sens,
tandis que retentissent les cris des Kraans qui tournoient dans le
ciel de la ville.
"""

if "item_removed_on_page_144" not in st.session_state:
    st.session_state.item_removed_on_page_144 = False

if st.session_state.last_page_number != st.session_state.current_page_number:
    st.write_stream(stream_text("Un cheval emballé, qui tire une charrette, passe devant vous à toute allure et vous heurte en vous projetant contre une porte cochère. Vous êtes à moitié assommé et vous perdez 2 points D'ENDURANCE."))
    st.session_state.endurance -= 2
    st.metric(label="Endurance", value=st.session_state.endurance, delta=-2)
    st.session_state.item_removed_on_page_144 = False

if not st.session_state.item_removed_on_page_144:
    st.write_stream(stream_text("Dans la bousculade, quelqu'un vous vole l'un des objets contenus dans votre Sac à Dos. Si vous n'avez plus de Sac à Dos, c'est une arme qu'on vous dérobe. Rayez l'objet ou l'arme perdue de votre Feuille d'Aventure (c'est vous qui choisissez ce qu'on vous a volé)."))

    items_to_choose_from = []
    has_backpack = False
    for item_name, item_data in st.session_state.inventory.to_dict(orient='index').items():
        if item_data['Type'] == 'Sac à Dos':
            has_backpack = True
            break

    if has_backpack:
        items_to_choose_from = [name for name, data in st.session_state.inventory.to_dict(orient='index').items() if data['Type'] != 'Sac à Dos']
        st.write_stream(stream_text("Vous avez un Sac à Dos. Un objet de votre inventaire (hors Sac à Dos) a été volé."))
    else:
        items_to_choose_from = [name for name, data in st.session_state.inventory.to_dict(orient='index').items() if data['Type'] == 'Arme']
        st.write_stream(stream_text("Vous n'avez pas de Sac à Dos. Une arme a été volée."))

    if items_to_choose_from:
        if "selected_item_to_lose" not in st.session_state or st.session_state.selected_item_to_lose not in items_to_choose_from:
            st.session_state.selected_item_to_lose = items_to_choose_from[0] if items_to_choose_from else None

        selected_item = st.selectbox(
            "Choisissez l'objet ou l'arme que vous souhaitez perdre :",
            options=items_to_choose_from,
            key="stolen_item_selector"
        )
        if st.button("Confirmer la perte", key="confirm_stolen_item"):
            if selected_item:
                remove_from_inventory(selected_item)
                st.success(f"{selected_item} a été retiré de votre inventaire.")
                st.session_state.item_removed_on_page_144 = True
                st.rerun()
            else:
                st.warning("Veuillez sélectionner un objet à retirer.")
    else:
        st.warning("Vous n'avez aucun objet ou arme à voler selon les règles du jeu. Vous avez eu de la chance !")
        st.session_state.item_removed_on_page_144 = True
        st.rerun()

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Vous vous relevez en titubant,
mais, au même moment, la porte s'ouvre à la volée et un vieil
homme décrépit se précipite sur vous en brandissant un couteau
à viande. Il est fou à lier et il vous faut le combattre ou tenter de
fuir."""
        )
    )

    st.write_stream(
        stream_text(f"""Si vous choisissez de le combattre, rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("pages/page_63.py", label="63", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez essayer d'éviter l'affrontement, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_XXX.py", label="---", icon="📄", disabled=True)


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

st.session_state.last_page_number = st.session_state.current_page_number