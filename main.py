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
    print("Je suis un ChatBot \n")
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
        directory = None
        while directory is None:
            #directory = input(("Saissisez votre chemin d'accès du dossier 'speeches' : "))
            directory = 'C:\\Users\\33643\\PycharmProjects\\pychatbot-CROGUENNEC-DOUNIAMA_OKANA\\speeches-20231110'

            #files_names = list_of_files(directory, "txt")
            #print_list(files_names)
            # ================== Création des fichiers du répertoire "Cleaned" ===========================
            cleaned(directory)
            directory1 = 'C:\\Users\\33643\\PycharmProjects\\pychatbot-CROGUENNEC-DOUNIAMA_OKANA\\Cleaned'
            TF(directory2)
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