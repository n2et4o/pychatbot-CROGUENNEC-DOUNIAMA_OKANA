from fonctions import *
import datetime as dt

print(dt.datetime.today(),'\n') # Affichage de l'heure de la date au début du programme
'''
directory = langue()
files_names = list_of_files(directory, "txt")
print_list(files_names)
            # ================== Création des fichiers du répertoire "Cleaned" ===========================
cleaned(directory)
#'''
# appel de la fonction pour choisir la langue du menu
#directory = langue()
#global run
#'''
run = True
while run == True:
    print("Bonjour !\n")
    time.sleep(1)
    print("Je suis ChatBot","\U0001F916"'\n')
    time.sleep(1)
    print("Tapez l'un des chiffres \n")
    time.sleep(1)
    print("1 - Commençez\n2 - Options\n3 - Comment ça marche ? \n4 - À quoi sert ?\n5 - Quittez\n")
    lancement = input(":")
    while lancement not in ['1', '2', '3', '4', '5']:
        lancement = input(":")
    if lancement == '1':
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
                "Pour ajouter un chemin d'accès, vous devez aller sur le fichier ou dossier que vous voulez son chemin d'accès, puis faites un clique droit. \nSéléctionnez 'Copy Path' puis 'Absolue path' et il ne vous restera plus qu'à coller le chemin d'accès que vous venez de copier \n")
            pass
        elif reponse == '3':  # Retour
            continue
        elif reponse == '4':  # Quittez
            break

        chemin_valide = False
        while not chemin_valide:
            directory = input(("Saissisez votre chemin d'accès du dossier 'speeches' : "))

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
        chemin2_valide = False

        while not chemin2_valide:
            directory1 = input(("Saissisez votre chemin d'accès du dossier 'Cleaned' : "))

            # Vérifier si le chemin existe
            if os.path.exists(directory1):
                chemin2_valide = True
                print("\nChemin d'accès valide.\n")
            else:
                print("\nLe chemin d'accès n'est pas valide. Veuillez réessayer.\n")

        # Accès rapide pour les développeurs
        #directory1 = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\Cleaned'

        tfidf_matrix = TF_IDF(directory1)
        debut = input("C'est parti !\n Que voulez-vous savoir ?\n 1 - Connaître le mot le plus important lors d'un discours de président.\n2 - Connaître les mots les moins importants lors d'un discours de président\n3 - Connaître les mots les plus répèter par un président.\n 4 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n5 - Connaître le premier président ayant aborder un sujet.\n6 - Connaître les mots prononcés par tous les présidents.\n7 - Retour.\n8 - Quittez.\n:")
        while debut not in ["1","2","3","4","5","6","7","8"]:
            debut = input(":")
        if debut == "1" :
            mot_max, score_max = mot_plus_important(tfidf_matrix)
            print("Le mot le plus important d'un discours de président. :", mot_max)
            debut = input("C'est parti !\n Que voulez-vous savoir ?\n 1 - Connaître le mot le plus importants lors d'un discours de président.\n2 - Connaître les mots les moins importants lors d'un discours de président\n3 - Connaître les mots les plus répèter par un président.\n 4 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n5 - Connaître le premier président ayant aborder un sujet.\n6 - Connaître les mots prononcés par tous les présidents.\n7 - Retour.\n8 - Quittez.\n:")
        elif debut == "2":
            print("Les Mots les moins importants:", mots_moins_importants(tfidf_matrix))
            debut = input("C'est parti !\n Que voulez-vous savoir ?\n 1 - Connaître le mot le plus importants lors d'un discours de président.\n2 - Connaître les mots les moins importants lors d'un discours de président\n3 - Connaître les mots les plus répèter par un président.\n 4 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n5 - Connaître le premier président ayant aborder un sujet.\n6 - Connaître les mots prononcés par tous les présidents.\n7 - Retour.\n8 - Quittez.\n:")
        elif debut == "3":
            print("pour quels présidents voulez vous connaître ces mots les plus utilisés ?\n")
            president = input("1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
            while president not in ["1","2","3","4","5","6"] :
                president = input("1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
            if president == "1":
                print("Pour quel mandat vous voulez connaître son mots le plus utilisé ?")
                mandat_chirac = input("1 - 1er Mandat\n2 - 2ème Mandat\n:")
                while mandat_chirac not in ["1","2"]:
                    mandat_chirac = input("1 - 1er Mandat\n2 - 2ème Mandat\n:")
                if mandat_chirac == "1":
                    mot_max_chirac, score_max_chirac = mots_plus_repeter_president(directory1,"Chirac_mandat1.txt")
                    print("Le mot le plus répété par Chirac dans 1er Mandat est :", mot_max_chirac)
                elif mandat_chirac == "2":
                    mot_max_chirac, score_max_chirac = mots_plus_repeter_president(directory1,"Chirac_mandat2.txt")
                    print("Le mot le plus répété par Chirac dans 2èmé Mandat est :", mot_max_chirac)
        elif debut == "8":
            break
            lancement = "5"
        break
        lancement = '5'


    elif lancement == '2':
        option = input("Tapez un chiffre\n1 - Langue\n2 - Crédit\n3 - Retour\n:")
        while option not in ['1', '2', '3']:
            option = input(":")
        if option == '1':
            langue = input("1 - Français\n2 - English\n3 - Espanõl\n4 - Retour\n: ")
            while langue not in ['1', '2', '3', '4']:
                langue = input(":")
            if langue == '1':
                continue
            elif langue == '2':
                end = new_menu_english()
                if end == '5':
                    run = False
                    run1 = False
                    run2 = False
                # continue
            elif langue == "3":
                end = new_menu_spanish()
                if end == '5':
                    run = False
                    run1 = False
                    run2 = False
                # continue
            elif langue == '4':
                continue
        elif option == '2':
            print("Crédit du programme")
            time.sleep(1)
            print("réalisé par : \n")
            time.sleep(1)
            print("Joss DOUNIAMA OKANA\n")
            time.sleep(1)
            print("Liam CROGUENNEC\n")
            time.sleep(1)
            print("Projet Python\n")
            time.sleep(1)
            print("Groupe BN 2023-2024\n")
            time.sleep(1)
            print("Fin\n")
            time.sleep(1)
            continue
        elif option == '3':
            continue
    elif lancement == '3':
        print("\nCommençez puis suivez les instructions. \n")
        continue
    elif lancement == '4':
        print("\nJe sers à donner des informations sur les discours de tous les présidents de la cinquième République. \n")
        continue
    elif lancement == '5':
        run = False


        '''

        #directory = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\speeches-20231110'



    #'''
#'''


#'''