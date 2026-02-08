import matplotlib.pyplot as plt

def plot_pair_plot(data, features):
	""" 
	Affiche une matrice de graphiques :
	- Sur la diagonale : un histogramme pour voir la distribution d'une matière.
	- Hors diagonale : un nuage de points pour voir la corrélation entre deux matières.
	"""
	n = len(features)

	houses = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}

	# Désigne l'emplacement où je vais afficher les données.
	# fig représente la fenetre entiere 
	# n , n = nombre de lignes et de colonnes
	fig, axs = plt.subplots(n, n, figsize=(20, 20))

	for r in range(n):
		for c in range(n):
			# On cible le graphique actuel dans la matrice
			ax = axs[r, c]

			course_c = features[c]
			course_r = features[r]
			
			# Si r == c on dessine un histogramme 
			if r == c:
				for house_name, color in houses.items():
					# On selection les notes de la matiere de la maison qui est sur la colonne 
					# sans les cases vides
					subset = data[data['Hogwarts House'] == house_name][course_c].dropna()
					ax.hist(subset, color = color, alpha=0.5)
			else: # On dessine un nuage de point
				for house_name, color in houses.items():
					house_data = data[data['Hogwarts House'] == house_name]
					ax.scatter(house_data[course_c], house_data[course_r], color = color, s = 1 , alpha= 0.5)

			if r == 0:
				ax.set_title(course_c)
			if c == 0:
				ax.set_ylabel(course_r)
	plt.tight_layout() # Permet d'eviter le chevauchement.
	plt.show()