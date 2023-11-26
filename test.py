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