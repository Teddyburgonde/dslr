import matplotlib.pyplot as plt
import numpy as np

def plot_all_histograms(data, features):
	"""
	Affiche une grille d'histogrammes pour comparer les distributions 
	des notes entre les 4 maisons de Poudlard.

	Logique de 'enumerate(features)'
	Cette fonction génère un couple (index, valeur) à chaque tour.
	- index : Position dans la grille (0 à 15).
	- course_name : Le nom de la matière actuelle (ex: 'Astronomy').

	Args:
		data (list): Liste de dictionnaires (chaque dict est une ligne du CSV).
		features (list): Liste des noms des colonnes numériques (les cours).
	"""
	houses = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	# 4 lignes , 4 colonnes, fig = fenêtre entiere , axs = Grille a l'interieur de la fenêtre
	fig, axs = plt.subplots(4, 4, figsize=(15, 15))

	# On aplatit la grille pour n'avoir qu'une seule dimension
	axs_plats = axs.flatten()

	for index, course_name in enumerate(features):
		current_ax = axs_plats[index]
		# On utilise .items() pour avoir le nom et la couleur
		for house_name, color in houses.items():
			clean_notes = []

			for student in data:
				# Vérification de la maison et de la présence d'une note
				if student['Hogwarts House'] == house_name and student[course_name] != "":
					# On convertit la note précise de ce cours en nombre
					note_value = float(student[course_name])
					clean_notes.append(note_value)
			# On génère l'histogramme
			current_ax.hist(clean_notes, color= color, alpha=0.5, label= house_name)
		
		current_ax.set_title(course_name)
		current_ax.legend()
	# Ajuste l'espacement entre les 16 graphiques
	plt.tight_layout()
	plt.show()


	# B. POUR chaque maison dans la liste des maisons :

		# iii. Tracer l'histogramme sur l'axe sélectionné :
		# Passer 'notes_propres', définir le nombre de bins (ex: 20),
		# l'opacité (alpha=0.5) et le label du nom de la maison

		# x : Ta liste de nombres (ex: clean_notes).

		# bins : Le nombre de colonnes. Plus il y en a, plus c'est précis. (Ex: bins=20).

		# color : La couleur des barres.

		# alpha : La transparence (de 0 à 1). Très important quand on superpose plusieurs maisons !

		# label : Le nom pour la légende (ex: "Gryffindor").

		# Ajouter le nom de la matière en haut du petit graphique
		# current_ax.set_title(course_name)

		# Afficher la petite boîte qui explique les couleurs (la légende)
		# current_ax.legend()





	# C. Configurer l'axe actuel :
	# Ajouter le titre (nom_matiere) et afficher la légende

