#!/usr/bin/env python3
import random
import time
import streamlit as st
import pandas as pd
import extra_streamlit_components as stx

import variable
from variable import KAI, AI_INSTRUCTION, GEMINI_API_KEY

T = 1000  # Tué sur le coup

def get_manager(key:str):
    return stx.CookieManager(key=key)


def change_visiblity(variable:bool):
    """
    Used when LS check one item to pick up into his bag.
    Change the variable in parameter that'll be used to able/disable checkbox
    """
    print(f"{st.session_state.current_page_number}: Changing visibilty for an item")
    if variable is True:
        return False
    else:
        return True

def set_cookies() -> None:
    """
    When called, set the cookies of all session_state (inventory, current pages...)
    """

    if 'cookie_manager' not in st.session_state:
        st.session_state.cookie_manager = get_manager()

    cookie_manager = st.session_state.cookie_manager

    name = "session_state"
    val = "|"

    val += "|" + str(st.session_state.weapon_mastery)
    val += "|" + str(st.session_state.purse)
    val += "|" + str(st.session_state.endurance)
    val += "|" + str(st.session_state.total_endurance)
    val += "|" + str(st.session_state.hability)
    val += "|" + str(st.session_state.weapon1)
    val += "|" + str(st.session_state.weapon2)
    val += "|" + str(st.session_state.weapon_mastery)
    val += "|" + str(list(st.session_state.kai.to_dict()["Mastery"].values()))
    val += "|" + str(list((st.session_state.special.to_dict())['Nom'].values()))
    val += "|" + str(list((st.session_state.backpack.to_dict())['Nom'].values()))
    val += "|" + str(st.session_state.current_page_number)

    cookie_manager.set(name, val)

    return

def called_cookies() -> bool:
    """
    When called, use the browser cookies to set up/update session_state
    """

    if 'cookie_manager' not in st.session_state:
        st.session_state.cookie_manager = get_manager(key='init')

    cookie_manager = st.session_state.cookie_manager

    cookies = cookie_manager.get_all()
    if "session_state" in cookies:
        saved_data = cookies["session_state"].split("|")
        print(saved_data)
        st.session_state.weapon_mastery = saved_data[1]
        st.session_state.purse = int(saved_data[3])
        st.session_state.endurance = int(saved_data[4])
        st.session_state.total_endurance = int(saved_data[5])
        st.session_state.hability = int(saved_data[6])
        st.session_state.weapon1 = saved_data[7]
        st.session_state.weapon2 = saved_data[8]

        lst_kai_mastery = [ele.replace('[', '').replace(']', '').replace("'","").strip() for ele in saved_data[10].split(",")]
        new_item = {
            "Mastery": lst_kai_mastery,
            "Description": [KAI[ele.strip()] for ele in lst_kai_mastery],
        }
        st.session_state.kai = pd.DataFrame(new_item)

        lst_special = [ele.replace('[', '').replace(']', '').replace("'","") for ele in saved_data[11].split(",")]
        if lst_special == ['']:
            new_item = {"Nom": [], "Description": []}
        else:
            new_item = {"Nom": lst_special, "Description": [variable.SPECIAL_ITEMS[ele] for ele in lst_special]}
        st.session_state.special = pd.DataFrame(new_item)

        lst_backpack = [ele.replace('[', '').replace(']', '').replace("'","").strip() for ele in saved_data[12].split(",")]
        new_item = {"Nom": [], "Description": [], "use": [], "delete": []}
        for name in lst_backpack:
            if name in variable.ACTIVE_ITEMS:
                new_item["Nom"].append(name)
                new_item["Description"].append(variable.ACTIVE_ITEMS[name])
                new_item["use"].append(False)
                new_item["delete"].append(False)
            elif name in variable.RANDOM_ITEMS:
                new_item["Nom"].append(name)
                new_item["Description"].append(variable.RANDOM_ITEMS[name])
                new_item["use"].append(False)
                new_item["delete"].append(False)
            else:
                new_item["Nom"].append(name)
                new_item["Description"].append("Unknown..")
                new_item["use"].append(False)
                new_item["delete"].append(False)

        st.session_state.backpack = pd.DataFrame(new_item)
        st.session_state.current_page_number = saved_data[13]
        st.session_state.last_page_number = st.session_state.current_page_number
        st.page_link(f"pages/page_{st.session_state.current_page_number}.py", label=f"Reprendre mon aventure page {st.session_state.current_page_number}", icon="📄", disabled=False)

        return True  # all is right
    else:
        st.error(
            f"Couldn't load data from cookies. If you were in game, we are sorry but you will have to start again."
        )
        st.page_link("pages/crafting_hero.py", label="Démarrer mon aventure", icon="⚔️")
        return False

