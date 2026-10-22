import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, receive_gold, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=62)

fr_text = """
Les « soldats » sont étendus raides morts à vos pieds. C'étaient
des brigands qui détroussaient les réfugiés de Toran et pillaient
les maisons et les fermes abandonnées de la région.

En fouillant leurs cadavres, vous trouvez 28 Pièces d'Or et deux
Sacs à Dos qui contiennent des provisions équivalant à trois
Repas. Ils étaient armés d'une Arbalète et de Trois Epées.
L'Arbalète a été endommagée au cours du combat, mais les trois
Epées sont intactes, et vous pouvez en emporter une si vous le
souhaitez. Vous modifiez, en conséquence, votre Feuille
d'Aventure, vous rangez soigneusement vos nouvelles
acquisitions et vous jetez un coup d'œil en direction de l'ouest
pour voir si la voie est libre. Enfin, vous vous remettez en route
vers le camp fortifié, dressé à l'extérieur de la ville.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    receive_gold(28)

    pickup_button("REPAS", key="meal_1", label="Prendre un Repas")
    pickup_button("REPAS", key="meal_2", label="Prendre un Repas")
    pickup_button("REPAS", key="meal_3", label="Prendre un Repas")
    pickup_button("ÉPÉE", key="sword", label="Prendre une Épée")
    pickup_button("SAC À DOS", key="backpack", label="Prendre un Sac à Dos (si vous n'en avez plus)")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au :"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_288.py", label="288", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
