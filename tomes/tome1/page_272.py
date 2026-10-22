import streamlit as st
from inventory import display_inventory, check_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=272)

fr_text = """
Vous vous hâtez le long du chemin tout en surveillant le ciel au-
dessus de vous. Vous savez que ce sentier mène au Bois des
Brumes ; c'est là que s'est installée, depuis presque cinquante
ans, une famille qui fait le commerce du charbon de bois. Les
membres de la famille vivent dans des huttes bâties en cercle au
milieu d'une clairière. Vingt minutes plus tard, vous parvenez à
la lisière de cette clairière. Les huttes, contrairement à l'habitude,
paraissent étrangement calmes, et on ne voit plus trace de la
fumée qui envahit ordinairement les environs. C'est cette fumée
qui a donné à l'endroit son nom de Bois des Brumes, et son
absence vous semble tout à fait insolite.
"""

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï de l'Orientation, rendez-vous au:"""
        )
    )
    if has_kai("L'Orientation"):
        st.page_link("tomes/tome1/page_134.py", label="134", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome1/page_134.py", label="134", icon="📄", disabled=True)

    st.write_stream(
        stream_text(
            f"""Dans le cas contraire, vous dégainez votre arme et vous vous approchez silencieusement des huttes. Rendez-vous alors au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_305.py", label="305", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
