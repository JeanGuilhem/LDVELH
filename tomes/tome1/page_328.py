import streamlit as st
from inventory import display_inventory, check_inventory, end_page, show_illustrations
from utils import stream_text, called_cookies

if "weapon_mastery" not in st.session_state:
    st.warning(f"Loading data from your previous session..")
    # means that session state is not set up, needs to fetch data from cookies
    is_good = called_cookies()  # in case of reloading page
    if not is_good:
        st.stop()

check_inventory(is_fighting=False,
                current_page_number=328)

fr_text = """
Tandis que la créature meurt, son corps se dissout lentement en
un liquide verdâtre et pestilentiel. Vous remarquez alors que les
herbes et les plantes parmi lesquelles se répand cette substance
se fanent et meurent aussitôt. Quelques instants plus tard, une
grosse Pierre Précieuse apparaît sur le sol, près du cadavre
décomposé : apparemment sa valeur doit être considérable.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    # Prendre la Pierre se joue au paragraphe 76 : pas de ramassage sur cette page.
    st.write_stream(
        stream_text(f"""Si vous souhaitez prendre cette Pierre, rendez-vous au:""")
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_76.py", label="76", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez quitter les lieux aussi vite que possible, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_118.py", label="118", icon="📄")

    show_illustrations()


with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
