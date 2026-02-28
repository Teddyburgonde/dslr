from math_utils import count, mean, std, min_val, max_val, percentile
import pandas as pd
import matplotlib.pyplot as plt
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


def histogram(df: pd.DataFrame):

	houses_list = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Hogwarts House"]
	fig, axs = plt.subplots(4, 4, figsize=(14, 10))
	axs_flat = axs.flatten()

	lessons = [c for c in df.columns if c not in exclude] # on cree une list contenant tout les nom de cours

	for i, course in enumerate(lessons):
		house_means = []
		for house_name, color in houses_list.items():
			scores = df[df['Hogwarts House'] == house_name][course].dropna()
			axs_flat[i].hist(scores, color = color, alpha=0.5, label=house_name)
			if not scores.empty:
				house_means.append(mean(scores))
		std_result = std(house_means)
		if i == 0:
			axs_flat[i].legend()
		axs_flat[i].set_title(f"{course}\n(std: {std_result:.4f})")

	for j in range(len(lessons), len(axs_flat)):
		axs_flat[j].axis('off')
	plt.tight_layout()
	plt.show()


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
			# Affiche le tableau de stats
			print_describe(all_stats)

			# Affiche l'histogramme 
			histogram(df)








			# Affiche un scatter plot
			# plot_scatter_comparison(df, "Astronomy", "Defense Against the Dark Arts")
			# or 
			# plot_scatter_comparison(df, "Arithmancy", "Care of Magical Creatures")

			# On récupere la liste des matières traitées
			# features_list = list(all_stats.keys())

			# Affiche un pair plot
			# plot_pair_plot(df, features_list)
	
	except FileNotFoundError:
		print(f"Error: The file '{filename}' cannot be found.")
		return
	
if __name__ == "__main__":
	main()