def initialize_session_state(reset: bool = True) -> None:
    """
    Initialize streamlit session state
    """

    if 'cookie_manager' not in st.session_state:
        st.session_state.cookie_manager = get_manager(key='0')

    if reset:
        cookie_manager = st.session_state.cookie_manager

        if "session_state" in cookie_manager.get_all():
            cookie_manager.delete("session_state")
    else:
        called_cookies()

    # Weapon bound to Kai Mastery of Weapon
    if "weapon_mastery" not in st.session_state:
        st.session_state.weapon_mastery = []

    # the purse containing the gold of the LS
    if "purse" not in st.session_state:
        st.session_state.purse = 0

    # the current endurance of the LS
    if "endurance" not in st.session_state:
        st.session_state.endurance = 0

    # the total endurance of the LS
    if "total_endurance" not in st.session_state:
        st.session_state.total_endurance = 0

    # the hability of the LS
    if "hability" not in st.session_state:
        st.session_state.hability = 0

    # the first weapon of the LS (can be None)
    if "weapon1" not in st.session_state:
        st.session_state.weapon1 = None

    # the second weapon of the LS (can be None)
    if "weapon2" not in st.session_state:
        st.session_state.weapon2 = None

    # a dataframe containing the kai mastery of the LS (and their description)
    if "kai" not in st.session_state:
        kai = {
            "Mastery": [None for _ in range(0, 6)],
            "Description": [None for _ in range(0, 6)],
        }
        st.session_state.kai = pd.DataFrame(kai)

    # all the special items gathered by the LS
    if "special" not in st.session_state:
        special = {"Nom": [], "Description": []}
        st.session_state.special = pd.DataFrame(special)

    # the inventory of the LS
    if "backpack" not in st.session_state:
        columns = ["Nom", "Description", "use", "delete"]
        # backpack = {
        #     "Nom": [],
        #     "Description": [],
        #     "use": [],
        #     "delete": [],
        # }
        st.session_state.backpack = pd.DataFrame(data=None, columns=columns)

    if "current_page_number" not in st.session_state:
        st.session_state.current_page_number = 0

    if "last_page_number" not in st.session_state:
        st.session_state.last_page_number = 0

    if "flee" not in st.session_state:
        st.session_state.flee = False

def ls_death():
    """
    Ths method is called when the LS died.
    """
    st.error("Vous êtes mort ! Votre aventure s'arrête ici, ainsi que la lignée des Kai.")
    st.page_link("pages/crafting_hero.py", label="Démarrer mon aventure", icon="⚔️")
    st.stop()

def table_des_hasards() -> int:
    """
    Chose between 0 et 9 (for the book, here 1 to 10)
    """
    res = random.randint(1, 10)
    print(f"Tables des hasards: {res}")
    return res

def before_fight(ls_hability: int, ennemy_psychique_sensibility: bool = True):
    """
    This method go throught the LS inventory, kai mastery and status in order to determine the LS hability and dammage.
    Called automaticaly before a fight.
    """
    if "La Maîtrise des armes" in list(st.session_state.kai["Mastery"].values):
        if (st.session_state.weapon1 in st.session_state.weapon_mastery) or (
            st.session_state.weapon2 in st.session_state.weapon_mastery
        ):
            st.write(f"*Maitrise d'arme: + 2 points d'habilité*")
            ls_hability += 2
    if "Puissance psychique" in list(st.session_state.kai["Mastery"].values) and ennemy_psychique_sensibility:
        ls_hability += 2
        st.write(f"*Puissance psychique: +2 points d'habilité*")
    if not st.session_state.weapon1 and not st.session_state.weapon2:
        st.write(f"*En possession d'aucune arme: -4 points d'habilité*")
        ls_hability -= 4

    return ls_hability

