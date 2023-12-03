import os
import sys
import time
import math
from collections import *

def list_of_files(directory, extension):
 files_names = []
 for filename in os.listdir(directory):
    if filename.endswith(extension):
        files_names.append(filename)
 return files_names

def trouver_dossier(nom_dossier):
    # Récupérer le répertoire racine du projet
    repertoire_racine = os.getcwd()
    # Parcourir récursivement le système de fichiers à partir du répertoire racine
    for dossier_racine, sous_repertoires, fichiers in os.walk(repertoire_racine):
        # Vérifier si le dossier recherché se trouve dans les sous-répertoires
        if nom_dossier in sous_repertoires:
            chemin_dossier = os.path.join(dossier_racine, nom_dossier)
            return chemin_dossier
    # Si le dossier n'est pas trouvé, retourner None
    return None

def print_list(files_names,name_dossier):
# ========== changement en dictionnaire =============== #
    # Associations de chaques prénoms à une présisents par dictionnaire

    #dictionnaire = {cles[i]: files_names[i] for i in range(len(cles))}
    dictionnaire ={}
    for i in range(files_names):
        dictionnaire[files_names[i]] = files_names[i]
    print(f"================ Voici la liste des fichiers qui sont dans {name_dossier} =========================",'\n')
    for cle, valeur in dictionnaire.items():
        print(f"{cle}: {valeur}", end=' \n',)
        print('\n')


# ============ Création des TF =============#
def TF(directory, filename):
    file_path = os.path.join(directory, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        words = content.split()
        word_counts = Counter(words)

    return word_counts

# ================== Création de IDF ================

def IDF(directory):
    # Dictionnaire pour stocker le nombre de dossiers contenant chaque mot
    occ_doc = {}

    # variable compteur total de fichier dans le dossier
    total_doc = 0

    # Parcourir tous les fichiers dans le dossier
    for nom_fichier in os.listdir(directory):
        chemin_fichier = os.path.join(directory, nom_fichier)

        # S'assurer que les éléments dans le dossier sont des fichiers
        if os.path.isfile(chemin_fichier):
            total_doc += 1

            # Lire le contenu du fichier
            with open(chemin_fichier, 'r', encoding='utf-8') as fichier:
                mots_uniques = set(fichier.read().split())

                # Mettre à jour le dictionnaire des occurrences
                for mot in mots_uniques:
                    occ_doc[mot] = occ_doc.get(mot, 0) + 1

    # Calculer le score IDF pour chaque mot
    idf_scores = {}
    for mot, occ in occ_doc.items():
        idf_scores[mot] = math.log(total_doc / (occ + 1))  # Éviter la division par zéro

    return idf_scores

# =================== Création des TF_IDF ====================
def TF_IDF(directory):
    # ============ Calcul de TF-IDF =============#

    # Calculer les scores IDF
    idf_scores = IDF(directory)

    # Initialiser une liste pour stocker les résultats pour chaque président
    tfidf_matrix = []

    for filename in os.listdir(directory):
        # Calculer les TF pour chaque document
        tf_document = TF(directory, filename)

        # Calculer les scores TF-IDF pour chaque document
        tfidf_document = {mot: tf_document[mot] * idf_scores.get(mot, 0) for mot in tf_document}

        # Ajouter les résultats à la matrice
        tfidf_matrix.append(tfidf_document)

    return tfidf_matrix

# ================== Création des fichiers du répertoire "Cleaned" ===========================
def cleaned_files(input_path,output_path):

    m2 = 'Nomination_Mitterrand2.txt'
    accent = {
        'à': 'a', 'â': 'a',
        'ê': 'e', 'è': 'e', 'é': 'e',
        'ù': 'u','ç': 'c','È':'e'
    }

    with open(input_path, "r",encoding="utf-8") as input_file, open(output_path, "w",encoding="utf-8") as output_file:
        mot = input_file.readlines()
        for i in range(len(mot)):
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if 'A' <= mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    output_file.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] in accent:
                    output_file.write(accent [mot[i][j]])
                # Délétion de la ponctuation
                elif mot[i][j] in ["-","'"]:
                    output_file.write(" ")
                elif '!' <= mot[i][j] <= '/':
                    pass
                else:
                    output_file.write(mot[i][j])

