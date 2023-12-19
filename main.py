from fonctions import *
import datetime as dt
#Liam CROGUENNEC et Joss DOUNIAMA OKANA
print("\U0001F4C6 ",dt.datetime.today()," \U0001F5D3"'\n') # Affichage de l'heure de la date au début du programme

run = True
while run == True:
    print("Bonjour !\n")
    time.sleep(1)
    print("Je suis ChatBot","\U0001F916"'\n')
    time.sleep(1)
    print("Tapez l'un des chiffres \n")
    time.sleep(1)
    print("1 - Commençez \U0001F3C1 \n2 - Options \u2699 \n3 - Comment ça marche ? \U0001F4D6 \n4 - À quoi ça sert ? \U0001F914 \n5 - Quittez \u274C \n")
    lancement = input(":")
    while lancement not in ['1', '2', '3', '4', '5']:
        lancement = input(":")
    if lancement == '1':

        path = trouver_dossier("speeches-20231110")
        cleaned_directory(path)
        path_cleaned = trouver_dossier("Cleaned")
        tfidf_matrix = TF_IDF(path_cleaned)

        debut = input("C'est parti !\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
        while debut not in ["1","2","3","4","5","6","7","8","9"]:
            debut = input(":")
        if debut == "1":
            print("\nSaississez votre question ")
            question =input(":")
            tokquestion = tokenizer_question(question)
            chemins_dossiers_corpus = lister_dossiers()
            termes_communs = rechercher_termes_dans_corpus(tokquestion, chemins_dossiers_corpus)
            scores_idf = IDF(path_cleaned)
            for filename in os.listdir(path_cleaned):
                # Calculer les TF pour chaque document
                scores_tf = TF(path_cleaned, filename)
            # Calculer le vecteur TF-IDF de la question
            vecteur_tfidf_question = calculer_vecteur_tfidf_question(tokquestion, scores_tf, scores_idf)
            # Obtenez les valeurs (values) de la matrice TF-IDF
            vecteur_document = []
            for i, vecteur_tfidf_document in enumerate(tfidf_matrix):
                vecteur_document.append(list(vecteur_tfidf_document.values()))
            liste = list_of_files(path, "txt")
            liste2= list_of_files(path_cleaned, "txt")
            file_names = liste + liste2
            most_relevant_document, relevant_folder = find_most_relevant_document(vecteur_document, vecteur_tfidf_question,file_names)
            # Afficher le résultat
            print("Le document le plus pertinent est :", most_relevant_document)
            print("Son équivalent dans le répertoire « ./speeches » est :", relevant_folder)
            max_tfidf_index = find_max_tfidf_word(vecteur_tfidf_document)
            max_tfidf_word = max_tfidf_index
            response = generate_response(relevant_folder, max_tfidf_word)
            # Afficher la réponse générée
            print("La réponse générée est :", response)
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "2" :
            mot_max, score_max = mot_plus_important(tfidf_matrix)
            print("Le mot le plus important d'un discours de président. :", mot_max)
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "3":
            print("Le mot le moins important:", mots_moins_importants(tfidf_matrix))
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "4":
            print("pour quels présidents voulez vous connaître ces mots les plus utilisés ?\n")
            president = input("1 - Chirac\n2 - Giscard\n3 - Holland\n 4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
            while president not in ["1","2","3","4","5","6"] :
                president = input("1 - Chirac\n2 - Giscard\n3 - Holland\n4 - Macron\n5 - Mitterand\n6 - sarkozy\n:")
            if president == "1":
                print("Pour quel mandat vous voulez connaître son mots le plus utilisé ?")
                mandat_chirac = input("1 - 1er Mandat\n2 - 2ème Mandat\n:")
                while mandat_chirac not in ["1","2"]:
                    mandat_chirac = input("1 - 1er Mandat\n2 - 2ème Mandat\n:")
                if mandat_chirac == "1":
                    mot_max_chirac, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Chirac1.txt")
                    print("Le mot le plus répété par Chirac dans 1er Mandat est :", mot_max_chirac)
                elif mandat_chirac == "2":
                    mot_max_chirac, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Chirac2.txt")
                    print("Le mot le plus répété par Chirac dans 2èmé Mandat est :", mot_max_chirac)
            elif president == "2":
                mot_max_giscard, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Giscard dEstaing.txt")
                print("Le mot le plus répété par Giscard est :", mot_max_giscard)
            elif president == "3":
                mot_max_hollande, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Hollande.txt")
                print("Le mot le plus répété par Hollande est :", mot_max_hollande)
            elif president == "4":
                mot_max_macron, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Macron.txt")
                print("Le mot le plus répété par Macron est :", mot_max_macron)
            elif president == "5":
                print("Pour quel mandat vous voulez connaître son mots le plus utilisé ?")
                mandat_chirac = input("1 - 1er Mandat\n2 - 2ème Mandat\n:")
                while mandat_chirac not in ["1", "2"]:
                    mandat_chirac = input("1 - 1er Mandat\n2 - 2ème Mandat\n:")
                if mandat_chirac == "1":
                    mot_max_mitterrand, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Mitterrand1.txt")
                    print("Le mot le plus répété par Mitterrand dans 1er Mandat est :", mot_max_mitterrand)
                elif mandat_chirac == "2":
                    mot_max_mitterrand, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Mitterrand2.txt")
                    print("Le mot le plus répété par Mitterrand dans 2èmé Mandat est :", mot_max_mitterrand)
            elif president == "6":
                mot_max_sarkozy, score_max_chirac = mots_plus_repeter_president(path_cleaned,"Cleaned_Nomination_Sarkozy.txt")
                print("Le mot le plus répété par Sarkozy est :", mot_max_sarkozy)
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "5":
            print("quel mot en particulier a été le plus utilisé par un président, que vous voulez savoir\nSaississez votre mot")
            mot = input(":")
            resultat_president = president_parlant_de_la_nation(tfidf_matrix, mot)
            # Affichez les résultats
            if isinstance(resultat_president, str):
                print(resultat_president)  # Aucun président n'a parlé de la Nation.
            else:
                president_max, score_max = resultat_president
                print(f"Le président qui parle le plus de '{mot}' est {president_max}.")
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "6" :
            print("Sur quel sujet aimeriez-vous savoir quel président l'a abordé en premier ?\nSaississez votre sujet")
            sujet = input(":")
            resultat_president = premier_president_parlant_de(tfidf_matrix, sujet)
            # Affichez les résultats
            if isinstance(resultat_president, str):
                print(resultat_president)  # Aucun président n'a parlé de la Nation.
            else:
                president_max, score_max = resultat_president
                print(f"Le permier président qui a abordé le '{sujet}' est {president_max}.")
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "7" :
            mots_non_importants_resultat = ['le', 'la', 'les', 'un', 'une', 'des','à', 'de', 'pour', 'avec', 'sans', 'chez', 'dans', 'sur', 'sous', 'entre', 'devant', 'derrière','mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses', 'notre', 'notre', 'nos', 'votre', 'votre', 'vos', 'leur', 'leur', 'leurs','ce', 'cette', 'ces', 'cet','et','que','qu','en','se',"j","l",]
            resultat_mots_evoques = mots_evoques_par_tous(tfidf_matrix, mots_non_importants_resultat)
            # Affichez les résultats
            print("Mots évoqués par tous les présidents sont :")
            print(resultat_mots_evoques)
            debut = input("\nQue souhaitez vous ?\n1 - Posez une question ?\n2 - Connaître le mot le plus important lors d'un discours de président.\n3 - Connaître les mots les moins importants lors d'un discours de président\n4 - Connaître les mots les plus répèter par un président.\n5 - Connaître le nom du président ayant répèter le plus un mot en particulier.\n6 - Connaître le premier président ayant aborder un sujet.\n7 - Connaître les mots prononcés par tous les présidents.\n8 - Retour.\n9 - Quittez.\n:")
            while debut not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                debut = input(":")

        elif debut == "8":
            print('\n')
            continue

        elif debut == "9":
            print("Au revoir !")
            sys.exit()

        lancement = "1"


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
            print("Crédit du programme ")
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
        print("\nJe sers à donner des informations sur les discours de tous les présidents de la cinquième République et je peux répondre à certains questions sur les sujets contenus dans votre bibliothèque.\n")
        continue
    elif lancement == '5':
        run = False
