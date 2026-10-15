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
                current_page_number=153)

fr_text = """
Au loin se dressent les hautes murailles blanches et les tours
scintillantes de Holmgard dont les étendards flottent au vent
frais du matin. S'étirant vers l'ouest, le fleuve Eledil jaillit des
monts Durncrag et se jette dans le golfe de Holm. Or, soudain,
vous distinguez au pied des montagnes une immense armée aux
uniformes noirs qui s'avance inexorablement vers la capitale. À
votre droite, la grand-route mène à Holmgard à travers les
plaines. En vous lançant au galop, vous pourriez atteindre en
moins d'une heure le camp fortifié qui entoure la ville, mais vous
seriez la plupart du temps à découvert, offrant aux Kraans une
proie facile. À quelque distance devant vous, cependant, une
large rivière aux eaux boueuses coule paresseusement en
direction du fleuve Eledil dans lequel elle finit par se jeter. Vous
pourriez abandonner votre cheval et profiter de l'escarpement de
ses berges pour nager à couvert jusqu'aux abords de la capitale. Il
existe enfin une troisième voie : à votre gauche s'étend, en effet,
le Cimetière des Anciens. Si vous marchiez parmi les tombes et
les monuments funéraires en ruine, vous n'auriez aucun mal à
vous approcher de votre but en échappant aux regards, mais c'est
là une zone interdite car des forces ténébreuses restent tapies
dans l'ombre de la nécropole et attendent qu'un passant
téméraire s'offre à leurs maléfices.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez tenter votre chance en empruntant la grand-route, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("pages/page_202.py", label="202", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous pensez que vous pourrez plus facilement atteindre la capitale par la rivière, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("pages/page_135.py", label="135", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si, enfin, vous vous sentez suffisamment courageux pour affronter les terribles périls du Cimetière des Anciens, rendez-vous au:"""
        )
    )
    fi_2 = True
    if fi_2:
        st.page_link("pages/page_329.py", label="329", icon="📄")


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
