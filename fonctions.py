import os
import time

def list_of_files(directory, extension):
 files_names = []
 for filename in os.listdir(directory):
    if filename.endswith(extension):
        files_names.append(filename)
 return files_names

def print_list(files_names):
    print("=====================")
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

# ======= changement en set ============ #
    '''
    ensemble_resultat = set()
    for sous_liste in files_names:
        for j in sous_liste:
            ensemble_resultat.add(sous_liste)
    # Affichage du résultat
    print(ensemble_resultat)
#'''
# ============ Création des TF =============#
def TF(directory):
    chir = "Chirac_mandat1.txt"
    with open(os.path.join(directory,chir),"r") as ch:
        contenu_ch = ch.read()
        mot_ch = contenu_ch.split()
        print(mot_ch)

    chir2 = "Chirac_mandat2.txt"
    with open(os.path.join(directory, chir2), "r") as ch2:
        contenu_ch2 = ch2.read()
        mot_ch2 = contenu_ch.split()
        print(mot_ch2)

    gis = "Giscard_mandat.txt"
    with open(os.path.join(directory, gis), "r") as gis:
        contenu_gis = gis.read()
        mot_gis = contenu_gis.split()
        print(mot_gis)

    holl = "Holland_mandat.txt"
    with open(os.path.join(directory, holl), "r") as holl:
        contenu_holl = holl.read()
        mot_holl = contenu_holl.split()
        print(mot_holl)

    mac = "Macron_mandat.txt"
    with open(os.path.join(directory, mac), "r") as mac:
        contenu_mac = mac.read()
        mot_mac = contenu_mac.split()
        print(mot_mac)

    mitt = "Mitterrand1_mandat.txt"
    with open(os.path.join(directory, mitt), "r") as mitt:
        contenu_mitt = mitt.read()
        mot_mitt = contenu_mitt.split()
        print(mot_mitt)

    mitt2 = "Mitterrand2_mandat.txt"
    with open(os.path.join(directory, mitt2), "r") as mitt2:
        contenu_mitt2 = mitt2.read()
        mot_mitt2 = contenu_mitt2.split()
        print(mot_mitt2)

    sarko = "Sarkozy_mandat.txt"
    with open(os.path.join(directory, sarko), "r") as sarko:
        contenu_sarko = sarko.read()
        mot_sarko = contenu_sarko.split()
        print(mot_sarko)


# ================== Création des fichiers du répertoire "Cleaned" ===========================
def cleaned(directory):
    ch = 'Nomination_Chirac1.txt'
    with open(os.path.join(directory,ch), "r") as Chirac1, open("Cleaned/Chirac_mandat1.txt", "w") as cm1:
        mot = Chirac1.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    cm1.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    cm1.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    cm1.write(mot[i][j])

    ch1 = 'Nomination_Chirac2.txt'
    with open(os.path.join(directory,ch1), "r") as Chirac2, open("Cleaned/Chirac_mandat2.txt", "w") as cm2:
        mot = Chirac2.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    cm2.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    cm2.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    cm2.write(mot[i][j])

    gd = 'Nomination_Giscard dEstaing.txt'
    with open(os.path.join(directory,gd), "r") as Giscard, open("Cleaned/Giscard_mandat.txt", "w") as gdm:
        mot = Giscard.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    gdm.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    gdm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    gdm.write(mot[i][j])

    h = 'Nomination_Hollande.txt'
    with open(os.path.join(directory,h), "r") as Holland, open("Cleaned/Holland_mandat.txt", "w") as hm:
        mot = Holland.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    hm.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    hm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    hm.write(mot[i][j])

    ma = 'Nomination_Macron.txt'
    with open(os.path.join(directory,ma), "r") as Holland, open("Cleaned/Macron_mandat.txt", "w") as mam:
        mot = Holland.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    mam.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    mam.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    mam.write(mot[i][j])

    m = 'Nomination_Mitterrand1.txt'
    with open(os.path.join(directory,m), "r") as Mitterand, open("Cleaned/Mitterrand1_mandat.txt", "w") as mm:
        mot = Mitterand.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    mm.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    mm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    mm.write(mot[i][j])

    m2 = 'Nomination_Mitterrand2.txt'
    with open(os.path.join(directory,m2), "r") as Mitterand2, open("Cleaned/Mitterrand2_mandat.txt", "w") as mm2:
        mot = Mitterand2.readlines()
        for i in range(len(mot)):
            # t = Chirac1.readline()
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    mm2.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    mm2.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    mm2.write(mot[i][j])

    s = 'Nomination_Sarkozy.txt'
    with open(os.path.join(directory,s), "r") as Sarkozy, open("Cleaned/Sarkozy_mandat.txt", "w") as sm:
        mot = Sarkozy.readlines()
        for i in range(len(mot)):
            for j in range(len(mot[i])):
                # Passage des lettres en minuscule
                if mot[i][j] >= 'A' and mot[i][j] <= 'Z':
                    temp = ord(mot[i][j])
                    Mot_minuscule = chr(temp + 32)
                    sm.write(Mot_minuscule)
                # Délétion de la ponctuation
                elif mot[i][j] == "-" or mot[i][j] == "'":
                    sm.write(" ")
                elif mot[i][j] >= '!' and mot[i][j] <= '/' or mot[i][j] == '`':
                    pass
                else:
                    sm.write(mot[i][j])

