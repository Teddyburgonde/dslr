import matplotlib.pyplot as plt
import pandas as pd

def pair_plot(df):
	""" 
	Affiche une matrice de graphiques :
	- Sur la diagonale : un histogramme pour voir la distribution d'une matière.
	- Hors diagonale : un nuage de points pour voir la corrélation entre deux matières.
	"""

	houses_list = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	exclude = ["Index", "First Name", "Last Name", "Birthday", "Best Hand", "Hogwarts House"]
	features = [c for c in df.columns if c not in exclude]
	n = len(features)
	fig, axs = plt.subplots(n, n, figsize=(20, 20))
	axs_flat = axs.flatten()

	lessons = [c for c in df.columns if c not in exclude]
	for i, course1 in enumerate(lessons):
		for j, course2 in enumerate(lessons):
			for house, color in houses_list.items():
				house_scores1 = df[df['Hogwarts House'] == house][course1].dropna()
				if course1 == course2:
					axs_flat[(i * n) + j].hist(house_scores1, alpha=0.5, color=color, label=house)
				else:
					house_note = df[df['Hogwarts House'] == house][[course1, course2]].dropna()
					axs_flat[(i * n) + j].scatter(
						house_note[course1],
						house_note[course2],
						c= color,
						s = 1,
						label=house,
						alpha=0.5)
			if i == 0:
				axs_flat[(i * n) + j].set_title(course2, fontsize=10)
			if j == 0:
				axs_flat[(i * n) + j].set_ylabel(course1, fontsize=8, rotation=55, ha='right', labelpad=2)
	plt.tight_layout() # Permet d'eviter le chevauchement.
	plt.show()