def fight(
    ls_hability: int,
    ls_endurance: int,
    ennemy_hability: int,
    ennemy_endurance: int,
    turn_before_flee: int = 0,
    add_dammage_ennemy: int = 0,
    add_dammage_LS: int = 0,
) -> int:
    """
    Execute a fight between the LS and an opposant.
    turn_before_flee: variable that indicate how many turn the LS needs to fight before he can flee. (if 0, he can't)
    add_dammage_LS: if the LS can add more dammage to its counter (due to certain events). Add it to the dammage done to the ennemy
    add_dammage_ennemy: the ennemy does X dammage in addition. To add to the dammage ammount done by the ennemy
    ennemy_endurance: ennemy endurance
    ennemy_hability: ennemy hability
    ls_endurance: LS endurance
    ls_hability: LS hability
    """
    quotient_attaque = ls_hability - ennemy_hability
    st.write(f"*Votre habilité pour ce combat est de {ls_hability}*")
    st.write(f"*Quotient d'attaque: {quotient_attaque}*")
    turn = 0
    flee = False


    while (ls_endurance > 0) or (ennemy_endurance > 0):

        if ls_endurance < 0:
            break

        if ennemy_endurance < 0:
            break

        st.divider()
        if turn_before_flee != 0:  # == possibility of flee the fight
            if turn == turn_before_flee:
                if st.button("Voulez-vous fuir ?"):  # yes or no
                    st.session_state.flee = True

        turn += 1
        with st.spinner():
            time.sleep(1)
        number = table_des_hasards()
        st.write_stream(stream_text(f"*Vous avez tiré le {number}*"))

        nbre_ls, nbre_ennemy = table_coups(
            quotient_attaque=quotient_attaque, dice_number=number
        )
        total_dammage_against_ls = nbre_ls + add_dammage_ennemy

        with st.chat_message("assistant", avatar="💀"):
            st.write_stream(stream_text(f"Vous perdez {total_dammage_against_ls}"))

        ls_endurance -= total_dammage_against_ls
        if not flee:
            total_dammage_against_ennemy = nbre_ennemy + add_dammage_LS

            with st.chat_message("user", avatar="🛡️️"):
                st.write_stream(stream_text(f"Vous infligez {total_dammage_against_ennemy}"))

            ennemy_endurance -= total_dammage_against_ennemy

        else:
            break # flee

        col1, col2 = st.columns(2)
        col1.metric(label="Endurance", value=ls_endurance, delta=-total_dammage_against_ls)
        col2.metric(label="Ennemi", value=ennemy_endurance, delta=-total_dammage_against_ennemy)

    # for ele in fight_history:
    #     time.sleep(1)
    #     if "infligez" in ele:
    #         with st.chat_message("user", avatar="🛡️"):
    #             st.write(ele)
    #     elif "tiré" in ele:
    #         st.write(ele)
    #     else:
    #         with st.chat_message("assistant", avatar="💀"):
    #             st.write(ele)

    if ls_endurance <= 0:
        ls_death()

    elif ennemy_endurance <= 0:
        st.success("You manage to defeat your ennemy.")
        st.session_state.done_fighting = True
        return ls_endurance

    else:
        st.success(f"You manage to espace")
        st.session_state.done_fighting = True
        return ls_endurance

