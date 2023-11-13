from fonctions import *
import datetime as dt

print(dt.datetime.today(),'\n') # Affichage de l'heure de la date au début du programme


# appel de la fonction pour choisir la langue du menu
#directory = langue()
directory = menu_french_new()
#'''
#directory = 'C:\\Users\\20220848\\PycharmProjects\\Project_with_Liam\\speeches-20231110'
files_names = list_of_files(directory, "txt")
print_list(files_names)

    # ================== Création des fichiers du répertoire "Cleaned" ===========================
cleaned(directory)

#'''

