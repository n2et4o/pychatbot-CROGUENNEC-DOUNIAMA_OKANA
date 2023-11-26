import os
import time
import math
from collections import *

def list_of_files(directory, extension):
 files_names = []
 for filename in os.listdir(directory):
    if filename.endswith(extension):
        files_names.append(filename)
 return files_names

def print_list(files_names):
    for i in files_names:
        print(i, '\n')

# ========== changement en dictionnaire =============== #
    # Associations de chaques prénoms à une présisents par dictionnaire

    cles = ['jacques1','Jacques2','Valéry','François','Emmanuel','François_Mitterand1','François_Mitterand2','Nicolas']
    #dictionnaire = {cles[i]: files_names[i] for i in range(len(cles))}
    dictionnaire ={}
    for i in range(len(cles)):
        dictionnaire[cles[i]] = files_names[i]
    print("================ dictionnaire =========================",'\n')
    for cle, valeur in dictionnaire.items():
        print(f"{cle}: {valeur}", end=' \n',)
        print('\n')


# ============ Création des TF =============#
def TF_Chirac1(directory):
    chir = "Chirac_mandat1.txt"
    with open(os.path.join(directory,chir),"r") as ch:
        contenu_ch = ch.read()
        # la fonction split qui nous permet de créer une liste à partir de notre fichier
        mot_ch = contenu_ch.split()
        # la fonction counter qui nous permet de determiner le nombre occurrence dans notre liste
        nb_motc = Counter(mot_ch)
    return nb_motc


def TF_Chirac2(directory):
    chir2 = "Chirac_mandat2.txt"
    with open(os.path.join(directory, chir2), "r") as ch2:
        contenu_ch2 = ch2.read()
        mot_ch2 = contenu_ch2.split()
        nb_motch2 = Counter(mot_ch2)

    return nb_motch2

def TF_Giscard(directory):
    gis = "Giscard_mandat.txt"
    with open(os.path.join(directory, gis), "r") as gis:
        contenu_gis = gis.read()
        mot_gis = contenu_gis.split()
        nb_motgis = Counter(mot_gis)
    return nb_motgis


def TF_Holland(directory):
    holl = "Holland_mandat.txt"
    with open(os.path.join(directory, holl), "r") as holl:
        contenu_holl = holl.read()
        mot_holl = contenu_holl.split()
        nb_motholl = Counter(mot_holl)
    return nb_motholl
def TF_Macron(directory):
    mac = "Macron_mandat.txt"
    with open(os.path.join(directory, mac), "r") as mac:
        contenu_mac = mac.read()
        mot_mac = contenu_mac.split()
        print(mot_mac)

def TF_Mitterand1(directory):
    mitt = "Mitterrand1_mandat.txt"
    with open(os.path.join(directory, mitt), "r") as mitt:
        contenu_mitt = mitt.read()
        mot_mitt = contenu_mitt.split()
        nb_motmitt = Counter(mot_mitt)
    return nb_motmitt

def TF_Mitterand2(directory):
    mitt2 = "Mitterrand2_mandat.txt"
    with open(os.path.join(directory, mitt2), "r") as mitt2:
        contenu_mitt2 = mitt2.read()
        mot_mitt2 = contenu_mitt2.split()
        nb_motmitt2 = Counter(mot_mitt2)
    return nb_motmitt2