def table_coups(quotient_attaque: int, dice_number: int) -> tuple[int, int]:
    """
    A partir du quotient d'attaque et d'un chiffre donnée par la table_des_hasards,
    renvoit un tuple(<dommage_LS>, <dommage_ennemi>)
    avec dommage_LS les dommages infligés au Loup Solitaire et dommage_ennemi ceux infligés à l'ennemi
    """
    if quotient_attaque >= 50:
        quotient_attaque = 49
    if quotient_attaque <= -50:
        quotient_attaque = -49

    if quotient_attaque >= 11 and dice_number == 10:
        return 0, T
    elif quotient_attaque >= 9 and dice_number >= 9:
        return 0, T
    elif quotient_attaque >= 5 and dice_number >= 7:
        return 0, 18
    elif quotient_attaque >= 3 and dice_number >= 7:
        return 0, 16
    elif quotient_attaque >= 11 and dice_number == 6:
        return 1, 16
    elif quotient_attaque >= 1 and dice_number >= 7:
        return 0, 14
    elif quotient_attaque >= 9 and dice_number >= 5:
        return 1, 14
    elif quotient_attaque >= 10 and dice_number >= 7:
        return 0, 12
    elif quotient_attaque >= 7 and dice_number == 6:
        return 1, 12
    elif quotient_attaque >= 7 and dice_number in [4, 5]:
        return 2, 12
    elif quotient_attaque in range(-2, 3) and dice_number in [10, 9, 8]:
        return 0, 11
    elif quotient_attaque in range(3, 7) and dice_number in [7, 6]:
        return 1, 11
    elif quotient_attaque in range(7, 50) and dice_number in [3, 4, 5]:
        return 2, 11
    elif quotient_attaque in range(-4, 1) and dice_number in [10, 9, 8]:
        return 0, 10
    elif quotient_attaque == 0 and dice_number == 7:
        return 1, 10
    elif quotient_attaque >= 3 and dice_number in range(1, 7):
        return 2, 10
    elif quotient_attaque in range(-6, -2) and dice_number in [10, 9]:
        return 0, 9
    elif quotient_attaque in range(-2, 1) and dice_number in [7, 8]:
        return 1, 9
    elif quotient_attaque in range(-2, 9) and dice_number in range(3, 7):
        return 2, 9
    elif quotient_attaque in range(9, 50) and dice_number in [1, 2]:
        return 3, 9
    elif quotient_attaque in range(-8, -4) and dice_number in [10, 9]:
        return 0, 8
    elif quotient_attaque in [-4, -3] and dice_number == 8:
        return 1, 8
    elif quotient_attaque in range(-2, 5) and dice_number in range(4, 8):
        return 2, 8
    elif quotient_attaque in range(5, 50) and dice_number in range(1, 4):
        return 3, 8
    elif quotient_attaque in [-10, -9] and dice_number == 10:
        return 0, 7
    elif quotient_attaque in range(-8, 1) and dice_number in range(5, 10):
        return 2, 7
    elif quotient_attaque in range(1, 7) and dice_number in [2, 3, 4]:
        return 3, 7
    elif quotient_attaque in [7, 8] and dice_number == 1:
        return 4, 7
    elif quotient_attaque in range(-50, -10) and dice_number == 10:
        return 0, 6
    elif quotient_attaque in range(-11, 5) and dice_number in range(2, 10):
        return 3, 6
    elif quotient_attaque in [5, 6] and dice_number == 1:
        return 4, 6
    elif quotient_attaque in range(-50, -10) and dice_number == 9:
        return 3, 5
    elif quotient_attaque in range(-10, 5) and dice_number in range(1, 9):
        return 4, 5
    elif quotient_attaque <= -11 and dice_number == 8:
        return 4, 4
    elif quotient_attaque in range(-10, -6) and dice_number in [6, 7]:
        return 5, 4
    elif quotient_attaque in range(-6, 1) and dice_number in range(2, 6):
        return 4, 4
    elif quotient_attaque in [1, 2] and dice_number == 1:
        return 5, 4
    elif quotient_attaque in range(-50, -10) and dice_number == 7:
        return 5, 3
    elif quotient_attaque in [-10, -9] and dice_number == 6:
        return 6, 3
    elif quotient_attaque in range(-8, 1) and dice_number in range(1, 6):
        return 5, 3
    elif quotient_attaque in range(-50, -6) and dice_number in [4, 5, 6]:
        return 6, 2
    elif quotient_attaque in range(-6, 0) and dice_number in [1, 2, 3]:
        return 5, 2
    elif quotient_attaque in range(-50, -8) and dice_number in [4, 5]:
        return 7, 1
    elif quotient_attaque in range(-8, -2) and dice_number in [1, 2, 3]:
        return 6, 1
    elif quotient_attaque <= -9 and dice_number == 4:
        return 8, 0
    elif quotient_attaque in range(-10, -6) and dice_number in [2, 3]:
        return 7, 0
    elif quotient_attaque in [-6, -5] and dice_number == 1:
        return 6, 0
    elif quotient_attaque <= -11 and dice_number == 2:
        return T, 0
    elif quotient_attaque <= -9 and dice_number == 1:
        return T, 0
    elif quotient_attaque <= -11 and dice_number == 3:
        return 8, 0
    elif quotient_attaque <= -9 and dice_number == 2:
        return 8, 0
    elif quotient_attaque in [-8, -7] and dice_number == 1:
        return 8, 0

