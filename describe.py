from math_utils import count, mean, std, min_val, max_val, percentile
from histogram import plot_all_histograms
from scatter_plot import plot_scatter_comparison
from statistics_calculation import get_stats
from pair_plot import plot_pair_plot
import pandas as pd

import sys
import csv

# ⚠️ numpy pour optimiser. 

# Data Analysis (V.1) -> Affiche les statistiques pour toutes les colonnes numériques. ✅
# Data Visualization (V.2) -> 3 programmes : 
#     - histogram.py - Affiche un histogramme ✅
#     - scatter_plot.py - Affiche un scatter plot ✅
#     - pair_plot.py - Affiche un pair plot (matrice de scatter plots) ✅

# Logistic Regression (V.3) -> 2 programmes
	#   - logreg_train.py - Entraîne le modèle ✅
	# 	   -Lit dataset_train.csv ✅
	# 	   - Entraîne une régression logistique (one-vs-all) ✅
	# 	   - Sauvegarde les poids dans un fichier ✅

	# 	- logreg_predict.py - Fait les prédictions
		# - Lit dataset_test.csv et le fichier de poids
		# - Prédit la maison de chaque élève
		# - Génère houses.csv



def print_describe(all_stats):
	"""
	Affiche les statistiques calculées sous forme de tableau aligné.
	"""
	labels = ["Count", "Mean", "Std", "Min_val", "25%", "50%", "75%", "Max_val"]
	header_line = " " * 8
	for subject in all_stats:
		subject_short = subject[:12]
		header_line += f"{subject_short:>14}"
	print(header_line)
	for label in labels:
		row = f"{label:<8}"
		for subject in all_stats:
			value = all_stats[subject][label]
			row += f"{value:>14.2f}"
		print(row)


def main():
	if len(sys.argv) != 2:
		print("Usage: python describe.py dataset.csv")
		return
	
	filename = sys.argv[1]
	all_stats = {}

	try:
		df = pd.read_csv(filename)
			
		exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Hogwarts House"]
			
		for column_name in df.columns:
			if column_name in exclude:
				continue

			current_col_values = df[column_name].dropna().tolist()	
			if len(current_col_values) > 0:
				all_stats[column_name] = get_stats(current_col_values)

		if all_stats:
			# Affiche le tableau de stats
			print_describe(all_stats)

			# Prépare la liste des matières pour les graphiques
			# features_list = list(all_stats.keys())

			# # Affiche l'histogramme 
			# plot_all_histograms(data, features_list)

			# Affiche un scatter plot
			# plot_scatter_comparison(data, "Astronomy", "Defense Against the Dark Arts")
			# or 
			# plot_scatter_comparison(data, "Arithmancy", "Care of Magical Creatures")

			# On récupere la liste des matières traitées
			# features_list = list(all_stats.keys())

			# Affiche un pair plot
			# plot_pair_plot(df, features_list)
	
	except FileNotFoundError:
		print(f"Error: The file '{filename}' cannot be found.")

if __name__ == "__main__":
	main()