def cleaned_directory(directory):
    # Créer le dossier "Cleaned" s'il n'existe pas
    cleaned_folder = "Cleaned"
    if not os.path.exists(cleaned_folder):
        os.makedirs(cleaned_folder)

    for i in os.listdir(directory): # extraction des noms des fichiers puis stockage de ceux-ci dans une liste
        if i.endswith(".txt"):
            input_path = os.path.join(directory, i)
            output_path = os.path.join(cleaned_folder, f"Cleaned_{i}")
            cleaned_files(input_path, output_path)


#================== Fonctionnalités à développer ================================
def mots_moins_importants(matrix):
    mmin = set()
    for i in matrix:
        for mot, score in i.items():
            if score != 0:
                mmin.discard(mot)
            else:
                mmin.add(mot)
    return list(mmin)

def mot_plus_important(tfidf_matrix):
    mmax = {}
    for tfidf_dict in tfidf_matrix:
        for mot, score in tfidf_dict.items():
            mmax[mot] = max(mmax.get(mot, 0), score)
    mot_max = max(mmax, key=mmax.get)
    return mot_max, mmax[mot_max]

def president_parlant_de_la_nation(tfidf_matrix,mot):
    presidents = ["Chirac1", "Chirac2", "Giscard", "Holland", "Macron", "Mitterand1", "Mitterand2", "Sarkozy"]
    mots_nation = {}
    for i, tfidf_dict in enumerate(tfidf_matrix):
        for mot, score in tfidf_dict.items():
            if mot.lower() == mot and score != 0:
                mots_nation[presidents[i]] = score
    if not mots_nation:
        return "Aucun président n'a parlé de la Nation."
    president_max = max(mots_nation, key=mots_nation.get)
    return president_max, mots_nation[president_max]


def premier_president_parlant_de(tfidf_matrix, mot):
    presidents = ["Chirac1", "Chirac2", "Giscard", "Holland", "Macron", "Mitterand1", "Mitterand2", "Sarkozy"]
    for i, tfidf_dict in enumerate(tfidf_matrix):
        if mot.lower() in tfidf_dict and tfidf_dict[mot.lower()] != 0:
            return presidents[i]
    return "Aucun président n'a parlé de {}".format(mot)

def mots_evoques_par_tous(tfidf_matrix, mots_non_importants):
    mots_evoques = set(tfidf_matrix[0].keys())
    for tfidf_dict in tfidf_matrix[1:]:
        mots_evoques.intersection_update(tfidf_dict.keys())
    mots_evoques.difference_update(mots_non_importants)
    return list(mots_evoques)

def mots_plus_repeter_president(directory,president):


    # Calculer les scores IDF
    idf_scores = IDF(directory)

    # Calculer les scores TF-IDF pour le président spécifié
    tfidf_president = {mot: tf_president[mot] * idf_scores.get(mot, 0) for mot in tf_president}

    # Trouver le mot le plus répété
    mot_max = max(tfidf_president, key=tfidf_president.get)
    return mot_max, tfidf_president[mot_max]




