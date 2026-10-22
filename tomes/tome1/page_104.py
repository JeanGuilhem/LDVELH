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
                current_page_number=104)

fr_text = """
Les parois sont humides et couvertes de moisissure. Il règne ici
une odeur de renfermé qui vous étouffe à moitié et des toiles
d'araignées vous balaient le visage. Vous sentez la peur vous
serrer la gorge tandis que le tunnel s'obscurcit, mais vous
continuez cependant d'avancer et vous arrivez bientôt à un
croisement : le tunnel aboutit à un couloir orienté nord-sud.
"""

tab1, tab2, tab3 = st.tabs(["Page", "Inventaire", "Carte"])

with tab1:
    st.write(fr_text)
    st.write_stream(
        stream_text(
            f"""Si vous souhaitez aller au nord, rendez-vous au:"""
        )
    )
    fi = True
    if fi:
        st.page_link("tomes/tome1/page_26.py", label="26", icon="📄")

    st.write_stream(
        stream_text(f"""Si vous préférez prendre la direction du sud, rendez-vous au:""")
    )
    fi_1 = True
    if fi_1:
        st.page_link("tomes/tome1/page_100.py", label="100", icon="📄")

    show_illustrations()

with tab2:
    display_inventory()

with tab3:
    st.image("static/map_1.png")

end_page()
