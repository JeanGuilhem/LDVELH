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
                current_page_number=298)

fr_text = """
L'oiseau tourne lentement la tête vers vous et se met à vous
injurier. Un instant plus tard, il s'envole au-dessus des arbres et
disparaît bientôt. Ce que vous venez d'entendre ne vous laisse
plus aucun doute : le corbeau était un éclaireur au service des
Maîtres des Ténèbres et il ne va sans doute pas tarder à les
informer de l'endroit où vous vous trouvez.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez poursuivre votre chemin le long du même sentier, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_121.py", label="121", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez quitter ce sentier et vous enfoncer dans la forêt, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_38.py", label="38", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