# ================================= Les nouvelles différentes langues du menu ===================================
def new_menu_english():
    run1 = True
    while run1 == True:
        print("Hello !\n")
        time.sleep(1)
        print("I'm ChatBot \n")
        time.sleep(1)
        print("Enter one of the numbers \n")
        time.sleep(1)
        print("1 - Get started\n2 - Options\n3 - How does it work ?\n4 - What's my utility ?\n5 - Quit\n")
        lancement = input(":")
        while lancement not in ['1', '2', '3', '4', '5']:
            lancement = input(":")
        if lancement == '1':
            print(
                "Before going any further, you'll need to enter an access path to facilitate my use.")
            reponse = input(
                "Do you know how to add a path ?\n1 - Yes\n2 - No\n3 - Return\n4 _ Quit\n:")
            while reponse not in ['1', '2', '3', '4']:
                reponse = input(":")
            if reponse == '1':  # confimation de passage à l'étape suivante
                pass
            elif reponse == '2':  # Non # qui permet d'expliquer l'ajout d'un chemin si besoin
                print(
                    "To add a path, go to the file or folder you want to add a path to, then right-click on it. \nSelect 'Copy Path' then 'Absolute path', and all that's left to do is paste the path you've just copied. \n")
                pass
            elif reponse == '3':  # Retour
                continue
            elif reponse == '4':  # Quittez
                break

            chemin_valide = False
            while not chemin_valide:
                directory = input(("Enter your path to the 'speeches' folder :"))

                # Vérifier si le chemin existe
                if os.path.exists(directory):
                    chemin_valide = True
                    print("Valid path.")
                else:
                    print("The path is invalid. Please try again.")

            cleaned_directory(directory)
            chemin2_valide = False

            while not chemin2_valide:
                directory1 = input(("Enter your path to the 'Cleaned' folder :"))

                # Vérifier si le chemin existe
                if os.path.exists(directory1):
                    chemin2_valide = True
                    print("Valid path.")
                else:
                    print("The path is invalid. Please try again.")

                # ================== Création des fichiers du répertoire "Cleaned" ===========================
                cleaned(directory)
                tfidf_matrix = TF_IDF(directory1)
                debut = input(
                    "Here we go !\nWhat do you want to know ?\n1 - Know the most important word in a president's speech.\n2 - Know the least important words in a presidential speech.\n3 - Know the words most repeated by a president.\n4 - Know the name of the president who has repeated a particular word the most.\n5 - To know the first president to address a topic.\n6 - To know the words pronounced by all the presidents.\n7 - Return.\n8 - Quit.\n:")
                while debut not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                    debut = input(":")
                if debut == "1":
                    mot_max, score_max = mot_plus_important(tfidf_matrix)
                    print("The most important word in a president's speech :", mot_max)
                    debut = input("What do you want to know ?\n1 - Know the most important word in a president's speech.\n2 - Know the least important words in a presidential speech.\n3 - Know the words most repeated by a president.\n4 - Know the name of the president who has repeated a particular word the most.\n5 - To know the first president to address a topic.\n6 - To know the words pronounced by all the presidents.\n7 - Return.\n8 - Quit.\n:")
                elif debut == "2":
                    print("The least important word in a president's speech :", mots_moins_importants(tfidf_matrix))
                    debut = input("What do you want to know ?\n1 - Know the most important word in a president's speech.\n2 - Know the least important words in a presidential speech.\n3 - Know the words most repeated by a president.\n4 - Know the name of the president who has repeated a particular word the most.\n5 - To know the first president to address a topic.\n6 - To know the words pronounced by all the presidents.\n7 - Return.\n8 - Quit.\n:")
                elif debut == "3":
                    print("For which presidents would you like to know the most frequently used words?\n")
                    president = input(
                        "1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
                    while president not in ["1", "2", "3", "4", "5", "6"]:
                        president = input(
                            "1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
                    if president == "1":
                        print("For which mandate would you like to know its most frequently used words ?")
                        mandat_chirac = input("1 - 1st mandate\n2 - 2nd mandate\n:")
                        while mandat_chirac not in ["1", "2"]:
                            mandat_chirac = input("1 - 1st mandate\n2 - 2nd mandate\n:")
                        if mandat_chirac == "1":
                            mot_max_chirac, score_max_chirac = mots_plus_repeter_president(directory1,"Chirac_mandat1.txt")
                            print("The word most repeated by Jacques Chirac in 1st mandate is :", mot_max_chirac)
                        elif mandat_chirac == "2":
                            mot_max_chirac, score_max_chirac = mots_plus_repeter_president(directory1,"Chirac_mandat2.txt")
                            print("The word most repeated by Jacques Chirac in 2nd mandate is :", mot_max_chirac)
                elif debut == "7":
                    print('\n')
                    continue
                elif debut == "8":
                    break
                    lancement = "5"
                break
                lancement = '5'

        elif lancement == '2':
            option = input("Type a number\n1 - Language\n2 - Credit\n3 - Return\n:")
            while option not in ['1', '2', '3']:
                option = input(":")
            if option == '1':
                langue = input("1 - Français\n2 - English\n3 - Espanõl\n4 - Return\n: ")
                while langue not in ['1', '2', '3', '4']:
                    langue = input(":")
                if langue == '1':
                    run1 = False
                    run2 = False
                elif langue == '2':
                    continue
                elif langue == "3":
                    end = new_menu_spanish()
                    if end == '5':
                        run = False
                        run1 = False
                        run2 = False
                    continue
                elif langue == '4':
                    continue
            elif option == '2':
                print("Program credit")
                time.sleep(1)
                print("produced by : \n")
                time.sleep(1)
                print("Joss DOUNIAMA OKANA\n")
                time.sleep(1)
                print("Liam CROGUENNEC\n")
                time.sleep(1)
                print("Python project\n")
                time.sleep(1)
                print("Group BN 2023-2024\n")
                time.sleep(1)
                print("End\n")
                time.sleep(1)
                continue
            elif option == '3':
                continue
        elif lancement == '3':
            print("\nStart, then follow the instructions. \n")
            continue
        elif lancement == '4':
            print("\nAvailable soon. \n")
            continue
        elif lancement == '5':
            #run1 = False
            #run = False
            #run2 = False
            sys.exit()
            return '5'
        break


def new_menu_spanish():
    run2 = True
    while run2 == True:
        print("Hola !\n")
        time.sleep(1)
        print("Soy ChatBot \n")
        time.sleep(1)
        print("Introduce uno de los números \n")
        time.sleep(1)
        print("1 - ¿Empezar?\n2 - Opciones\n3 - ¿Cómo funciona?\n4 - ¿Para qué sirve?\n5 - Abandone\n")
        lancement = input(":")
        while lancement not in ['1', '2', '3', '4', '5']:
            lancement = input(":")
        if lancement == '1':
            print("Antes de seguir adelante, tendrás que introducir una ruta de acceso para facilitar mi uso.")
            reponse = input(
                "¿Sabes cómo añadir una ruta?\n1 - Sì\n2 - No\n3 - Volver\n4 _ Abandone\n:")
            while reponse not in ['1', '2', '3', '4']:
                reponse = input(":")
            if reponse == '1':  # confimation de passage à l'étape suivante
                pass
            elif reponse == '2':  # Non # qui permet d'expliquer l'ajout d'un chemin si besoin
                print("Para añadir una ruta, vaya al archivo o carpeta al que desea añadir una ruta y haga clic con el botón derecho del ratón. \nSeleccione 'Copiar ruta' y luego 'Ruta absoluta', y ya sólo te quedará pegar la ruta que acabas de copiar. \n")
                pass
            elif reponse == '3':  # Retour
                continue
            elif reponse == '4':  # Quittez
                break
            chemin_valide = False
            while not chemin_valide:
                directory = input(("Introduzca la ruta a la carpeta 'Speeches' : "))

                # Vérifier si le chemin existe
                if os.path.exists(directory):
                    chemin_valide = True
                    print("Ruta de acceso válida.")
                else:
                    print("La ruta no es válida, inténtelo de nuevo.")

            cleaned_directory(directory)
            chemin2_valide = False

            while not chemin2_valide:
                directory1 = input(("Introduzca la ruta a la carpeta 'Cleaned' : "))

                # Vérifier si le chemin existe
                if os.path.exists(directory1):
                    chemin2_valide = True
                    print("Ruta de acceso válida.")
                else:
                    print("La ruta no es válida, inténtelo de nuevo.")

            tfidf_matrix = TF_IDF(directory1)
            debut = input(
                "¡Allá vamos!\n¿Qué quieres saber?\n1 - Conocer la palabra más importante del discurso de un presidente.\n2 - Conocer las palabras menos importantes de un discurso presidencial.\n3 - Conocer las palabras más repetidas por un presidente.\n4 - Saber el nombre del presidente que más ha repetido una determinada palabra.\n5 - Conocer el primer presidente que ha hablado sobre un tema.\n6 - Conocer las palabras pronunciadas por todos los presidentes.\n7 - Volver.\n8 - Salir\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                debut = input(":")
            if debut == "1":
                mot_max, score_max = mot_plus_important(tfidf_matrix)
                print("Le mot le plus important d'un discours de président. :", mot_max)
                debut = input("¿Qué quieres saber?\n1 - Conocer la palabra más importante del discurso de un presidente.\n2 - Conocer las palabras menos importantes de un discurso presidencial.\n3 - Conocer las palabras más repetidas por un presidente.\n4 - Saber el nombre del presidente que más ha repetido una determinada palabra.\n5 - Conocer el primer presidente que ha hablado sobre un tema.\n6 - Conocer las palabras pronunciadas por todos los presidentes.\n7 - Volver.\n8 - Salir\n:")
            elif debut == "2":
                print("Palabras menos importantes:", mots_moins_importants(tfidf_matrix))
                debut = input("¿Qué quieres saber?\n1 - Conocer la palabra más importante del discurso de un presidente.\n2 - Conocer las palabras menos importantes de un discurso presidencial.\n3 - Conocer las palabras más repetidas por un presidente.\n4 - Saber el nombre del presidente que más ha repetido una determinada palabra.\n5 - Conocer el primer presidente que ha hablado sobre un tema.\n6 - Conocer las palabras pronunciadas por todos los presidentes.\n7 - Volver.\n8 - Salir\n:")
            elif debut == "3":
                print("¿Para qué presidentes le gustaría conocer las palabras más utilizadas?\n")
                president = input("1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
                while president not in ["1", "2", "3", "4", "5", "6"]:
                    president = input(
                        "1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
                if president == "1":
                    print("¿Para qué mandato le gustaría conocer las palabras más utilizadas?")
                    mandat_chirac = input("1 - 1er Mandato\n2 - 2º Mandato\n:")
                    while mandat_chirac not in ["1", "2"]:
                        mandat_chirac = input("1 - 1er Mandato\n2 - 2º Mandato\n:")
                    if mandat_chirac == "1":
                        mot_max_chirac, score_max_chirac = mots_plus_repeter_president(directory1, "Chirac_mandat1.txt")
                        print("La palabra más repetida por Chirac en 1er Mandat es :", mot_max_chirac)
                    elif mandat_chirac == "2":
                        mot_max_chirac, score_max_chirac = mots_plus_repeter_president(directory1, "Chirac_mandat2.txt")
                        print("La palabra más repetida por Chirac en 2º Mandat es :", mot_max_chirac)
            elif debut == "7":
                print('\n')
                continue
            elif debut == "8":
                break
                lancement = "5"
            break
            lancement = '5'

        elif lancement == '2':
            option = input("Escribe un número\n1 - Idioma\n2 - Crédito\n3 - Devolución\n:")
            while option not in ['1', '2', '3']:
                option = input(":")
            if option == '1':
                langue = input("1 - Français\n2 - English\n3 - Espanõl\n4 - Devolución\n: ")
                while langue not in ['1', '2', '3', '4']:
                    langue = input(":")
                if langue == '1':
                    run = False
                    run1 = False
                    run2 = False
                elif langue == '2':
                    end = new_menu_english()
                    if end == '5':
                        run = False
                        run1 = False
                        run2 = False
                elif langue == "3":
                    continue
                elif langue == '4':
                    continue
            elif option == '2':
                print("Crédito del programa")
                time.sleep(1)
                print("dirigido por : \n")
                time.sleep(1)
                print("Joss DOUNIAMA OKANA\n")
                time.sleep(1)
                print("Liam DéCROGUENNEC\n")
                time.sleep(1)
                print("Proyecto Python\n")
                time.sleep(1)
                print("Grupo BN 2023-2024\n")
                time.sleep(1)
                print("Fin\n")
                time.sleep(1)
                continue
            elif option == '3':
                continue
        elif lancement == '3':
            print("\nInicie y siga las instrucciones. \n")
            continue
        elif lancement == '4':
            print("\nPronto disponible. \n")
            continue
        elif lancement == '5':
            #run = False
            #run1 = False
            #run2 = False
            sys.exit()
            return '5'
        break