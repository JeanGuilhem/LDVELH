import streamlit as st
from inventory import display_inventory, check_inventory, end_page, pickup_button, pickup_gold, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=319)

fr_text = """
La gluante créature laisse échapper un long cri d'agonie et s'écroule sur le sol.
Vous êtes proche de la panique et vous vous hâtez de vous relever en arrachant des mâchoires du monstre ce que vous pensez être votre ceinture.
Vous apercevez une lumière au loin et vous courez à toutes jambes dans cette direction.
Lorsque, enfin, vous vous retrouvez à l'air libre, vous vous laissez tomber à terre parmi les feuilles mortes et vous essayez de reprendre votre souffle en haletant désespérément.
Dès que vous pouvez à nouveau respirer normalement, vous vous asseyez et vous remarquez alors que votre ceinture est toujours nouée autour de votre taille : finalement, vous ne l'aviez pas perdue dans la bagarre.
Ce que vous avez arraché aux mâchoires de la créature est, en fait, une lanière de cuir à laquelle sont attachés une Bourse et un Poignard dans son fourreau.
En ouvrant la Bourse, vous trouvez 20 Pièces d'Or.
Vous pouvez prendre ces Pièces et le Poignard si vous le désirez.
Faites les modifications nécessaires sur votre Feuille d'Aventure.
Vous vous sentez mieux à présent : vous ramassez donc vos affaires et vous poursuivez votre route vers l'est en vous enfonçant dans la forêt.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)

    st.write_stream(stream_text("Vous pouvez ajouter les objets suivants à votre inventaire :"))
    pickup_gold(20)
    pickup_button("POIGNARD", key="dagger", label="Prendre le Poignard")

    st.write_stream(
        stream_text(
            f"""Rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_157.py", label="157", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
