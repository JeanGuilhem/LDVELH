
import streamlit as st
from inventory import display_inventory, check_inventory, add_to_inventory, end_page, has_kai, show_illustrations
from utils import stream_text, set_cookies, called_cookies, handle_repas, table_des_hasards, ls_death



if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=172)

fr_unkown_kai = "Vous ne maîtrisez pas cette discipline Kaï."

fr_text = """
La nuit tombe et l'obscurité bientôt vous engloutit. Il serait vain
de poursuivre votre route car vous vous perdriez à coup sûr. Vous
attachez donc votre cheval à un arbre, vous vous étendez sur le
sol en vous emmitouflant dans votre cape de Seigneur Kaï et vous
sombrez dans un sommeil sans rêves. Au matin vous êtes réveillé
par des bruits de galops lointains. De l'autre côté du lac, vous
distinguez des silhouettes noires de Drakkarims et une meute de
Loups Maudits. Un Kraan apparaît également au-dessus des
arbres et se pose sur le toit de la petite cabane. Il est monté par
une créature vêtue de rouge. Un instant plus tard, le monstre
redoutable reprend son vol et traverse le lac en se dirigeant vers
l'endroit où vous êtes caché.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez vous enfoncer plus profondément dans la forêt afin d'échapper au Kraan, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_239.py", label="239", icon="📄")

    st.write_stream(
        stream_text(
            f"""Si vous maîtrisez la Discipline Kaï du Camouflage et que vous désirez en faire usage pour vous dissimuler aux regards, vous et votre cheval, rendez-vous au:"""
        )
    )
    if has_kai("Le Camouflage"):
        st.page_link("tomes/tome1/page_114.py", label="114", icon="📄")
    else:
        st.write_stream(stream_text(fr_unkown_kai))
        st.page_link("tomes/tome1/page_114.py", label="114", icon="📄", disabled=True)

    st.write_stream(
        stream_text(f"""Enfin, si vous préférez vous préparer à combattre l'ignoble créature, rendez-vous au:""")
    )
    fi_2 = True
    if fi_2:
        st.page_link("tomes/tome1/page_29.py", label="29", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