# ================================= Les différentes langues du menu ===================================
def menu_french():
    # boucle du menu
    run = False
    while run == False:
        print("Bonjour ! " '\n')
        time.sleep(1)
        print("Je suis ChatBot \n")
        time.sleep(1)
        lancement = input("Êtes vous prêt(e) à commencer ? : ")
        time.sleep(1.5)
        if lancement.lower() in ['non', 'no', 'une prochaine fois', 'apres', 'après', 'demain']:
            print("Au revoir !")
            break
        elif lancement.lower() in ['oui', 'ok', 'yes', 'je suis prêt', 'vas y', 'vasy', 'je suis pret', "let's go",
                                   'let s go', 'lets go']:
            print("Commençons !\n")

        while lancement.lower() not in ['oui', 'ok', 'yes', 'je suis prêt', 'vas y', 'vasy', 'je suis pret', "let's go",
                                        'let s go', 'lets go']:
            print("Désolé je n'ai pas compris votre réponse. \nVeuillez réésayer !")
            lancement = input("Prêt ? :")

        print("Avant d'aller plus loin, vous allez devoir saisir un chemin d'accès pour faciliter mon utilisation. ")
        reponse = input("Savez vous comment ajouter un chemin d'accès ? \n"
                        "réponse : ")
        while reponse.lower() not in ['oui', 'yes', 'bien sûr', 'je sais', 'bien sur'] or reponse.lower() not in ['non','no','je ne connais pas','je ne sais pas']:
            if reponse.lower() in ['oui', 'yes', 'bien sûr', 'je sais']:
                break
            elif reponse.lower() in ['non', 'no', 'je ne connais pas', 'je ne sais pas', 'explique', 'dit moi tous']:
                print(
                    "Pour ajouter un chemin d'accès, vous devez aller sur le fichier ou dossier que vous voulez son chemin d'accès, puis faites un clique droit. \nSéléctionnez 'Copy Path' puis 'Absolue path' et il ne vous restera plus qu'à coller le chemin d'accès que vous venez de copier \n")
                break
            else:
                print("Désolé je n'ai pas compris votre réponse. \n"
                      "Veuillez rééssayer !")
                reponse = input("réponse : ")

        # ========== Affichage des présidents =====================
        # '''
        directory = None
        while directory == None:
            directory = input(("Saissisez votre chemin d'accès du dossier 'speeches' : "))
        run = True
            # la saisie de l'accès au chemin permettra à n'importe quels utilisateurs d'utiliser le programme
    return directory



def menu_english():
    # boucle du menu
    run = False
    while run == False:
        print("Hello ! " '\n')
        time.sleep(1)
        print("I'm ChatBot \n")
        time.sleep(1)
        lancement = input("Are you ready to get started ? : ")
        time.sleep(1.5)
        if lancement.lower() in ['non', 'no', 'next time', 'after', 'tomorrow','later','afterwards']:
            print("Goodbye !")
            break
        elif lancement.lower() in ['oui', 'ok', 'yes', "i'm ready", 'go ahead','im ready','i m ready', "let's go",'let s go', 'lets go']:
            print("Let's get started !\n")

        while lancement.lower() not in ['oui', 'ok', 'yes', "i'm ready", 'go ahead','im ready','i m ready', "let's go",'let s go', 'lets go']:
            print("Sorry, I didn't understand your answer. \nPlease try again !")
            lancement = input("Ready ? :")

        print("Before going any further, you'll need to enter an access path to facilitate my use. ")
        reponse = input("Do you know how to add a path ? \n"
                        "answer : ")
        while reponse.lower() not in ['oui', 'yes', 'of course', 'i know','sure'] or reponse.lower() not in ['non', 'no', "I don't know", "I don't know", 'Explain', 'Tell me all about it']:
            if reponse.lower() in ['oui', 'yes', 'of course', 'i know','sure']:
                break
            elif reponse.lower() in ['non', 'no', "I don't know", "I don't know", 'Explain', 'Tell me all about it']:
                print(
                    "To add a path, go to the file or folder you want to add the path to, then right-click on it. \nSelect 'Copy Path' then 'Absolute path' and all you have to do is paste the path you've just copied \n")
                break
            else:
                print("Sorry, I didn't understand your answer. \n"
                      "Please try again !")
                reponse = input("answer : ")

        # ========== Affichage des présidents =====================
        # '''
        directory = None
        while directory == None:
            directory = input(("Enter your 'speeches' folder path:"))
        run = True
            # la saisie de l'accès au chemin permettra à n'importe quels utilisateurs d'utiliser le programme
    return directory


