'''#and lancement not in ['non','no','No','NON']:
        #if 'oui' in lancement or 'yes' in lancement:
            #print("Commençons !")
            #break
        #elif lancement in ['non','no','No','NON'] :
         #   print("Au revoir !")
          #  run = True
           # break
        #else :

        # Boucle pour l'affichage d'un dictionnaire

        for mot, occ in nb_motc.items():
            print(f"Le mot '{mot}' apparaît {occ} fois.")


        '''

'''
        somme = 0
        if nb_motc > 0:
            somme += 1
        elif nb_motsarko > 0:
            somme += 1
        elif nb_motmitt2 > 0:
            somme += 1
        elif nb_motmitt > 0:
            somme += 1
        elif nb_motmac > 0:
            somme += 1
        elif nb_motholl > 0:
            somme += 1
        elif nb_motgis > 0:
            somme += 1
        elif nb_motch2 > 0:
            somme += 1
        elif nb_motch > 0:
            somme += 1
        '''

'''
chir = "Chirac_mandat1.txt"
    with open(os.path.join(directory, chir), "r") as ch:
        contenu_ch = ch.read()
        # la fonction split qui nous permet de créer une liste à partir de notre fichier
        mot_ch = contenu_ch.split()
        # la fonction counter qui nous permet de determiner le nombre occurrence dans notre liste
        nb_motc = Counter(mot_ch)

        tf_ch = []
        for mot, occ in nb_motc.items():
            mot = math.log(8 / (occ + 1))
            tf_ch.append(mot)
            # print(mot)  "verification de le valeur de mots après calcul
            TF_ch = dict(zip(nb_motc.keys(), tf_ch))
        for i in TF_ch.items():
            print(i)

        fichiers_et_repertoires = os.listdir(directory)
        print(fichiers_et_repertoires)

'''

# ======= changement en set ============ #
'''
    ensemble_resultat = set()
    for sous_liste in files_names:
        for j in sous_liste:
            ensemble_resultat.add(sous_liste)
    # Affichage du résultat
    print(ensemble_resultat)
#'''

'''
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
        
        directory = None
        while directory == None:
            directory = input(("Introduzca la ruta de su carpeta 'speeches' : "))
        run = True
            # la saisie de l'accès au chemin permettra à n'importe quels utilisateurs d'utiliser le programme
    return directory

'''

'''



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
'''

'''
directory = langue()
files_names = list_of_files(directory, "txt")
print_list(files_names)
            # ================== Création des fichiers du répertoire "Cleaned" ===========================
cleaned(directory)
#'''



''' # calcul de TF avec la formule de TF = nb occurence d'un mot / nb total de mots 
        tf_ch = []
        for mot, occ in nb_motc.items():
            #print(f"Le mot '{mot}' apparaît {occ} fois.") # verification des valeurs de chaques mots
            # mot correspond à la clé et occ correspond à la valeur associée à la clé
            mot = occ / len(contenu_ch)
            tf_ch.append(mot)
            #print(mot)  "verification de le valeur de mots après calcul
            TF_ch = dict(zip(nb_motc.keys(), tf_ch))
        for i in TF_ch.items():
            print(i) 
            
            '''
# Afficher les scores IDF pour chaque mot # Et verification des valeurs
'''for mot, score in idf.items():
    print(f"{mot}: {score}")
'''

'''
tf_ch = TF_Chirac1(directory1)
        for mot, score in tf_ch.items():
            print(f"{mot}: {score}")
        idf = IDF(directory1)
'''

# appel de la fonction pour choisir la langue du menu
#directory = langue()
#global run
#'''

