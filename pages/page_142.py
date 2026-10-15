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
                current_page_number=142)

fr_text = """
Vous apercevez les hautes murailles blanches et les tours
scintillantes de Holmgard, dont les étendards flottent au vent
frais du matin. S'étirant vers l'ouest, le fleuve Eledil jaillit des
monts Durncrag et se jette dans le golfe de Holm. Or, soudain,
vous distinguez au loin, à l'ombre des montagnes, une immense
armée aux uniformes noirs qui marche sans répit vers la capitale.
A votre droite, la grand-route mène à Holmgard à travers les
plaines. En courant vite, vous pourriez atteindre en une heure le
camp fortifié qui se dresse autour de la ville, mais vous seriez la
plupart du temps à découvert, offrant aux Kraans une proie
facile. A quelque distance devant vous, cependant, une large
rivière aux eaux boueuses coule paresseusement en direction du
fleuve Eledil dans lequel elle finit par se jeter. Vous pourriez
profiter de l'escarpement de ses berges pour nager à couvert et
rejoindre ainsi la capitale. A votre gauche, par ailleurs, s'étend le
Cimetière des Anciens. En marchant parmi les tombes et les
monuments funéraires en ruine, vous pourriez échapper aux
regards et vous approcher de votre but, mais c'est là une zone
interdite : des forces ténébreuses restent, en effet, tapies dans
l'ombre de la nécropole, attendant qu'un passant téméraire
s'offre à leurs maléfices.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous voulez tenter votre chance en empruntant la grand-route, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_58.py", label="58", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous pensez avoir plus de chance d'atteindre la capitale par la rivière, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_135.py", label="135", icon="📄")

    st.write_stream(
        stream_text(
            f"""Enfin, si vous êtes suffisamment courageux pour vous risquer dans le Cimetière des Anciens, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_102.py", label="102", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