def stream_text(text: str, time_to_sleep: int = 0.03):
    for word in text.split():
        yield word + " "
        time.sleep(time_to_sleep)

def handle_repas():
    """
    Gère la consommation d'un Repas par le joueur.
    Retire 1 Repas si disponible, ou inflige 3 points de dégâts d'Endurance sinon.
    """
    
    if st.session_state.last_page_number != st.session_state.current_page_number:

        if "La Chasse" in list(st.session_state.kai.to_dict()["Mastery"].values()):
            st.success(
                "*Grâce à votre Maitrise Kai de la Chasse, il vous est inutile de piocher parmi vos rations et vous parvenez à trouver votre nourriture par vous-même.*"
            )
        else:
            # Trouver l'index du premier Repas dans le sac à dos
            repas_index = -1
            for idx, item_name in st.session_state.backpack["Nom"].items():
                if item_name == "Repas":
                    repas_index = idx
                    break

            if repas_index != -1:
                # Repas trouvé : le consommer
                st.session_state.backpack.drop(index=repas_index, inplace=True)
                st.session_state.backpack.reset_index(drop=True, inplace=True)
                st.success("Vous avez mangé. 1 REPAS vous a été retiré.")
            else:
                # Aucun Repas trouvé : perte d'Endurance
                if st.session_state.endurance > 3:
                    st.session_state.endurance -= 3
                    st.metric(label="Endurance", value=st.session_state.endurance, delta=-3)
                    st.error("Vous n'aviez pas de Repas. Vous perdez 3 points d'ENDURANCE.")
                else:
                    # Si la perte d'endurance mène à la mort, nous faisons le calcul
                    st.session_state.endurance = 0
                    st.metric(label="Endurance", value=0, delta=-3)
                    st.error("Vous n'aviez pas de Repas et votre ENDURANCE tombe à zéro.")
                    ls_death()

def ai_generate_page(page_text:str, page_number:int):
    """
    Using gemini to generate page content.

    Args:
        page_text (str): A page
    """
    from google import genai
    from google.genai import types

    print(f"Page number: {page_number}")

    prompt = f"Convertis ce contenu brut de la page {page_number} en script Python Streamlit en appliquant toutes les règles. Le contenu est : \n---\n{page_text}\n---"
    
    with open("template.py", 'r') as template_file:
        template_content = template_file.read()

    instructions = AI_INSTRUCTION.replace("#TEMPLATE#",template_content)

    config = types.GenerateContentConfig(
        system_instruction=instructions,
        temperature=0.0 # Très faible, car nous voulons un formatage précis et non créatif
    )

    try:
        print("Generating response...")
        client = genai.Client(api_key=GEMINI_API_KEY)
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=prompt,
            config=config,
        )

        print("Creating page...")
        file_name = f"pages/page_{page_number}.py"
        with open(file_name, "w", encoding="utf-8") as f:
            code = response.text.strip().replace("```python", "").replace("```", "")
            f.write(code)

        print(f"✅ Fichier {file_name} généré avec succès.")

    except Exception as e:
        print(f"❌ Erreur lors de la génération de la page {page_number}: {e}")

