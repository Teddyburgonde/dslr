from math_utils import count, mean, std, min_val, max_val, percentile
from statistics_calculation import get_stats
import sys
import csv

# Ce que je dois faire: 
# Je dois creer un programme qui analyse les donnees du fichier dataset_train.csv 
# pour pouvoir predire dans quelle maison(Gryffondor, Serpentard...) chaque eleve doit aller.
#
#
# Fichier a lire dataset_train.csv (Liste des éleves)
# 1. Nettoyage : Parcoure ta liste data et pour chaque colonne, 
# récupère uniquement les valeurs numériques et mets-les dans une liste.
# 2. Calculs : Crée une fonction pour chaque statistique. 
# Par exemple, pour la moyenne : somme_des_notes / nombre_de_notes.
# 3. Affichage : Utilise des print formatés pour que tes colonnes soient 
# bien alignées comme dans l'exemple du sujet.
# 

#             Arithmancy    Astronomy    Herbology ...
# Count        1566.00000   1568.00000   1567.00000
# Mean        49634.57024     39.79713      1.14102
# Std         16674.47957    520.13232      5.21801
...

# ⚠️ transformer chaque valeur en nombre. Si ça marche, c'est que la colonne est numérique.
#
# 
# ⚠️ numpy pour optimiser. 


def print_describe(all_stats):
	"""
    Affiche les statistiques calculées sous forme de tableau aligné.
	"""
	ligne_of_header = " " * 15 
	for matiere in all_stats:
		ligne_of_header += f"{matiere:>25}"
	print(ligne_of_header)


def main():
	if len(sys.argv) != 2:
		print("Usage: python describe.py dataset.csv")
		return
	
	filename = sys.argv[1]
	all_stats = {}
	try:
		with open(filename, "r") as f:
			reader = csv.DictReader(f)
			data = list(reader)
			exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Hogwarts House"]
			if data:
				for x in data[0].keys():
					if x in exclude:
						continue
					current_col_values = []
					for row in data:
						try:
							if row[x] != "": # Si la case n'est pas vide
								value = float(row[x]) # On garde que les valeurs numeriques.
								current_col_values.append(value)

						except ValueError:
							pass # Ce n'est pas une valeur numeriques donc on passe.
					
					if len(current_col_values) > 0:
						all_stats[x] = get_stats(current_col_values)
		if all_stats:
			print_describe(all_stats)

	except FileNotFoundError:
		print(f"Error: The file '{filename}' cannot be found.")

	# 2. Calculer les statistiques pour chaque colonne numérique (count, Mean etc...)  
	# 3. Affichier les résultats.

if __name__ == "__main__":
	main()

