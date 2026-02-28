import matplotlib.pyplot as plt
import pandas as pd

def scatter_plot(df: pd.DataFrame, feature_x: str, feature_y: str):
	"""
	Affiche un nuage de points comparant deux matières.
	Chaque point est coloré selon la maison de l'élève.
	Args:
		df (pd.DataFrame): Le DataFrame contenant les données des élèves.
		feature_x (str): Nom de la première matière (ex: 'Astronomy').
		feature_y (str): Nom de la deuxième matière (ex: 'Defense Against the Dark Arts').
	"""
	houses_list = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	plt.figure(figsize=(10, 8))

	for house_name, color in houses_list.items():
		house_note = df[df['Hogwarts House'] == house_name][[feature_x, feature_y]].dropna()
		plt.scatter(house_note[feature_x], house_note[feature_y], c =color, label=house_name, alpha=0.5)
	plt.xlabel(feature_x)
	plt.ylabel(feature_y)
	plt.title(f"Correlation between {feature_x} and {feature_y}")
	plt.legend()
	plt.show()