def TF_Sarkozy(directory):
    sarko = "Sarkozy_mandat.txt"
    with open(os.path.join(directory, sarko), "r") as sarko:
        contenu_sarko = sarko.read()
        mot_sarko = contenu_sarko.split()
        nb_motsarko = Counter(mot_sarko)
    return nb_motsarko

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

    # Calculer les TF pour chaque document
    tf_chirac1 = TF_Chirac1(directory)
    tf_chirac2 = TF_Chirac2(directory)
    tf_giscard = TF_Giscard(directory)
    tf_holland = TF_Holland(directory)
    tf_macron = TF_Macron(directory)
    tf_mitterand1 = TF_Mitterand1(directory)
    tf_mitterand2 = TF_Mitterand2(directory)
    tf_sarkozy = TF_Sarkozy(directory)

    # Calculer les scores IDF
    idf_scores = IDF(directory)

    # Calculer les scores TF-IDF pour chaque document
    tfidf_chirac1 = {mot: tf_chirac1[mot] * idf_scores.get(mot, 0) for mot in tf_chirac1}
    tfidf_chirac2 = {mot: tf_chirac2[mot] * idf_scores.get(mot, 0) for mot in tf_chirac2}
    tfidf_giscard = {mot: tf_giscard[mot] * idf_scores.get(mot, 0) for mot in tf_giscard}
    tfidf_holland = {mot: tf_holland[mot] * idf_scores.get(mot, 0) for mot in tf_holland}
    tfidf_macron = {mot: tf_macron[mot] * idf_scores.get(mot, 0) for mot in tf_macron}
    tfidf_mitterand1 = {mot: tf_mitterand1[mot] * idf_scores.get(mot, 0) for mot in tf_mitterand1}
    tfidf_mitterand2 = {mot: tf_mitterand2[mot] * idf_scores.get(mot, 0) for mot in tf_mitterand2}
    tfidf_sarkozy = {mot: tf_sarkozy[mot] * idf_scores.get(mot, 0) for mot in tf_sarkozy}

    # Créer la matrice TF-IDF
    tfidf_matrix = [tfidf_chirac1, tfidf_chirac2, tfidf_giscard, tfidf_holland,
                    tfidf_macron, tfidf_mitterand1, tfidf_mitterand2, tfidf_sarkozy]

    return tfidf_matrix

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

def mots_plus_repeter_president(tf_function, directory):
    tf_president = tf_function(directory)
    mots_president = tf_president(president)
    mot_max = max(mots_president, key=mots_president.get)
    return mot_max, mots_president[mot_max]

