import matplotlib.pyplot as plt
import numpy as np



# Pseudo code for plot_all_histograms

# 1. Définir la liste des maisons et une palette de couleurs associée
# (ex: Gryffindor: red, Hufflepuff: yellow, Ravenclaw: blue, Slytherin: green)

# 2. Créer une figure avec plt.subplots (ex: 4 lignes, 4 colonnes)
# Récupérer l'objet 'fig' et le tableau d'axes 'axs'

# 3. Aplatir le tableau d'axes avec .flatten() pour itérer facilement dessus

# 4. POUR chaque index et chaque nom_matiere dans la liste 'features' :
	
	# A. Sélectionner l'axe (le sous-graphique) correspondant à l'index actuel

	# B. POUR chaque maison dans la liste des maisons :

		# i. Filtrer les données : extraire les notes de 'nom_matiere' 
		# uniquement pour les élèves appartenant à cette 'maison'

		# ii. Nettoyage : Créer une liste 'notes_propres' en ignorant les 
		# valeurs vides ("") et en convertissant le reste en float

		# iii. Tracer l'histogramme sur l'axe sélectionné :
		# Passer 'notes_propres', définir le nombre de bins (ex: 20),
		# l'opacité (alpha=0.5) et le label du nom de la maison

	# C. Configurer l'axe actuel :
	# Ajouter le titre (nom_matiere) et afficher la légende

# 5. POUR les axes restants dans la grille (ceux qui n'ont pas de matière) :
	# Désactiver l'affichage de l'axe (axis off) pour ne pas avoir de carrés vides

# 6. Ajuster l'espacement entre les graphiques avec plt.tight_layout()

# 7. Afficher la fenêtre finale avec plt.show()

# student['Hogwarts House'] donne le nom de sa maison.
# student['Astronomy'] donne sa note en Astronomie.


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

			# current_ax.hist(data_list)
			#  

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

