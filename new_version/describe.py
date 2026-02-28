from math_utils import count, mean, std, min_val, max_val, percentile
from scatter_plot import scatter_plot
from histogram import histogram
from pair_plot import pair_plot

import pandas as pd
# import matplotlib.pyplot as plt
import sys


def get_stats(values: list):
	"""
	Calcule toutes les statistiques nécessaires pour une colonne de données
	et les retourne sous forme de list.
	"""
	
	stats_function = {
		"Count": count(values),
		"Mean": mean(values),
		"Std": std(values),
		"Min_val": min_val(values),
		"Max_val": max_val(values),
		"25%": percentile(values, 25),
		"50%": percentile(values, 50),
		"75%": percentile(values, 75)
		}
	result = stats_function
	return result



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
	try:
		filename = sys.argv[1]
		all_stats = {}
		df = pd.read_csv(filename)
		exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Hogwarts House"]
	
		for column_name in df.columns:
			if column_name in exclude:
				continue

			current_col_values = df[column_name].dropna().tolist()	
			if len(current_col_values) > 0:
				all_stats[column_name] = get_stats(current_col_values)

		if all_stats:
			# Affiche le tableau de stats (P1)
			print_describe(all_stats)

			# Affiche l'histogramme (P2)
			histogram(df)
			
			# Affiche un scatter plot (P2)
			scatter_plot(df, "Astronomy", "Defense Against the Dark Arts")
			
			# Affiche un pair plot (P2)
			pair_plot(df)

	
	except FileNotFoundError:
		print(f"Error: The file '{filename}' cannot be found.")
		return
	
if __name__ == "__main__":
	main()