def menu_spanish():
    # boucle du menu
    run = False
    while run == False:
        print("Hola ! " '\n')
        time.sleep(1)
        print("Soy ChatBot \n")
        time.sleep(1)
        lancement = input("¿Estás listo para empezar? : ")
        time.sleep(1.5)
        if lancement.lower() in ['non', 'no', 'mañana','después de','la próxima vez' ]:
            print("Adiós !")
            break
        elif lancement.lower() in ['oui','ok','si','sí','estoy listo','vamos']:
            print("Comencemos !\n")

        while lancement.lower() not in ['oui','ok','si','sí','estoy listo','vamos']:
            print("Lo siento, no entendí su respuesta. \nPor favor, inténtelo de nuevo.")
            lancement = input("¿Preparado ? :")

        print("Antes de seguir adelante, tendrás que introducir una ruta para facilitar su uso. ")
        reponse = input("¿Sabes cómo añadir una ruta ? \n"
                        "responder : ")
        while reponse.lower() not in ['oui', "sí",'si', "por supuesto", "lo sé"] or reponse.lower() not in ['non', 'no', 'no lo sé', 'no lo sé', 'explícame', 'cuéntamelo todo']:
            if reponse.lower() in ['oui', "sí",'si', "por supuesto", "lo sé"]:
                break
            elif reponse.lower() in ['non', 'no', 'no lo sé', 'no lo sé', 'explícame', 'cuéntamelo todo']:
                print("Para añadir una ruta, tienes que ir al archivo o carpeta de la que quieres su ruta, luego hacer clic con el botón derecho. \nSelecciona 'Copiar ruta' y luego 'Ruta absoluta' y todo lo que tienes que hacer es pegar la ruta que acabas de copiar \n")
                break
            else:
                print("Lo siento, no he entendido su respuesta. \n"
                      "Por favor, inténtelo de nuevo !")
                reponse = input("responder : ")

        # ========== Affichage des présidents =====================
        # '''
        directory = None
        while directory == None:
            directory = input(("Introduzca la ruta de su carpeta 'speeches' : "))
        run = True
            # la saisie de l'accès au chemin permettra à n'importe quels utilisateurs d'utiliser le programme
    return directory





# =========================== Choix d'une langue pour le menu ============================
def langue():
    directory = None
    langues = ['Veuillez choisir une langue', 'Please select a language', 'Seleccione una lengua', ]
    language = 'saisir'
    while language.lower not in ['francais', 'français', 'french', 'francès', 'anglais', 'english', 'ingles', 'inglés',
                                 'espagnol', 'espanõl', 'espanol', 'spanish']:
        for i in langues:
            print(i, '\n')
            time.sleep(1)
        language = input(": ")
        if language.lower() in ['francais', 'français', 'french', 'francès']:
            print("Vous êtes sûr ? \n")
            confirmation = input(":")
            if confirmation.lower() in ['oui', 'yes', 'bien sûr', 'je sais', 'bien sur']:
                directory = menu_french()
                return directory
            else:
                langue()
        elif language.lower() in ['anglais', 'english', 'ingles', 'inglés']:
            directory = menu_english()
            return directory
        elif language.lower() in ['ingles', 'inglés', 'espagnol', 'espanõl', 'espanol', 'spanish']:
            directory = menu_spanish()
            return directory
        else:
            no = ['Désolé nous avons pas encore cette langue dans notre répertoire.\nVeuillez recommencer \n',
                  "Sorry, we don't have this language in our repertoire yet.\nPlease start again \n",
                  "Lo sentimos, aún no tenemos este idioma en nuestro repertorio.\nPor favor, empieza de nuevo \n"]
            for i in no:
                print(i, '\n')
                time.sleep(1.5)





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
        print("1 - Get started\n2 - Options\n3 - How does it work ?\n4 - What's it for?\n5 - Quit\n")
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
            directory = None
            while directory is None:
                directory = input(("Enter your 'speeches' folder path:"))
                # directory = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\speeches-20231110'

                files_names = list_of_files(directory, "txt")
                print_list(files_names)

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
    #run2 = True
    #while run2 == True:
    # appel de la fonction pour choisir la langue du menu
    # directory = langue()
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
            print(
                "Antes de seguir adelante, tendrás que introducir una ruta de acceso para facilitar mi uso.")
            reponse = input(
                "¿Sabes cómo añadir una ruta?\n1 - Sì\n2 - No\n3 - Volver\n4 _ Abandone\n:")
            while reponse not in ['1', '2', '3', '4']:
                reponse = input(":")
            if reponse == '1':  # confimation de passage à l'étape suivante
                pass
            elif reponse == '2':  # Non # qui permet d'expliquer l'ajout d'un chemin si besoin
                print(
                    "Para añadir una ruta, vaya al archivo o carpeta al que desea añadir una ruta y haga clic con el botón derecho del ratón. \nSeleccione 'Copiar ruta' y luego 'Ruta absoluta', y ya sólo te quedará pegar la ruta que acabas de copiar. \n")
                pass
            elif reponse == '3':  # Retour
                continue
            elif reponse == '4':  # Quittez
                break
            directory = None
            while directory is None:
                directory = input(("Introduzca la ruta a su carpeta 'speeches':"))
                # directory = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\speeches-20231110'

                files_names = list_of_files(directory, "txt")
                print_list(files_names)

                # ================== Création des fichiers du répertoire "Cleaned" ===========================
                cleaned(directory)
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