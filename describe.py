from math_utils import count, mean, std, min_val, max_val, percentile
from statistics_calculation import get_stats
import sys
import csv

# ⚠️ numpy pour optimiser. 

# Data Analysis (V.1) -> Affiche les statistiques pour toutes les colonnes numériques.
# Data Visualization (V.2) -> 3 programmes : 
#     - histogram.py - Affiche un histogramme
#     - scatter_plot.py - Affiche un scatter plot
#     - pair_plot.py - Affiche un pair plot (matrice de scatter plots)

# Logistic Regression (V.3) -> 2 programmes
	#   - logreg_train.py - Entraîne le modèle
	# 	   -Lit dataset_train.csv
	# 	   - Entraîne une régression logistique (one-vs-all)
	# 	   - Sauvegarde les poids dans un fichier

	# 	- logreg_predict.py - Fait les prédictions
		# - Lit dataset_test.csv et le fichier de poids
		# - Prédit la maison de chaque élève
		# - Génère houses.csv


def print_describe(all_stats):
	"""
	Affiche les statistiques calculées sous forme de tableau aligné.
	"""
	labels = ["Count", "Mean", "Std", "Min_val", "25%", "50%", "75%", "Max_val"]
	ligne_of_header = " " * 8
	for matiere in all_stats:
		matiere_short = matiere[:12]
		ligne_of_header += f"{matiere_short:>14}"
	print(ligne_of_header)
	for label in labels:
		line = f"{label:<8}"
		for matiere in all_stats:
			value = all_stats[matiere][label]
			line += f"{value:>14.2f}"
		print(line)


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

if __name__ == "__main__":
	main()