'''
 print(
            "Avant d'aller plus loin, vous allez devoir saisir un chemin d'accès pour faciliter mon utilisation. ")
        reponse = input(
            "Savez vous comment ajouter un chemin d'accès ?\n1 - Oui\n2 - Non\n3 - Retour\n4 _ Quittez\n:")
        while reponse not in ['1', '2', '3', '4']:
            reponse = input(":")
        if reponse == '1':  # confimation de passage à l'étape suivante
            pass
        elif reponse == '2':  # Non # qui permet d'expliquer l'ajout d'un chemin si besoin
            print(
                "Pour ajouter un chemin d'accès, vous devez aller sur le fichier ou dossier sur lequel vous voulez son chemin d'accès, puis faites un clique droit. \nSéléctionnez 'Copy Path' puis 'Absolue path' et il ne vous restera plus qu'à coller le chemin d'accès que vous venez de copier \n")
            pass
        elif reponse == '3':  # Retour
            continue
        elif reponse == '4':  # Quittez
            break

        chemin_valide = False
        while not chemin_valide:
            directory = input("Saissisez votre chemin d'accès du dossier 'speeches' : ")

            # Vérifier si le chemin existe
            if os.path.exists(directory):
                chemin_valide = True
                print("\nChemin d'accès valide.\n")
            else:
                print("\nLe chemin d'accès n'est pas valide. Veuillez réessayer.\n")

        # Accès rapide pour les développeurs
        #directory = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\speeches-20231110'

        files_names = list_of_files(directory, "txt")
        print_list(files_names)
        # ================== Création des fichiers du répertoire "Cleaned" ===========================
        cleaned(directory)
        print("Félicitation1 ! Vous avez réussit. Vous venez de créer des fichiers qui sont dans le dossier cleaned.")
        firt_stage = input("\n1 - continuer\n2 - Retour\n3 - Quitter\n:")
        while firt_stage not in ["1","2","3"]:
            firt_stage = input("\n1 - continuer\n2 - Retour\n3 - Quitter\n:")
        if firt_stage == "1":
            pass
        elif firt_stage == "2":
            continue
        elif firt_stage == "3":
            print("Au revoir !")
            break
            lancement = '5'
        chemin2_valide = False
        directory1 = None
        while not chemin2_valide or directory1 == directory :
            directory1 = input(("Saissisez votre chemin d'accès du dossier 'Cleaned' : "))

            # Vérifier si le chemin existe
            if os.path.exists(directory1) and directory1 != directory:
                chemin2_valide = True
                print("\nChemin d'accès valide.\n")
            elif directory1 == directory:
                print("\nCe chemin d'accès est le même que celui du dossier 'Speeches'. Veuillez réessayer.\n")
            else:
                print("\nLe chemin d'accès n'est pas valide. Veuillez réessayer.\n")

        # Accès rapide pour les développeurs
        #directory1 = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\Cleaned'
'''
# ========================= cleaned_first_version ================================
'''
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
'''

# ============================= TF_IDF ==================================================
'''
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
    tfidf_macron =  {mot: tf_macron[mot] * idf_scores.get(mot, 0) for mot in tf_macron}
    tfidf_mitterand1 = {mot: tf_mitterand1[mot] * idf_scores.get(mot, 0) for mot in tf_mitterand1}
    tfidf_mitterand2 = {mot: tf_mitterand2[mot] * idf_scores.get(mot, 0) for mot in tf_mitterand2}
    tfidf_sarkozy = {mot: tf_sarkozy[mot] * idf_scores.get(mot, 0) for mot in tf_sarkozy}

    # Créer la matrice TF-IDF
    tfidf_matrix = [tfidf_chirac1, tfidf_chirac2, tfidf_giscard, tfidf_holland,
                    tfidf_macron, tfidf_mitterand1, tfidf_mitterand2, tfidf_sarkozy]

'''
# ======================= first_TF ========================
'''
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
        nb_motmac = Counter(mot_mac)
    return nb_motmac

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
    
'''

'''print("saississez le nom de votre dossier \U0001F5C2")
        path = None
        error = 0
        while path == None:
            name_dossier = input(':')
            path = trouver_dossier(name_dossier)
            if path:
                print(f"Le dossier '{name_dossier}' a été trouvé à l'emplacement : {path}")
            else:
                print(f"Le dossier '{name_dossier}' n'a pas été trouvé.\nVeillez réessayer")
                error += 1
                if error == 3:
                    print("Astuce\nPour vous assurer que bien saisir le nom de votre dossier, il est préférable de copier son nom directement son nom depuis le dossier" )

        firt_stage = input("\n1 - continuer\n2 - Voir le contenu du dossier\n3 - Retour\n4 - Quitter\n:")
        while firt_stage not in ["1", "2", "3","4"]:
            firt_stage = input("\n1 - continuer\n2 - Voir le contenu du dossier\n3 - Retour\n4 - Quitter\n:")
        if firt_stage == "1":
            pass
        elif firt_stage == "2":
            liste = list_of_files(path,"txt")
            print_list(liste,name_dossier)
            time.sleep(3)
            print('\n')
        elif firt_stage == "3":
            continue
        elif firt_stage == "4":
            print("Au revoir !")
            break
            lancement = '5'
            '''