def extract_chapters_from_pdf(pdf_path: str, max_chapters: int = 350) -> dict:
    """
    Extrait le texte d'un PDF, identifie les chapitres par un numéro seul
    sur une ligne, et les stocke dans un dictionnaire.

    Args:
        pdf_path: Chemin vers le fichier PDF de Loup Solitaire.
        max_chapters: Limite supérieure du numéro de chapitre attendu (ex: 350).

    Returns:
        Un dictionnaire {numéro_de_page: contenu_texte_brut}.
    """
    import fitz
    import re
    
    # Nouveau pattern pour détecter un numéro seul sur une ligne.
    # r"^\s*(\d{1,3})\s*$" : Cherche 1 à 3 chiffres (le groupe 1) entourés uniquement d'espaces
    CHAPTER_START_PATTERN = re.compile(r"^\s*(\d{1,3})\s*$")
    
    chapters = {}
    current_page_num = 0
    current_chapter_text = []

    try:
        doc = fitz.open(pdf_path)
    except Exception as e:
        print(f"Erreur lors de l'ouverture du fichier PDF: {e}")
        return {}

    print(f"Nombre de pages dans le PDF: {doc.page_count}")

    for page_num_pdf in range(doc.page_count):
        page = doc.load_page(page_num_pdf)
        text = page.get_text("text")

        lines = text.splitlines()

        for line in lines:
            line_stripped = line.strip()
            
            match = CHAPTER_START_PATTERN.search(line_stripped)
            
            # 1. Tenter de détecter un nouveau marqueur de chapitre
            if match:
                try:
                    new_page_num = int(match.group(1))
                except ValueError:
                    continue # Ce n'est pas un nombre valide

                # Vérifie si le numéro est dans la plage attendue (1 à max_chapters)
                if 1 <= new_page_num <= max_chapters:
                    
                    # 2. Logique de Filtrage des Doublons :
                    # Si le nouveau numéro de page est inférieur ou égal au numéro en cours,
                    # ET si ce numéro a déjà été traité (c'est-à-dire qu'il est déjà dans 'chapters'),
                    # c'est probablement un faux positif (un chiffre seul dans le texte).
                    if new_page_num <= current_page_num and new_page_num in chapters:
                        # On ignore ce marqueur et on le traite comme du texte normal.
                        if len(line_stripped) > 0:
                            current_chapter_text.append(line_stripped)
                        continue
                    
                    # 3. Marqueur valide : Sauvegarder le chapitre précédent
                    if current_page_num != 0:
                        chapters[current_page_num] = "\n".join(current_chapter_text).strip()

                    # Démarrer le nouveau chapitre
                    current_page_num = new_page_num
                    current_chapter_text = []
            
            # 4. Continuer l'accumulation du texte pour le chapitre en cours
            elif current_page_num != 0:
                # Filtre pour éviter les lignes trop courtes (pieds de page, etc.)
                if len(line_stripped) > 5:
                    current_chapter_text.append(line_stripped)

    # Sauvegarder le dernier chapitre
    if current_chapter_text and current_page_num != 0:
        chapters[current_page_num] = "\n".join(current_chapter_text).strip()

    # for number, text in chapters.items():
    #     print("="*50)
    #     print(number)
    #     print(text)

    return chapters


if __name__ == "__main__":
    page_text = """
Vous parvenez bientôt à une petite clairière. En son centre, vous
trouvez un banc taillé dans le tronc d'un arbre.
Vous avez faim, et il vous faut prendre un Repas, sinon, vous
perdrez 3 points d'ENDURANCE. Lorsque vous avez fini de
manger, vous pourrez quitter la clairière par le sud en vous
rendant au 28. Mais si vous préférez emprunter le sentier plus
étroit qui mène vers l'est en s'enfonçant dans la forêt, rendezvous au 201.
"""
    # ai_generate_page(page_number=130, page_text=page_text)
    chapters = extract_chapters_from_pdf(pdf_path="./tome1.pdf")

    for page_number, page_text in chapters.items():
        if int(page_number)<130:
            continue
        ai_generate_page(page_number=page_number, page_text=page_text)
        time.sleep(20)