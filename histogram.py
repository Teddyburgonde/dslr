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


def plot_scatter_comparison(data, feature_x, feature_y):
	"""
	Affiche un nuage de points comparant deux matières.
	Chaque point est coloré selon la maison de l'élève.

	Args:
		data (list): Liste de dictionnaires (les élèves).
		feature_x (str): Nom de la première matière (ex: 'Astronomy').
		feature_y (str): Nom de la deuxième matière (ex: 'Defense Against the Dark Arts').
	"""
	houses = {
		"Gryffindor": "red",
		"Hufflepuff": "yellow",
		"Ravenclaw": "blue",
		"Slytherin": "green"
	}
	plt.figure(figsize=(10, 8))

	for house_name, color in houses.items():
		note_x = []
		note_y = []
		for student in data:
			if student['Hogwarts House'] == house_name:
				value_x = student[feature_x]
				value_y = student[feature_y]
				if value_x != "" and value_y != "":
					note_x.append(float(value_x))
					note_y.append(float(value_y))
		plt.scatter(note_x, note_y, c=color, label=house_name, alpha=0.5)
	plt.xlabel(feature_x)
	plt.ylabel(feature_y)
	plt.legend()
	plt.show()












# scatter_plot.py 

# Affiche un scatter plot

# Pour dessiner: plt.scatter(liste_x, liste_y, color=color)
# donné a creer: notes_x et notes_y
# plt.show()