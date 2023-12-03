from fonctions import *
import datetime as dt

print("\U0001F4C6 ",dt.datetime.today()," \U0001F5D3"'\n') # Affichage de l'heure de la date au début du programme

run = True
while run == True:
    print("Bonjour !\n")
    time.sleep(1)
    print("Je suis ChatBot","\U0001F916"'\n')
    time.sleep(1)
    print("Tapez l'un des chiffres \n")
    time.sleep(1)
    print("1 - Commençez\n2 - Options ""\u2699""\n3 - Comment ça marche ? \n4 - À quoi sert ?\n5 - Quittez\n")
    lancement = input(":")
    while lancement not in ['1', '2', '3', '4', '5']:
        lancement = input(":")
    if lancement == '1':
        print("saississez le nom de votre dossier \U0001F5C2")
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
        elif firt_stage == "3":
            continue
        elif firt_stage == "4":
            print("Au revoir !")
            break
            lancement = '5'
        cleaned_directory(path)
        tfidf_matrix = TF_IDF(path)
        debut = input("C'est parti !\nQue voulez-vous savoir ?\n1 - Connaître le mot le plus important lors d'un discours de président.\n2 - Connaître les mots les moins importants lors d'un discours de président\n3 - Connaître les mots les plus répèter par un président.\n4 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n5 - Connaître le premier président ayant aborder un sujet.\n6 - Connaître les mots prononcés par tous les présidents.\n7 - Retour.\n8 - Quittez.\n:")
        while debut not in ["1","2","3","4","5","6","7","8"]:
            debut = input(":")
        if debut == "1" :
            mot_max, score_max = mot_plus_important(tfidf_matrix)
            print("Le mot le plus important d'un discours de président. :", mot_max)
            debut = input("C'est parti !\n Que voulez-vous savoir ?\n 1 - Connaître le mot le plus importants lors d'un discour de président.\n2 - Connaître les mots les moins importants lors d'un discour de président\n3 - Connaître les mots les plus répèter par un président.\n 4 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n5 - Connaître le premier président ayant aborder un sujet.\n6 - Connaître les mots prononcés par tous les présidents.\n7 - Retour.\n8 - Quittez.\n:")
        elif debut == "2":
            print("Le mot le moins important:", mots_moins_importants(tfidf_matrix))
            debut = input("C'est parti !\n Que voulez-vous savoir ?\n 1 - Connaître le mot le plus importants lors d'un discour de président.\n2 - Connaître les mots les moins importants lors d'un discour de président\n3 - Connaître les mots les plus répèter par un président.\n 4 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n5 - Connaître le premier président ayant aborder un sujet.\n6 - Connaître les mots prononcés par tous les présidents.\n7 - Retour.\n8 - Quittez.\n:")
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
        elif debut == "7":
            print('\n')
            continue
            pass
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