# ================== Création des fichiers du répertoire "Cleaned" ===========================
def cleaned(directory):
    ch = 'Nomination_Chirac1.txt'
    with open(os.path.join(directory,ch), "r",encoding="utf-8") as Chirac1, open("Cleaned/Chirac_mandat1.txt", "w",encoding = "utf-8") as cm1:
        mot = Chirac1.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    cm1.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    cm1.write('u')
                elif mot[i][j] == 'ç':
                    cm1.write('c')
                elif mot[i][j] == 'à' or mot[i][j] == 'â':
                    cm1.write('a')
                elif mot[i][j] in ['é', 'è', 'ê', 'È']:
                    cm1.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    cm1.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass

                else:
                    cm1.write(mot[i][j])

    ch1 = 'Nomination_Chirac2.txt'
    with open(os.path.join(directory,ch1), "r",encoding = "utf-8") as Chirac2, open("Cleaned/Chirac_mandat2.txt", "w",encoding = "utf-8") as cm2:
        mot = Chirac2.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    cm2.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    cm2.write('u')
                elif mot[i][j] == 'ç':
                    cm2.write('c')
                elif mot[i][j] == 'à' or mot[i][j] == 'â':
                    cm2.write('a')
                elif mot[i][j] in ['é', 'è', 'ê', 'È']:
                    cm2.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    cm2.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass
                else:
                    cm2.write(mot[i][j])

    gd = 'Nomination_Giscard dEstaing.txt'
    with open(os.path.join(directory,gd), "r",encoding = "utf-8") as Giscard, open("Cleaned/Giscard_mandat.txt", "w",encoding = "utf-8") as gdm:
        mot = Giscard.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    gdm.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    gdm.write('u')
                elif mot[i][j] == 'ç':
                    gdm.write('c')
                elif mot[i][j] == 'à' or mot[i][j] == 'â':
                    gdm.write('a')
                elif mot[i][j] in ['é', 'è', 'ê', 'È']:
                    gdm.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    gdm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass
                else:
                    gdm.write(mot[i][j])

    h = 'Nomination_Hollande.txt'
    with open(os.path.join(directory,h), "r",encoding="utf-8") as Holland, open("Cleaned/Holland_mandat.txt", "w",encoding = "utf-8") as hm:
        mot = Holland.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    hm.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    hm.write('u')
                elif mot[i][j] == 'ç':
                    hm.write('c')
                elif mot[i][j] == 'à' or mot[i][j] == 'â':
                    hm.write('a')
                elif mot[i][j] in ['é', 'è', 'ê', 'È']:
                    hm.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    hm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass
                else:
                    hm.write(mot[i][j])

    ma = 'Nomination_Macron.txt'
    with open(os.path.join(directory,ma), "r",encoding="utf-8") as Holland, open("Cleaned/Macron_mandat.txt", "w",encoding = "utf-8") as mam:
        mot = Holland.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    mam.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    mam.write('u')
                elif mot[i][j] == 'ç':
                    mam.write('c')
                elif mot[i][j] == 'à' or mot[i][j] == 'â':
                    mam.write('a')
                elif mot[i][j] in ['é','è','ê','È'] :
                    mam.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    mam.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass
                else:
                    mam.write(mot[i][j])

    m = 'Nomination_Mitterrand1.txt'
    with open(os.path.join(directory,m), "r",encoding="utf-8") as Mitterand, open("Cleaned/Mitterrand1_mandat.txt", "w",encoding = "utf-8") as mm:
        mot = Mitterand.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    mm.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    mm.write('u')
                elif mot[i][j] == 'ç':
                    mm.write('c')
                elif mot[i][j] == '131' and mot[i][j] == '134':
                    mm.write('a')
                elif mot[i][j] in ['é', 'è', 'ê', 'È']:
                    mm.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    mm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass
                else:
                    mm.write(mot[i][j])

    m2 = 'Nomination_Mitterrand2.txt'
    accent = {
        'à': 'a', 'â': 'a',
        'ê': 'e', 'è': 'e', 'é': 'e',
        'ù': 'u','ç': 'c','È':'e'
    }

    with open(os.path.join(directory, m2), "r",encoding="utf-8") as Mitterand2, open("Cleaned/Mitterrand2_mandat.txt", "w",encoding="utf-8") as mm2:
        mot = Mitterand2.readlines()
        for i in range(len(mot)):
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if 'A' <= mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    mm2.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] in accent:
                    mm2.write(accent [mot[i][j]])
                # Délétion de la ponctuation
                elif mot[i][j] in ["-","'"]:
                    mm2.write(" ")
                elif '!' <= mot[i][j] <= '/':
                    pass
                else:
                    mm2.write(mot[i][j])

    s = 'Nomination_Sarkozy.txt'
    with open(os.path.join(directory,s), "r") as Sarkozy, open("Cleaned/Sarkozy_mandat.txt", "w",encoding = "utf-8") as sm:
        mot = Sarkozy.readlines()
        for i in range(len(mot)):
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    sm.write(Mot_minuscule)
                # suppression de tous les accents
                elif mot[i][j] == 'ù':
                    sm.write('u')
                elif mot[i][j] == 'ç':
                    sm.write('c')
                elif mot[i][j] == 'à' or mot[i][j] == 'â':
                    sm.write('a')
                elif mot[i][j] == 'ê' or mot[i][j] == 'è' or mot[i][j] == 'é':
                    sm.write('e')
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    sm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/':
                    pass
                else:
                    sm.write(mot[i][j])


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

            cleaned(directory)
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
        elif lancement == '2':
            option = input("Type a number\n1 - Language\n2 - Credit\n3 - Return\n:")
            while option not in ['1', '2', '3']:
                option = input(":")
            if option == '1':
                langue = input("1 - Français\n2 - English\n3 - Espanõl\n4 - Return\n: ")
                while langue not in ['1', '2', '3', '4']:
                    langue = input(":")
                if langue == '1':
                    #run = False
                    run1 = False
                    run2 = False
                elif langue == '2':
                    # print("Bientôt disponible.\n ")
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
            run1 = False
            run = False
            run2 = False
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

            cleaned(directory)
            chemin2_valide = False

            while not chemin2_valide:
                directory1 = input(("Introduzca la ruta a la carpeta 'Cleaned' : "))

                # Vérifier si le chemin existe
                if os.path.exists(directory1):
                    chemin2_valide = True
                    print("Ruta de acceso válida.")
                else:
                    print("La ruta no es válida, inténtelo de nuevo.")

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
                print("Liam CROGUENNEC\n")
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
            run = False
            run1 = False
            run2 = False
            return '5'
        break